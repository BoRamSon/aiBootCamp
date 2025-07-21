#파일명 : exam10_8.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv(r"C:\python_workspace\파이썬데이터분석\pandas2\data\auto-mpg.csv")


#value_counts 각 데이터별 고유카운트 
print( data['model-year'].value_counts())

#평균, 최대, 최소 
print("연비평균 : ",  data['mpg'].mean())
print("연비최대 : ", data['mpg'].max())
print("연비최소 : ", data['mpg'].min())
print("연비중간 : ", data['mpg'].median())
print("연비분산 : ", data['mpg'].var())
print("연비표준편차 : ", data['mpg'].std())

print("1사분위수 : ", data['mpg'].quantile(0.25))  # 1/4
print("2사분위수 : ", data['mpg'].quantile(0.5))   # 2/4
print("3사분위수 : ", data['mpg'].quantile(0.75))  # 3/4


#상관계수
print( data.corr() )

print( data[['mpg', 'cylinders']])
print( data[['mpg', 'cylinders']].corr() )

import matplotlib.pyplot as plt 
#차트
data.plot() 
plt.show()


