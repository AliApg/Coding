import contextlib
import ctypes
import os
import time
from typing import Literal

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tqdm.notebook import tqdm_notebook

from .scopusLogin import login
from .scopusUtils import get_bib_file_row_count, log, time_formatter


def set_chrome_options(user_data_directory: str, headless: bool = True) -> Options:
    """s
    Configures Chrome options for Selenium WebDriver with specific settings.

    Args:
        user_data_dir (str): The path to the user data directory for the Chrome browser.
        headless (bool): Whether to enable headless mode for running without a graphical interface or not.

    Returns:
        selenium.webdriver.chrome.options.Options: Configured Chrome options for WebDriver.

    Description:
        This function sets up Chrome options for the Selenium WebDriver with several customizations,
        including user data directory, disabling browser features, setting download preferences, and enabling headless mode.

        The following options are applied:
        - Disables certain Blink features controlled by Automation.
        - Excludes switches for enabling automation.
        - Disables browser extensions.
        - Sets the user data directory for Chrome.
        - Maximizes the browser window.
        - Enables headless mode for running without a graphical interface.
        - Disables GPU usage for headless mode.
        - Disables sandboxing.
        - Disables shared memory usage for the renderer processes.
        - Configures download preferences to avoid download prompts and upgrade downloads.

    # Use the configured WebDriver for automation tasks.

    Example:
        >>> user_data_dir = "/path/to/user-data-directory"
        >>> chrome_options = set_chrome_options(user_data_dir)
        >>> driver = webdriver.Chrome(options=chrome_options)
        >>> driver.get("https://www.example.com")
    """

    chrome_options = Options()
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument(f"user-data-dir={user_data_directory}")
    chrome_options.add_argument("--start-maximized")
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })
    return chrome_options


def search_queries(driver_object, search_within_param: str, query: str) -> int:
    """
    Searches for a specified query within a specified search category using the provided WebDriver instance.

    Args:
        driver_object (WebDriver): The Selenium WebDriver instance used for performing the search.
        search_within_param (str): The search category or filter parameter.
        query (str): The search query to be entered.

    Returns:
        int: The number of search results obtained after the search operation.

    Raises:
        TimeoutException: If the search results are not found within the specified time limit.

    Description:
        This function automates the process of performing a search operation on Scopus web page using Selenium WebDriver.
        It locates the search category dropdown, enters the search category, clears the search input field,
        enters the search query, clicks the search button, waits for the search results to load,
        and then extracts and returns the number of search results as an integer.

    Usage:
        driver = webdriver.Chrome()  # Initialize a Chrome WebDriver instance
        num_results = search_queries(driver, "Category", "Search Query")
        print(f"Number of search results: {num_results}")

    Example:
        >>> driver = webdriver.Chrome()
        >>> num_results = search_queries(driver, "Books", "ALL")
        >>> print(f"Number of search results: {num_results}")
        Number of search results: 3500
    """

    search_within_selector = driver_object.find_element(
        By.CSS_SELECTOR, 'select[data-testid="select-field-select"]')
    search_within_selector.send_keys(search_within_param)

    query_input = driver_object.find_element(
        By.CSS_SELECTOR, 'input[data-testid="search-field-input"]')
    query_input.clear()
    query_input.send_keys(query)

    search_button = driver_object.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    search_button.click()

    row_element = WebDriverWait(driver_object, 7).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        'div[class="SearchResultsHeader-module__Qq2ZF"]')),
        'The number of results was not found!')
    result_number_element = row_element.find_element(By.CSS_SELECTOR, 'h2')

    return int(result_number_element.text.split()[0].replace(',', ''))


