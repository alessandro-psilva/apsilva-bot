from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random



class ApsilvaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver   = webdriver.Firefox(
            executable_path='geckodriver\geckodriver.exe')
        
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)

        # username
        user_element = driver.find_element_by_xpath(
            '//input[@name="username"]')
        user_element.click()
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)

        # password
        password_element = driver.find_element_by_xpath(
            '//input[@name="password"]')
        password_element.click()
        password_element.clear()
        time.sleep(random.randint(4, 6))
        password_element.send_keys(self.password)

        # Conecta
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))

    def like_photos(self):
        driver  = self.driver
        hashtag = input('hashtag: ')
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)

        for pagina in range(1, 5):
            script = "window.scrollTo(0, document.body.scrollHeight);"
            driver.execute_script(script)
            time.sleep(3)

        row_hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [href.get_attribute("href") for href in row_hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))

if __name__ == '__main__':
    apsilva_bot = ApsilvaBot(
        username=input('username: '),
        password=input('password: ')
    )

    apsilva_bot.login()
    apsilva_bot.like_photos()