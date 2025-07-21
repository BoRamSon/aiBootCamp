import numpy as np 
height = [170,178,165,164,190,192,172,171,170,168,169,177,175]
height = np.array(height)

print("평균 : ", height.mean() )
print("표준편차 : ", height.std() )
print("분산 : ", height.var() )
print("최대값 : ", height.max() )
print("최대값위치 : ", height.argmax() )

print("최소값 : ", height.min() )
print("최소값위치 : ", height.argmin() )

print("중위수 : ", np.percentile(height, 50) )
print("1/4분위수 : ", np.percentile(height,25) )
print("3/4분위수 : ", np.percentile(height, 75) )

print(np.sort(height))