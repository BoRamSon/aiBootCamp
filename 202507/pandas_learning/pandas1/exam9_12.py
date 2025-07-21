import pandas as pd
 
data = {
    'fruits':['망고', '딸기', '수박', '파인애플'],
    'price':[2500, 5000,10000, 7000],
    'count':[5, 2, 2, 4],
}
 
df = pd.DataFrame(data)

#새로운 행 추가하기 , 주의 : 반드시 반환되는 값을 받아야 추가가 된다 
#append 함수는 데이터가 추가된 객체를 반환한다 . 
df.append({'fruits':'사과', 'price':3500, 'count':10} , ignore_index=True)
print(df)

#ignore_index=True 옵션 : 기존의 인덱스를 무시하라는 옵션인데 붙여야 한다  
print("데이터가 추가된 객체를 받을 경우 --------")
df = df.append({'fruits':'사과', 'price':'3500', 'count':10}, ignore_index=True )
print(df)


#특정 필드 삭제 : axis는 축을 말하는데 axis값이 0이면 가로, axis 값이 1이면 세로를 말함 
df2 = df.drop("price", axis=1) #필드가 하나 삭제된 객체를 반환 
print(df2)
print("원본")
print(df)


#특정행을 삭제 
df3 = df.drop(0, axis=0) #행의 인덱스를 이용해서 삭제한다 
print(df3)

