
#파일명 : exam10_7.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/auto-mpg.csv")

print("조건식 적용하기 ")
#실린더 개수 4개 짜리만 
print( data[data.cylinders==4] )

#연비가 27 이상만 
print( data[data.mpg>=27] )

#모델 연도가 70년이고 연비가 27이상만, -(하이픈) 때문데 data.model-year 는 안된다. 
#아래처럼 하던지 아니면 컬럼명을 수정해야 한다 
print ( data[data['model-year']==70])

#두가지 조건을 동시에 주고 싶을때 - 에러발생 이렇게 못쓴다 
#print( data[ data['model-year']==70 or data['mpg']>=25 ])
#ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

#두가지 조건을 동시에 주고 싶을때 
import numpy as np 
print(data [np.logical_and(data['model-year']==70, data['mpg']>=25)])
