from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os



class ApsilvaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver   = webdriver.Firefox(
            executable_path='geckodriver\geckodriver.exe')

        os.system("cls")
        
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

        script = "window.scrollTo(0, document.body.scrollHeight);"

        qtde_pag = int(input('qtde_paginas: '))
        for pagina in range(1, qtde_pag):
            driver.execute_script(script)
            time.sleep(3)

        row_hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [href.get_attribute("href") for href in row_hrefs]

        qtde_links     = len(pic_hrefs)
        qtde_links_erro  = 0
        qtde_links_sucesso  = 0

        for href in pic_hrefs:
            try:
                href.index("https://www.instagram.com/p")
                qtde_links_sucesso += 1
            except ValueError as err:
                qtde_links_erro += 1
                continue

            driver.get(href)

            try:
                time.sleep(random.randint(19, 23))  
                driver.execute_script(script)              
                driver.find_element_by_xpath(
                    '//span[@class="fr66n"]').click()
            except Exception as e:
                print(e)
                time.sleep(5)

            os.system("cls")
            print('Total de links recuperados {}'.format(qtde_links))
            print('Total de links com sucesso {}'.format(qtde_links_sucesso))
            print('Total de links com erro {}'.format(qtde_links_erro))      

if __name__ == '__main__':
    apsilva_bot = ApsilvaBot(
        username=input('username: '),
        password=input('password: ')
    )

    apsilva_bot.login()
    apsilva_bot.like_photos()