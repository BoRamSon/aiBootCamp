# 2025년 5월 2일 금요일 (7일차)

### 🔵 들어가기 전

4월 29일 (5일차) / 4월 30일 (6일차)에 예비창업패키지 발표로 인하여 2일을 빠지게 되었다..  
그래서 def함수 수업을 듣지 못하게 되어 아쉬웠다.  
쉬는 날에 따로 공부를 해야겠다.

<br><br>

# 🟩 복습의 날

강사님께서 오늘은 지금까지 배워온 것들을 복습 하신다고 하셨다.

## 🟢 파이썬은 인간다운 언어

- 저급언어
- 고급언어
  - 고급 python
- 직관적이다.
- 문법이 쉬워 빠르게 배울 수 있다.
- 무료이지만 강력하다.
  - 파이썬은 오픈 소스(open source)이며 무료 소프트웨어이다. 사용료 걱정 없이 언제 어디서든 파이썬을 내려받아 사용할 수 있다.
  - 오픈 소스란 저작권자가 소스 코드를 공개하여 누구나 별다른 제한 없이 자유롭게 사용·복제 ·배포·수정할 수 있는 소프트웨어를 말한다.
  - '파이썬과 C는 찰떡궁합'이라는 말이 있다. 프로그램의 전반적인 뼈대는 파이썬으로 만들고 빠른 실행 속도가 필요한 부분은 C로 만들어서 파이썬 프로그램 안에 포함시킬 수 있기 때문
- Python으로 할 수 있는 일
  - Web Programming
  - 인공지능과 Machine Learning
  - 수치 연산 프로그래밍
  - Data 분석
  - Database Programming
  - 시스템 유틸리티 제작하기
  - GUI(graphic user interface) Programming
  - C / C++와 결합하기
  - 사물 인터넷
- 파이썬으로 할 수 없는 일
  - 시스템과 밀접한 프로그래밍 영역 (모바일 절대 불가)
  - 모바일 프로그래밍

<br><br>

## 🟢 자료형 (int)

```
# 사칙 연산
a = 10
b = 3
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b} 이라는 몫을 구합니다.")
print(f"{a} % {b} = {a%b} 이라는 나머지를 구합니다.")
print(f"{a} ** {b} = {a**b} | 10을 3번 거듭제곱 했습니다.")
```

### 🟡 진수 변환하는 방법

아래 숫자(10진수)를 각각 2진수 / 8진수 / 16진수 로 변환해보시오!  
15 ->  
27 ->  
68 ->  
127 ->  
356 ->

| 10진수 (Decimal) | 2진수 (Binary) | 8진수 (Octal) | 16진수 (Hex) |
| ---------------- | -------------- | ------------- | ------------ |
| 15               | 0b1111         | 0o17          | 0xf          |
| 27               | 0b11011        | 0o33          | 0x1b         |
| 68               | 0b1000100      | 0o104         | 0x44         |
| 127              | 0b1111111      | 0o177         | 0x7f         |
| 356              | 0b101100100    | 0o544         | 0x164        |

<br><br>

## 🟢 자료형 (string)

```python
# string
s = 'Life is too short, you need python'
print(s)

# slicing
print(s[:4])
print(s[8:11])
print(s[0]) # 문자열은 인덱싱은 데이터 수정이 불가능하다.
print(s[1]) #

# replace
s = s.replace('short', 'long')  # 바꾼 데이터를 return 한다.
print(s)
```

### 🟡 주석으로 된 data를 가지고 데이터화 시키기

```python
data = """
홍길동,90,90,80
임꺽정,80,80,80
장길산,100,100,90
"""

lines = data.split('\n')
print(lines)
# 출력되는 결과를 보니 ['', '홍길동,90,90,80', '임꺽정,80,80,80', '장길산,100,100,90', '']
# 이렇게 되있는 것을 양쪽의 공백을 없애보겠다.

# 🟡 양쪽의 공백을 없애는 방법 slicing을 활용해보았습니다.
lines = lines[1:len(lines)-1]
print(lines)
# ['홍길동,90,90,80', '임꺽정,80,80,80', '장길산,100,100,90']


# 🟡 이제는 각 줄을 ,로 나누어 보겠습니다.
for line in lines:
  words = line.split(',')
  print(words)
```

