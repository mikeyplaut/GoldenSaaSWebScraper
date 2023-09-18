from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
import requests

#read
url = "https://golden.com/query/list-of-software-as-a-service-companies-BMY"

webpage = requests.get(url)

soup = BeautifulSoup(webpage.content, "html.parser")

tree = html.fromstring(webpage.content)



companies = tree.xpath('//*[@id="root"]/div[2]/div/div/div[2]/div[4]/div[2]/div[2]/div')


#for i in range(len(companies)):
#	print("\n")
	#print(companies[i].text_content())
	
#print(companies[0].text_content())

print("INNER DATA OF INDEX 0")
#companyInfo = companies[0].find("div").find("div")

companyInfo = tree.xpath('//*[@id="root"]/div[2]/div/div/div[2]/div[4]/div[2]/div[2]/div[' + str(1) + ']/div/div')

for i in range(len(companyInfo)):
	print("\nInfo #", i)
	text = companyInfo[i].xpath('//text()')
	print(text)
	print(companyInfo[i].text_content())
	print(companyInfo[i].text)



print("\n")
print("INDEX 1")
print(companies[1].text_content())


