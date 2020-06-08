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

# comment these last 2 lines out, if you don't get a pop up asking about notifications
notnow = webdriver.find_element_by_css_selector(
    'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()
print('not now')



hashtag_list = ['moodyports', 'quietthechaos',
                'featuremyworld', 'theportraitculture',
                'cityports', 'earth_portraits', 'portraitsociety',
                'creative_portraits', 'of2humans', 'portraits_mf',
                'aovportrait', 'localwolves', 'pr0ject_soul', 'agameoftones',
                'bravogreatphoto', 'pursuitofportraits', 'gramkilla',
                'portraitgasm', 'yourvisiongallery', 'portraitfolk',
                'ig_mood', 'foundvisuals', 'portraitstream', 'portraits_ig',
                'portraitvision', 'liveauthentic', '777luckyfish',
                'girlsonfilm', 'postthepeople', 'makeportraits', 'expofilm3k', 'life_portraits',
                'thelightsofbeauty', 'bravoportraits', 'humaneffect',
                'expofilm', 'portraits_ig', 'igpodium_portraits']
# hashtag_list = ['gramkilla']


# prev_user_list = []
prev_user_list = pd.read_csv('20200420-131230_users_followed_list.csv',
                             delimiter=',').iloc[:, 1:2]  # useful to build a user log
prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0


for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' +
                  hashtag_list[tag] + '/')
    print('select hashtag')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(randint(1, 2))
    try:
        for x in range(1, 200):
            username = webdriver.find_element_by_css_selector(
                'body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > a').text

            if username not in prev_user_list:
                # follow if not already following
                if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                    webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                    new_followed.append(username)
                    followed += 1
                    print('followed', followed)

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')

                    button_like.click()
                    likes += 1
                    print(likes, 'likes')
                    sleep(randint(20, 30))

                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(25, 29))
                print('next')
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(20, 26))
                print('skip')
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0, len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv(
    '{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('add to csv')
print('Liked {} photos.'.format(likes))
print('Followed {} new people.'.format(followed))
