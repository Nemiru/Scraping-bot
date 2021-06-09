import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\user1\Downloads\chromedriver_win32\chromedriver')
# executable_path= 'c:\path\to\windows\webdriver\executable.exe')
driver.get('https://suite.endole.co.uk/explorer/?id=CA11897780#')
results=[]
content= driver.page_source
soup = BeautifulSoup(content,"html.parser")
for element in soup.findAll(attrs={'class':' content explorer-table'}):
    name = element.find('td')
    results.append(name.text)
    #for x in results:
     #   print(x)
df =pd.DataFrame({'Names:results'})
df.to_('names.csv', index=False, encoding='utf-8')