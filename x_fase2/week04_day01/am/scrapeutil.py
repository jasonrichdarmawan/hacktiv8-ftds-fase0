from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install())
# )

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
)

print("connected")

def get_db():
    return "db"