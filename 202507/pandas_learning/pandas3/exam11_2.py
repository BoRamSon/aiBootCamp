#파일명 : exam11_1.py
#누락데이터 치환하기 

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/data.csv")

#누란된 데이터가 있는지 확인하자. 
print( data['height'].value_counts(dropna=False))
print( data['height'].isnull()) #NaN이면 True, 아니면 False반환
print( data['height'].notnull())

#null값인것에 대한 개수 확인 
print("height 필드 Nan 개수 : ", data['height'].isnull().sum(axis=0))
print("weight 필드 Nan 개수 : ", data['weight'].isnull().sum(axis=0))

print("전체 확인 : ",  data.isnull().sum())

print("누락값 대체 후 ------------------")
#누락값 대체하기 
mean_height = data['height'].mean()
mean_weight = data['weight'].mean()

data['height'].fillna( mean_height, inplace=True) #기존 객체를 바꿔라 
data['weight'].fillna( mean_weight, inplace=True)

print("height 필드 Nan 개수 : ", data['height'].isnull().sum(axis=0))
print("weight 필드 Nan 개수 : ", data['weight'].isnull().sum(axis=0))

print( data )


