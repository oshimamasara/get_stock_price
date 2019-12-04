import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(5)

url = "https://finance.yahoo.com/quote/4151.T/history?period1=1230735600&period2=1575126000&interval=1d&filter=history&frequency=1d"
driver.get(url)
time.sleep(5)

page = driver.find_element_by_tag_name("html")
page.send_keys(Keys.END)

old_date = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[2713]/td[1]/span').text
old_stock = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[2713]/td[5]/span').text
print(old_date)
print(old_stock)

now_date = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[1]/td[1]/span').text
now_stock = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[1]/td[5]/span').text
print(now_date)
print(now_stock)