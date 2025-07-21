#파일명 : exam11_3.py
#중복데이터 제거하기 

import pandas as pd 

data = {
    'passenger_code':['A101', 'A102', 'A103', 'A101', 'A104', 'A101', 'A103'],
    'target':['광주', '서울', '부산', '광주', '대구', '광주', '부산'],
    'price':[25000, 27000, 45000, 25000, 35000, 27000, 45000]
}

df = pd.DataFrame(data)

print( df )

print("중복된 데이터 ")
col = df['passenger_code'].duplicated() 
print( col )

#중복 제거시 모든 데이터가 일치된것만 제거한다. 
df2 = df.drop_duplicates()
print( df2 )

print("특정 컬럼값이 중복일때 제거하기 -----")
df3 = df.drop_duplicates(['passenger_code'])
print( df3 )


print("두개의 컬럼값이 중복일때 제거하기 -----")
df3 = df.drop_duplicates(subset=['passenger_code', 'target'])
print( df3 )