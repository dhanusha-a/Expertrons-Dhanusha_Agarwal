import requests
import json
import itertools

def news(choice):

    query='bitcoin'
    source='techcrunch'

    #fetching url response
    if(choice==1):
        url = ('http://newsapi.org/v2/everything?'
               'q='+query+'&'
               'apiKey=6623a87608f24b48ba010a42f3ba9b00')
    elif(choice==2):
        url = ('http://newsapi.org/v2/everything?'
               'q='+source+'&'
               'apiKey=6623a87608f24b48ba010a42f3ba9b00')
    else:
        print('Invalid Choice')

    
    #storing requested result in json format in variable
    data=requests.get(url).json()

    limit=10

    #loop to display top 10 news
    for index, item in zip(range(limit),data['articles']):
        print (index+1,item['title'])


    #bonus
    print("\n Custom Search")
    topic=input("Enter search query: ")
    date=input("Enter date since past 1 month (format:yyyy-mm-dd): ")

    custom_url = ('http://newsapi.org/v2/everything?'
               'q='+topic+'&'
               'from='+date+'&'
               'apiKey=6623a87608f24b48ba010a42f3ba9b00')

    custom_data = requests.get(custom_url).json()

    for index, item in zip(range(limit),custom_data['articles']):
        print (index+1,item['title'])   
        


if __name__ == '__main__':

    #user input
    choice=int(input("Enter choice for news 1.Bitcoin 2.Techcrunch: "))

    #function call
    news(choice)
    
    

    