주석을 가지고 가공해 보는 것은 처음이었다. string type으로 생각하면서 list 형태로 만들고 이렇게 저렇게 가공을 하면서 사용을 해보니 데이터처럼 사용할 수 있구나를 느끼게 되었다.

### 🟡 .format

```python
name = '홍길동'
age = 20
kor = 90
eng = 90
mat = 80
total = kor + eng + mat
avg = total / 3

# 아주 옛날 버전
print("%s %d %s %d %d" % (name, age, kor, eng, mat))

# 3.6 이전 버전까지 섰던 것
print("{} {} {} {} {}".format(name, age, kor, eng, mat))

# 3.6 이후 버전부터 사용가능한 것 (현재 가장 많이 사용함)
print(f"{name} {age} {kor} {eng} {mat}") # f-string
```

<br><br>

## 🟢 자료형 (list)

- 배열 - 프로그램 수행 전에 반드시 메모리를 확보해야함
- index를 통해 읽고 쓴다. 수행 도중에 크기 변화 불가
- 연속된 Memory 공간 => Python의 list는 배열구조가 아님
- 인덱싱과 슬라이싱을 써서 접근한다는 부분만 배열구조와 일치한다.

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[0])
print(list1[3])
print(list1[4])

# 🟡 slicing
print(list1[:5])
print(list1[2:3])

# list1[1:6] = 8   # 이건 안됩니다.
print(list1)


# 🟡 데이터 추가
list1.append(11)
list1.append(12)
list1.extend([10, 20, 30, 40])
print(list1)


# 🟡 데이터 모두 삭제하고 몇번쨰 자리에 넣기
list1.clear()  # 모든 데이터를 삭제합니다.
list1.insert(0, 10)
list1.insert(1, 10)
print(list1)
```

#### 🔵 쉬운 문제 풀어보기

```python
# 1. 리스트에 5의 배수를 10개 채우기

multiple_five_list = []

for i in range(1, 11):
    multiple_five_list.append(i * 5)
    print(multiple_five_list)


# 2. 리스트에 100부터 90, 80, 70 역순

for i in range(100, 9, -10):
  print(i)
```

#### 🔵 list 내부 중복관련 처리 방법 (int, string 요소들 가능)

| 방법                    | 순서 유지 | 속도      | 설명                      |
| ----------------------- | --------- | --------- | ------------------------- |
| set()                   | ❌        | 빠름      | 간단하지만 순서 없어짐    |
| dict.fromkeys()         | ✅        | 빠름      | 순서 유지하면서 중복 제거 |
| 반복문 + 조건문         | ✅        | 느림      | 원리 이해용               |
| 리스트 컴프리헨션 + set | ✅        | 중간~빠름 | 성능과 순서 모두 만족     |

```python
# 🔥 3. 중복된 값이 포함된 리스트
# a = [1,2,3,2,4,3,5,1] 가 있습니다.
# 중복을 제거하고 정렬된 리스트를 출력해보세요.

# 중복제거와 sort를 사용해야합니다. 저는 해본 적이 없습니다.

a = [1,2,3,2,4,3,5,1]
a = list(set(a)) # 중복제거
a.sort() # 정렬
print(a) # [1, 2, 3, 4, 5]



# 🟡 같이 풀어보기
a = [1,2,3,2,4,3,5,1]
b = []
for i in a:
  if i not in b:
    b.append(i)
  print(b)
```

#### 🔵 쉬운 문제 풀어보기

```python
# 4.
# score = [80, 95, 70, 100, 85]
# 평균 점수보다 높은 점수만 골라 새로운 리스트로 만들고 출력해보세요.

score = [80, 95, 70, 100, 85]

score_avg = sum(score) / len(score)

score_then_avg = []

for i in score:
  if i > score_avg:
    score_then_avg.append(i)

print(score_then_avg)
```

## 🟢 이차원 배열

이차원 : 본래 의미의 배열이 아니다.  
list if list로 표현해야 한다.

```python
a = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15]]

# 출력해보기
for i in a:
  print(i)

print()

print(a[0])

print()
print(a[0][0])
```

---

## 🟢 어려운 문제 풀어보기

### 🟢 1번 문제

10 by 10 | 100개 | 1~100까지 채워서 출력하기

```python
output_number = 1

