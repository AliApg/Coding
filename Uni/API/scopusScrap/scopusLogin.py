import os
import shutil

from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver

from .scopusUtils import log


def login(
    user_name: str = 'sut402@yopmail.com',
    pass_word: str = 'biblio402@SUT',
    headless: bool = True,
    clear_cash: bool = False
) -> tuple[bool, str, str] | tuple[bool, str, list[dict[str, str | bool]], str, str]:
    """
    This function logs in to the Scopus website using the provided username, password, and a random user agent.

    Args:
        user_name (str): Your Scopus account username. Default is 'sut402@yopmail.com'.
        pass_word (str): Your Scopus account password. Default is 'biblio402@SUT'.
        headless (bool): If True, the browser will run in headless mode (without a graphical interface). Default is True.

    Returns:
        Tuple[bool, str, list[dict[str, str | bool]], str, str]:
            - A tuple containing a boolean indicating whether the login was successful (True) or not (False).
            - The page title after login.
            - List of Selenium cookies.
            - User data directory path used for the Chrome browser.
            - User agent string used in the browser.

    Raises:
        TimeoutException: If certain elements on the Scopus website are not found within the specified time limit.

    Usage:
        Set your Scopus account username and password in the 'user_name' and 'pass_word' function arguments when calling this function, or use the default values.
        After calling this function, check the return value to verify if the login was successful.

    Example:
        >>> login()
        (True, 'Scopus - Document search | Signed in', [<selenium cookie objects>], 'path/to/user-data-dir', 'user-agent-string')
    """

    user_data_dir = os.getcwd()
    user_data_dir = user_data_dir[:-len('\\Download')] if user_data_dir.endswith(
        '\\Download') else user_data_dir
    user_data_dir += '\\selenium'

    if clear_cash:
        try:
            shutil.rmtree(user_data_dir)
            log('Cash folder has been cleared')
        except FileNotFoundError:
            log('Cash folder does not exist')

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'user-data-dir={user_data_dir}')
    if headless:
        chrome_options.add_argument("--headless=new")

    # Initialize Chrome driver
    user_agent = UserAgent().random
    with webdriver.Chrome(options=chrome_options) as driver:
        log('Login webdriver start')
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {
                               "userAgent": user_agent})
        driver.get('https://www.scopus.com')
        driver.get('https://www.scopus.com/signin.uri')

        title = driver.title
        valid_titles = ['Scopus preview -  \nScopus - Welcome to Scopus',
                        'Scopus preview - Scopus - Welcome to Scopus',
                        'Scopus - Document search | Signed in']

        if title in valid_titles:
            print('You are already signed in!\n')
            return True, user_data_dir, user_agent

        try:
            # Fill in the username and click continue
            email_input = driver.find_element(
                By.CSS_SELECTOR, 'input[name="pf.username"]')
            email_input.send_keys(user_name)
            log('Username entered')

            continue_button = driver.find_element(
                By.CSS_SELECTOR, 'button[name="action"]')
            continue_button.click()
        except NoSuchElementException:
            pass

        # Fill in the password and click sign in
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[name="password"]')),
            'Password aria was not found!'
        )
        password_input.send_keys(pass_word)
        log('Password entered')

        signin_button = driver.find_element(
            By.CSS_SELECTOR, 'button[name="action"]')
        signin_button.click()

        # Get Selenium cookies
        selenium_cookies = driver.get_cookies()
        title = driver.title

        print(title, end='\n\n')
        return (
            True if title in valid_titles else False,
            title,
            selenium_cookies,
            user_data_dir,
            user_agent
        )
