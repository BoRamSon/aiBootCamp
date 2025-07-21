#파일명 : exam10_5.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/auto-mpg.csv")

#어떤 컬럼을 갖고 있나 
print(data.columns)

print("앞에서 부터 5개만 미리 보기") 
print( data.head() )

print("뒤에서 부터 5개만 미리 보기") 
print( data.tail() )

print("앞에서 부터 10개만 미리 보기") 
print( data.head(10))
#데이터프레임의 차원 행, 열의 개수 확인 가능 
print( data.shape )

row, col = data.shape  
#tuple타입임, 행과 열에 대한 정보를 모두 가지고 있음
print("행의 개수 ", row)
print("열의 개수 ", col)