def click_all_checkboxes(driver_object, start_at: int, end_at: int, file_format_int: int) -> None:
    """
    Selects all checkboxes within a specified range of search results using the provided WebDriver instance.

    Args:
        driver_object (WebDriver): The Selenium WebDriver instance used for interacting with the web page.
        start_at (str): The starting point of the range of search results.
        end_at (str): The ending point of the range of search results.

    Returns:
        None

    Description:
        This function automates the process of selecting all checkboxes within a specified range of search results
        on Scopus search page. It locates the export button, selects the option to export all results,
        sets the specified range of search results (from start_at to end_at), finds all checkboxes,
        and clicks on each of them. Finally, it clicks the export button to confirm the selection.

    Usage:
        driver = webdriver.Chrome()  # Initialize a Chrome WebDriver instance
        click_all_checkboxes(driver, "1", "100")
        # All checkboxes within the range of 1 to 100 will be selected.

    Example:
        >>> driver = webdriver.Chrome()
        >>> click_all_checkboxes(driver, "1", "50")
        # All checkboxes within the range of 1 to 50 will be selected.
    """

    export_div = driver_object.find_elements(
        By.CSS_SELECTOR, 'div[role="group"]')[-3]

    export_button = export_div.find_elements(
        By.CSS_SELECTOR, 'button')[file_format_int]

    export_button.click()

    driver_object.implicitly_wait(.5)

    all_result_radio_button = driver_object.find_elements(
        By.CSS_SELECTOR, 'input[id="select-current-page"]')[1]
    all_result_radio_button.click()

    results_start = driver_object.find_element(
        By.CSS_SELECTOR, 'input[placeholder="From"')
    results_start.clear()
    results_start.send_keys(start_at)

    results_end = driver_object.find_element(
        By.CSS_SELECTOR, 'input[placeholder="To"')
    results_end.clear()
    results_end.send_keys(end_at)

    checkboxes = driver_object.find_elements(
        By.CSS_SELECTOR, 'span[class="Checkbox-module__SaBg7"')[2:-1]
    for check in checkboxes:
        check.click()

    all_result_radio_button = driver_object.find_element(
        By.CSS_SELECTOR, 'button[data-testid="submit-export-button"')
    all_result_radio_button.click()

    return None


