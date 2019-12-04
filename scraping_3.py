import time
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(5)

count = 1
csvfile = "225.csv"

with open(csvfile, "r") as f:
    rows = csv.reader(f)
    for row in rows:

        print("ループ回数: " + str(count))
        row_str = str("".join(row))

        url = "https://finance.yahoo.com/quote/" + row_str + ".T/history?period1=1230735600&period2=1575126000&interval=1d&filter=history&frequency=1d"
        driver.get(url)
        time.sleep(5)

        page = driver.find_element_by_tag_name("html")

        i = 0
        while i < 20:
            page.send_keys(Keys.END)
            print("スクロールダウン:  " + str(i))
            i = i + 1
            time.sleep(0.5)

        try:
            old_date = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[2713]/td[1]/span').text
            old_stock = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[2713]/td[5]/span').text
            print(old_date)
            print(old_stock)

            now_date = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[1]/td[1]/span').text
            now_stock = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[1]/td[5]/span').text
            print(now_date)
            print(now_stock)


            old_stock = old_stock.replace(',', '')
            now_stock = now_stock.replace(',', '')
            change_rate = float(now_stock)/float(old_stock)
            print(change_rate)
            change_rate_str = str('{:.2f}'.format(change_rate))
            print(change_rate_str)

            with open("225Price.csv", "a") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([row_str, old_date, old_stock, now_date, now_stock, change_rate_str])

            count = count + 1
            time.sleep(1)

        except:
            print("try error:: データ取得できず....")
            with open("225Price.csv", "a") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([row_str, "エラー"])
            csvFile.close()

            count = count + 1
            time.sleep(1)