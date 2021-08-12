from time import sleep
from selenium import webdriver

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://popcat.click/")
a = driver.find_element_by_xpath('//*[@id="app"]/div')
while True:
    a.click()
    sleep(0.055)