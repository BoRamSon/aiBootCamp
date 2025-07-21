#파일명 : exam10_1.py

import pandas as pd 

data = pd.read_csv("./data/score.csv")
print(data)
print(data.head())

print("컬럼명 : ", data.columns)
print("인덱스 : ", data.index)

#총점, 평균 구하기 
data['total'] = data['kor'] + data['eng']+data['mat']
data['avg'] = data['total']/3

print( data )
