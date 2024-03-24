from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv
from datetime import datetime




chromedriver_path = '/Users/0heon_j/Desktop/NEXT/Session/NEXT_Session_6/chromedriver-mac-arm64/chromedriver'
user_data_dir = "/Users/0heon_j/Desktop/NEXT/HW/NEXT_HW_6/results"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://news.hada.io/')


today = datetime.now().strftime('%Y%m%d')

filename = f'{today}_dev_article.csv'

with open(filename, mode="w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["title", "content", "info"])
    
   
    for i in range(1, 21):
        try:
            title = driver.find_element(By.XPATH, f'/html/body/main/article/div/div[{i}]/div[3]').text
            content = driver.find_element(By.XPATH, f'/html/body/main/article/div/div[{i}]/div[4]/a').text
            info = driver.find_element(By.XPATH, f'/html/body/main/article/div/div[{i}]/div[5]').text
            writer.writerow([title, content, info])
        except Exception as e:
            print(f"Error processing article {i}: {e}")
    
file.close()