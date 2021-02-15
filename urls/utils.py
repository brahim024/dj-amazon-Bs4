import requests
import lxml

from BeautifulSoup bs4

def get_urls_data(url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
		'Accept_Language':'en;q=0.8, de;q=0.7'
	}

	response=requests.get(url,headers=headers)
	soup=BeautifulSoup(response.txt,'lxml')

	name=soup.select_one(selector='#productTile').getText()
	name=name.strip()
	price=soup.select_one(selector='#priceblock_ourprice').getText()
	price=float(price[1:])

	return name,price