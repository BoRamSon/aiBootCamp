<br>

### 🟡 구간 나누기 2


```python
import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/auto-mpg.csv')
# print(data.info())
# print(data.head())

#타입이 맞지 않을 경우 전환을 해서 사용해야 한다 
#현재 사용하는 파이썬 버전은 문자열 데이터라도 수치 형태면 자동으로 수치자료로 처리한다 
#파이썬 버전에 따라 다르게 동작할 수 도 있다 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.dtypes)
print(data.head())

print( data['disp'].unique()) #중복된거 배제하고 보여준다 

# #잘못된 데이터를 NaN으로 먼저 바꾼다 
#정규식 sup함수 
data['disp'].replace('?', np.nan, inplace=True)
print(data.head())

data.dropna(subset=['disp'], axis=0, inplace=True)

print(data.head())
print(data.dtypes)
data['disp'] = data['disp'].astype('float')
print(data.dtypes)

# #범주형으로 바꾼다 
print(data.dtypes)
data['model'] = data['model'].astype('category')
print(data.dtypes)

#DataFrame의 버그( 카테고리)- 그 범위를 벗어나는 데이터는 받으면 안된다. 
#카테고리타입에 데이터 추가했더니 스스로 float로 바뀌었다 
#허용되면 안된다. 
#판다스 2.0에서 지원안함
#data = data.append({'mpg':90, 'model':93}, ignore_index=True)
#판다스 2.0 부터 
#data.loc[len(data)] = {'mpg':90, 'model':93}
#모델타입이 카테코리라서 없는 카테고리 값을 추가할 경우에 오류가 발생한다 
#파일을 읽을때 범위가 결정되어서 93이 해당사항이 없어서 에러가 발생한다 

#반드시 범주형으로 되어야 할것들은 범주형으로 바꿔줘야 한다 
print(data.dtypes)
print( data['model'].value_counts())#빈도표, 범주형의 경우에는 엄청 중요하다 




# ==================================
# 구간 나누기 코딩
import pandas as pd 
import numpy as np 


# bits = 나눠야할 구간의 개수
# 구간을 나눠서 각 구간별 데이터 개수와 구간에 대한 정보를 반환한다.

# NaN 제거

data.dropna(subset=['power'], axis=0, inplace=True)
count, bin_dividers = np.histogram(data['power'], bins=4)
print("각 구간별 데이터 개수 : ", count)
print("구간정보 : ", bin_dividers)

bin_dividers = np.array([40, 120, 140, 200, 300])  # 직접 부여 가능
bin_names = ['D', 'C', 'B', 'A']
data["grade"] = pd.cut(x=data['power'], 
                        bins=bin_dividers, 
                        labels=bin_names, 
                        include_lowest=True
                    )
print(data[:20])
print(data['grade'].value_counts())




# ==============================================
# 원핫인코딩   
    # - 사이킷런 (pip install scikit-learn)
    # - 사이킷런 라이브러리 안에 있는 원핫인코더 클래스를 사용한다.
# 사이킷런의 모든 모델은 입력갑이 2차원이여야 한다. 무조건 narray, numpy 2차원 배열
# 2D 형식이여야 한다.
grade = data['grade']
print(type(grade))
# 2D 형식으로 바꿔야 한다.
Y_class = np.array(grade)  # 1d array
Y_class = Y_class.reshape(-1, 1)   # 축이 하나 추가되어서 2D type이 된다.
print(Y_class[:5])
# print(Y_class.shape)


from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(Y_class)  
#내부적으로 저 배열을 읽어들여서 어떻게 변형할지에 대한 정보가 내부에 저장됨
Y_class_onnhot = enc.transform(Y_class).toarray()
print(Y_class_onnhot[:5])
# print(Y_class_onnhot.shape)



```

    mpg       float64
    cyl         int64
    disp      float64
    power     float64
    weight      int64
    acce      float64
    model       int64
    dtype: object
        mpg  cyl   disp  power  weight  acce  model
    0  18.0    8  307.0  130.0    3504  12.0     70
    1  15.0    8  350.0  165.0    3693  11.5     70
    2  18.0    8  318.0  150.0    3436  11.0     70
    3  16.0    8  304.0  150.0    3433  12.0     70
    4  17.0    8  302.0  140.0    3449  10.5     70
    [307.  350.  318.  304.  302.  429.  454.  440.  455.  390.  383.  340.
     400.  113.  198.  199.  200.   97.  110.  107.  104.  121.  360.  140.
      98.  232.  225.  250.  351.  258.  122.  116.   79.   88.   71.   72.
      91.   97.5  70.  120.   96.  108.  155.   68.  114.  156.   76.   83.
      90.  231.  262.  134.  119.  171.  115.  101.  305.   85.  130.  168.
     111.  260.  151.  146.   80.   78.  105.  131.  163.   89.  267.   86.
     183.  141.  173.  135.   81.  100.  145.  112.  181.  144. ]
        mpg  cyl   disp  power  weight  acce  model
    0  18.0    8  307.0  130.0    3504  12.0     70
    1  15.0    8  350.0  165.0    3693  11.5     70
    2  18.0    8  318.0  150.0    3436  11.0     70
    3  16.0    8  304.0  150.0    3433  12.0     70
    4  17.0    8  302.0  140.0    3449  10.5     70
        mpg  cyl   disp  power  weight  acce  model
    0  18.0    8  307.0  130.0    3504  12.0     70
    1  15.0    8  350.0  165.0    3693  11.5     70
    2  18.0    8  318.0  150.0    3436  11.0     70
    3  16.0    8  304.0  150.0    3433  12.0     70
    4  17.0    8  302.0  140.0    3449  10.5     70
    mpg       float64
    cyl         int64
    disp      float64
    power     float64
    weight      int64
    acce      float64
    model       int64
    dtype: object
    mpg       float64
    cyl         int64
    disp      float64
    power     float64
    weight      int64
    acce      float64
    model       int64
    dtype: object
    mpg       float64
    cyl         int64
    disp      float64
    power     float64
    weight      int64
    acce      float64
    model       int64
    dtype: object
    mpg        float64
    cyl          int64
    disp       float64
    power      float64
    weight       int64
    acce       float64
    model     category
    dtype: object
    mpg        float64
    cyl          int64
    disp       float64
    power      float64
    weight       int64
    acce       float64
    model     category
    dtype: object
    model
    73    40
    78    36
    76    34
    82    31
    75    30
    70    29
    79    29
    80    29
    81    29
    71    28
    72    28
    77    28
    74    27
    Name: count, dtype: int64
    각 구간별 데이터 개수 :  [193 116  70  17]
    구간정보 :  [ 46.  92. 138. 184. 230.]
         mpg  cyl   disp  power  weight  acce model grade
    0   18.0    8  307.0  130.0    3504  12.0    70     C
    1   15.0    8  350.0  165.0    3693  11.5    70     B
    2   18.0    8  318.0  150.0    3436  11.0    70     B
    3   16.0    8  304.0  150.0    3433  12.0    70     B
    4   17.0    8  302.0  140.0    3449  10.5    70     C
    5   15.0    8  429.0  198.0    4341  10.0    70     B
    6   14.0    8  454.0  220.0    4354   9.0    70     A
    7   14.0    8  440.0  215.0    4312   8.5    70     A
    8   14.0    8  455.0  225.0    4425  10.0    70     A
    9   15.0    8  390.0  190.0    3850   8.5    70     B
    10  15.0    8  383.0  170.0    3563  10.0    70     B
    11  14.0    8  340.0  160.0    3609   8.0    70     B
    12  15.0    8  400.0  150.0    3761   9.5    70     B
    13  14.0    8  455.0  225.0    3086  10.0    70     A
    14  24.0    4  113.0   95.0    2372  15.0    70     D
    15  22.0    6  198.0   95.0    2833  15.5    70     D
    16  18.0    6  199.0   97.0    2774  15.5    70     D
    17  21.0    6  200.0   85.0    2587  16.0    70     D
    18  27.0    4   97.0   88.0    2130  14.5    70     D
    19  26.0    4   97.0   46.0    1835  20.5    70     D
    grade
    D    294
    B     67
    C     25
    A     10
    Name: count, dtype: int64
    <class 'pandas.core.series.Series'>
    [['C']
     ['B']
     ['B']
     ['B']
     ['C']]
    [[0. 0. 1. 0.]
     [0. 1. 0. 0.]
     [0. 1. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]]
    

    C:\Users\user\AppData\Local\Temp\ipykernel_6760\1579180568.py:19: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
    
    
      data['disp'].replace('?', np.nan, inplace=True)
    

