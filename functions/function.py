from time import sleep
import os
from selenium import webdriver
from bs4 import BeautifulSoup
# import requests
import json
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from functions import APIdatabase as db
import datetime
from flask import send_file

time = datetime.datetime.now()

def get_Link_img(url):

    if int(db.getTime(1)) == time.day:
        return json.dumps( db.get_Link() )
    else:
        db.insert_or_Update_Time(1 , time.day)

        op = webdriver.ChromeOptions()
        op.binary_location = os.environ.get("GOOGLE CHROME_BIN")
        op.add_argument("--headless")
        op.add_argument("--no-sandbox")
        op.add_argument("--disable-dev-sh-usage")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

        driver.get(url)

        sleep(2)
        for i in range(6):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight + 10000)")
            sleep(2)

        html = driver.page_source

        # html = requests.get(url).text

        soup = BeautifulSoup(html, 'html.parser')

        sum = 0
        link_list = []

        for link in soup.find_all('img'):
            link = link.get('src')
            # print(link)
            sum += 1
            link_list.append(link)
            # insert to database
            db.insert_or_Update_Link(0 , link)

        # print(soup)
        print(f'sum :  {sum} link ảnh')
        link_json = json.dumps(link_list)
        # print(link_json)

        driver.quit()
        return link_json

def get_Link_Img_from_WEB(url):
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=op)

    driver.get(url)

    sleep(2)
    for i in range(12):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight + 20000)")
        sleep(0.5)

    html = driver.page_source

    # html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser')

    sum = 0
    link_list = []

    for link in soup.find_all('img'):
        link = link.get('src')
        # print(link)
        sum += 1
        link_list.append(link)

    # print(soup)
    print(f'sum :  {sum} link ảnh ' + '-' * 200)
    link_json = json.dumps(link_list)
    # print(link_json)

    driver.quit()
    return link_json

def get_Link_ImgHD_from_WEB():
    pass

def lai_Ngan_hang(tien_gui = 0 , lai_suat = 0 , so_Ngay_Gui = 0):
    soTienGui = int(tien_gui)
    # print(soTienGui)

    laiSuat_Nam = float(lai_suat)
    laiSuat = laiSuat_Nam / 100
    # print(laiSuat_Nam)
    # print(laiSuat)

    soNgayGui = int(so_Ngay_Gui)
    # print(soNgayGui)

    tienLai = ((soTienGui * laiSuat) / 365) * soNgayGui
    print()
    print("Tiền lãi của bạn là: ", float(tienLai), end=" ")
    print("VND")
    print("Tiền lãi của bạn sau khi làm tròn là: ", int(tienLai), end=" ")
    print("VND \n")
    print()
    return f"Tiền lãi của bạn là :  {int(tienLai)} VNĐ"

from gtts import gTTS
# import playsound
import os

def speak(text):
    path = str(os.getcwd())
    fileName = path + "/private/sound.mp3"
    # print(fileName)
    # print("Trợ Lý ảo:  ", text)

    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # rate = engine.getProperty('rate')
    # volume = engine.getProperty('volume')
    # engine.setProperty('volume', volume - 0.0)  # tu 0.0 -> 1.0
    # engine.setProperty('rate', rate - 50)
    # engine.setProperty('voice', voices[1].id)
    # engine.say(text)
    # engine.runAndWait()


    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save(fileName)
    # playsound.playsound("sound.mp3", True)
    # os.remove("sound.mp3")
    print("\n\nxong")
    return send_file(fileName)