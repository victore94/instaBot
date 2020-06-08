from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import os

username = os.environ.get('USER')
password = os.environ.get('PASS')

# Change this to your own chromedriver path!
chromedriver_path = '/Users/Victor/Downloads/chromedriver'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys(username)
password = webdriver.find_element_by_name('password')
password.send_keys(password)

button_login = webdriver.find_element_by_css_selector(
    '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
button_login.click()
print('logged in')
sleep(3)

notnow = webdriver.find_element_by_css_selector(
    'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()
print('not now')

user = 'petermckinnon'
webdriver.get('https://www.instagram.com/' + user + '/')
print('get user profile')
sleep(randint(3, 10))

first_thumbnail = webdriver.find_element_by_css_selector(
    '#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1)')
first_thumbnail.click()
print('clicked thumbnail')
sleep(randint(3, 10))

button_like = webdriver.find_element_by_xpath(
    '/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button')
button_like.click()
sleep(randint(3, 10))

for n in range(1, 12):
    if webdriver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div/div/div[' + str(n) + ']/div[3]/button').text == 'Follow':
        webdriver.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div/div/div[' + str(n) + ']/div[3]/button').click()
        sleep(randint(2, 20))
    continue
