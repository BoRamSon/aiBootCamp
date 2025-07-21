# 🟩 pandas (판다스)

## 🟢 개념
pandas는 **표 형식의 데이터(데이터프레임)**를 쉽게 다룰 수 있는 라이브러리입니다.
엑셀처럼 행과 열로 구성된 데이터를 읽고, 쓰고, 정리하고, 분석할 수 있게 도와줍니다.


## 🟢 핵심 구조
| 구조          | 설명                     |
| ----------- | ---------------------- |
| `Series`    | 1차원 데이터 (컬럼 하나)        |
| `DataFrame` | 2차원 데이터 (엑셀 시트처럼 행과 열) |


## 🟢 주요 기능
- ❤️ CSV, Excel, SQL 등 다양한 데이터 파일 읽기/쓰기
- 결측치 처리 (NaN 제거, 채우기 등)
- 필터링, 정렬, 그룹화, 피벗 등 강력한 데이터 조작 기능
- 통계 요약 및 시계열 처리


## 🟢 예시
```python
import pandas as pd

# 딕셔너리를 데이터프레임으로 변환
data = {'name': ['홍길동', '이몽룡'], 'age': [30, 25]}
df = pd.DataFrame(data)

print(df)
print(df['age'].mean())   # 평균 나이 계산

```

## 🟢 추가적으로 특징 정리
- pandas는 앞으로 가장 자주 살펴볼 라이브러리다. pandas는 고수준의 자료 구조와 파이썬을 통한 빠르고 쉬운 데이터 분석 도구를 포함한다.
- pandas는 NumPy 기반에서 개발되어 NumPy를 사용하는 애플리케이션에서 쉽게 사용할 수 있다.
- 자동적으로 혹은 명시적으로 축의 이름에 따라 데이터를 정렬할 수 있는 자료 구조, 잘못 정렬된 데이터에 의한 일반적인 오류를 예방하고 다양한 소스에서 가져온 다양한 방식으로 색인되어 있는 데이터를 다룰 수 있는 기능
- 통합된 시계열 기능
- 시계열 데이터와 비시계열 데이터를 함께 다룰 수 있는 통합 자료 구조
- 산술연산과 한 축의 모든 값을 더하는 등의 데이터 축약연산은 축의 이름 같은 메타데이터로 전달될 수 있어야 한다.
- SQL같은 일반 데이터베이스처럼 데이터를 합치고 관계연산을 수행하는 기능





<br><br><br>

---

# 🟩 pandas 핵심자료구조 2가지 파악하기

| 자료구조        | 설명                     | 형태              |
| ----------- | ---------------------- | --------------- |
| `Series`    | 1차원 데이터 (리스트 + 인덱스 느낌) | `[index] value` |
| `DataFrame` | 2차원 테이블 (엑셀표 같은 형태)    | 행과 열로 구성된 표     |


<br>

## 🟢 Series



```python
import pandas as pd

s2 = pd.Series([1,2,3,4,5])

print(s2)

print('\n----------------')
print( s2[:3])
print( s2[1:3])
print( s2[1:])




```

    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64
    
    ----------------
    0    1
    1    2
    2    3
    dtype: int64
    1    2
    2    3
    dtype: int64
    1    2
    2    3
    3    4
    4    5
    dtype: int64
    

<br>

## 🟢 DataFrame

- 데이터 프레임 형태로 만들어봅니다.
- 여러 형태로 선택적 출력을 해봅니다.
- 행과 열에 접근하는 방법을 알아야합니다.



