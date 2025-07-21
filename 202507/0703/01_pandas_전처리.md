# 2025년 07월 03일 목요일 (49일차)  
어렵다...


<br><br><br>

# 📜 목차  
- pandas
  - 누락된 데이터 확인
  - fillna(대체값, inplace=True) : 데이터프레임 전체의 결측치를 확인하기
  - duplicated() - 중복제거
  - 머신러닝 알로리즘 이론 - 선형회귀분석
  - 정규화
    - 컬럼 정규화하기
  - 타입 변환
    - 구간 나누기 1
    - 구간 나누기 2
      - 원핫인코딩
  - 문제 풀어보기
  - 정규표현식
  - 문제 풀어보기 (정규표현식)

<br><br><br>

<br>

## 🟢 누락된 데이터 확인


```python
import pandas as pd


# header가 3번째 줄에 있음
data = pd.read_csv('data/data.csv')

print('\n--- 데이터 확인 ---')
print(data.head())
print(data.tail())


print('\n--- height 결측치 확인 ---')
print("height 결측치 : ", data["height"].isnull().sum())

print("\n--- weight 결측치 확인 ---")
print("weight 결측치 : ", data["weight"].isnull().sum())

```

    
    --- 데이터 확인 ---
      name  height  weight
    0   A1   180.0    92.0
    1   A2   176.0    70.0
    2   A3   175.0    65.0
    3   A4   172.0    64.0
    4   A5   168.0     NaN
       name  height  weight
    25  A26   176.0     NaN
    26  A27   175.0    59.0
    27  A28   173.0    62.0
    28  A29   169.0    53.0
    29  A30   174.0    59.0
    
    --- height 결측치 확인 ---
    height 결측치 :  3
    
    --- weight 결측치 확인 ---
    weight 결측치 :  2
    

<br>

## 🟢 fillna(대체값, inplace=True) : 데이터프레임 전체의 결측치를 확인하기


```python
import pandas as pd

# header가 3번째 줄에 있음
data = pd.read_csv('data/data.csv')


# 데이터프레임 전체의 결측치를 확인하기
print(data.isnull().sum())

mean_height = data["height"].mean()
mean_weight = data["weight"].mean()

# fillna 메서드를 사용하여 결측치를 채우기
# fillna(대체값, inplace=True) inplace=True 옵션을 사용하면 원본 데이터프레임을 수정합니다.
                                           # 그게 아니라면 반환을 받아야 한다.
data["height"] = data["height"].fillna(mean_height)
data["weight"] = data["weight"].fillna(mean_weight)

print('\n--- 누락된 데이터 처리 후 결측치 확인 ---')
print(data.isnull().sum())

```

    name      0
    height    3
    weight    2
    dtype: int64
    
    --- 누락된 데이터 처리 후 결측치 확인 ---
    name      0
    height    0
    weight    0
    dtype: int64
    

## 🟢 duplicated() - 중복제거


```python
import pandas as pd

data = {
    'passenger_code':['A101', 'A102', 'A103', 'A101', 'A104', 'A101', 'A103'],
    'target':['광주', '서울', '부산', '광주', '대구', '광주', '부산'],
    'price':[25000, 27000, 45000, 25000, 35000, 27000, 45000]
}

print('--- DataFrame으로 만들어서 데이터 확인 ---')
df = pd.DataFrame(data)
print(df)

print('\n--- 중복 데이터 확인 ---')
col = df['passenger_code'].duplicated()  # True, False의 리스트로 보여준다.
print(col)

print('\n--- 중복 데이터 삭제 ---')
df = df.drop_duplicates()   # 삭제된 데이터를 변환, 전체 필드가 완전히 일치하는 데이터만 삭제한다.
print(df)

print('\n--- 서브셋 1 ---')
df3 = df.drop_duplicates(subset=['passenger_code'])
print(df3)

print('\n--- 서브셋 2 ---')
df3 = df.drop_duplicates(subset=['passenger_code', 'target'])
print(df3)


```

    --- DataFrame으로 만들어서 데이터 확인 ---
      passenger_code target  price
    0           A101     광주  25000
    1           A102     서울  27000
    2           A103     부산  45000
    3           A101     광주  25000
    4           A104     대구  35000
    5           A101     광주  27000
    6           A103     부산  45000
    
    --- 중복 데이터 확인 ---
    0    False
    1    False
    2    False
    3     True
    4    False
    5     True
    6     True
    Name: passenger_code, dtype: bool
    
    --- 중복 데이터 삭제 ---
      passenger_code target  price
    0           A101     광주  25000
    1           A102     서울  27000
    2           A103     부산  45000
    4           A104     대구  35000
    5           A101     광주  27000
    
    --- 서브셋 1 ---
      passenger_code target  price
    0           A101     광주  25000
    1           A102     서울  27000
    2           A103     부산  45000
    4           A104     대구  35000
    
    --- 서브셋 2 ---
      passenger_code target  price
    0           A101     광주  25000
    1           A102     서울  27000
    2           A103     부산  45000
    4           A104     대구  35000
    

