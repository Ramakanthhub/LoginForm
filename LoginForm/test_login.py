
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("12345")

    # Click the actual Login button
    driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()

    message = driver.find_element(By.ID, "message").text

    print("Message:", message)

    if message == "Login Successful!":
        print("Login Test Passed")
    else:
        print("Login Test Failed")

finally:
    driver.quit()