```python
import pandas as pd

data = {
    "name" : ["홍길동", "임꺽정", "장길산", "홍경래"],
    "kor" : [20, 30, 40, 50],
    "eng" : [90, 80, 70, 60],
    "mat" : [80, 70, 70, 50],
}

df = pd.DataFrame(data)  # 데이터프레임 생성
print(type(df))   # 데이터프레임 타입 출력
print(df)         # 데이터프레임 출력


print('\n------ 인덱스 출력 ------')
print(df.index)

print('\n------ 컬럼 출력 ------')
print(df.columns)

print('\n------ 값 출력 ------')
print(df.values)

print('\n------ 상위 3개 행 출력 ------')
print(df.head(3))

print('\n------ 하위 2개 행 출력 ------')
print(df.tail(2))

print('\n------ 인덱스 0, 0 출력 ------')
print(df.iloc[0,0])

print('\n------ 인덱스 0, 0 출력 ------')
print(df.loc[0, 'name'])
print(df.loc[0, 'kor'])
print(df.loc[0, 'kor'])
print(df.loc[0, 'eng'])
print(df.loc[0, 'mat'])


# 한 컬럼을 통으로 출력
print('\n------ 한 컬럼을 통으로 출력 ------')
print(df['name'])
print(df['kor'])
print(df['eng'])
print(df['mat'])

# for 문으로 출력 (을 왜 하는지는 잘 모르겠다.)
print('\n------ 한 컬럼을 통으로 출력 ------')
for i in range(len(df)):
    print(df.iloc[i, 0])

# for 문으로 출력 (을 왜 하는지는 잘 모르겠다.)
print('\n------ 한 컬럼을 통으로 출력 ------')
for i in range(len(df)):
    for j in range(0, df.shape[1]):
        print(df.iloc[i, j], end=' ')
    print()


print('\n------ 정보 출력 ------')
print(df.info())

print('\n------ 기술 통계 출력 ------')
print(df.describe())



```

    <class 'pandas.core.frame.DataFrame'>
      name  kor  eng  mat
    0  홍길동   20   90   80
    1  임꺽정   30   80   70
    2  장길산   40   70   70
    3  홍경래   50   60   50
    
    ------ 인덱스 출력 ------
    RangeIndex(start=0, stop=4, step=1)
    
    ------ 컬럼 출력 ------
    Index(['name', 'kor', 'eng', 'mat'], dtype='object')
    
    ------ 값 출력 ------
    [['홍길동' 20 90 80]
     ['임꺽정' 30 80 70]
     ['장길산' 40 70 70]
     ['홍경래' 50 60 50]]
    
    ------ 상위 3개 행 출력 ------
      name  kor  eng  mat
    0  홍길동   20   90   80
    1  임꺽정   30   80   70
    2  장길산   40   70   70
    
    ------ 하위 2개 행 출력 ------
      name  kor  eng  mat
    2  장길산   40   70   70
    3  홍경래   50   60   50
    
    ------ 인덱스 0, 0 출력 ------
    홍길동
    
    ------ 인덱스 0, 0 출력 ------
    홍길동
    20
    20
    90
    80
    
    ------ 한 컬럼을 통으로 출력 ------
    0    홍길동
    1    임꺽정
    2    장길산
    3    홍경래
    Name: name, dtype: object
    0    20
    1    30
    2    40
    3    50
    Name: kor, dtype: int64
    0    90
    1    80
    2    70
    3    60
    Name: eng, dtype: int64
    0    80
    1    70
    2    70
    3    50
    Name: mat, dtype: int64
    
    ------ 한 컬럼을 통으로 출력 ------
    홍길동
    임꺽정
    장길산
    홍경래
    
    ------ 한 컬럼을 통으로 출력 ------
    홍길동 20 90 80 
    임꺽정 30 80 70 
    장길산 40 70 70 
    홍경래 50 60 50 
    
    ------ 정보 출력 ------
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4 entries, 0 to 3
    Data columns (total 4 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   name    4 non-null      object
     1   kor     4 non-null      int64 
     2   eng     4 non-null      int64 
     3   mat     4 non-null      int64 
    dtypes: int64(3), object(1)
    memory usage: 260.0+ bytes
    None
    
    ------ 기술 통계 출력 ------
                 kor        eng        mat
    count   4.000000   4.000000   4.000000
    mean   35.000000  75.000000  67.500000
    std    12.909944  12.909944  12.583057
    min    20.000000  60.000000  50.000000
    25%    27.500000  67.500000  65.000000
    50%    35.000000  75.000000  70.000000
    75%    42.500000  82.500000  72.500000
    max    50.000000  90.000000  80.000000
    
