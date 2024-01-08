import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.ui.gradescope import Gradescope
from src.ui.dashboard import Dashboard
from src.ui.piazza import Piazza
from src.ui.course_info import CourseInfo
from src.ui.student_info import StudentInfo
from src.ui.moodle import Moodle
class TestStreamlitAllMenu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.server_url = "http://localhost:8501"
        # self.login()

    def tearDown(self):
        self.driver.quit()

    def login(self):
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
        time.sleep(5)

    def test_moodle_test(self):
        self.login()
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@title='streamlit_option_menu.option_menu']")
        self.driver.switch_to.frame(iframe_element)
        your_element_inside_iframe = self.driver.find_element(By.XPATH, "//a[normalize-space()='Moodle']")
        your_element_inside_iframe.click()

        self.assertIsNotNone(your_element_inside_iframe)
        time.sleep(1)

    def test_gradescope(self):
        self.login()
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@title='streamlit_option_menu.option_menu']")
        self.driver.switch_to.frame(iframe_element)
        your_element_inside_iframe = self.driver.find_element(By.XPATH, "//a[normalize-space()='Gradescope']")
        your_element_inside_iframe.click()

        self.assertIsNotNone(your_element_inside_iframe)
        time.sleep(1)

    def test_piazza(self):
        self.login()
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@title='streamlit_option_menu.option_menu']")
        self.driver.switch_to.frame(iframe_element)
        your_element_inside_iframe = self.driver.find_element(By.XPATH, "//a[normalize-space()='Piazza']")
        your_element_inside_iframe.click()

        self.assertIsNotNone(your_element_inside_iframe)
        time.sleep(1)

    def test_course_info(self):
        self.login()
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@title='streamlit_option_menu.option_menu']")
        self.driver.switch_to.frame(iframe_element)
        your_element_inside_iframe = self.driver.find_element(By.XPATH, "//a[normalize-space()='Course Info']")
        your_element_inside_iframe.click()

        self.assertIsNotNone(your_element_inside_iframe)
        time.sleep(1)

    def test_student_info(self):
        self.login()
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@title='streamlit_option_menu.option_menu']")
        self.driver.switch_to.frame(iframe_element)
        your_element_inside_iframe = self.driver.find_element(By.XPATH, "//a[normalize-space()='Student Info']")
        your_element_inside_iframe.click()

        self.assertIsNotNone(your_element_inside_iframe)
        time.sleep(1)



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
