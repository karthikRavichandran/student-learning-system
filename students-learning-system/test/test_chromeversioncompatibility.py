
import unittest
from selenium import webdriver


class TestChromeVersionCompatibility(unittest.TestCase):

    def test_chrome_version_compatibility(self):
        # Specify the expected Chrome version
        expected_chrome_version = 'localhost'  # Update this to the version you expect

        # Get the actual Chrome version
        actual_chrome_version = self.get_chrome_version()

        # Check if the actual version matches the expected version
        self.assertEqual(actual_chrome_version, expected_chrome_version,
                         f"Chrome version mismatch. Expected: {expected_chrome_version}, Actual: {actual_chrome_version}")

        # Additional tests or actions with the web application using selenium can be added here

    def get_chrome_version(self):
        # Use selenium to open Chrome and retrieve its version
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')  # Run Chrome in headless mode
            driver = webdriver.Chrome(options=chrome_options)
            version_info = driver.capabilities['goog:chromeOptions']['debuggerAddress']
            chrome_version = version_info.split(' ')[0].split(":")[0]
            return chrome_version
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()
