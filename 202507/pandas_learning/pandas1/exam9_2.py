import pandas as pd

#dict 타입의 데이터를 정의한다
#dict타입은 키와 값 쌍으로 이루어진다. 
#특정키값에 데이터를 여러개 넣을 경우에 키:리스트 형태로 저장할 수 있다  
data = {
    'name':['홍길동', '임꺽정', '장길산', '홍경래'],
    'kor':[90, 80, 70, 70],
    'eng':[99, 98, 97, 46],
    'mat':[90, 70, 70, 60],
}
 
df = pd.DataFrame(data)
print("타입 : ", type(df))
print(df)


print(df.describe())#데이타프레임 통계치 요약
print(df.head(2)) #앞에서 2개 데이터만 확인 

#dataframe[행, 열] -- 못만들었음 
#df.iloc[행, 열]

print(df.iloc[0, :]) #1행
print(df.iloc[1]) #2행
print(df.iloc[2]) #3행
print(df.iloc[3]) #4행

print( df.iloc[:, 0]) #1열 
print( df.iloc[:, 1]) #2열
print( df.iloc[:, 2]) #3열 

print( df.iloc[0:2]) #슬라이싱 

print( df.loc[0, 'name']) 
print( df.loc[1:3, 'name':'eng'])

print(df.name.count())
print(df['name'].count())

for i in range(0, df.name.count()):
    print( df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3])

print( df.index)
