#문제1) ndarray 타입으로 3 by 4의 배열을 만들고 정수값(1~100)으로 랜덤하게 채운다음 
#다음 출력들을 실행해보세요 

import numpy as np 
n1 = np.zeros((3,4))
print(n1)

for i in range(0,3):
    for j in range(0,4):
        n1[i,j]=np.random.randint(20)

print(n1)

#문제2) 행 출력하기 
print( n1[0] )
print( n1[1] )
print( n1[2] )

#문제3)열 출력하기 
print( n1[:, 0])
print( n1[:, 1])
print( n1[:, 2])
print( n1[:, 3])

#문제4)행의 누적합계 구하기 
print(n1.cumsum(axis=0))

#문제5)열의 누적합계 구하기 
print(n1.cumsum(axis=1))

#문제6) n1을 파일로 저장하기 

np.save("test1.npy", n1)

#load - 데이터 읽어오기 
data2 = np.load("test1.npy")
print(data2)
