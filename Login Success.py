import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://myappventure.herokuapp.com/login"
email="vyanuarpr29@gmail.com"
passw="y0urN@m3"

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #test case pertama
    def test_passed_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(response_data, 'Kata Sandi Benar')

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()