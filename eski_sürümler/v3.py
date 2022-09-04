#
#   whatsapp otomatik profil fotoğrafı değiştirici
#   by @zewzack
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random, os

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_executable = Service(executable_path='chromedriver.exe', log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get('https://web.whatsapp.com/')

sleep(3)
input('qr kodu okuttuktan sonra herhangi bir tuşa basınız...')
 
for x in range(100):
 dir = ("C:\\Users\\zewza\\Pictures\\Saved Pictures\\")
 random_picture = random.choice(os.listdir(dir))
 random_filename = (dir,random_picture)
 
 sleep(3)
 filepath = (random_filename)
 
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
 sleep(2)

 for x in range(5):
    minus_box = driver.find_element("xpath", '//span[@data-icon="minus"]')
    minus_box.click()

 sleep(3)
 send_button = driver.find_element("xpath", '//span[@data-icon="checkmark-large"]')
 send_button.click()

 sleep(2)
 back_button = driver.find_element("xpath", '//span[@data-icon="back"]')
 back_button.click() 
 sleep(10)
