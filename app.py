from flask import Flask, render_template, request, flash, send_file
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import requests
import pandas as pd
import gspread
import csv
import time
import os
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
app.secret_key = "lousieasy2digital_19u04358454"

@app.route("/bot")

def index():
	flash("Please enter a sector or product category or product type keyword. For example, smart home")
	return render_template("index.html")


@app.route("/Result", methods=["POST", "GET"])
def StoreUrl():
	flash("Great! " + str(request.form['kw_input']) + " - This is the scraped on-going crowdfunding project, check it out!")

	kickstarterBot = []

	keyword = str(request.form['kw_input'])

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('lang=zh_CN.UTF-8')
	chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
	chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), options=chrome_options)

	for x in range (1,3):

		try:
			URL = driver.get('https://www.kickstarter.com/discover/advanced?term=' + keyword + '&page=' + str(x))
		except Exception as e:
			URL = 'None'
		print(URL)
		time.sleep(10)
# 		soup = BeautifulSoup(driver.page_source,'html.parser')
# 		content = soup.find_all('div',class_='js-track-project-card')
# # 		time.sleep(10)
# 		for element in content:
# 			try:
# 				pageURL = element.find('a',{'class': 'soft-black mb3'})['href']
# 			except Exception as e:
# 				pageURL = 'None'
	
# 			try:
# 				title = element.find('h3',{'class': 'type-18 light hover-item-text-underline mb1'}).text.strip()
# 			except Exception as e:
# 				title = 'None'

# 			try:
# 				location = element.find('a',{'class': 'dark-grey-500 hover-soft-black text-underline type-13 medium ml4'}).text.strip()
# 			except Exception as e:
# 				location = 'None'

# 			try:
# 				BrandPage = element.find('a', {'class': 'soft-black hover-text-underline medium'})['href']
# 			except Exception as e:
# 				BrandPage = 'None'

# 			try:
# 				BrandName = element.find('a', {'class': 'soft-black hover-text-underline medium'}).text.strip()
# 			except Exception as e:
# 				BrandName = 'None'

# 			try:
# 				Pledged = element.find('div', {'class': 'type-13 mr2'}).text.strip()
# 			except Exception as e:
# 				Pledged = 'None'

# 			try:
# 				Funded = element.find('div', {'class': 'type-13 mr2 dark-grey-500 medium'}).text.strip()
# 			except Exception as e:
# 				Funded = 'None'

# 			try:
# 				WhomAndBackers = element.find('div', {'class': 'soft-black text-ellipsis'}).text.strip()
# 			except Exception as e:
# 				WhomAndBackers = 'None'

# 			try:
# 				image = element.find('img', {'class': 'border-grey-400 border-bottom w100p absolute t0'})['src']
# 			except Exception as e:
# 				image = 'None'

# 			element_info = {
# 				'Keyword': keyword,
# 				'Product Headline': title,
# 				'Page URL': pageURL,
# 				'market': location,
# 				'Brand Name': BrandName,
# 				'BrandPage': BrandPage,
# 				'Pledged': Pledged,
# 				'Funded': Funded,
# 				'Creator and Amount of Backers': WhomAndBackers,
# 				'Image': image
# 			}

# 			kickstarterBot.append(element_info)

# 	df = pd.DataFrame(kickstarterBot)
# 	df.to_csv('kickstarter1.csv')
# 	return send_file('kickstarter1.csv', mimetype='text/csv', attachment_filename='kickstarter1.csv',as_attachment=True)









