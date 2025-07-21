import pandas as pd

#dict 타입의 데이터를 정의한다
#dict타입은 키와 값 쌍으로 이루어진다. 
#특정키값에 데이터를 여러개 넣을 경우에 키:리스트 형태로 저장할 수 있다  
data = {
    'name':['홍길동', '임꺽정', '장길산', '홍경래', '이상민', '김수경'],
    'kor':[90, 80, 70, 70, 60, 70],
    'eng':[99, 98, 97, 46, 77, 56],
    'mat':[90, 70, 70, 60, 88, 99],
}
 
df = pd.DataFrame(data)

print( df.head() ) #앞의 다섯명에 대한 데이터만 나온다. 

print("지정한 열만 출력")
print( df['name'])
print( df['kor'])
print( df.columns) #컬럼이름만 출력 
#iloc 함수 : 배열에서의 위치값으로 데이터를 접근 할 수 있다. 
print("iloc 함수 사용 -----------")
print( df.iloc[0,0]) #0,0번에 해당하는 데이터 출력하기 
print( df.iloc[3,2]) #3번째 행의 2번째 열 
print( df.iloc[2:4,2])

print( df.iloc[2:4,2:4])

print("loc함수 사용 -------------")
#loc 함수는 필드명으로 데이터를 출력할 수 있다 .
print( df.loc[0, 'name']) #0번째 행의 name필드 값 출력 
print( df.loc[3, 'eng']) #0번째 행의 name필드 값 출력 
print( df.loc[:, 'name':'eng'])


