from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

class music():
    def __init__(self):
        self.service = Service(r"C:/Users/jagad/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")  # Replace with your ChromeDriver path
        self.driver = webdriver.Chrome(service=self.service, options=options)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)

        # Use By.XPATH to locate elements:
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        video.click()

        input("Press Enter to quit...")
        self.driver.quit()
