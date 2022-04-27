from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('D:/Python_BOT/Curso/chromedriver')
driver.get('https://registro.br/')

time.sleep(8)
driver.close()