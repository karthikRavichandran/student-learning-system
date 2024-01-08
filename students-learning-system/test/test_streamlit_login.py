import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestStreamlitLoginApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.server_url = "http://localhost:8501"

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        self.driver.get(self.server_url)
        time.sleep(3)
        # Enter valid credentials
        self.enter_credentials("bob", "bobpw")
        time.sleep(3)
        # Click the login button
        login_button = self.driver.find_element(By.XPATH, "//p[normalize-space()='Login']")
        login_button.click()
        login_button = self.driver.find_element(By.XPATH, "//p[normalize-space()='Login']")
        login_button.click()
        login_button = self.driver.find_element(By.XPATH, "//p[normalize-space()='Login']")
        login_button.click()

        # Wait for the success message
        time.sleep(3)  # Introduce a brief delay to allow the page to update
        success_message = self.driver.find_element(By.XPATH, "//p[normalize-space()='Logout']")

        # Check if the success message is displayed
        self.assertIsNotNone(success_message)

    def test_invalid_login(self):
        self.driver.get(self.server_url)
        time.sleep(3)
        # Enter invalid credentials
        self.enter_credentials("invalid_user", "invalid_password")
        time.sleep(3)
        # Click the login button
        # login_button = self.driver.find_element(By.CLASS_NAME, 'row-widget stButton')
        login_button = self.driver.find_element(By.XPATH, "//p[normalize-space()='Login']")
        login_button.click()

        # Wait for the error message
        time.sleep(10)  # Introduce a brief delay to allow the page to update
        error_message = self.driver.find_element(By.XPATH, "//p[normalize-space()='Username/password is incorrect']")

        # Check if the error message is displayed
        self.assertIsNotNone(error_message)

    def enter_credentials(self, username, password):
        # Find and enter the username
        # driver.find_elements_by_css_selector("[aria-label=XXXX]")
        # driver.find_elements(By.CSS_SELECTOR, 'p.product-card__name')
        username_input = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label=Username]")[0]
        username_input.send_keys(username)

        # Find and enter the password
        password_input = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label=Password]")[0]
        password_input.send_keys(password)


if __name__ == '__main__':
    unittest.main()
