import numpy as np 

def fileToIntArray(filename):
    file = open(filename, "r")
    lines = file.readlines()#한번에 파일을 다 읽는다
    file.close()

    #간략list 써서 
    height =[int(x) for x in lines]
    return height 

data = fileToIntArray("height.txt")

ht = np.array(data)
print("키 평균 : ", np.mean(ht))
print("키 표준편차 : ", np.std(ht))
print("키 최대치 : ", np.max(ht))

np.save('height.npy', ht)
   
