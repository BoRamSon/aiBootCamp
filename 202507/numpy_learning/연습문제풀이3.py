a = [1,2,3,4,5]
b = [6,7,8,9,10]

import numpy as np 
a1 = np.array(a)
b1 = np.array(b)

print( a1 + b1)
print( a1 - b1)
print( a1 * b1)
print( a1 / b1)
print( a1.dot( b1))


#풀이2 
a =[70, 80, 90, 60, 60, 50, 50, 60, 70, 80, 90, 95, 100, 100, 90, 60, 70]
a1 = np.array(a)

print("합계 : ", np.sum(a1))
print("평균 : ", np.mean(a1))
print("표준편차 : ", np.std(a1))
print("분산 : ", np.var(a1))

print ( np.arange(1,11,1) )

a = np.arange(1,21,1)
print( a.reshape( (4,5))) 
print( a.reshape( (5,4)))
print( a.reshape( (2,10)))  

"""
4 2 3    1 2       
4 5 1    2 2 
         2 1
"""
a = [[4,2,3], [4,5,1]]
b = [[1,2], [2,2], [2,1]]

#에러 자동 전환은 안함 2차원 이상일 경우에는 
#b = [ [1,2,2], [2,2,1]]

a1 = np.array(a)
b1 = np.array(b)

c1 = a1.dot(b1)
print(c1)
