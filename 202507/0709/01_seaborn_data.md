# 2025년 07월 09일 수요일 (53일차)  


<br><br><br>

# 📜 목차  
- seaborn data - iris.csv 사용하기
- seaborn data - penguins.csv 사용하기
- seaborn data - diamonds.csv 사용하기
- 이상치
- 정규화
- 서포트벡터머신 

<br><br><br>

## 🟢 seaborn data - iris.csv 사용하기


```python
import pandas as pd
import numpy as np

# 파일 불러오기
df = pd.read_csv("./data/iris.csv")

# 데이터 확인
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

# 데이터 전처리 작업 시작
X = df.iloc[:, :4]
y = df.iloc[:, 4]
print(X[:4])
print(y[:4])

# 그 다음부터는 맨날 동일한거 그대로 하면 됩니다.
# ================================================
# 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# ================================================
# 로지스틱 회귀
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print(f"훈련셋 : {model.score(X_train, y_train)}")
print(f"테스트셋 : {model.score(X_test, y_test)}")


```

       sepal_length  sepal_width  petal_length  petal_width species
    0           5.1          3.5           1.4          0.2  setosa
    1           4.9          3.0           1.4          0.2  setosa
    2           4.7          3.2           1.3          0.2  setosa
    3           4.6          3.1           1.5          0.2  setosa
    4           5.0          3.6           1.4          0.2  setosa
    Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
           'species'],
          dtype='object')
           sepal_length  sepal_width  petal_length  petal_width
    count    150.000000   150.000000    150.000000   150.000000
    mean       5.843333     3.057333      3.758000     1.199333
    std        0.828066     0.435866      1.765298     0.762238
    min        4.300000     2.000000      1.000000     0.100000
    25%        5.100000     2.800000      1.600000     0.300000
    50%        5.800000     3.000000      4.350000     1.300000
    75%        6.400000     3.300000      5.100000     1.800000
    max        7.900000     4.400000      6.900000     2.500000
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   sepal_length  150 non-null    float64
     1   sepal_width   150 non-null    float64
     2   petal_length  150 non-null    float64
     3   petal_width   150 non-null    float64
     4   species       150 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 6.0+ KB
    None
       sepal_length  sepal_width  petal_length  petal_width
    0           5.1          3.5           1.4          0.2
    1           4.9          3.0           1.4          0.2
    2           4.7          3.2           1.3          0.2
    3           4.6          3.1           1.5          0.2
    0    setosa
    1    setosa
    2    setosa
    3    setosa
    Name: species, dtype: object
    훈련셋 : 0.9666666666666667
    테스트셋 : 1.0
    

## 🟢 seaborn data - penguins.csv 사용하기


