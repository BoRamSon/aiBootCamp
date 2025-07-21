## 🟢 iris data를 통한 문제 풀기기

### 🟡 data 폴더 아래에 있는 iris.csv 파일을 읽어서 다음 동작들을 수행해 보세요
1) iris 데이터셋에 몇개의 필드가 있고 각 필드의 타입이 무엇인지 확인해 보세요
2) 맨 앞의 데이터를 7개만 출력해보세요
3) iris 데이터셋의 통계량을 확인해보세요(평균, 표준편차, 중간값, 사분위수...)
4) variety 이 Setosa 인 데이터의 통계량을 출력하세요
5) 각각 variety가 Setosa, Virginica Versicolor 의 sepal.length 값의 평균값을 출력하시오
6) 꽃의 종류가 Setosa   이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오 




```python
import pandas as pd
import numpy as np

df = pd.read_csv('./data/iris.csv')

# print(df.head())

print('------ 1. iris 데이터셋에 몇개의 필드가 있고 각 필드의 타입이 무엇인지 확인해 보세요 ------')
print(df.head(2))
print(f"{df.shape[1]}개의 필드가 존재합니다.")
# 타입은 어떻게 아는거지....

print(df.info())


# print('\n------ 2. 맨 앞의 데이터를 7개만 출력해보세요 ------')
# print(df.head(7))


print('\n------ 3. iris 데이터셋의 통계량을 확인해보세요(평균, 표준편차, 중간값, 사분위수...) ------')

# print('🟡 기준 : sepal.length')
# print(f"평균 : {df["sepal.length"].mean()}")
# print(f"표준편차 : {df["sepal.length"].std()}")
# print(f"중간값 : {df["sepal.length"].median()}")
# print(f"1사분위수 : {df["sepal.length"].quantile(0.25)}")
# print(f"2사분위수 : {df["sepal.length"].quantile(0.5)}")
# print(f"3사분위수 : {df["sepal.length"].quantile(0.75)}")

# 정답
print(df.describe())  # 통계량 출력



print('\n--- 4. variety 이 Setosa 인 데이터의 통계량을 출력하세요 ---')

df4 = df[df["variety"]=="Setosa"]

# print('🟡 기준 : sepal.length')
# print(f"평균 : {df4['sepal.length'].mean()}")   
# print(f"표준편차 : {df4['sepal.length'].std()}")
# print(f"중간값 : {df4['sepal.length'].median()}")
# print(f"1사분위수 : {df4['sepal.length'].quantile(0.25)}")
# print(f"2사분위수 : {df4['sepal.length'].quantile(0.5)}")
# print(f"3사분위수 : {df4['sepal.length'].quantile(0.75)}")

# 정답
print(df4.describe())  # 통계량 출력




print('\n--- 5. 각각 variety가 Setosa, Virginica, Versicolor 의 각각의 sepal.length 값의 평균값을 출력하시오 ---')
df5 = df[df["variety"]=="Setosa"]
print(f"Setosa 평균 : {df5['sepal.length'].mean()}")

df6 = df[df["variety"]=="Virginica"]
print(f"Virginica 평균 : {df6['sepal.length'].mean()}")

df7 = df[df["variety"]=="Versicolor"]
print(f"Versicolor 평균 : {df7['sepal.length'].mean()}")




print('\n--- 6. 꽃의 종류가 Setosa 이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오 ---')
df8 = df[df["variety"]=="Setosa"]
print(f"Setosa 개수 : {df8[df8['sepal.length']>=5].shape[0]}")



# print('연비평균 : ', data["mpg"].mean())
# print('연비최대 : ', data["mpg"].max())
# print('연비최소 : ', data["mpg"].min())
# print('연비중앙값 : ', data["mpg"].median())
# print('연비분산 : ', data["mpg"].var())
# print('연비최빈값 : ', data["mpg"].mode())
# print('연비표준편차 : ', data["mpg"].std())

# print('1사분위수 : ', data["mpg"].quantile(0.25))
# print('2사분위수 : ', data["mpg"].quantile(0.5))
# print('3사분위수 : ', data["mpg"].quantile(0.75))








```

    ------ 1. iris 데이터셋에 몇개의 필드가 있고 각 필드의 타입이 무엇인지 확인해 보세요 ------
       sepal.length  sepal.width  petal.length  petal.width variety
    0           5.1          3.5           1.4          0.2  Setosa
    1           4.9          3.0           1.4          0.2  Setosa
    5개의 필드가 존재합니다.
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   sepal.length  150 non-null    float64
     1   sepal.width   150 non-null    float64
     2   petal.length  150 non-null    float64
     3   petal.width   150 non-null    float64
     4   variety       150 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 6.0+ KB
    None
    
    ------ 3. iris 데이터셋의 통계량을 확인해보세요(평균, 표준편차, 중간값, 사분위수...) ------
    🟡 기준 : sepal.length
           sepal.length  sepal.width  petal.length  petal.width
    count    150.000000   150.000000    150.000000   150.000000
    mean       5.843333     3.057333      3.758000     1.199333
    std        0.828066     0.435866      1.765298     0.762238
    min        4.300000     2.000000      1.000000     0.100000
    25%        5.100000     2.800000      1.600000     0.300000
    50%        5.800000     3.000000      4.350000     1.300000
    75%        6.400000     3.300000      5.100000     1.800000
    max        7.900000     4.400000      6.900000     2.500000
    평균 : 5.843333333333334
    표준편차 : 0.8280661279778629
    중간값 : 5.8
    1사분위수 : 5.1
    2사분위수 : 5.8
    3사분위수 : 6.4
    
    --- 4. variety 이 Setosa 인 데이터의 통계량을 출력하세요 ---
    🟡 기준 : sepal.length
    평균 : 5.006
    표준편차 : 0.3524896872134512
    중간값 : 5.0
    1사분위수 : 4.8
    2사분위수 : 5.0
    3사분위수 : 5.2
    
    --- 5. 각각 variety가 Setosa, Virginica, Versicolor 의 각각의 sepal.length 값의 평균값을 출력하시오 ---
    Setosa 평균 : 5.006
    Virginica 평균 : 6.587999999999998
    Versicolor 평균 : 5.936
    
    --- 6. 꽃의 종류가 Setosa 이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오 ---
    Setosa 개수 : 30
    
