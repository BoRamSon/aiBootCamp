import requests 
from bs4 import BeautifulSoup
import pandas as pd 

url = "http://www.weather.go.kr/weather/observation/currentweather.jsp"
response = requests.get(url)
if response.status_code!=200:
    print("데이터를 불러올 수 없습니다")
    exit() 

content = response.content
bs = BeautifulSoup(content, 'html.parser')

table = bs.find("table", {'class':'table_develop3'})
trList = table.findAll("tr")
df = pd.DataFrame()
for tr in trList:
    tdList = tr.findAll("td")
    data = dict()
    i=1
    for td in tdList:
        if i==12:
            #data[f"x{i}"] = td.text.strip() 
            continue 
        else:
            data[f"x{i}"] = td.text.strip() 
        i=i+1
        #print(td.text, end='\t')
        #print(data)
    df  = df.append(data, ignore_index=True)

df.to_csv("기상정보.csv", mode="w", encoding="cp949", index=False)  




