import requests
import lxml
import sys
from bs4 import BeautifulSoup



'''def get_urls_data(url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
		'Accept_Language':'en'
	}

	response=requests.get(url,headers=headers)
	soup=BeautifulSoup(response.text,'lxml')

	name=soup.select_one(selector='#productTile').getText()
	name=name.strip()
	price=soup.select_one(selector='#priceblock_ourprice').getText()
	price=float(price[1:])

	return name,price'''

def get_urls_data(url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
		'Accept_Language':'en-GB,en-US;q=0.9'
	}
	response=requests.get(url)
	soup=BeautifulSoup(response.text,'html.parser')
	name=soup.find(class_='small-12 columns product-title').find('h1')
	#name=name.stripe()
	price=soup.find(class_='price is sk-clr1').getText()
	price=float(price.split()[0])
	return name.getText(),price
#productTile
#priceblock_ourprice