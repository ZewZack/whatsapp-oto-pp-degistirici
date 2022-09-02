#
#   whatsapp otomatik profil fotoğrafı değiştirici
#   @zewzack
#
from time import sleep
from typing import ByteString
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random, os
import sys
import time

options = Options()
#   chrome'un kurulu olduğu ana dizini aşağıya girin:
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
#   seleniumun ve otomasyonun doğru çalışması için chromedriver indirdikten sonra aşağıda belirttiğim klasör yoluna chromedriver.exe yi atın.
#   sistem değişkenlerinde SYSTEM PATH ayarlayıp daha sonra çalışıp çalışmadığını cmd -> chromedriver ile anlayabilirsiniz.
#   eğer çıktı vermiyor ise instagram: @zewzack ulaşabilirsiniz. her zaman yardımcı olmaya çalışırım.
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Program Files\chromedriver\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

input('qr kodu okuttuktan sonra herhangi bir tuşa basınız...')
 
for x in range(7):
 path = r"C:\Users\zewza\Pictures\Saved Pictures"
 random_filename = random.choice([
     x for x in os.listdir(path)
     if os.path.isfile(os.path.join(path, x))
 ])
 
 sleep(3)
 #filepath = input('Enter your filepath (images/video): ')
 resim = r"C:\Users\zewza\Pictures\Saved Pictures\test.jpg"
 filepath = (resim)
 
 sleep(2)
 user = driver.find_element("xpath", '//img[@class="_8hzr9 M0JmA i0jNr"]')
 user.click()

 sleep(2)
 attachment_box = driver.find_element("xpath", '//div[@class="_3yg5l"]')
 attachment_box.click()

 sleep(2)
 attachment_box = driver.find_element("xpath", '//div[@aria-label = "Fotoğraf Yükle"]')
 attachment_box.click()

 sleep(3)
 image_box = driver.find_element("xpath", '//input[@accept="image/gif,image/jpeg,image/jpg,image/png"]')
 image_box.send_keys(filepath)

 sleep(3)
 send_button = driver.find_element("xpath", '//span[@data-icon="checkmark-large"]')
 send_button.click()

 sleep(2)
 back_button = driver.find_element("xpath", '//span[@data-icon="back"]')
 back_button.click() 
 sleep(10)

# -----------------------------------------------------------------------------------------------------------------

 resim2 = r"C:\Users\zewza\Pictures\Saved Pictures\test2.jpg"
 filepath2 = (resim2)

 sleep(2)
 user = driver.find_element("xpath", '//img[@class="_8hzr9 M0JmA i0jNr"]')
 user.click()

 sleep(2)
 attachment_box = driver.find_element("xpath", '//div[@class="_3yg5l"]')
 attachment_box.click()

 sleep(2)
 attachment_box = driver.find_element("xpath", '//div[@aria-label = "Fotoğraf Yükle"]')
 attachment_box.click()

 sleep(3)
 image_box = driver.find_element("xpath", '//input[@accept="image/gif,image/jpeg,image/jpg,image/png"]')
 image_box.send_keys(filepath)

 sleep(3)
 send_button = driver.find_element("xpath", '//span[@data-icon="checkmark-large"]')
 send_button.click()

 sleep(2)
 back_button = driver.find_element("xpath", '//span[@data-icon="back"]')
 back_button.click() 
 sleep(10)
