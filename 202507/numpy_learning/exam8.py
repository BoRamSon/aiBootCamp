#행렬은 2 by 3 등 이차원의 형태로 만들어지는 배열, 벡터의 벡터 
#파이썬은 2차원부터는 list of list 로 나타내야 한다 
#list 안에 또다른 리스트의 묶음 

# 2행 3열 
a = [ 
        [1,2,3], 
        [4,5,6]
    ]

print(a)
for i in range(0, 2):
    for j in range(0, 3):
        print( a[i][j], end = ' ')
    print()

import numpy as np 

m1 = np.array( a )
print(m1)

b = [[10,20,30], [40,50,60]]

c = a + b 
print(c )

m2 = np.array(b)

m3 = m1 + m2 
print(m3)

#슬라이싱 
print( m1[:1, :3] ) #시작:마지막값:스텝
"""
1 2 3 
4 5 6
""" 
print(m1[:,:2])  # : 전체행에 대해서, :2

m1 = np.array( [[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20]])

print(m1)
print("-- 앞의 2행만 가져오기")
print(m1[:2, :]) #2행전까지 0행,1행만, 열은 모두

print("-- 뒤의 2행만 가져오기")
print(m1[2:, :]) #2 행부터 마지막까지, 열은 전부 

#행렬의 연산 = 행렬의 곱셈 
# 2 by 3  3 by 2 행열 곱 가능 하다 

m1 = np.array( [ [1,2], [3,4] ] )
m2 = np.array( [ 1, 2 ]) 

m3 = m1 * m2 
print(m3)

print("-- 행렬의 곱 --")
m3 = m1.dot( m2 )
print(m3)

#deepcopy, dot 함수, 파일명:mymodule.py
#행렬의 곱구하는 함수 만들기 

#요소가 0 또는 1인 ndarray - numpy의 array 타입 
print ( np.zeros(10) ) 

#이 함수가 매개변수가 tuple타입으로 받아간다 
#2 by 10 크기의 배열을 만들고 0으로 채운다 
print( np.zeros( (2, 10) ))

print( np.zeros( (3, 4 )) )

print ( np.ones(3))

print ( np.ones( (3,4,5)) )

a = [
       [[1,2,3],[4,5,6]],
       [[7,8,9],[10,11,12]],
       [[13,14,15],[16,17,18]] 
]

print(a)

#가짜로 데이터 만들어 쓸때 - 랜덤값 생성하기
#0~1까지의 값 중에서 랜덤하게 shpe 2, 4튜플아님 
#가우스분포를 따르는 랜덤값을 생성한다. 정규분포

# seed random numbers to make calculation
# deterministic (just a good practice)

np.random.seed(0)
print ( np.random.rand(2, 4) ) 

print ( np.random.rand(2, 4) ) 

#행렬의 크기 변환하기 

a = np.arange(10) #1차원
b = a.reshape(2,5) #2차원 , 2 by 5

print(a)
print(b)


a=[[1,2],[2,3], [4,5]]

ncol = len(a[0])
nrow = len(a)

print(ncol, nrow)

def myarray(a):
    ncol = len(a[0])
    nrow = len(a)
    print(ncol, nrow)