```python
#iris_파일.py 

import pandas as pd
import numpy as np 
df = pd.read_csv("./data/penguins.csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

#라벨인코딩 작업 island 연산이 불가 => 연산이 가능하게 도와준다. 
df.loc[df["island"] == "Torgersen", "island"] = 1
df.loc[df["island"] == "Dream",     "island"] = 2
df.loc[df["island"] == "Biscoe",    "island"] = 3

#성별 
df.loc[df["sex"] == "MALE", "sex"] = 1
df.loc[df["sex"] == "FEMALE", "sex"] = 2
#map과 유사하게 apply, 함수만들어서 모든 요소한테 그 함수를 적용해라  
print(df.head(10))

#결측치 - 중간에 있을 수도 있으니까 
print(df.isna().sum())
#결측치 - 제거, 대부분의 경우는 제거보다는 다른값으로 대체하는경우가 많다. 
df = df.dropna(how="any", axis=0) #NaN 값이 있는 행은 모두 삭제해라 

print("------------- 결측치 삭제이후 -------------")
print(df.isna().sum())
print("------------")
print(df.shape)
print(df.shape)

X = df.iloc[:, 1:] #전체행, 나머지가 입력데이터, 특성, 픽처 
y = df.iloc[:,  0] #0번열이 목표치 라벨
print(X[:4])
print(y[:4])

#이상치제거, 
#스케일링(정규화, 표준화)-서포트벡터머신, 딥러닝은 반드시 해줘야한다 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0 )

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

```

      species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
    0  Adelie  Torgersen            39.1           18.7              181.0   
    1  Adelie  Torgersen            39.5           17.4              186.0   
    2  Adelie  Torgersen            40.3           18.0              195.0   
    3  Adelie  Torgersen             NaN            NaN                NaN   
    4  Adelie  Torgersen            36.7           19.3              193.0   
    
       body_mass_g     sex  
    0       3750.0    MALE  
    1       3800.0  FEMALE  
    2       3250.0  FEMALE  
    3          NaN     NaN  
    4       3450.0  FEMALE  
    Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm',
           'flipper_length_mm', 'body_mass_g', 'sex'],
          dtype='object')
           bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
    count      342.000000     342.000000         342.000000   342.000000
    mean        43.921930      17.151170         200.915205  4201.754386
    std          5.459584       1.974793          14.061714   801.954536
    min         32.100000      13.100000         172.000000  2700.000000
    25%         39.225000      15.600000         190.000000  3550.000000
    50%         44.450000      17.300000         197.000000  4050.000000
    75%         48.500000      18.700000         213.000000  4750.000000
    max         59.600000      21.500000         231.000000  6300.000000
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 344 entries, 0 to 343
    Data columns (total 7 columns):
     #   Column             Non-Null Count  Dtype  
    ---  ------             --------------  -----  
     0   species            344 non-null    object 
     1   island             344 non-null    object 
     2   bill_length_mm     342 non-null    float64
     3   bill_depth_mm      342 non-null    float64
     4   flipper_length_mm  342 non-null    float64
     5   body_mass_g        342 non-null    float64
     6   sex                333 non-null    object 
    dtypes: float64(4), object(3)
    memory usage: 18.9+ KB
    None
      species island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
    0  Adelie      1            39.1           18.7              181.0   
    1  Adelie      1            39.5           17.4              186.0   
    2  Adelie      1            40.3           18.0              195.0   
    3  Adelie      1             NaN            NaN                NaN   
    4  Adelie      1            36.7           19.3              193.0   
    5  Adelie      1            39.3           20.6              190.0   
    6  Adelie      1            38.9           17.8              181.0   
    7  Adelie      1            39.2           19.6              195.0   
    8  Adelie      1            34.1           18.1              193.0   
    9  Adelie      1            42.0           20.2              190.0   
    
       body_mass_g  sex  
    0       3750.0    1  
    1       3800.0    2  
    2       3250.0    2  
    3          NaN  NaN  
    4       3450.0    2  
    5       3650.0    1  
    6       3625.0    2  
    7       4675.0    1  
    8       3475.0  NaN  
    9       4250.0  NaN  
    species               0
    island                0
    bill_length_mm        2
    bill_depth_mm         2
    flipper_length_mm     2
    body_mass_g           2
    sex                  11
    dtype: int64
    ------------- 결측치 삭제이후 -------------
    species              0
    island               0
    bill_length_mm       0
    bill_depth_mm        0
    flipper_length_mm    0
    body_mass_g          0
    sex                  0
    dtype: int64
    ------------
    (333, 7)
    (333, 7)
      island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g sex
    0      1            39.1           18.7              181.0       3750.0   1
    1      1            39.5           17.4              186.0       3800.0   2
    2      1            40.3           18.0              195.0       3250.0   2
    4      1            36.7           19.3              193.0       3450.0   2
    0    Adelie
    1    Adelie
    2    Adelie
    4    Adelie
    Name: species, dtype: object
    훈련셋 0.9959839357429718
    테스트셋 0.9642857142857143
    

    a:\programs\anaconda3\envs\aiBootCamp\Lib\site-packages\sklearn\linear_model\_logistic.py:465: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      n_iter_i = _check_optimize_result(
    

## 🟢 seaborn data - diamonds.csv 사용하기


```python
import pandas as pd
import numpy as np 
df = pd.read_csv("./data/diamonds.csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())
#1. cut 나 clarity 의 경우면 분류 
#2.price 의 경우는 회귀로 
# cut color clarity -> 카테고리화 시켜서 -> 라벨인코딩을 하거나 원핫인코딩하기 
# value_counts()->속성하고 개수
print("cutting") 
print(df["cut"].value_counts()) 
print("color") 
print(df["color"].value_counts()) 
print("clarity") 
print(df["clarity"].value_counts()) 
print(df["color"].unique()) #특정필드에서 값 하나씩만 가져온다 

def getLabelMap(field):
    colorList = df[field].unique()
    #list를 받아와서 map으로 바꾸기  
    colorMap = {item: index + 1 for index, item in enumerate(colorList)}
    # for key, value in colorMap.items():
    #     print(key, value)
    return colorMap 

def changeLabeling():
    colorMap = getLabelMap('color')
    df['color_label'] = df['color'].map(colorMap)
    colorMap = getLabelMap('clarity')
    df['clarity_label'] = df['clarity'].map(colorMap)
    colorMap = getLabelMap('cut')
    df['cut_label'] = df['cut'].map(colorMap)

changeLabeling()
print(df.head())

X = df.loc[:, ['carat', 'depth', 'table', 'price', 'x', 'y',
       'z','color_label', 'clarity_label']]

y = df.loc[:, 'cut_label']
print(X[:5])
print(y[:5])

# #결측치 - 중간에 있을 수도 있으니까 
# print(df.isna.sum())
# #결측치 - 제거, 대부분의 경우는 제거보다는 다른값으로 대체하는경우가 많다. 
# df = df.dropna(how="any", axis=0) #NaN 값이 있는 행은 모두 삭제해라 

# print("결측치 삭제이후")
# print(df.isna().sum())
# print("------------")
# print(df.shape)
# print(df.shape)

# X = df.iloc[:, 1:] #전체행, 나머지가 입력데이터, 특성, 픽처 
# y = df.iloc[:,  0] #0번열이 목표치 라벨
# print(X[:4])
# print(y[:4])

# #이상치제거, 
# #스케일링(정규화, 표준화)-서포트벡터머신, 딥러닝은 반드시 해줘야한다 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0 )

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))








```

       carat      cut color clarity  depth  table  price     x     y     z
    0   0.23    Ideal     E     SI2   61.5   55.0    326  3.95  3.98  2.43
    1   0.21  Premium     E     SI1   59.8   61.0    326  3.89  3.84  2.31
    2   0.23     Good     E     VS1   56.9   65.0    327  4.05  4.07  2.31
    3   0.29  Premium     I     VS2   62.4   58.0    334  4.20  4.23  2.63
    4   0.31     Good     J     SI2   63.3   58.0    335  4.34  4.35  2.75
    Index(['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y',
           'z'],
          dtype='object')
                  carat         depth         table         price             x  \
    count  53940.000000  53940.000000  53940.000000  53940.000000  53940.000000   
    mean       0.797940     61.749405     57.457184   3932.799722      5.731157   
    std        0.474011      1.432621      2.234491   3989.439738      1.121761   
    min        0.200000     43.000000     43.000000    326.000000      0.000000   
    25%        0.400000     61.000000     56.000000    950.000000      4.710000   
    50%        0.700000     61.800000     57.000000   2401.000000      5.700000   
    75%        1.040000     62.500000     59.000000   5324.250000      6.540000   
    max        5.010000     79.000000     95.000000  18823.000000     10.740000   
    
                      y             z  
    count  53940.000000  53940.000000  
    mean       5.734526      3.538734  
    std        1.142135      0.705699  
    min        0.000000      0.000000  
    25%        4.720000      2.910000  
    50%        5.710000      3.530000  
    75%        6.540000      4.040000  
    max       58.900000     31.800000  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 53940 entries, 0 to 53939
    Data columns (total 10 columns):
     #   Column   Non-Null Count  Dtype  
    ---  ------   --------------  -----  
     0   carat    53940 non-null  float64
     1   cut      53940 non-null  object 
     2   color    53940 non-null  object 
     3   clarity  53940 non-null  object 
     4   depth    53940 non-null  float64
     5   table    53940 non-null  float64
     6   price    53940 non-null  int64  
     7   x        53940 non-null  float64
     8   y        53940 non-null  float64
     9   z        53940 non-null  float64
    dtypes: float64(6), int64(1), object(3)
    memory usage: 4.1+ MB
    None
    cutting
    cut
    Ideal        21551
    Premium      13791
    Very Good    12082
    Good          4906
    Fair          1610
    Name: count, dtype: int64
    color
    color
    G    11292
    E     9797
    F     9542
    H     8304
    D     6775
    I     5422
    J     2808
    Name: count, dtype: int64
    clarity
    clarity
    SI1     13065
    VS2     12258
    SI2      9194
    VS1      8171
    VVS2     5066
    VVS1     3655
    IF       1790
    I1        741
    Name: count, dtype: int64
    ['E' 'I' 'J' 'H' 'F' 'G' 'D']
       carat      cut color clarity  depth  table  price     x     y     z  \
    0   0.23    Ideal     E     SI2   61.5   55.0    326  3.95  3.98  2.43   
    1   0.21  Premium     E     SI1   59.8   61.0    326  3.89  3.84  2.31   
    2   0.23     Good     E     VS1   56.9   65.0    327  4.05  4.07  2.31   
    3   0.29  Premium     I     VS2   62.4   58.0    334  4.20  4.23  2.63   
    4   0.31     Good     J     SI2   63.3   58.0    335  4.34  4.35  2.75   
    
       color_label  clarity_label  cut_label  
    0            1              1          1  
    1            1              2          2  
    2            1              3          3  
    3            2              4          2  
    4            3              1          3  
       carat  depth  table  price     x     y     z  color_label  clarity_label
    0   0.23   61.5   55.0    326  3.95  3.98  2.43            1              1
    1   0.21   59.8   61.0    326  3.89  3.84  2.31            1              2
    2   0.23   56.9   65.0    327  4.05  4.07  2.31            1              3
    3   0.29   62.4   58.0    334  4.20  4.23  2.63            2              4
    4   0.31   63.3   58.0    335  4.34  4.35  2.75            3              1
    0    1
    1    2
    2    3
    3    2
    4    3
    Name: cut_label, dtype: int64
    훈련셋 0.4045729823260413
    테스트셋 0.40044493882091214
    

    a:\programs\anaconda3\envs\aiBootCamp\Lib\site-packages\sklearn\linear_model\_logistic.py:465: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      n_iter_i = _check_optimize_result(
    
