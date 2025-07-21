#numpy연습/exam5.py 
import numpy as np 
#랜덤하게 실수값 생성
data = np.random.randn(10)
#정규분포를 따르는 랜덤한 실수 10개를 만들어 낸다 
print(data)

#데이타 한개만 저장하기 
#확장자가 무조건 npy이어야 한다. 아니면 못 읽음 
np.save("datafile.npy", data)

#load - 데이터 읽어오기 
data2 = np.load("datafile.npy")
print(data2)


#여러개 저장하기 
data1 = np.random.rand(10) 
data2 = np.random.rand(10) 

print(data1, data2)

#각 요소는 dict타입 형태로 저장 키1=값1, 키2=갑2 형태로 , 확장자 못바꿈
np.savez("datafile2.npz",  m1 = data1, m2=data2,  m3=data )

result = np.load("datafile2.npz")
print("***", result.files) #저장된 키값 
for key in result.files:
    print( result[key])
d1 = result['m1']
d2 = result['m2']
d3 = result['m3']

print(d1, d2, d3)