<br>

## 🟢 문제 풀어보기

1. data폴더내의 iris.csv파일을 읽어서, 누락된 데이터가 어떤 필드에 몇개 있는지 찾아내세요 
2. 누락된 데이터들을 평균치고 대체하세요
3. sepal.length, sepal.width, petal.width 세개의 필드에 정규화를 진행하세요 
4. petal.length 필드를 3개의 구간으로 나누어서  A, B, C 이라고 구간 이름을 붙여서 petal_grade 필드를 추가하세요. 그리고 '원핫인코딩'으로 전환하세요.




```python
import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/iris_NaN.csv')


# ------------------

# 1. data폴더내의 iris.csv파일을 읽어서, 누락된 데이터가 어떤 필드에 몇개 있는지 찾아내세요.
print("\n------ 1. 누락된 데이터가 어떤 필드에 몇개 있는지 찾아내세요. ------")
print(data.isnull().sum())


# 2. 누락된 데이터들을 평균치고 대체하세요.
print("\n------ 2. 누락된 데이터들을 평균치고 대체하세요. ------")
# data.fillna(data.mean(), inplace=True)
# print(data.head())
sepal_length_mean = data['sepal.length'].mean() 
sepal_width_mean = data['sepal.width'].mean() 
petal_length_mean = data['petal.length'].mean() 
petal_width_mean = data['petal.width'].mean() 

data['sepal.length'].fillna( sepal_length_mean, inplace=True)
data['sepal.width'].fillna( sepal_width_mean, inplace=True)
data['petal.length'].fillna( petal_length_mean, inplace=True)
data['petal.width'].fillna( petal_width_mean, inplace=True)


# 3. sepal.length, sepal.width, petal.width 세개의 필드에 정규화를 진행하세요.
print("\n------ 3. sepal.length, sepal.width, petal.width 세개의 필드에 정규화를 진행하세요. ------")
# 편하게 함수를 만들었습니다.
def normalize(columnname):
    max = data[columnname].max()
    min = data[columnname].min()
    return (data[columnname] - min) / (max - min)

data['sepal.length'] = normalize('sepal.length')
data['sepal.width'] = normalize('sepal.width')
data['petal.length'] = normalize('petal.length')
print(data.head())


# 4. petal.length 필드를 3개의 구간으로 나누어서  A, B, C 이라고 구간 이름을 붙여서 petal_grade 필드를 추가하세요.
print("\n------ 4. petal.length 필드를 3개의 구간으로 나누어서  A, B, C 이라고 구간 이름을 붙여서 petal_grade 필드를 추가하세요. ------")
count, bin_dividers = np.histogram(data['petal.length'], bins=3)
bin_names = ['A', 'B', 'C']
data['petal_grade'] = pd.cut(x=data['petal.length'], 
                                bins=bin_dividers, 
                                labels=bin_names, 
                                include_lowest=True
                            )
print(data.head())


# 카테고리타입분석, 분류 분석, 텍스트 분석
# 사이킷런 fit 학습하다. 이차원배열(2D)형태로만 입력을 받는다.
# 새로운 축을 추가해서 1d -> 2d 로 변환해준다.
Y_class = np.array(data['petal_grade']).reshape(-1, 1)

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(Y_class)  

#내부적으로 저 배열을 읽어들여서 어떻게 변형할지에 대한 정보가 내부에 저장됨
Y_class_onehot = enc.transform(Y_class).toarray()
Y_class_recovery = np.argmax(Y_class_onehot, axis=1).reshape(-1, 1)

print(Y_class_onehot[:10])
print(Y_class_recovery[:10])



```

    
    ------ 1. 누락된 데이터가 어떤 필드에 몇개 있는지 찾아내세요. ------
    sepal.length    3
    sepal.width     2
    petal.length    1
    petal.width     2
    variety         9
    dtype: int64
    
    ------ 2. 누락된 데이터들을 평균치고 대체하세요. ------
    
    ------ 3. sepal.length, sepal.width, petal.width 세개의 필드에 정규화를 진행하세요. ------
       sepal.length  sepal.width  petal.length  petal.width variety
    0      0.222222     0.625000      0.067797          0.2  Setosa
    1      0.166667     0.416667      0.067797          0.2  Setosa
    2      0.111111     0.500000      0.050847          0.2  Setosa
    3      0.083333     0.458333      0.084746          0.2  Setosa
    4      0.194444     0.666667      0.067797          0.2  Setosa
    
    ------ 4. petal.length 필드를 3개의 구간으로 나누어서  A, B, C 이라고 구간 이름을 붙여서 petal_grade 필드를 추가하세요. ------
       sepal.length  sepal.width  petal.length  petal.width variety petal_grade
    0      0.222222     0.625000      0.067797          0.2  Setosa           A
    1      0.166667     0.416667      0.067797          0.2  Setosa           A
    2      0.111111     0.500000      0.050847          0.2  Setosa           A
    3      0.083333     0.458333      0.084746          0.2  Setosa           A
    4      0.194444     0.666667      0.067797          0.2  Setosa           A
    [[1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]
     [1. 0. 0.]]
    [[0]
     [0]
     [0]
     [0]
     [0]
     [0]
     [0]
     [0]
     [0]
     [0]]
    

    C:\Users\user\AppData\Local\Temp\ipykernel_6760\939217606.py:23: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
    
    
      data['sepal.length'].fillna( sepal_length_mean, inplace=True)
    C:\Users\user\AppData\Local\Temp\ipykernel_6760\939217606.py:24: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
    
    
      data['sepal.width'].fillna( sepal_width_mean, inplace=True)
    C:\Users\user\AppData\Local\Temp\ipykernel_6760\939217606.py:25: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
    
    
      data['petal.length'].fillna( petal_length_mean, inplace=True)
    C:\Users\user\AppData\Local\Temp\ipykernel_6760\939217606.py:26: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
    
    
      data['petal.width'].fillna( petal_width_mean, inplace=True)
    
