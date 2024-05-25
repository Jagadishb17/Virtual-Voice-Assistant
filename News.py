import requests
from key import *

api_add = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+key
json_data = requests.get(api_add).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number "+str(i+1)+": "+ json_data["articles"][i]["title"]+".")

    return ar

arr=news()