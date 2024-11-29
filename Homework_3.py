from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


amazon_logo = driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")
create_account = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
your_name = driver.find_element(By.ID, "ap_customer_name")
email = driver.find_element(By.ID, "ap_email")
password = driver.find_element(By.ID, "ap_password")
password_must_be_at_least_6 = driver.find_element(By.ID, "auth-password-requirement-info")
re_enter_password_field = driver.find_element(By.ID, "ap_password_check")
create_your_amazon_account_button = driver.find_element(By.ID, "continue")
conditions_of_use = driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'condition_of_use')]")
privacy_notice = driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'privacy_notice')]")
sign_in_bottom = driver.find_element(By.CSS_SELECTOR, "div.a-row a.a-link-emphasis")

driver.quit()