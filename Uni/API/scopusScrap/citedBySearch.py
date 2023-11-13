import ctypes
import os
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm.notebook import tqdm_notebook

from .scopusLogin import login
from .scopusSearch import set_chrome_options
from .scopusUtils import log


def article_cited_by(url: str, driver) -> int:
    driver.get(url)

    cited_bys_link = driver.find_element(
        By.CSS_SELECTOR, 'a[title="View all citing documents"]')
    cited_bys_link.click()

    driver.implicitly_wait(0.5)  # change

    select_all_results = driver.find_element(
        By.CSS_SELECTOR, 'li[id="selectAllCheck"]')

    if not select_all_results.find_element(By.CSS_SELECTOR, 'input[id="mainResults-allPageCheckBox"]').is_selected():
        select_all_results.click()

    export_button = driver.find_element(By.CSS_SELECTOR,
                                        'button[id="export_results"]')
    export_button.click()

    csv_button = driver.find_element(By.CSS_SELECTOR,
                                     'label[for="CSV"]')
    csv_button.click()

    table_head = driver.find_element(By.CSS_SELECTOR,
                                     'tr[id="exportCheckboxHeaders"]')
    table_head_elements = zip(table_head.find_elements(
        By.CSS_SELECTOR, 'label'), table_head.find_elements(By.CSS_SELECTOR, 'input'))

    for label, checkbox in table_head_elements:
        if not checkbox.is_selected():
            label.click()

    number_of_results = int(driver.find_element(By.CSS_SELECTOR,
                                                'span[class="resultsCount"]').text.split()[0].replace(',', ''))
    if number_of_results <= 20_000:
        select_all = driver.find_element(
            By.CSS_SELECTOR, 'th[id="otherInformationCheckboxes"]')

        export_all_results = driver.find_element(
            By.CSS_SELECTOR, 'button[id="exportTrigger"]')
        export_all_results.click()
    else:
        export_all_results = driver.find_element(
            By.CSS_SELECTOR, 'button[id="exportTrigger"]')
        export_all_results.click()

        select_all = driver.find_element(
            By.CSS_SELECTOR, 'label[id="exportTypeAndFormat"]')
        select_all.click()

        export_all_results = driver.find_element(
            By.CSS_SELECTOR, 'button[id="chunkExportTrigger"]')
        export_all_results.click()

    return number_of_results


def search_cited_by(download_folder_directory: str | None = None,
                    allowed_retries: int = 3,
                    timeout: int = 5*60):
    '''
    Documentation
    '''
    *_, user_data_dir, user_agent = login()

    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    if download_folder_directory:
        os.chdir(download_folder_directory)
    elif not os.getcwd().endswith('Download'):
        os.chdir('Download')

    searched_queries_folders = [dr for dr in os.listdir() if os.path.isdir(dr)]

    with webdriver.Chrome(options=set_chrome_options(user_data_dir)) as cited_by_driver:
        cited_by_driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        cited_by_driver.execute_cdp_cmd("Network.setUserAgentOverride", {
            "userAgent": user_agent})

        log('Cited by Webdriver start')
        print()

        for query_folder in searched_queries_folders:
            log(f'"{query_folder}" folder')
            csv_files = [file for file in os.listdir(query_folder) if file.endswith(
                '.csv') and file.startswith(query_folder)]
            doi_folders = [file for file in os.listdir(
                query_folder+r'\Cited by') if os.path.isdir(f'{query_folder}\\Cited by\\{file}')]

            for query_file in csv_files:
                log(f'"{query_file}" file')

                query_df = pd.read_csv(
                    f"{query_folder}\\{query_file}",
                    low_memory=False,
                    usecols=['Cited by', 'DOI', 'Link']).dropna()

                query_df = query_df[query_df['Cited by']
                                    != 0].loc[:, ['DOI', 'Link']]

                for doi, url in tqdm_notebook(query_df.values):
                    retries = 0
                    flag = True
                    sanitized_doi = doi.replace('/', '_')
                    while sanitized_doi not in doi_folders and flag and retries <= allowed_retries:
                        log(f"Searching for DOI: {doi} cited by's")
                        results_number = article_cited_by(url, cited_by_driver)
                        log(f'Exporting {min(2_000, results_number):,} citation results')

                        start_time = time.time()
                        while True:
                            time.sleep(1)
                            if os.path.exists('scopus.csv'):
                                os.mkdir(
                                    f'{query_folder}\\Cited by\\{sanitized_doi}')
                                os.rename(
                                    'scopus.csv', f'{query_folder}\\Cited by\\{sanitized_doi}\\{sanitized_doi}.csv')

                                log('Download complete')
                                flag = False
                                print()
                                break

                            if time.time() - start_time > timeout:
                                retries += 1
                                print()
                                log(f'Timeout ({timeout//60} minutes) reached')

                                if retries <= allowed_retries:
                                    log(f'Retrying... (retry number {retries})')
                                else:
                                    log('Moving on to the next article')
                                    flag = False
                                print()
                                break

    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