for i in range(1, 11):
  for j in range(1, 11):
    print(output_number, end=' ')
    output_number += 1
  print()

# 결과
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30
# 31 32 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48 49 50
# 51 52 53 54 55 56 57 58 59 60
# 61 62 63 64 65 66 67 68 69 70
# 71 72 73 74 75 76 77 78 79 80
# 81 82 83 84 85 86 87 88 89 90
# 91 92 93 94 95 96 97 98 99 100
```

#### 🟡 1번문제 같이 풀어보기

```python
#10 by 10 100개 1~100까지 채워서 출력하기

a = []
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)
a.append(9)
a.append(10)  #a.append(i)
print( a)

totalList=[]
for k in range(0,10):
  a = []
  for i in range(k*10+1, (k+1)*10+1):
    a.append(i)
  totalList.append(a)

for i in range(0, 10):
  for j in range(0, 10):
    print("%4d" % totalList[i][j], end="" )
  print()

 # 결과
  #  1   2   3   4   5   6   7   8   9  10
  # 11  12  13  14  15  16  17  18  19  20
  # 21  22  23  24  25  26  27  28  29  30
  # 31  32  33  34  35  36  37  38  39  40
  # 41  42  43  44  45  46  47  48  49  50
  # 51  52  53  54  55  56  57  58  59  60
  # 61  62  63  64  65  66  67  68  69  70
  # 71  72  73  74  75  76  77  78  79  80
  # 81  82  83  84  85  86  87  88  89  90
  # 91  92  93  94  95  96  97  98  99 100
```

### 🟢 2번 문제 (너무 어렵다...)

```python
# 1차 시도
go_list = []

for i in range(1, 11):
  for j in range(i, i+1):
    go_list.append(j)
    print(go_list[:j], '0 ' * (10 - i))
```

```
# 2차 시도
go_list = [1,2,3,4,5,6,7,8,9,10]

for i in range(1, 11):
  for j in range(0, i):
    print(go_list[j], '0 ' * (10 - i))
```

```
# 3차 시도

# 1 0 0 0 0 0 0 0 0 0
# 2 3 0 0 0 0 0 0 0 0
# 4 5 6 0 0 0 0 0 0 0
# 7 8 9 10 0 0 0 0 0 0

# p_list = []
zero_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
  if i == 0:
    zero_list[0] = i+1
    print(zero_list)
  if i == 1:
    zero_list[0] = i+1
    zero_list[1] = i+2
    print(zero_list)
  if i == 2:
    zero_list[0] = i+2
    zero_list[1] = i+3
    zero_list[2] = i+4
    print(zero_list)
  if i == 3:
    zero_list[0] = i+4
    zero_list[1] = i+5
    zero_list[2] = i+6
    zero_list[3] = i+7
    print(zero_list)
```

#### 🟡 2번문제 같이 풀어보기

```python
totalList=[]
kk=1
for k in range(0,10):
  a = []
  for i in range(0, 10):
    if i < (k+1):
      a.append(kk)
      kk+=1
    else:
      a.append(0)
  totalList.append(a)

for i in range(0, 10):
  for j in range(0, 10):
    print("%4d" % totalList[i][j], end="" )
  print()
```

---

## 🟢 최댓값을 고르는 알고리즘!!!

### 🟡 문제 - 함수, 최대값과 최대값 위치를 반환하는 함수

```python
a = \[5,4,1,7,8,3,6\]
```

1.  첫번째 방의 데이터가 젤 크다고 가정을 한다. / max 라는 변수에 첫번째 방의 데이터를 저장해 놓는다.
1.  두번째 방의 데이터를 비교해서 두번째 방의 값이 더 크면 값을 max의 값을 변경한다
1.  세번째 방의 데이터를 비교해서 두번째 방의 값이 더 크면 값을 max의 값을 변경한다
1.  ....... 마지막 방까지 가고 나면 max저장된 값이 제일 크다

```python
a = [5,4,1,7,8,3,6]
max = a[0]
pos = 0   # 0번째 방이 제일 크다고 가정하자!

# 🟡 방법 1
# if max < a[1]:
#   max = a[1]
# if max < a[2]:
#   max = a[2]

# 🟡 방법 2
for i in range(1, len(a)):
  if max < a[i]:
    max = a[i]
    pos = i
print(max, pos)
```

```python
a = [5,4,1,7,8,3,6]

