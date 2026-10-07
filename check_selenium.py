from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup

import requests
import shutil
from urllib.parse import urlparse
import json
import time
from datetime import datetime

import smtplib
import random
import math

import tempfile
from os import listdir
from pathlib import Path
import os.path
import os
import codecs
import io
import pandas as pd
import openpyxl 


DATA_PATH = Path.cwd()


with tempfile.TemporaryDirectory() as tmpdirname:
        chrome_options = webdriver.ChromeOptions()
        #chromium_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode
        chrome_options.add_argument('--remote-debugging-pipe')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-extensions")
        preferences = {"download.default_directory": tmpdirname,
               "download.prompt_for_download": False,
               "download.directory_upgrade": True}
        chrome_options.add_experimental_option("prefs",preferences)
        # options.setCapability(

        driver = webdriver.Chrome(options=chrome_options)

        #driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        #self.driver = webdriver.Chrome(service=driver_path, options=chromium_options)

        page = driver.get("https://translate.google.com/?sl=de&tl=en&op=translate")
        print(page)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, 'gb')))
        ##element = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea')))
        print(element)
        ##driver.find_element(By.XPATH, "//button[@form='login']")

