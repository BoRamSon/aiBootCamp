## 🟢 문제 풀어보기

#### data 폴더 아래에 있는 iris.csv 파일을 읽어서 다음 동작들을 수행해 보세요
1) iris 데이터셋에 몇개의 필드가 있고 각 필드의 타입이 무엇인지 확인해 보세요
2) 맨 앞의 데이터를 7개만 출력해보세요.
3) iris 데이터셋의 통계량을 확인해보세요(평균, 표준편차, 중간값, 사분위수...)
4) variety 이 Setosa 인 데이터의 통계량을 출력하세요.
5) 각각 variety가 Setosa, Virginica Versicolor 의 sepal.length 값의 평균값을 출력하시오.
6) 꽃의 종류가 Setosa   이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오.




```python
import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/iris.csv')
# print(data.info())
# print(data.head())


# 1) iris 데이터셋에 몇개의 필드가 있고 각 필드의 타입이 무엇인지 확인해 보세요.
# print("\n------ 필드의 개수와 타입 ------")
# print(data.shape[1]) #열의 개수
# print(data.dtypes)   # 열(필드)의 타입


# 2) 맨 앞의 데이터를 7개만 출력해보세요
# print("\n------ 맨 앞의 데이터를 7개만 출력해보세요 ------")
# print(data.head(7))


# 3) iris 데이터셋의 통계량을 확인해보세요(평균, 표준편차, 중간값, 사분위수...)
# print("\n------ 통계량 ------")
# print(data.describe())


# 4) variety 이 Setosa 인 데이터의 통계량을 출력하세요.
print("\n------ variety 이 Setosa 인 데이터의 통계량을 출력하세요. ------")
df3 = data[data['variety'] == 'Setosa']
print(df3.describe())


# 5) 각각 variety가 Setosa, Virginica, Versicolor 의 sepal.length 값의 평균값을 출력하시오.
print("\n------ 각각 variety가 Setosa, Virginica, Versicolor 의 sepal.length 값의 평균값을 출력하시오. ------")
df4 = data[data['variety'].isin(['Setosa', 'Virginica', 'Versicolor'])]
print(df4['sepal.length'].mean())


# 6) 꽃의 종류가 Setosa 이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오.
print("\n------ 꽃의 종류가 Setosa 이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오. ------")
df5 = np.logical_and(data['variety'] == 'Setosa', data['sepal.length'] >= 5)
print(f"{df5.shape[0]} 개")










```

    
    ------ variety 이 Setosa 인 데이터의 통계량을 출력하세요. ------
           sepal.length  sepal.width  petal.length  petal.width
    count      50.00000    50.000000     50.000000    50.000000
    mean        5.00600     3.428000      1.462000     0.246000
    std         0.35249     0.379064      0.173664     0.105386
    min         4.30000     2.300000      1.000000     0.100000
    25%         4.80000     3.200000      1.400000     0.200000
    50%         5.00000     3.400000      1.500000     0.200000
    75%         5.20000     3.675000      1.575000     0.300000
    max         5.80000     4.400000      1.900000     0.600000
    
    ------ 각각 variety가 Setosa, Virginica, Versicolor 의 sepal.length 값의 평균값을 출력하시오. ------
    5.843333333333334
    
    ------ 꽃의 종류가 Setosa 이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오. ------
    150 개
    

<br>

## 🟢
