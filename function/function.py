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

def get_Link_img(url):
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")
    driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = op)



    # chrome_options = webdriver.ChromeOptions()
    # prefs = {
    #     "profile.managed_default_content_settings.images": 2
    # }
    # chrome_options.add_experimental_option("prefs", prefs)

    # driver = webdriver.Chrome('./chromedriver')
    # driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    # url = "https://www.facebook.com/groups/697332711026460/media/photos"

    driver.get(url)

    sleep(2)
    driver.execute_script("window.scroll(0 , 10000)")
    sleep(3)
    driver.execute_script("window.scroll(0 , 10000)")
    sleep(3)

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
    print(f'sum :  {sum} link ảnh')
    link_json = json.dumps(link_list)
    # print(link_json)

    driver.quit()
    return link_json