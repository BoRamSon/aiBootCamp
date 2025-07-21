import pandas as pd 

data1 = {'kor':90, 'eng':70, 'mat':80}
data2 = {'kor':90, 'eng':70, 'mat':80}
data3 = {'kor':90, 'eng':70, 'mat':80}

#dataframe의 한 행이 하나의 series 가 될 수도 있고, 열도 
#dataframe 에 데이터를 추가할 때 dict 타입으로 추가한다 
data = pd.DataFrame()

#ignore_index 옵션, 데이터를 추가하면 원래 있던 인덱스가 문제가 된다 
#새로 인덱스를 부가하라 
data = data.append( data1 , ignore_index=True)
data = data.append( data2 , ignore_index=True)
data = data.append( data3 , ignore_index=True)

print(data)

#각 필드값들을 더하여 새로 작성한 필드에 저장함 
#data.total -이런식으로 쓸 수 없다. 추가시에는 
data['total'] = data.kor + data.eng + data.mat
data['avg'] = data.total/3  # 벡터연산이라 for문 필요없음 

print(data)
