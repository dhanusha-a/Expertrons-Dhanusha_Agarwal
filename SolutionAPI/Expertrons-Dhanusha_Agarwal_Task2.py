import requests
import json

print('URLs of all the articles fetched using the API:')

#fetching url response
url = ('https://api.nytimes.com/svc/search/v2/articlesearch.json?q=indigo&api-key=Idj6dpTkDefby1xQek3X7L9NuQye4twh')

#storing requested result in json format in variable
data = requests.get(url).json()

#looping the data to fetch url and store in file
for key,values in data['response'].items():
    for i in values:
        if isinstance(i,dict):
            #print(i['web_url'])
            #writing data to file
            f=open("url.txt","a+")
            f.write(i['web_url'])
            f.close()
            
