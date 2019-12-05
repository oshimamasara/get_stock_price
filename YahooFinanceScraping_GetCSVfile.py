from selenium import webdriver
import os
import time
import csv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
csvfile = "225.csv"

def get_csv():
    count = 1
    with open(csvfile, "r") as f:
        rows = csv.reader(f)
        for row in rows:
            print("Yahoo Finance アクセス回数: " + str(count))
            row_str = str("".join(row))

            url = "https://finance.yahoo.com/quote/" + row_str + ".T/history?period1=946652400&period2=1575385200&interval=1d&filter=history&frequency=1d"
            driver.get(url)
            time.sleep(5)

            page = driver.find_element_by_tag_name("html")

            try:
                download_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a')))
                download_button.click()
                time.sleep(3) 

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


def create_225data():
    count = 1
    with open(csvfile, "r") as f:
        rows = csv.reader(f)
        for row in rows:
            print("225銘柄読み込み中... ループ回数: " + str(count))
            row_str = str("".join(row))
            stock_csvfile = open(row_str + ".T.csv")
            df = pd.read_csv(stock_csvfile)
            old_date = df.iloc[0][0]
            new_date = df.iloc[-1][0]
            old_price = df.iloc[0][4]
            new_price = df.iloc[-1][4]

            with open("my225.csv", "a") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([row_str, old_date, old_price, new_date, new_price])

            count = count + 1
            time.sleep(1)


print("--- START ---")
get_csv()
create_225data()
print("--- FINISH ---")