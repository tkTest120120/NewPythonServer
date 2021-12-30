from time import sleep
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# driver = webdriver.Chrome('./chromedriver')
# driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

url = "https://www.facebook.com/groups/697332711026460/media/photos"

driver.get(url)
sleep(3)
html = driver.page_source

# html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

sum = 0
for link in soup.find_all('img'):
    print(link.get('src'))
    sum += 1

# print(soup)
print(f'sum :  {sum}')

driver.quit()