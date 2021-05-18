from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class ApsilvaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver   = webdriver.Firefox(
            executable_path='geckodriver\geckodriver.exe'
            )
        
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)

        # username
        user_element = driver.find_element_by_xpath(
            '//input[@name="username"]')
        user_element.click()
        user_element.clear()
        user_element.send_keys(self.username)

        # password
        password_element = driver.find_element_by_xpath(
            '//input[@name="password"]')
        password_element.click()
        password_element.clear()
        password_element.send_keys(self.password)

        # Conecta
        password_element.send_keys(Keys.RETURN)

if __name__ == '__main__':
    apsilva_bot = ApsilvaBot(
        username=input('username: '),
        password=input('password: ')
    )

    apsilva_bot.login()