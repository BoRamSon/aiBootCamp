
import pandas as pd 
import numpy as np 

#nan 은 numpy를 사용해 직접 입력 가능하다
s = pd.Series([1,2,3,4,np.nan])

data = s.dropna(how='any', axis=0)
print(data)

data = data.reset_index(drop=True)
