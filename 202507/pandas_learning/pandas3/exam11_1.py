#파일명 : exam11_1.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/data.csv")

print("컬럼명 : ", data.columns)
print("인덱스 : ", data.index)

print( data.info() )
print("------------------------------")
#누락된 데이터가 있는지 확인하자. 
print( data['height'].value_counts(dropna=False))

print( data['height'].isnull()) #NaN이면 True, 아니면 False반환
print( data['height'].notnull())


#null값인것에 대한 개수 확인 
print( data['height'].isnull().sum(axis=0))

#전체에 대해서 확인 
print( data.isnull().sum(axis=0))


# thresh 비율로 남겨놓고 

import numpy  as np 
data.iloc[:15, 1:3]=np.nan  
#NaN이 아닌값이 2개 이하면 그행을 삭제한다 
# name, height, weight 가 있을때 저 3개중에 두개 필드가 NaN 이면 삭제 
# 0~14까지가 NaN 들어가 있고 전체 데이터 개수가 29 - 14 = 15

#thresh 에서 지정한 만큼의 유효한 데이터가 없으면 필요없는 열이므로 삭제하자


data2 = data.dropna(axis=1, thresh=15)#NaN이 아닌게개수거 thresh에서 지정한 만큼은 있어야 한다 
print(data2)
# data_thresh = data.dropna(thresh=2)#적어도 두개 필드가 NaN이 아닐것 
# print(data)

# print("삭제 후 ----")
# print(data_thresh)
# print(data_thresh['height'].isnull().sum())

# #합계- 단순 데이터 합계 
# print ( data['height'].sum() )

# print("데이터 개수")
# print(data.shape)
# data = data.dropna(subset=['height'], how='any', axis=0)
# print("삭제후 데이터개수")
# print(data.shape)

# data = data.dropna(subset=['weight'], how='any', axis=0)
# print("삭제후 데이터개수")
# print(data.shape)

# #인덱스 다시 부여
# data = data.reset_index(drop=True)
# print(data)
