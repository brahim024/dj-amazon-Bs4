import requests
import lxml

from bs4 import BeautifulSoup


'''
def get_urls_data(url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
		'Accept_Language':'en'
	}

	response=requests.get(url,headers=headers)
	soup=BeautifulSoup(response.text,'lxml')

	name=soup.select_one(selector='#productTile').get_text()
	name=name.strip()
	price=soup.select_one(selector='#priceblock_ourprice').get_text()
	price=float(price[1:])

	return name,price'''

def get_urls_data(url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
		'Accept_Language':'en-GB,en-US;q=0.9'
	}
	response=requests.get(url,headers=headers)
	soup=BeautifulSoup(response.text,'lxml')
	name=soup.select_one(selector='#productTile').getText()
	name=name.strip()
	price=soup.select_one(selector='#priceblock_ourprice').getText()
	price=float(price[1:])
	return name,price