def getMax(a):
  max = a[0]
  pos = 0   # 0번째 방이 제일 크다고 가정하자!

  for i in range(1, len(a)):
    if max < a[i]:
      max = a[i]
      pos = i
  # print(max, pos)
  return max, pos  # 다른 언어는 에러발생, 파이썬은 시스템이 알아서 tuple로 변환해줌

print(getMax(a))

# 🔥 return 값이 tuple로 나오기 때문에
m, p = getMax(a) # 이렇게 변수에 저장이 가능합니다.
print(m, p)
```

<br><br>

## 🟢 자료형 (dict)

```python
# =============================================================
# 🟡 1. 예시 1
person = dict()

person['name'] = '홍길동'
person['age'] = 23
person['phone'] = '010-0000-0001'
print(person)

# 🟡 2. 예시 2
person2 = {'name' : '장길사', 'age' : 21, 'phone' : '010-0000-0002'}
print(person2)



# =============================================================
print('-------------------')
# 🟡 키값으로 찾기
for key in person.keys():
  print(key, person[key])

for key in person2.keys():
  print(key, person2[key])

# 🟡 값으로 찾기
for value in person.values():
  print(value)

for value in person2.values():
  print(value)

# 🟡 키와 값으로 쌍으로 찾기
for item in person.items():
  print(item)

for key, value in person2.items(): # 튜플로된 items를 가지고 오면 tuple이 나눠지면서 key, value 형태로 가져오게 됩니다.
  print(key, value)


# =============================================================
# 🟡 🔥🔥🔥🔥🔥 enumerate
print('-------------------')
# 이것은 앞에 enumerate를 붙여서 인덱스와 함께 가져오는 방법입니다.
for i, key in enumerate(person2.keys()):
  print(i, key, person2[key])
```

<br><br>

## 🟢 자료형 - set()

- 중복 x / 순서 x
- 파이썬의 데이터 타입 중 하나로, 중복을 허용하지 않고 순서가 없는 데이터의 집합입니다.
- 세트는 중괄호 {}를 사용하여 생성하며, 리스트나 튜플과는 다르게 인덱싱이 불가능합니다.
- 세트는 주로 중복된 데이터를 제거하거나, 집합 연산(합집합, 교집합, 차집합 등)을 수행할 때 사용됩니다.
- set의 경우에는 int, str 모두에 사용할 수 있나요???
  - \= Python의 set은 int, str 등 해시 가능(hashable)한 모든 자료형에 사용할 수 있습니다.
  - hashable한게 뭐에요?
    - 한 번 정해지면 값이 바뀌지 않는 객체를 말합니다.
      - 이런 객체는 고유한 hash값이 있어서, 빠르게 찾을 수 있습니다.
      - set이나 dict는 내부적으로 hash 값을 이용해서 값을 저장하거나 검색합니다.

```python
# int 사용
s1 = set([1, 2, 3, 4, 5, 6, 3, 4])
print(s1)  # 중복 제거 → {1, 2, 3, 4, 5, 6}

# str 사용
s2 = set(["apple", "banana", "apple", "orange"])
print(s2)  # 중복 제거 → {'apple', 'banana', 'orange'}
```

## 🔥 중요한 이해가 있습니다.

- Hashable이 뭐야?
  - Python에서 hashable 객체는 해시 값을 가지는 객체입니다. 해시 값은 객체의 내용을 고유한 숫자(해시)로 변환한 결과로, 이 값은 객체가 바뀌지 않는 한 항상 같아야 합니다.
  - set이나 dict 같은 자료구조는 내부적으로 이 해시 값을 사용해서 데이터를 빠르게 저장하고 찾습니다.
  - 그래서 set.add()나 dict\[key\] = value 같은 작업을 할 때, 객체가 hashable이어야 합니다.
- 쉽게 말해서
  - Hashable 객체는 set에 추가하거나 dict의 키로 사용할 수 있다. (예: int, str, tuple(조건부), frozenset)
  - Unhashable 객체는 set이나 dict의 키로 못 쓴다. (예: list, dict, set)
    - 이유는 Python이 내부적으로 해시 값을 이용해 데이터를 관리하는데, 값이 바뀌면 해시 값도 바뀌어서 혼란이 생기기 때문.
    - `# Hashable 객체 s = set() s.add(10) # OK s.add("hello") # OK s.add((1, 2)) # OK s.add(frozenset([1, 2])) # OK print(s) # {10, 'hello', (1, 2), frozenset({1, 2})} # Unhashable 객체 s.add([1, 2]) # TypeError: unhashable type: 'list' s.add({1: 2}) # TypeError: unhashable type: 'dict' s.add({1, 2}) # TypeError: unhashable type: 'set'`