<br>

## 🟢 머신러닝 알로리즘 이론 - 선형회귀분석

y = ax + b      자동으로  a와 b를 찾아내는 과정
                a, b     2  1
                x = [1,2,3,4,5,6,7, ....]
                y = [...................]     기대값
                real_y = [.................]  오차의 제곱의 합 : 4843783873

y = w1 x 1  +  w2 x 2  +  w3 x 3  +  w4 x 4  .........  + b

y에 영향을 미치는 x1, x2, .......
            기울기들 w1, w2, ......   '가중치'라고 부른다.

모든 데이터들(필드, 특성, 픽처)들의 단위가 비슷해야 한다.






<br>

## 🟢 정규화


### 🟡 컬럼 정규화하기

- 머신러닝이나 딥러닝에서 경우에 따라서 데이터의 단위가 너무 다를 경우 전체 예측 평가에 영향을 미칩니다. 

- 그래서 일부 알고리즘에서는 데이터값을 평균을 0, 분산을 1이 되도록 만들어 줘야합니다. 이를 정규화라고 합니다. 다음은 정규화 수식입니다. 



- (정규화하고자 하는 값 - 데이터 값들 중 최소값) / (데이터 값들 중 최대값 - 데이터 값들 중 최소값)

- 물론  sklearn(사이킷런)라이브러리 같은 경우 정규화를 지원하는 클래스도 있습니다.

- 사이킷런은 이 과정이 범위를 벗어나므로 지원 라이브러리가 있다는 정도만 다루도록 하겠습니다.



```python
import pandas as pd

data = pd.read_csv('data/auto-mpg.csv')

print('--- 데이터 확인 ---')
# print(data.info())
print(data.head())


# 컬럼명 변경하기 => 프로그램 안에서 바꾸기
print('\n--- 컬럼명 변경하기 ---')
data.columns = ['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.head())


# 정규화 (정규화하고자하는 값 - 최소값) / (최대값 - 최소값)
print('\n--- 정규화 ---')
data['mpg2'] = (data['mpg'] - data['mpg'].min()) / (data['mpg'].max() - data['mpg'].min())
print(data.head())


#단위환산 - 한국 단위로 환산하기 
print('\n--- 단위 환산 ---')
mpg_unit = 1.60934 / 3.78541
data['kpl'] = (data['mpg'] * mpg_unit).round(2)     # 소수점 이하 2자리 반올림
print( data.head() )


```

    --- 데이터 확인 ---
        mpg  cylinders  displacement  horsepower  weight  acceleration  model-year
    0  18.0          8         307.0       130.0    3504          12.0          70
    1  15.0          8         350.0       165.0    3693          11.5          70
    2  18.0          8         318.0       150.0    3436          11.0          70
    3  16.0          8         304.0       150.0    3433          12.0          70
    4  17.0          8         302.0       140.0    3449          10.5          70
    
    --- 컬럼명 변경하기 ---
        mpg  cyl   disp  power  weight  acce  model
    0  18.0    8  307.0  130.0    3504  12.0     70
    1  15.0    8  350.0  165.0    3693  11.5     70
    2  18.0    8  318.0  150.0    3436  11.0     70
    3  16.0    8  304.0  150.0    3433  12.0     70
    4  17.0    8  302.0  140.0    3449  10.5     70
    
    --- 정규화 ---
        mpg  cyl   disp  power  weight  acce  model      mpg2
    0  18.0    8  307.0  130.0    3504  12.0     70  0.239362
    1  15.0    8  350.0  165.0    3693  11.5     70  0.159574
    2  18.0    8  318.0  150.0    3436  11.0     70  0.239362
    3  16.0    8  304.0  150.0    3433  12.0     70  0.186170
    4  17.0    8  302.0  140.0    3449  10.5     70  0.212766
    
    --- 단위 환산 ---
        mpg  cyl   disp  power  weight  acce  model      mpg2   kpl
    0  18.0    8  307.0  130.0    3504  12.0     70  0.239362  7.65
    1  15.0    8  350.0  165.0    3693  11.5     70  0.159574  6.38
    2  18.0    8  318.0  150.0    3436  11.0     70  0.239362  7.65
    3  16.0    8  304.0  150.0    3433  12.0     70  0.186170  6.80
    4  17.0    8  302.0  140.0    3449  10.5     70  0.212766  7.23
    

