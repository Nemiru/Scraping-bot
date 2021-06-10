from bs4 import BeautifulSoup
import requests

with open('parce.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

# will find the 1st div and its text
match = soup.div.text
# will find the 1st div
match = soup.find('div')

#will find the tr with class as nobosop
nobosop = soup.find('tr', class_='nobosop')
#print(nobosop)

# no text in 1st a under nobosop
headline = nobosop.a.text
#print(headline)

#every td shows up
match = soup.find_all('td')
# shows every td elements text
match = soup.get_text('td')




print(match)