- 그래서 Python은 "이 값의 hash는 항상 같다"고 믿고 내부 구조에 저장함.

#### <표 정리>

| 자료형      | hashable 여부  | 설명                          |
| ----------- | -------------- | ----------------------------- |
| `int`       | ✅ 가능        | 정수, 불변                    |
| `float`     | ✅ 가능        | 실수, 불변                    |
| `str`       | ✅ 가능        | 문자열, 불변                  |
| `bool`      | ✅ 가능        | True, False                   |
| `tuple`     | ✅ 조건부 가능 | 내부에 mutable 없을 때만 가능 |
| `frozenset` | ✅ 가능        | set의 불변 버전               |
| `list`      | ❌ 불가능      | 가변 자료형                   |
| `dict`      | ❌ 불가능      | 키-값 구조, 가변              |
| `set`       | ❌ 불가능      | 중복 없는 집합, 가변          |

### 🟡 set으로 만들어서 수정을 못하기 때문에 '형전환'을 해줘야 합니다.

```python
# int 사용
s1 = set([1, 2, 3, 4, 5, 6, 3, 4])
print(s1)  # 중복 제거 → {1, 2, 3, 4, 5, 6}

# 형변환
s11 = list(s1)
print(type(s11), s11)  # 리스트로 변환 → [1, 2, 3, 4, 5, 6]

# str 사용
s2 = set(["apple", "banana", "apple", "orange"])
print(s2)  # 중복 제거 → {'apple', 'banana', 'orange'}

# 형변환
s22 = tuple(s2)
print(s22)  # 튜플로 변환 → ('apple', 'banana', 'orange')
```

### 🟡 set()의 대표적인 예시 - 교집합, 차집합, 합집합

```python
# int 사용
s1 = set([1, 2, 3, 4, 5, 6, 3, 4])
print(s1)  # 중복 제거 → {1, 2, 3, 4, 5, 6}

# 형변환
s11 = list(s1)
print(type(s11), s11)  # 리스트로 변환 → [1, 2, 3, 4, 5, 6]

# str 사용
s2 = set(["apple", "banana", "apple", "orange"])
print(s2)  # 중복 제거 → {'apple', 'banana', 'orange'}

# 형변환
s22 = tuple(s2)
print(s22)  # 튜플로 변환 → ('apple', 'banana', 'orange')


# ==========================================================


# 교집합
print('-------- 교집합 --------')
s3 = s1.intersection(s11)
print(s3)

# 합집합
print('-------- 합집합 --------')
s3 = s1.union(s11)
print(s3)

# 차집합
print('-------- 차집합 --------')
s3 = s1.difference(s11)
print(s3)
```

<br><br>

# 🟩 4일 휴일간의 과제

## ⚾ 숫자 야구 게임 만들기 (Python 프로젝트 문제)

#### 📃 실행 예시

09 중에 숫자 3개를 컴퓨터가 랜덤하게 3 7 9  
09 중에 숫자 3개를 입력받는다. 1 4 5 3out  
09 중에 숫자 3개를 입력받는다. 3 2 6 1strike 2out  
09 중에 숫자 3개를 입력받는다. 8 2 6 3out  
09 중에 숫자 3개를 입력받는다. 3 9 7 1strike 2ball  
09 중에 숫자 3개를 입력받는다. 3 7 9 3strike  
5번만에 맞췄습니다.  
6번 넘어가면 못 맞췄습니다.

🟡 통계  
컴퓨터가 지정한 값 : 3 4 5  
사용자가 입력한 값 : 0 0 0

사용자가 맞추기 위해 진행한 과정 출력

1번째에 5번 만에 맞췄고,  
3번째 때 몇번 만에 맞췄고  
.......  
....  
마지막에 종료 후에는 승률이 나온다. (10번 게임 중 3번을 맞췄다. 다 30%이다.)
