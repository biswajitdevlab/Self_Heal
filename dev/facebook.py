from selenium.webdriver.common.by import By
from selenium import webdriver
class facebook_test_cases():
        driver=webdriver.Chrome()
        driver.get("https://www.facebook.com")
        driver.find_element(By.ID,'email').send_keys('abc123@gmail.com')
        driver.find_element(By.ID,'pass').send_keys('rama3456')
        driver.find_element(By.LINK_TEXT,'Log in').click()
        driver.quit()
facebook_test_cases()