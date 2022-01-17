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
import function.database as db
import datetime

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
    for i in range(8):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight + 10000)")
        sleep(1)

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