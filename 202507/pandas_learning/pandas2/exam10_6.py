#파일명 : exam10_6.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/auto-mpg.csv")

print("데이터의 기본 구조")
print( data.info() )

print("데이터의 요약정보 확인")
print( data.describe())