<br>

## 🟢 타입 변환


```python
import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/auto-mpg.csv')
print(data.info())
print(data.head())

#타입이 맞지 않을 경우 전환을 해서 사용해야 한다 
#현재 사용하는 파이썬 버전은 문자열 데이터라도 수치 형태면 자동으로 수치자료로 처리한다 
#파이썬 버전에 따라 다르게 동작할 수 도 있다 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.dtypes)
print(data.head())

print( data['disp'].unique())

```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 398 entries, 0 to 397
    Data columns (total 7 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   mpg           398 non-null    float64
     1   cylinders     398 non-null    int64  
     2   displacement  398 non-null    float64
     3   horsepower    396 non-null    float64
     4   weight        398 non-null    int64  
     5   acceleration  398 non-null    float64
     6   model-year    398 non-null    int64  
    dtypes: float64(4), int64(3)
    memory usage: 21.9 KB
    None
        mpg  cylinders  displacement  horsepower  weight  acceleration  model-year
    0  18.0          8         307.0       130.0    3504          12.0          70
    1  15.0          8         350.0       165.0    3693          11.5          70
    2  18.0          8         318.0       150.0    3436          11.0          70
    3  16.0          8         304.0       150.0    3433          12.0          70
    4  17.0          8         302.0       140.0    3449          10.5          70
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
    

<br>

### 🟡 구간 나누기 1


#### ⚫  📊 머신러닝에서 왜 타입 변환(수치화)을 해야 할까?

머신러닝 모델은 **숫자(수치형 데이터)** 만 이해할 수 있습니다.  
따라서 문자열로 된 데이터를 반드시 **숫자로 변환(전처리)** 해야 합니다.

##### 🔧 예시: 문자열로 된 연비 등급

```
연비등급: A, B, C, D
```

이건 사람이 보기엔 쉽지만, 머신러닝은 이걸 이해하지 못합니다.  
그래서 숫자로 바꾸는 전처리가 필요합니다.

##### 1️⃣ Label Encoding (레이블 인코딩)

각 카테고리 값을 **고유 숫자**로 바꿉니다.

| 등급 | 숫자 |
|------|------|
| A    | 1    |
| B    | 2    |
| C    | 3    |
| D    | 4    |

⚠️ **문제점**  
모델이 숫자의 **크기(순서)** 를 의미 있다고 착각할 수 있어요.  
즉, D > A 라고 생각하게 되어버릴 수 있습니다.

##### 2️⃣ One-Hot Encoding (원-핫 인코딩)

각 값을 **별도의 열(column)** 로 나누고, 해당 값만 1로 표시합니다.

| A | B | C | D |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 |

✅ **장점**  
- 숫자의 크기 비교가 없어 안전합니다.  
- 모델이 각 등급을 **동등한 독립 변수**로 인식합니다.

##### 🧹 이름 같은 필드는 왜 제거해야 할까?

예: 이름 = "홍길동", "김철수", "이영희", ...

- 이름은 너무 다양하고 고유값이 많습니다.
- 의미 있는 수치로 바꾸기 어렵습니다.
- 원-핫 인코딩 시 **수천~수만 개의 열**이 생길 수 있습니다.

🚫 그래서 이름 같은 필드는 **삭제**합니다.  
(혹은 자연어처리(NLP)가 필요할 수도 있음)

##### ✅ 정리표

| 처리 방법       | 설명                              | 주의점/특징                          |
|----------------|-----------------------------------|-------------------------------------|
| Label Encoding | 문자열 → 정수 1, 2, 3...          | 순서 의미가 생겨서 오해 가능       |
| One-Hot Encoding | 문자열 → 0과 1로 이루어진 벡터 | 안전함, 다차원 문제만 주의         |
| 이름 필드 제거  | 수치화 불가, 차원 폭발 위험       | 모델에 방해되므로 제거하는 게 일반적 |


##### 🧠 결론

- 머신러닝 모델은 숫자만 처리할 수 있으므로 문자열을 반드시 수치화해야 합니다.
- **One-Hot Encoding**은 가장 일반적이고 안전한 방법입니다.
- 의미 없는 텍스트(이름, ID)는 제거하는 것이 좋습니다.



```python
import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/auto-mpg.csv')
# print(data.info())
# print(data.head())

"""
<타입 변환을 해야하는 이유>
머신러닝 - 수치화가 가능해야 우리가 머신러닝을 할 수가 있습니다.

ex) 연비가 A, B, C, D  ->  문자열이 있다고 가정하자.
        -> 이걸 카테고리 타입으로 전환을 한다.  
            A, B, C, D 들의 타입을 제외한 나머지 타입은 
            프로그램으로 넣을 수 없게 차단을 해야한다.
            카테고리화 할 수 없는 문자열 = 이름같은 필드   이름 필드는 삭제시켜야 한다.

            A - 1
            B - 2
            C - 3
            D - 4

            A, B, C, D 하나 올 수 있었다.

            필드를 4개로 바꾼다.
            A B C D             원핫인코딩  =>  단어 10000
            1 0 0 0
            0 1 0 0
            0 0 1 0
            0 0 0 1      

            원핫인코딩 해서 넣어야 한다.


"""

#타입이 맞지 않을 경우 전환을 해서 사용해야 한다 
#현재 사용하는 파이썬 버전은 문자열 데이터라도 수치 형태면 자동으로 수치자료로 처리한다 
#파이썬 버전에 따라 다르게 동작할 수 도 있다 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.dtypes)
print(data.head())

print( data['disp'].unique())   # 중복된거 배제하고 보여준다.

#잘못된 데이터를 NaN으로 먼저 바꾼다 
#data['disp'].replace('?', np.nan, inplace=True)
#data['acce'].replace('?', np.nan, inplace=True)
#data['model'].replace('?', np.nan, inplace=True)

# 🔥 정규식 sub 함수
data['disp'] = data['disp'].str.replace('?', np.nan)
print(data.head())

data.dropna(subset=['disp'], axis=0, inplace=True)
print(data.head())
print(data.dtypes)
data['disp'] = data['disp'].astype('float')
print(data.dtypes)

#DataFrame의 버그( 카테고리)- 그 범위를 벗어나는 데이터는 받으면 안된다. 
#카테고리타입에 데이터 추가했더니 스스로 float로 바뀌었다 
#허용되면 안된다. 
# 판다스 2.0에서 지원안함
# data = data.append({'mpg':90, 'model':93}, ignore_index=True)
data.loc[len(data)] = {'mpg':90, 'model':93}
#모델타입이 카테고리라서 없는 카테고리 값을 추가할 경우에 오류가 발생한다 
#파일을 읽을때 범위가 결정되어서 93이 해당사항이 없어서 에러가 발생한다 

#반드시 범주형으로 되어야 할것들은 범주형으로 바꿔줘야 한다 
print(data.dtypes)
print( data['model'].value_counts())#빈도표, 범주형의 경우에는 엄청 중요하다 

# # ---------------------------------------------
# # 기존에 있었던 내용용
# data.replace('?', np.nan, inplace=True)
# print(data.head())
# print(data.dtypes)
# #삭제를 했고 
# data.dropna(subset=['disp', 'acce', 'model'], axis=0, inplace=True)
# print(data.head())
# print(data.dtypes)
# data['disp'] = data['disp'].astype('float')
# data['acce'] = data['acce'].astype('float')
# print(data.dtypes)

# #범주형으로 바꾼다 - 대표적인 범주형 자료, 수치자료로 취급하면 안된다  
# data['model'] = data['model'].astype('category')
# print(data.dtypes)

```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 398 entries, 0 to 397
    Data columns (total 7 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   mpg           398 non-null    float64
     1   cylinders     398 non-null    int64  
     2   displacement  398 non-null    float64
     3   horsepower    396 non-null    float64
     4   weight        398 non-null    int64  
     5   acceleration  398 non-null    float64
     6   model-year    398 non-null    int64  
    dtypes: float64(4), int64(3)
    memory usage: 21.9 KB
    None
        mpg  cylinders  displacement  horsepower  weight  acceleration  model-year
    0  18.0          8         307.0       130.0    3504          12.0          70
    1  15.0          8         350.0       165.0    3693          11.5          70
    2  18.0          8         318.0       150.0    3436          11.0          70
    3  16.0          8         304.0       150.0    3433          12.0          70
    4  17.0          8         302.0       140.0    3449          10.5          70
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
    
