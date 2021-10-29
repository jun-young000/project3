from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


url='https://www.menupan.com/Restaurant/search/search_main.asp?areacode=jj201'

driver=wd.Chrome(executable_path='chromediver.exe')