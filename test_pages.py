import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

class SullenClothing:

    URL = "https://sullenclothing.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

        self.men_menu = (By.CSS_SELECTOR, "summary[data-follow-link='/collections/new-releases']")
        self.standard_tees = (By.CSS_SELECTOR, "a[href='/collections/standard-tees']")
        self.premium_tees = (By.CSS_SELECTOR, "a[href='/collections/premium']")
        self.longsleeves = (By.CSS_SELECTOR, "a[href='/collections/long-sleeves']")

    def open(self):
        self.driver.get(self.URL)    

    def close_popup(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "adroll_allow_all"))).click()    

    def hover_men(self):
        menu = self.wait.until(EC.visibility_of_element_located(self.men_menu))
        self.actions.move_to_element(menu).perform()

    def click_standard_tees(self):
        self.hover_men()
        self.wait.until(EC.element_to_be_clickable(self.standard_tees)).click()

    def click_premium_tees(self):
        self.hover_men()
        self.wait.until(EC.element_to_be_clickable(self.premium_tees)).click()

    def click_longsleeves(self):
        self.hover_men()
        self.wait.until(EC.element_to_be_clickable(self.longsleeves)).click()

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))).text

