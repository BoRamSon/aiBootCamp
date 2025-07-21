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

#연비 30, 19, 29, 28,............(연속형자료 )->구간 : A B C D(비연속적, 범주형자료) 

#연속적인 값을 구간으로 나누어 비연속적인값(범주형)으로 나눈다 
#print(data['power'])

#power  필드쪽에 null값 있으면 이건 제거하고 
print(data['power'].isnull().sum(axis=0))
data.dropna(subset=['power'], inplace=True)

#구간을 4개로 쪼개주세요 
count, bin_dividers = np.histogram(data['power'], bins=4)
print( count ) #각 구간별 데이터 개수 
print( bin_dividers) #구간을 4개로 쪼개라고 했으니까 
#46-92, 92-138, 138-184, 184-230

bin_names = ["D", "C", "B", "A"] #각 구간에 이름을 부여한다 
data["grade"] = pd.cut( x=data['power'],   #구간을 나누고자 하는 데이터 
                        bins=bin_dividers,  #구간정보
                        labels = bin_names, #라벨에 구간이름  
                        include_lowest=True)# 92를 어느쪽으로 넣을거냐 B그룹으로 넣겠다 

#print( data )
data.to_csv("auto-mpg-result.csv", mode="w", encoding="cp949", index=False)


"""
원핫인코딩 - 범주형 데이터의 경우에 연산이 안된다. 
연비               ==>     A B C D             A    B   C   D
A                          1 0 0 0            0.8  0.1 0.1  0   A라고 본다 
B                          0 1 0 0
C                          0 0 1 0
D                          0 0 0 1 

                          개 고양이  입력시        출력   개  고양이 
                          1 0                             0.7  0.3
                          0 1 
"""
#onehot encoding  reshape(-1,1) 차원이 하나 는다 

#2D만 받는다  OneHotEncoder라는게 
Y_class = np.array(data['grade']).reshape(-1,1)# 2D 배열 
print(Y_class)

#print(data['grade'])
print(np.shape(Y_class))

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(Y_class)

Y_class_onehot = enc.transform(Y_class).toarray()
print(Y_class_onehot[:10])

cols=["A","B", "C", "D"]
Y_class_recovery = [cols[i] for i in np.argmax(Y_class_onehot, axis=1)]
print(Y_class_recovery[:10])
print(data['grade'][:10])
# print(Y_class_onehot)