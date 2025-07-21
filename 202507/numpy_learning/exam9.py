food1 = ['짬뽕', '짜장', '탕수육', '난자완스', '라조기']
food2 = deepcopy( food1 )

def deepcopy(a):
    #이 함수에 전달될 변수 a 는 list 타입이다 
    b = list()
    for item in a:
        b.append(item)
    #이 함수에서 외부로 나가야 할 대상로 list 
    return b 



def mydot(m1, m2):
    nrow1 = len(m1)
    ncol1 = len(m1[0])

    nrow2 = len(m2)
    ncol2 = len(m2[0])

    if( ncol1 != nrow2):
        print("연산불가")
        return None 
    
    m3 = list()
    for i in range(0, nrow1):
       
        temp = list()
        for j in range(0, ncol1):
            s=0
            for k in range(0, nrow2):
                s = s + m1[i][k] * m2[k][j]
            temp.append(s)
        m3.append(temp)

    return m3 

a= [[1,2,3], [4,5,6], [7,8,9]]
b= [[1,2,3], [2,3,4], [4,5,4]]

c = mydot(a, b)
print(c)        

import numpy as np 
a1 = np.array(a) 
a2 = np.array(b)
a3 = np.dot(a1, a2)
print(a3)
