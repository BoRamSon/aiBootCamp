import pandas as pd
import numpy as np 

#pandas 가 1차원-series, 2차원 -dataframe, 3차원-panel 
#3차원 ndarray 타입 배열을 만든다. 

array =  [  [[1,2,3],    [4,5,6]],
            [[7,8,9],    [10,11,12]],
            [[13,14,15], [16,17,18]]] 

array= pd.Panel(array)
print("타입 : ", type(array))
print(array)