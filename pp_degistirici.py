#
#   whatsapp otomatik profil fotoğrafı değiştirici
#   by @zewzack
#
from doctest import master
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random, os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from importlib.resources import path
from tkinter import *

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_executable = Service(executable_path='chromedriver.exe', log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get('https://web.whatsapp.com/')
sleep(1)

# QR kodu okuttuktan sonra devam etmek için butona basın.
def devamet():
    window.destroy()

window = tk.Tk()
window.eval('tk::PlaceWindow . center')
button = tk.Button(
    text="QR kodu okuttuktan sonra bana tıkla",
    width=50,
    height=10,
    bg="black",
    fg="white",
    command=devamet
)
button.pack()
window.mainloop()
# butona basınca üstteki devamet() fonksiyonu window.destroy() eder ve program devam eder.

# ___________________________________________________________________________________________________________________________________

win = Tk()
win.geometry("750x250")

def kapat():
   win.destroy()

Label(win, text="resimlerin olduğu dosyayı seçin:", font=('Aerial 18 bold')).pack(pady=20)
button= ttk.Button(win, text="Select", command= kapat)

button.pack(ipadx=5, pady=15)
win.mainloop()

dir = filedialog.askdirectory(title="dosya dizini seçin")

# dir konumu kullanıcıdan alındı.

# __________________________________________________________________________________________________________________________________

for x in range(100):
 #dir = input("Resimlerin alınacağı konumu giriniz: ") # C:/Users/zewza/Pictures/Saved Pictures/
 #dir = ("C:/Users/zewza/Pictures/Saved Pictures/")
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
