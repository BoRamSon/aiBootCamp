#파일명 : exam11_5.py
#이상데이터 처리

import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/auto-mpg.csv')
print(data.info())
print(data.head())

#타입이 맞지 않을 경우 전환을 해서 사용해야 한다 
#현재 사용하는 파이썬 버전은 문자열 데이터라도 수치 형태면 자동으로 수치자료로 처리한다 
#파이썬 버전에 따라 다르게 동작할 수 도 있다 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.dtypes)
print(data.head())

print( data['disp'].unique())

#잘못된 데이터를 NaN으로 먼저 바꾼다 
#data['disp'].replace('?', np.nan, inplace=True)
#data['acce'].replace('?', np.nan, inplace=True)
#data['model'].replace('?', np.nan, inplace=True)

data.replace('?', np.nan, inplace=True)
print(data.head())
print(data.dtypes)
#삭제를 했고 
data.dropna(subset=['disp', 'acce', 'model'], axis=0, inplace=True)
print(data.head())
print(data.dtypes)
data['disp'] = data['disp'].astype('float')
data['acce'] = data['acce'].astype('float')
print(data.dtypes)

#범주형으로 바꾼다 - 대표적인 범주형 자료, 수치자료로 취급하면 안된다  
data['model'] = data['model'].astype('category')
print(data.dtypes)