def scopus_search(
    queries_location: str = 'Queries.txt',
    file_format: Literal['CSV', 'RIS', 'BibTeX', 'Plain text'] = 'CSV',
    search_within: Literal["ALL", "TITLE_ABS_KEY", "AUTHOR_NAME",
                           "FIRSTAUTH", "SRCTITLE", "TITLE", "ABS",
                           "KEY", "AFFIL", "AFFILORG", "AFFILCITY",
                           "AFFILCOUNTRY", "FUND_ALL", "FUND_SPONSOR",
                           "FUND_ACR", "FUND_NO", "LANGUAGE", "ISSN",
                           "CODEN", "DOI", "REF", "CONF", "TITLE_ABS_KEY_AUTH",
                           "CHEMNAME", "CASREGNUMBER", "ORCID"] = 'ALL',
    export_interval: int = 500,
    timeout_time: float = 5*60,
    number_of_allowed_retries: int = 3,
    dynamic_timeout: bool = True,
    multiplier: int = 3,
    headless_login: bool = False,
    first: int = 1
) -> None:
    """
    Automates the process of searching and exporting data from Scopus based on specified queries and parameters.

    Args:
        queries_location (str): Path to the file containing search queries. Defaults to 'Queries.txt'.
        file_format (str): File format for exported data (e.g., 'csv'). Defaults to 'csv'.
        search_within (str): Search category or filter parameter. Defaults to 'ALL'.
        export_interval (int): Number of search results per export segment. Defaults to 500.
        timeout_time (float): Timeout duration for each export segment in seconds. Defaults to 300 seconds (5 minutes).
        number_of_allowed_retries (int): Number of allowed retries for failed exports. Defaults to 3.
        dynamic_timeout (bool): Whether to dynamically adjust the timeout based on export duration. Defaults to True.
        multiplier (int): Multiplier used for dynamic timeout calculation. Defaults to 3.

    Returns:
        None

    Description:
        This function automates the process of searching for specified queries on Scopus, exporting the search results
        in segments, and organizing the exported data into separate folders. It utilizes Selenium WebDriver for
        interacting with the Scopus website, exporting data, and handling errors during the export process.

    Usage:
        scopus_search(queries_location='queries.txt', file_format='csv', search_within='ALL',
                      export_interval=500, timeout_time=300, number_of_allowed_retries=3,
                      dynamic_timeout=True, multiplier=3)

    Example:
        >>> scopus_search(queries_location='queries.txt', file_format='csv', search_within='ALL',
                          export_interval=500, timeout_time=300, number_of_allowed_retries=3,
                          dynamic_timeout=True, multiplier=3)
    """
    format_dict = {
        'csv': [0, 'csv'],
        'ris': [1, 'ris'],
        'bibtex': [2, 'bib'],
        'plain text': [3, 'txt']
    }
    file_format_int, file_extension = format_dict[file_format.lower()]

    url: str = 'https://www.scopus.com/search/form.uri'
    logged_in, *_, user_data_dir, user_agent = login(headless=headless_login)

    if not logged_in:
        raise PermissionError("Couldn't log into Scopus")

    current_directory = os.getcwd()
    if not current_directory.endswith('Download'):
        if not os.path.isdir('Download'):
            os.mkdir('Download')
        os.chdir('Download')

    with open(queries_location, 'r+', encoding='utf8') as queries_txt:
        queries = queries_txt.read().strip().split('\n')
        queries = [q for q in queries if q not in os.listdir() and q.strip()]

    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    with webdriver.Chrome(options=set_chrome_options(user_data_dir)) as search_driver:
        log('Search webdriver start')
        print()

        search_driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        search_driver.execute_cdp_cmd("Network.setUserAgentOverride", {
            "userAgent": user_agent})
        search_driver.get(url)

        for input_query in queries:
            flag = True
            query_start_time = time.time()

            directory_name = input_query
            log(f'Searching for "{input_query}"')

            number_of_results = search_queries(
                search_driver, search_within, input_query)
            log(f'{number_of_results:,} results were found')
            number_of_results = min(number_of_results, 20_000)

            list_of_range = list(
                range(first - 1, number_of_results, export_interval))
            list_of_range.append(number_of_results)
            interval_list = list_of_range[1:]
            interval_list.reverse()

            second = interval_list.pop()
            retries = 0

            while flag:
                time_spent = 0
                start_time = time.time()

                for _ in range(number_of_allowed_retries+1):
                    try:
                        export_button = WebDriverWait(search_driver, 7
                                                      ).until(EC.presence_of_element_located(
                                                          (By.CSS_SELECTOR,
                                                           'div[class="export-dropdown"]')),
                            'Dropdown menu was not found!')

                    except ElementNotInteractableException:
                        log('Dropdown menu was not found')
                        search_driver.refresh()

                    else:
                        export_button.click()
                        break

                click_all_checkboxes(search_driver, first,
                                     second, file_format_int)

                log(f'Exporting {first:,}-{second:,} "{input_query}"')

                last_export_percent = 0
                export_progress = tqdm_notebook(total=100)

                while True:
                    time.sleep(1)
                    if os.path.exists(f'scopus.{file_extension}'):
                        if file_extension == 'csv':
                            number_of_results = pd.read_csv(
                                'scopus.csv', low_memory=False).shape[0]
                            message_str = f' ({number_of_results:,} results)'
                        elif file_extension == 'bib':
                            message_str = f' ({get_bib_file_row_count("scopus.bib"):,} results)'
                        else:
                            message_str = f' ({file_extension} file)'

                        with contextlib.suppress(FileExistsError):
                            os.mkdir(directory_name)
                            timeout_time = int(
                                (time.time() - start_time) * multiplier
                            ) if dynamic_timeout else timeout_time

                            log(f'The timeout is set to {timeout_time//60} minutes')

                        os.rename(
                            f'scopus.{file_extension}', f'{input_query}\\{input_query}_{first}-{second}.{file_extension}')
                        log('Download complete' + message_str)

                        export_progress.update(100-export_progress.n)
                        export_progress.close()

                        first = second+1
                        retries = 0

                        try:
                            second = interval_list.pop()
                        except IndexError:
                            flag = False
                            log(
                                f'Exporting "{input_query}" has ended. {time_formatter(query_start_time)} was spent')
                        print()
                        break

                    with contextlib.suppress(NoSuchElementException, StaleElementReferenceException):
                        time_spent = time.time() - start_time
                        if time_spent > timeout_time or search_driver.find_element(By.CSS_SELECTOR, 'div[role="alert"]').text.strip().lower().split()[0] == 'unable':
                            export_progress.close()

                            if time_spent > timeout_time:
                                log(f'Timeout ({timeout_time//60} minutes) reached')
                            else:
                                log('Error occurred while exporting')

                            retries += 1

                            if retries <= number_of_allowed_retries:
                                log(f'Retrying... (retry number {retries})')

                            elif not interval_list:
                                log(f'Exporting "{input_query}" has ended.')
                                log(f'{time_formatter(query_start_time)} was spent')
                                print()
                                log('Moving on to the next query')
                                flag = False

                            else:
                                first = second + 1
                                second = interval_list.pop()
                                retries = 0
                                log('Skipping on to the next segment')

                            break

                        export_percentage = int(search_driver.find_element(By.CSS_SELECTOR,
                                                                           'progress').text.strip()[:-1])
                        if export_percentage != last_export_percent:
                            export_progress.update(
                                export_percentage - last_export_percent)
                            last_export_percent = export_percentage
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    print()
    log('Searching for all search queries has finished')
    return None
