import pytest
import time
import csv
from selenium import webdriver
from pages.population_page import PopulationPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_population_live(driver):
    page = PopulationPage(driver)
    page.load()


    log_file = "logs/population_log.csv"
    with open(log_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Population Count"])

        try:
            while True:
                population = page.get_population_count()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp} - Current World Population: {population}")


                writer.writerow([timestamp, population])
                file.flush()

                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopped by user (Ctrl+C).")
