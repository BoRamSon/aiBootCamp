#파일명 : exam10_2.py

import pandas as pd 

data = pd.read_csv("./data/score_noheader.csv", header=None)
print(data)

print("컬럼명 : ", data.columns)
print("인덱스 : ", data.index)

print("컬럼부여후 ----------")
data.columns = ['name', 'kor', 'eng', 'mat']
print("컬럼명 : ", data.columns)
print(data)


print("필드추가후")
#총점, 평균 구하기 
data['total'] = data['kor'] + data['eng']+data['mat']
data['avg'] = data['total']/3

print( data )

