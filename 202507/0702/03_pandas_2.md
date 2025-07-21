# 2025년 07월 02일 수요일 (48일차)  
오늘은 pandas 2일차이다. 뭔가 쉬운 것 같으면서도 너무 복잡한 것 같기도 하다.
공부할게 정말 왜 이렇게 많은지 모르겠다.


<br><br><br>

# 📜 목차  

- [pandas](#pandas)
  - [DataFrame 복습하기!](#DataFrame-복습하기!)
  - [Series 사용 시 해당 data를 자동정렬](#Series-사용-시-자동정렬)
  - [pandas 2.0 버전 이후에 append 메서드가 삭제됨](#append-메서드가-삭제됨)
  - [concat - 여러개의 dataframe 합치기](#여러개의-dataframe-합치기)
  - [문제 풀어보기](#문제-풀어보기)
  - [DataFrame 열삭제 행삭제](#DataFrame-열삭제-행삭제)
  - [문제 풀어보기](#문제-풀어보기)

<br>

- [pandas - 외부파일 읽고 쓰기](#pandas-외부파일-읽고-쓰기)
  - [파일의 경로 표현 방법](#파일의-경로-표현-방법)
  - [파일 읽기](#파일-읽기)
  - [파일 내보내기](#파일-내보내기)
  - [엑셀 파일 읽어보기](#엑셀-파일-읽어보기)
  - [파일 데이터 분석](#파일-데이터-분석)
  - [데이터 필터링](#데이터-필터링)
  - [문제 풀어보기](#문제-풀어보기)
  - [데이터 분석2](#데이터-분석2)
  - [iris data를 통한 문제 풀기기](#-iris-data를-통한-문제-풀기기)
  - [데이터프레임 API 알아보기](#-데이터프레임-API-알아보기)

<br>

- [전처리 - 데이터 변환과 정제](#-전처리-데이터-변환과-정제)
  - [누락 데이터 처리](#-누락-데이터-처리)


<br><br><br>

## 🟢 분석에 사용할 데이터 자료 다운로드

### seaborn
https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn-load-dataset

### data
https://github.com/mwaskom/seaborn-data/blob/master/diamonds.csv



---

# 🟩 pandas

## 🟢 DataFrame 복습하기!

#### ⚫ loc
- 정의 : 라벨(label) 기반으로 데이터를 선택할 때 사용하는 인덱서
- 형태 : df.loc[행 인덱스, 열 이름]
- "label-location" 의 줄임말

- 예제
```python
        import pandas as pd

        data = {
            '이름': ['홍길동', '김철수', '이영희'],
            '나이': [25, 30, 22],
            '성별': ['남', '남', '여']
        }
        df = pd.DataFrame(data, index=['학생1', '학생2', '학생3'])
```
- 결과
```markdown
                이름  나이 성별  
        학생1   홍길동  25  남  
        학생2   김철수  30  남  
        학생3   이영희  22  여 
``` 
- 요약

    | 기능        | 예시                                     |
    | --------- | -------------------------------------- |
    | 행 선택      | `df.loc['학생1']`                        |
    | 행 + 열 선택  | `df.loc['학생2', '이름']`                  |
    | 여러 행/열 선택 | `df.loc[['학생1', '학생3'], ['이름', '성별']]` |
    | 조건 필터링    | `df.loc[df['나이'] > 24]`                |



#### ⚫ iloc
- 정의 : 정수 위치 기반 인덱싱(integer position indexing) 을 통해 Pandas의 DataFrame이나 Series의 특정 데이터를 선택할 수 있게 해주는 인덱서
- 형태 : df.iloc[행_번호, 열_번호]
- 행이나 열의 숫자 위치(index) 를 기준으로 접근
- 슬라이싱 시 끝 인덱스는 제외
- integer-location의 줄임말
- 예제
```python
        import pandas as pd

        data = {
            '이름': ['홍길동', '김철수', '이영희'],
            '나이': [25, 30, 22],
            '성별': ['남', '남', '여']
        }
        df = pd.DataFrame(data)
```
- 결과과
```markdown
            이름  나이 성별
        0  홍길동  25  남
        1  김철수  30  남
        2  이영희  22  여
```
- 요약

    | 기능         | 예시                        |
    | ---------- | ------------------------- |
    | 행 선택       | `df.iloc[0]`              |
    | 행 + 열 선택   | `df.iloc[1, 0]`           |
    | 여러 행/열 선택  | `df.iloc[[0, 2], [0, 2]]` |
    | 슬라이싱       | `df.iloc[0:2, 0:2]`       |
    | 마지막 행 선택   | `df.iloc[-1]`             |
    | 전체 행, 특정 열 | `df.iloc[:, 1]`           |
    | 특정 행, 전체 열 | `df.iloc[2, :]`           |  
<br>

- 특정 행 선택
```python
        df.iloc[0]
```

- 특정 행과 열 선택
```python
        df.iloc[1, 0]
```




```python
import pandas as pd

data = {
    'name':['홍길동', '임꺽정', '장길산', '홍경래', '이상민', '김수경'],
    'kor':[90, 80, 70, 70, 60, 70],
    'eng':[99, 98, 97, 46, 77, 56],
    'mat':[90, 70, 70, 60, 88, 99],
}

df = pd.DataFrame(data)


print('--------  데이터 출력하기  --------')
# print(df)  # 몇개 안되기 때문에 일단 다 찍어보았습니다. 표 형태로 데이터를 잘 만들었다.
# df.head()는 내부적으로 df.head(5)와 동일합니다.
print( df.head() )          #앞의 다섯명에 대한 데이터만 나온다. 
# print( df.head(3) )         #앞의 세명에 대한 데이터만 나온다. 


print("------ 지정한 열만 출력 ------")
print( df['name'])          # 이름만 출력
print( df['kor'])           # 국어점수만 출력
print( df.columns)          # 컬럼이름만 출력 


print('--------  loc  --------')
# loc
    # "label-location" 의 줄임말

# print(df['name':'eng'])     # 이것은 안됨. 
print(df.loc['name':'eng'])
print(df.loc[:, 'name':'eng'])  # 모든 행에 대해서 name부터 eng까지 출력
print(df.loc[:, ['name','eng','mat']])  # 모든 행에 대해서 name, eng, mat 출력
print(df.loc[0:2, ['name','eng','mat']])  # 0부터 2까지의 행에 대해서 name, eng, mat 출력
print(df.loc[[1,3,5], ['name','eng','mat']])  # 1, 3, 5 행에 대해서 name, eng, mat 출력
print(df.loc[[1,3,5], [0, 2]]) # 1, 3, 5 행에 대해서 0, 2 열 출력


print('--------  iloc  --------')
# iloc
    # "integer-location" 의 줄임말
    
print(df.iloc[0,0])
print(df.iloc[0,1])
print(df.iloc[0,2])
print(df.iloc[0,3])

```

    --------  데이터 출력하기  --------
      name  kor  eng  mat
    0  홍길동   90   99   90
    1  임꺽정   80   98   70
    2  장길산   70   97   70
    3  홍경래   70   46   60
    4  이상민   60   77   88
    ------ 지정한 열만 출력 ------
    0    홍길동
    1    임꺽정
    2    장길산
    3    홍경래
    4    이상민
    5    김수경
    Name: name, dtype: object
    0    90
    1    80
    2    70
    3    70
    4    60
    5    70
    Name: kor, dtype: int64
    Index(['name', 'kor', 'eng', 'mat'], dtype='object')
    --------  loc  --------
    Empty DataFrame
    Columns: [name, kor, eng, mat]
    Index: []
      name  kor  eng
    0  홍길동   90   99
    1  임꺽정   80   98
    2  장길산   70   97
    3  홍경래   70   46
    4  이상민   60   77
    5  김수경   70   56
      name  eng  mat
    0  홍길동   99   90
    1  임꺽정   98   70
    2  장길산   97   70
    --------  iloc  --------
    홍길동
    90
    99
    90
    


```python
import pandas as pd

# 분석하다 / 부분집합 가져와서 상세히 봐야할 때
df2 = df.loc[[0,2,4,], ['name', 'eng', 'mat']]
print(df2)

# 인덱스 다시 부여
df2 = df2.reset_index()
```

## 🟢 Series 사용 시 해당 data를 자동정렬

- 3개의 갯수를 가지는 score data가 4개가 있다. 하지만 각각의 score 점수는 뒤죽박죽 정렬이 되어있다.   
- series 변환 시 name 오름차순으로 자동 정렬하여 series 변환하기 때문에 바로 계산을 해도 충분한 계산이 가능하다.


```python
import pandas as pd

data1 = {'mat':80, 'kor':90, 'eng':70}
data2 = {'kor':90, 'eng':70, 'mat':80}
data3 = {'kor':90, 'eng':70, 'mat':80}
data4 = {'eng':90, 'mat':70, 'kor':80}  
#인덱스의 순서가 바뀌어도 정렬을 진행하기때문에 알아서 대응된다. 

series1 = pd.Series( data1 )
series2 = pd.Series( data2 )
series3 = pd.Series( data3 )
series4 = pd.Series( data4 )

result1 = series1 + series2 + series3 + series4
result2 = result1/4

print("--- 총점 ----------")
print( result1 )
print("--- 평균 ----------")
print( result2 )



```

    총점 ----------
    eng    300
    kor    350
    mat    310
    dtype: int64
    평균 ----------
    eng    75.0
    kor    87.5
    mat    77.5
    dtype: float64
    


```python
import pandas as pd

data1 = {'mat':80, 'kor':90, 'eng':70}
data2 = {'kor':90, 'eng':70, 'mat':80}
data3 = {'kor':90, 'eng':70}    # 🔥 수학 데이터 지워줬다.
data4 = {'mat':70, 'kor':80}    # 🔥 영어 데이터 지워줬다.

# 데이터 변환
series1 = pd.Series( data1 )
series2 = pd.Series( data2 )
series3 = pd.Series( data3 )
series4 = pd.Series( data4 )

result1 = series1 + series2 + series3 + series4
result2 = result1/4

print("------ 총점 ----------")
print( result1 )
print("------ 평균 ----------")
print( result2 )

# 결과는 영어와 수학이 NaN으로 나오게 된다. 계산을 못했기 때문이다.


# ===========================================================
# 그냥 없는대로 합하기
result3 = series1.add(series2, fill_value=0).add(series3, fill_value=0).add(series4, fill_value=0)
print("\n------ 그냥 없는대로 합하기 ----------")
print( result3 )

```

    ------ 총점 ----------
    eng      NaN
    kor    350.0
    mat      NaN
    dtype: float64
    ------ 평균 ----------
    eng     NaN
    kor    87.5
    mat     NaN
    dtype: float64
    
    ------ 그냥 없는대로 합하기 ----------
    eng    210.0
    kor    350.0
    mat    230.0
    dtype: float64
    

## 🟢 pandas 2.0 버전 이후에 append 메서드가 삭제됨


```python
import pandas as pd

data1 = {'mat':80, 'kor':90, 'eng':70}
data2 = {'kor':90, 'eng':70, 'mat':80}
data3 = {'kor':90, 'eng':70, 'mat':80}
data4 = {'eng':90, 'mat':70, 'kor':80}  
#인덱스의 순서가 바뀌어도 정렬을 진행하기때문에 알아서 대응된다. 

df = pd.DataFrame()

# ----------------------------------------
# pandas 2.0 버전 이후에 append 메서드가 삭제되었다.
# df = df.append(data1, ignore_index=True)

# ----------------------------------------
# 이렇게 바뀌었다.
# 1. 먼저 columns 를 만들어준다.
df = pd.DataFrame(columns=['mat', 'kor', 'eng'])
# 2. 그 다음에 데이터를 추가해준다.
df.loc[len(df)] = data1     
df.loc[len(df)] = data2     
df.loc[len(df)] = data3     
df.loc[len(df)] = data4     
     
print(df)





```

    Empty DataFrame
    Columns: [mat, kor, eng]
    Index: []
    

## 🟢 concat - 여러개의 dataframe 합치기


```python
import pandas as pd

data1 = {'mat':80, 'kor':90, 'eng':70}
data2 = {'kor':90, 'eng':70, 'mat':80}
data3 = {'kor':90, 'eng':70, 'mat':80}
data4 = {'eng':90, 'mat':70, 'kor':80}  
#인덱스의 순서가 바뀌어도 정렬을 진행하기때문에 알아서 대응된다. 


df = pd.concat([
    pd.DataFrame([data1]),
    pd.DataFrame([data2]),
    pd.DataFrame([data3]),
    pd.DataFrame([data4]),
], ignore_index=True)


print("\nconcat 함수 사용 결과")
print(df)

df['total'] = df['mat'] + df['kor'] + df['eng']
df['avg'] = df['total'] / 3

print(df)


```

    
    concat 함수 사용 결과
       mat  kor  eng
    0   80   90   70
    1   80   90   70
    2   80   90   70
    3   70   80   90
       mat  kor  eng  total   avg
    0   80   90   70    240  80.0
    1   80   90   70    240  80.0
    2   80   90   70    240  80.0
    3   70   80   90    240  80.0
    

## 🟢 문제 풀어보기

- 문제 : dict  타입을 데이터 프레임으로 전환후 새로운 필드를 추가하기 
    - 새로운 필드라고 하는 것에 의미는 결과에 대한 새로운 열(total, avg)를 의미합니다.


```python
import pandas as pd

data = {
'fruits':['망고', '딸기', '수박', '파인애플'],
'price':[2500, 5000,10000, 7000],
'count':[5, 2, 2, 4],
}

# 기존 DataFrame
df = pd.DataFrame(columns=['fruits', 'price', 'count'])

# 새로운 행 추가
df.loc[len(df)] = {'fruits': '사과', 'price': 3500, 'count': 10}

print(df)


```

      fruits  price  count
    0     사과   3500     10
    
