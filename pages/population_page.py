from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")

    def get_population_count(self):

        population_locator = (
            By.XPATH,
            "//div[contains(@class,'counter-ticker')]"
        )

        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(population_locator)
        )

        return element.text