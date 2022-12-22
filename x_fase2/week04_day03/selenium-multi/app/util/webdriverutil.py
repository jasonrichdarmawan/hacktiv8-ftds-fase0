from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from configparser import ConfigParser

caps = DesiredCapabilities.CHROME.copy()
caps['pageLoadStrategy'] = "none"

drivers = {}

secret = ConfigParser()
secret.read('./secret.ini')

email = secret['DEFAULT']['email']
password = secret['DEFAULT']['password']

def get_or_load_driver(symbol: str):
    driver = drivers.get(symbol)
    
    if driver is None:
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
        #                           desired_capabilities=caps)
        driver = webdriver.Remote(desired_capabilities=caps)
    
        driver.get('https://stockbit.com/login')
        WebDriverWait(
            driver=driver, 
            timeout=30).until(EC.presence_of_element_located((By.XPATH, "//button[@id='email-login-button']")))
        driver.find_element(by=By.XPATH, value="//input[@id='username']").send_keys(email)
        driver.find_element(by=By.XPATH, value="//input[@id='password']") \
              .send_keys(password)
        driver.find_element(by=By.XPATH, value="//button[@id='email-login-button']") \
              .click()
        WebDriverWait(
            driver=driver, 
            timeout=30).until(EC.presence_of_element_located((By.XPATH, "//img[@class='announcement-image']")))
    
    url = f'https://stockbit.com/#/symbol/{symbol}'

    if driver.current_url != url:
        driver.get(url=url)
    
    drivers[symbol] = driver
    
    return driver

def get_comments(driver: WebDriver, end_at: int):
    while True:
        # if not logged in
        # date_elements = driver.find_elements(by=By.XPATH, value="//a[@color='#B5B5B5']")
        # if logged in
        date_elements = driver.find_elements(by=By.XPATH, value="//div[@class='stream-date']")
        
        # Handle: IndexError: list index out of range
        if len(date_elements) != 0: break
        
    while True:
        if len(date_elements) < end_at:
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
            date_elements = driver.find_elements(by=By.XPATH, value="//div[@class='stream-date']")
        else: break
        
    # Handle: All arrays must be of the same length
    # if not logged in
    # comment_elements = driver.find_elements(by=By.XPATH, value="//p[@color='#333333' and @style='word-wrap:break-word']")
    # if logged in
    comment_elements = driver.find_elements(by=By.CLASS_NAME, value="stream-text-single")
        
    dates = []
    comments = []
        
    for index, (date_element, comment_element) in enumerate(zip(date_elements, comment_elements)):
        # Handle: StaleElementReferenceException or ''
        if index == len(date_elements) - 1:
            break
        
        dates.append(date_element.text)
        comments.append(comment_element.text)
    
    return pd.DataFrame(data={'date': dates, 'comment': comments})