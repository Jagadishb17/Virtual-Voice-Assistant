import pyttsx3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver .chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()  # Customize options if needed

class infow():
    def __init__(self):
        self.service = Service(r"C:/Users/jagad/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")  # Replace with your ChromeDriver path
        self.driver = webdriver.Chrome(service=self.service, options=options)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

        # Use By.XPATH to locate elements:
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        enter_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')

        # Interact with elements:
        search.click()
        search.send_keys(query)
        enter_button.click()  # Use parentheses for calling the click method

        first_paragraph = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]')
        paragraph_text = first_paragraph.text



        engine = pyttsx3.init()  # Initialize the text-to-speech engine
        engine.say(paragraph_text)  # Pass the text to be spoken
        engine.runAndWait()

        # Prevent immediate closure:
        input("Press Enter to quit...")  # Or use a different method to keep the browser open
        self.driver.quit()

