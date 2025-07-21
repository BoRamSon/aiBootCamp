#파일명 : exam10_8.py

import pandas as pd 
import numpy as np 
#header가 3번째 줄에 있음 
data = pd.read_csv("./data/iris.csv")

#1) iris 데이터셋에 몇개의 필드가 있고 각 필드의 타입이 무엇인지 확인해 보세요
print(data.info())

#2) 앞에 7개 데이터 
print(data.head(7))

#3)통계량 요약정보 
print(data.describe())

#4)variety 이 Setosa 인 데이터의 통계량을 출력하세요

temp = data[data['variety']=='Setosa']
print(temp)

#5) 각각 variety가 Setosa, Virginica Versicolor 의 sepal.length 값의 평균값을 출력하시오
temp = data[data['variety']=='Setosa']['sepal.length']
print("Setosa 평균 : ", temp.mean())
temp = data[data['variety']=='Versicolor']['sepal.length']
print("Versicolor 평균 : ", temp.mean())
temp = data[data['variety']=='Virginica']['sepal.length']
print("Virginica 평균 : ", temp.mean())


#6) 꽃의 종류가 Setosa   이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오 

temp = data[np.logical_and(data['variety']=='Setosa', data['sepal.length']>=5)]
print(temp)
