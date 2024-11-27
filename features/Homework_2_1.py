from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fsign-in.html&psig=AOvVaw39FVXWHQ-Yz0kFHHJjilfW&ust=1732495433222000&source=images&cd=vfe&opi=89978449&ved=0CAYQrpoMahcKEwior9vI3vOJAxUAAAAAHQAAAAAQBA")

amazon_logo = driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")
amazon_email_search_field = driver.find_element(By.ID, "ap_email")
amazon_continue_button = driver.find_element(By.ID, "continue")
amazon_conditions_of_use = driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")[0]
amazon_privacy_notice = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(), 'Privacy Notice')]")
amazon_need_help_link = driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?')]")
amazon_forgot_your_password_link = driver.find_element(By.XPATH, "//div//a[@id='auth-fpp-link-bottom']")
amazon_other_issues_with_sign_in_link = driver.find_element(By.XPATH, "//div//a[@id='ap-other-signin-issues-link']")
amazon_create_your_amazon_account_button = driver.find_element(By.ID, "createAccountSubmit")

driver.quit()