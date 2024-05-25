from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()  # Customize options if needed

class maps():
    def __init__(self):
        self.service = Service(r"C:/Users/jagad/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")  # Replace with your ChromeDriver path
        self.driver = webdriver.Chrome(service=self.service, options=options)

    def place(self, query):
        self.query = query
        self.driver.get(url="https://www.google.com/maps/@18.0601188,79.5491037,15z?entry=ttu")

        sleep(1)
        search = self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        enter_button = self.driver.find_element(By.XPATH, '//*[@id="searchbox"]/div[1]')
        search.click()
        search.send_keys(query)
        enter_button.click()

    def direction(self):
        sleep(1)
        dir = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button')
        dir.click()

    def start_point(self,point):
        sleep(1)
        self.point = point
        start = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
        search_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]')
        start.click()
        start.send_keys(point)
        search_button.click()

        input("Press Enter to quit...")  # Or use a different method to keep the browser open
        self.driver.quit()


