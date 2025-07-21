import numpy as np 

height =[168, 176, 167, 174, 169]

ht = np.array(height)
print("키 평균 : ", np.mean(ht))
print("키 표준편차 : ", np.std(ht))

#1번 데이터를 리스트로 만든다 
#2번 위 1번을 np.array 타입으로 전환한다 
#3. np.mean, np.std, np.var, np.max, np.min등을 이용해서 구한다
weight = [52, 68, 47, 82, 51] 
wt = np.array(weight)
print("몸무게 평균 : ", np.mean(wt))
print("몸무게 표준편차 : ", np.std(wt))



