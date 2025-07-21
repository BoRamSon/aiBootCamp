import pandas as pd

#list를 사용하여 Series 만들기
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(type(series)) 
print(series)
print()

#직접 index 를 부여해보기 
data2 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
series2 = pd.Series(data2)
print(series2)

print(series.index)
print(series.values)

