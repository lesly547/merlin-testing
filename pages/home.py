from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.google.es/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_search = "q"
        self.key_search = "//h3[contains(text(),'Wikipedia')]"
        self.button_accept_cookies = "//div[@class='QS5gu sy4vM' and contains(text(),'Aceptar todo')]"
        self.div_cookies = "//div[@class='jw8mI']"

    def get_textarea_search(self):
        return self.driver.find_element(By.XPATH, self.textarea_search)

    def find_div_cookies(self):
        return self.driver.find_element(By.XPATH, self.div_cookies)

    def get_key_search(self):
        return self.driver.find_element(By.XPATH, self.key_search)

    def find_button_accept_cookies(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.button_accept_cookies)))

    def find_search_tool(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, self.input_search)))

    @staticmethod
    def get_base_url():
        return base_url
