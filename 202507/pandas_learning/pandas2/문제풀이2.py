import os
import sys
from urllib.parse import quote
import json 
import requests 
import pandas as pd 

#dataframe객체를 내놓도록 
def searchKeyword(keyword):
    KakaoAK ='KakaoAK 9053945496bbd327a150809c5bcec75f'

    encText = quote(keyword)
    url = "https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=15&sort=accuracy"
    url = url + "&query=" + encText

    #
    header = { "Authorization":KakaoAK }
    #print(url)

    response = requests.get(url, headers=header)
    #print(requests)
    #print(response.status_code)
    data = json.loads(response.content)

    documents = data['documents']

    return pd.DataFrame(documents)  #dict -> dataframe으로 바뀐다 


keyword = input("키워드 : ")
df = searchKeyword(keyword)

print(df.columns)

df = df[ ['address_name', 'place_name', 'x', 'y', 'road_address_name','place_url'] ]
#print(df)

df.to_csv(f"{keyword}.csv",  mode='w', encoding="cp949", index=False)

