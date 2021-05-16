# importing libraries
from bs4 import BeautifulSoup as BS
import requests


# method to get the info
def get_info(country_name):
	
	# creating url using country name
	url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"
	
	# getting the request from url
	data = requests.get(url)

	# converting the text
	soup = BS(data.text, 'html.parser')
	
	# finding meta info for cases
	cases = soup.find_all("div", class_ = "maincounter-number")
	
	# getting total cases number
	total = cases[0].text
	
	# filtering it
	total = total[1 : len(total) - 2]
	
	# getting recovered cases number
	recovered = cases[2].text
	
	# filtering it
	recovered = recovered[1 : len(recovered) - 1]
	
	
	# getting death cases number
	deaths = cases[1].text
	
	# filtering it
	deaths = deaths[1 : len(deaths) - 1]
	
	# saving details in dictionary
	ans ={'Total Cases' : total, 'Recovered Cases' : recovered,
								'Total Deaths' : deaths}
	
	# returnng the dictionary
	return ans

# setting country name
country_name = "us"

# calling the get_info method
us = get_info(country_name)

# printing the results for us
print("Cases in United States")
for i, j in us.items():
	print(i + " : " + j)
	
print("----------------------------")
country_name = "india"
india = get_info(country_name)
print("Cases in India")
for i, j in india.items():
	print(i + " : " + j)



print("----------------------------")
country_name = "pakistan"
pakistan = get_info(country_name)
print("Cases in pakistan")
for i, j in pakistan.items():
	print(i + " : " + j)

print("----------------------------")
country_name = "Afghanistan"
Afghanistan = get_info(country_name)
print("Cases in Afghanistan")
for i, j in Afghanistan.items():
	print(i + " : " + j)

print("----------------------------")
country_name = "Australia"
Australia = get_info(country_name)
print("Cases  in Australia")
for i, j in Australia.items():
	print(i + " : " + j)
print("----------------------------")
country_name = "Brazil"
Brazil= get_info(country_name)
print("Cases in Brazil")
for i, j in Brazil.items():
	print(i + " : " + j)

print("----------------------------")
country_name = "Bangladesh"
Bangladesh = get_info(country_name)
print("Cases in Bangladesh")
for i, j in Bangladesh.items():
	print(i + " : " + j)

print("----------------------------")
country_name = "China"
China= get_info(country_name)
print("Cases in China")
for i, j in China.items():
	print(i + " : " + j)

print("----------------------------")
country_name = "Japan"
Japan = get_info(country_name)
print("Cases in Japan")
for i, j in Japan.items():
	print(i + " : " + j)

	print("----------------------------")
country_name = "Zimbabwe"
Zimbabwe = get_info(country_name)
print("Cases in Zimbabwe")
for i, j in Zimbabwe.items():
	print(i + " : " + j)
print("----------------------------")
country_name = "Turkey"
Turkey = get_info(country_name)
print("Cases in Turkey")
for i, j in Turkey.items():
	print(i + " : " + j)
print("----------------------------")
country_name = "Spain"
Spain = get_info(country_name)
print("Cases in Spain")
for i, j in Spain.items():
	print(i + " : " + j)
print("----------------------------")
