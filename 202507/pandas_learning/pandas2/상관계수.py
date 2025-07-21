import pandas as pd 

data = {'height':[160, 170, 180, 190, 200],
        'weight':[53, 61, 69, 74, 89]  }

df = pd.DataFrame(data)
print(df)

print( "상관계수 : ", df['height'].corr(df['weight']) )

print( df['height'].value_counts())

obj = pd.Series(['a', 'b', 'a', 'a', 'a', 'b', 'c', 'c', 'd'])
print( obj.value_counts())
#빈도표-몇번 출현했느냐 
                                                                                       