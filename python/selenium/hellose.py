from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://formy-project.herokuapp.com/form")
    driver.find_element(By.ID, "first-name").send_keys("Firstname")
    driver.find_element(By.ID, "last-name").send_keys("Lastname")
    driver.find_element(By.ID, "job-title").send_keys("Tester")

    driver.find_element(By.CSS_SELECTOR,"a.btn").click()

    wait.until(presence_of_element_located((By.XPATH, "//div[contains(text(),'The form was successfully submitted!')]")))