import requests
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
# print(r.text[0:500])
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})

# first_result = results[0]
# # date and year
# first_result.find('strong').text[0:-1] + ', 2017'
# # lie
# first_result.contents[1][1:-2]
# # explanation for lie
# first_result.find('a').text[1:-1]
# # url for explanation
# first_result.find('a')['href']

records = []

# loop to go through all lies
for result in results:
	date = result.find('strong').text[0:-1] + ', 2017'
	lie =  result.contents[1][1:-2]
	explanation = result.find('a').text[1:-1]
	url = result.find('a')['href']
	records.append((date, lie, explanation, url))

# print(records[0][0])
import pandas as pd
df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')

print(df.tail())