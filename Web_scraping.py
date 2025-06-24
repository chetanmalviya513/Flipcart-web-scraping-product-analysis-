import pandas as pd
import requests
from bs4 import BeautifulSoup
#from lxml import lxml

Product_name = []
Prices_List = []
Description = []
Reviews = []


for i in range(2,100):
	url ="https://www.flipkart.com/search?q=mobail+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
	r = requests.get(url)

	#print(r)

	#soup = BeautifulSoup(r.text, "lxml")
	soup = BeautifulSoup(r.content,"html.parser")
	#box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

	#print(soup)

	# Product_Name find



	# Product_Name import

	names = soup.find_all("div", class_ = "_4rR01T")
	#print(names)

	for i in names:
		name = i.text
		Product_name.append(name)

	#print(Product_name)


	# Price_Lisr import

	prices = soup.find_all("div", class_ = "_30jeq3 _1_WHN1")
	for i in prices:
		price = i.text
		Prices_List.append(price)
	#print(Prices_List)
	#print('after loop   ',price)

		# review = soup.find_all("div", class_ = "_3LWZlK")
	
		# for i in review:
		# 	revi = i.text
		# 	Reviews.append(revi)
		# #print(len(Reviews))
	
		
# 	desc = soup.find_all("ul", class_ = "_1xgFaf")

# 	for i in desc:
# 		des = i.text
# 		Description.append(des)
# #print(len(Description))

"""
for i in Description:
	print(i)
"""

#df = pd.DataFrame({"Product_name": Product_name,"Prices_List": Prices_List}, dtype = {"Product_name":str, "Prices_List":str})

df = pd.DataFrame({"Product_name":Product_name,"Prices_List":Prices_List})
#print(df)

df.to_csv("C:/Users/cheta/Desktop/Python/Flipcart Web Scraping/Flipcart_mobile_under_50000_4.csv")
#print(df)
 
