import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

class HelloTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def test_hello_text(self):
        driver = self.driver
        driver.get('http://localhost:5000')
        time.sleep(5)
        
        hello_button = driver.find_element_by_id("hellobtn")
        hello_textarea = driver.find_element_by_id("hellotext")

        hello_button.click()
        assert "Hello" in hello_textarea.get_attribute('value')
        hello_button.click()
        assert "Hello\nHello" in hello_textarea.get_attribute('value')
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()