#   Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#   Standard static stuff
URL = 'https://memes.com/'
CHROMEDRIVER_PATH = 'chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)
os.system('cls')

#   Main scrape
with webdriver as driver:

    #   Define timeout
    wait = WebDriverWait(driver, 5)

    #   Get website source
    driver.get(URL)

    #   Wait until meme loads
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'post-body-container')))

    #   Find meme
    memes = driver.find_elements_by_class_name('post-media-container')
    for meme in memes:
        meme = meme.find_elements_by_tag_name('img')
        for meme_img in meme:
            image = meme_img.get_attribute('src')
            print(image)
            break
        break

    #   Close browser
    driver.close()
