# 🟩 전처리 - 데이터 변환과 정제


### 🟡 결측치(누락된 값)와 이상치 처리
- 결측치(NaN)를 제거하거나 대체할 수 있다.
- 데이터 범위에서 벗어난 이상치를 탐지하고 제거 또는 수정할 수 있다.

### 🟡 데이터 타입 변환 및 인코딩
- 수치형, 문자열형 등의 데이터 타입을 필요에 따라 변환할 수 있다.
- 문자열 데이터를 **범주형(Categorical)** 자료형으로 변환할 수 있다.
- 범주형 데이터를 분석에 활용하기 위해 **원-핫 인코딩(One-Hot Encoding)**으로 변환할 수 있다.



### 🧹 결측치와 이상치 처리의 중요성

#### ⚫ 데이터 수집 과정의 오류

- 데이터를 수집하는 방식이 크롤링, 공공 데이터 포털, 실무자 제공, 설문조사 등 다양하더라도,
  수집 과정이나 응답 과정에서 **누락된 값(결측치)**이나 **이상치**가 발생하는 것은 흔한 일입니다.

#### ⚫ 이상치란?

- **이상치(Outlier)**는 다음과 같은 경우에 해당할 수 있습니다:
  - 단위 불일치 (예: 일부는 미터, 일부는 인치)
  - 수집 오류 (예: 오타, 비정상적인 입력)
  - **통계적으로 지나치게 크거나 작은 값**

- 예를 들어, 대부분 연봉이 5,000만 원에서 6,000만 원 사이인 집단에 3억 원짜리 연봉이 포함되면,
  평균이 왜곡되어 전체 집단을 잘못 해석할 수 있습니다.
  - 구성원이 충분히 많으면 영향이 적지만,
  - 소규모 집단이라면 **3억 원도 이상치로 간주**되어야 합니다.

#### 🎯 이 장의 목표

- 데이터 분석의 신뢰성을 높이기 위해,
  **결측치와 이상치를 탐지하고 적절히 처리하는 방법**을 살펴봅니다.


## 🧩 누락 데이터 처리

### 🟡 누락 데이터가 중요한 이유
- 머신러닝이나 딥러닝에서는 **누락된 데이터가 전체 예측 결과에 큰 영향을 미칩니다**.
- 신뢰도 높은 분석 결과를 얻기 위해서는 **누락된 값, 중복된 값, 이상치**에 대한 적절한 처리가 필수입니다.

### 🟡 누락 데이터의 표현
- `pandas`의 데이터프레임에서는 누락된 값이 **NaN (Not a Number)** 으로 표시됩니다.

### 🟡 사람이 직접 오류를 찾는 것은 거의 불가능
- 실제 분석에서는 수십만~수백만 건의 데이터가 사용됩니다.
- Excel 등으로 일일이 눈으로 확인하는 방식은 **비효율적이며 사실상 불가능**합니다.

### 🟡 해결 방법
- 파이썬에서는 `pandas`, `numpy` 등 다양한 라이브러리를 통해
  누락된 값이나 이상치를 **자동으로 탐지하고 처리하는 기능**을 제공합니다.

> 이 장에서는 이러한 도구를 활용하여 **누락 데이터나 이상치를 탐지하고 처리하는 방법**을 배웁니다.




```python
import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5, np.nan])  #프로그램에서 NaN값을 직접 입력할 때는 np.nan 사용
# print(s1)

print(s1.isnull().sum())   # 누락된 값의 개수를 출력
    # isnull() 결과  : [False, False, False, False, False, True]
        # s1.isnull()은 각 요소가 NaN인지 아닌지를 불리언 시리즈로 반환
    # 여기서 sum()은 누락된 값(True)의 수량을 총 합하여 출력한다. 즉, 누락된 개수를 출력한다.

# C언어는   True는 1이고, False는 0으로 해석
# [0, 0, 0, 0, 0, 1].sum()


# 데이터 읽어와서 처리해보기
data = pd.read_csv('data/data.csv')
# print(data)
print(f"현재 행의 개수 : {data.shape[0]}개")
# print(data.info())
# print(data.describe())


# 누락된 값 개수 확인
print(data.isnull().sum())


# # 
# print('------- height / value_counts ---------')
# print(data['height'].value_counts())
# print('------- weight / value_counts ---------')
# print(data['weight'].value_counts(dropna=False))


# # 누락된 값 파악
# print('------- height / isnull().sum() ---------')
# print(data['height'].isnull().sum())   
# print('------- weight / isnull().sum() ---------')
# print(data['weight'].isnull().sum())


# 결측치가 발생하면 행이나 열을 삭제시키거나 평균값이나 중간값으로 대체를 한다.
# 표준편차가 크면 평균값 보다는 중간값으로 대체를 하는 것이 좋다.

# 누락된 값 제거
print('------- 결측치 제거 후 행의 개수 ---------')
# Pandas의 dropna() 함수는 결측치(NaN) 가 포함된 행(row) 또는 열(column) 을 삭제하는 함수
data = data.dropna( how = 'any',  axis = 0 )   # 행 중에 NaN값이 있으면 행 전체를 삭제해라..
print(f"결측치 제거 후 행의 개수 : {data.shape[0]}개")
# print(data.info())
# print(data.describe())



# thresh 옵션 - 최소한의 실효성 있는 데이터 개수를 유지해라
print('\n------- thresh 옵션 - 최소한의 실효성 있는 데이터 개수를 유지해라 ---------')
# thresh는 **"threshold(임계값)"**의 줄임말
    # NaN이 아닌 값이 n개 이상 있어야 유지, 그렇지 않으면 삭제.
data2 = data.dropna( thresh = 28, axis = 1 )
print(data2.shape)
print(data.head())

# | 옵션          | 의미                                       |
# | -----------  | ---------------------------------------- |
# | `axis=1`     | 열(column) 기준으로 작업하겠다는 의미                 |
# | `thresh=28`  | NaN이 **아닌 값이 28개 이상 있어야** 그 열을 유지하겠다는 의미 |



data6 = pd.read_csv('data/auto-mpg.csv')
print( data.info() )

print( data['horsepower'].isnull().sum() )
data = data.dropna( how = 'any',  axis = 0 )
print( data.shape )






```

    1
    현재 행의 개수 : 30개
    name      0
    height    3
    weight    2
    dtype: int64
    ------- 결측치 제거 후 행의 개수 ---------
    결측치 제거 후 행의 개수 : 25개
    
    ------- thresh 옵션 - 최소한의 실효성 이는 데이터 개수를 유지해라 ---------
    (25, 0)
      name  height  weight
    0   A1   180.0    92.0
    1   A2   176.0    70.0
    2   A3   175.0    65.0
    3   A4   172.0    64.0
    5   A6   175.0    74.0
    
