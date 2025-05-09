# 2025년 4월 30일 수요일 (6일차)

## 🟢 스스로 보충 수업

예비창업패키지 발표로 인해 빠지게된 날 2일차

<br><br>

# 📜 목차

- zip() 내장함수
- 성적처리 문제 고도화 (리스트 검색, 삭제, 수정 기능 추가)
- 검색 알고리즘
- 정렬 알고리즘
- 가변 매개변수
  - 위치 인자 (\*)
  - 키워드 인자 (\*\*)

<br><br>

# 🟩 def() 함수 활용 2

# 🟩 zip()

### 🟡 정의

- 각 iterable의 동일한 인덱스 요소들을 묶어 tuple로 반환합니다.
- zip() 객체는 이터레이터이므로, 한 번 순회하면 소모됩니다.
  - (filter, map 들과 같은 iterator)
  - type zip <class 'zip'>
  - list(zip()) 이렇게 되어야 결과물을 볼 수 있습니다.

#### ❓ 궁금증: zip()과 extend하고 어떻게 다를까???

| 항목      | `zip()`                                         | `extend()`                               |
| --------- | ----------------------------------------------- | ---------------------------------------- |
| 목적      | 여러 iterable의 요소들을 **묶어서 튜플로 반환** | 리스트에 다른 iterable을 **풀어서 추가** |
| 반환 값   | zip 객체 (이터레이터)                           | 반환값 없음 (`None`)                     |
| 사용 대상 | 반복 가능한 자료형 여러 개                      | 리스트 하나 + 반복 가능한 자료형         |
| 결과 형태 | 튜플의 이터러블                                 | 리스트가 길어짐 (in-place 수정)          |
| 대표 예시 | `zip([1,2], ['a','b']) → [(1,'a'),(2,'b')]`     | `[1,2].extend([3,4]) → [1,2,3,4]`        |

### 🟡 형태

```python
# 1
zip(iter1, iter2, ...)

# 2
zip(반복가능한 객체1, 반복가능한 객체2, ...)
```

```
z = zip([1, 2, 3], ['a', 'b', 'c'])
print(type(z))  # <class 'zip'>   # iterator
print(list(z))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 🟡 특징

- 가장 짧은 iterable의 길이에 맞춰 동작합니다.
- 유일하게 파이썬에서만 제공해주는 함수
- 이것은 <class 'zip'>이라는 타입입니다. list로 변환하기 전까지는 결과를 볼 수 있습니다.
- 리스트가 2 개 이상 있을 때, 2 개의 리스트를 조합해서 새로운 형태로 만들고 싶을 때 사용
- a = \[1,2,3,4,5\]
- b = \["a","b","c","d","e"\]
- \== \[("a,1"),("b,2"),("c,3"),("d,4"),("e,5")\]

## 🟢 예제

```python
# 🟡
names = ['홍길동', '김철수', '이영희']
scores = [90, 85, 88]

for name, score in zip(names, scores):
    print(f"{name}의 점수는 {score}점입니다.")


# 🟡
z = zip([1, 2, 3], ['a', 'b', 'c'])
print(type(z))  # <class 'zip'>
print(list(z))  # [(1, 'a'), (2, 'b'), (3, 'c')]


# 🟡
a = [1,2,3,4,5]
b = ["a","b","c","d","e"]

for item in zip (a,b,a) :  # 만들어진 tuple list가 for문에 하나씩 넣어지면서 출력됨
    print(item)

ab_list = list(zip(a,b))  # 단순히 2개 묶었음.
print(ab_list)

# 🟡 길이가 다를 경우, 자동으로 짧은 쪽을 기준으로 반환을 합니다.
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b')] → 더 짧은 쪽 기준

# 🟡 packing / unpacking
# ---------------------------------------------------------
# zip()으로 두 리스트의 각 인덱스 요소를 묶어서 튜플의 리스트로 만듦
zipped = list(zip([1, 2], ['a', 'b']))
# => [(1, 'a'), (2, 'b')] : 숫자 1과 문자 'a', 숫자 2와 문자 'b'가 각각 짝을 이룸
print(zipped)  # [(1, 'a'), (2, 'b')]
# ---------------------------------------------------------
# * 연산자 (언패킹)를 이용해서 각 튜플의 요소를 같은 인덱스끼리 다시 모음
# zip(*zipped)는 zip((1, 'a'), (2, 'b')) 와 같으며,
# → 첫 번째 요소들만 모아 (1, 2), 두 번째 요소들만 모아 ('a', 'b') 생성
a, b = zip(*zipped)

# 결과 확인
print(a)  # (1, 2) : 첫 번째 요소들만 모임
print(b)  # ('a', 'b') : 두 번째 요소들만 모임

# 🟡 dictionary 만들기
# 딕셔너리는 이런 식으로 존재하면 만들 수 있다. 그런데 zip이 이런 식으로 만들어주니깐 zip과 밀접한 관련이 있습니다.
# pairs = [('name', 'Alice'), ('age', 30)]
# d = dict(pairs)
# print(d)
# {'name': 'Alice', 'age': 30}

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Seoul']

dict_result = dict(zip(keys, values))
print(dict_result)
# {'name': 'Alice', 'age': 25, 'city': 'Seoul'}
```

<br><br>

# 🟩 검색 알고리즘

## 🔍 검색 알고리즘 요약

### 📌 검색 방법 비교

| 번호  | 검색 방식      | 설명                                                                   | 시간 복잡도     | 특징                                                        |
| ----- | -------------- | ---------------------------------------------------------------------- | --------------- | ----------------------------------------------------------- |
| \[1\] | 순차 검색      | 데이터를 **처음부터 끝까지** 순서대로 검사하여 찾음                    | `O(n)`          | 단순하지만 데이터가 많아질수록 느림                         |
| \[2\] | 색인 순차 검색 | 데이터를 **정렬 후**, 인덱스를 활용하여 검색 (자세한 설명은 추후 다룸) | \-              | 정렬 기반이므로 정렬 시간 필요                              |
| \[3\] | 이분 검색      | **정렬된 데이터**를 절반씩 나누며 검색                                 | `O(log n)`      | 빠르지만 정렬이 필수, 자주 변경되는 데이터엔 적합하지 않음  |
| \[4\] | 해시 검색      | **해시 함수**를 이용해 위치를 계산하여 빠르게 검색                     | `O(1)` (이론상) | 가장 빠름. 대신 **많은 메모리 사용** + **구현 복잡성** 있음 |

### 🧠 추가 설명

- **해시 검색**은 `dict`(딕셔너리) 타입이 대표적입니다.
  - `dict = Dictionary = Hashmap = Hashtable = Map`
- **과거**에는 비싼 메모리 때문에 메모리 절약을 중시했지만,  
  **현재**는 성능 향상을 위해 **속도를 우선**시합니다.

```python
a = [1,2,3,4,5,6,7,8,9,10]
key = 5         # 찾아야하는 값
find = -1       # bool 변수 / key 값을 못 찾은 상태

# --------------------------------------------------------

for i in range(0,len(a)) :
    if key == a[i] :
        print("found")
        find = i
        break

if find == -1 :
    print("not found")
else :
    print(f"{find} 번째에 있음")

# --------------------------------------------------------

def myFilter(a_list,key) :
    for i in range(0,len(a_list)) :
        if key == a[i] :
            return i
    return -1

pos = myFilter(a,4)
print(pos)

# --------------------------------------------------------

a = ["red" , "green" , "cyan" , "gray" , "blue"]
str = myFilter(a,"blue")
print(str)

# --------------------------------------------------------

a = [
    {"name" : "A" , "age" : 12},
    {"name" : "B" , "age" : 14},
    {"name" : "C" , "age" : 16},
    {"name" : "D" , "age" : 18},
    {"name" : "E" , "age" : 20}
]

dic = myFilter(a,{"name" : "A" , "age" : 12})
print(dic)

# --------------------------------------------------------

# 🔽 조건을 만족하는 첫 번째 요소의 위치를 반환하는 함수 (key가 함수형태)
def myFilter2(key, a_list):
    for i in range(0, len(a_list)):
        if key(a_list[i]):              # key는 함수 (lambda 등), 조건이 참이면
            return i                    # 해당 index 반환
    return -1                           # 조건 만족 못 하면 -1

# 이름이 "C"인 요소의 index를 찾는 예시 (람다 함수 사용)
pos = myFilter2(lambda x: x["name"] == "C", a)
print(pos)
```

<br><br>

# 🟩 정렬 알고리즘

| 정렬 알고리즘 | 특징                                     | 시간 복잡도 (최악)     |
| ------------- | ---------------------------------------- | ---------------------- |
| 버블 정렬     | 인접한 요소를 비교하여 큰 값을 뒤로 이동 | O(n²)                  |
| 선택 정렬     | 가장 작은 값을 선택해 앞으로 이동        | O(n²)                  |
| 삽입 정렬     | 앞에서부터 정렬된 위치에 삽입            | O(n²)                  |
| 퀵 정렬       | 피벗 기준으로 분할 정렬                  | O(n²), 평균 O(n log n) |
| 병합 정렬     | 데이터를 반으로 나누고 합쳐 정렬         | O(n log n)             |
| 힙 정렬       | 힙 구조로 최소/최댓값 우선 추출          | O(n log n)             |

## 🟢 bubble 정렬

- 작동 방식: 인접한 두 값을 비교해서 더 큰 값을 오른쪽으로 보냄 (큰 수가 "버블"처럼 끝으로 감).
- 반복 횟수: 리스트 크기만큼 반복.
- 장점: 구현이 매우 쉬움.
- 단점: 매우 느림. 거의 모든 경우에 비효율적.

#### 🟡 쉽게 이해하기

numbers = \[5, 3, 8, 1, 2\]  
단순하게 주어진 list의 0번째 요소와 1번째 요소를 비교하고 큰 수를 뒤로 보낸다.  
그것을 1번째 요소와 2번째 요소, 2번째 요소와 3번째 요소를 지속적으로 반복하면서 오름차순 정렬이 됩니다.

```python
def bubble_sort(arr):
    # 배열 길이만큼 반복
    for i in range(len(arr)):
        # 마지막 i개는 정렬되었으므로 비교할 필요 없음
        for j in range(len(arr) - 1 - i):
            # 지금 처음으로 0번째 요소와 1번째 요소를 비교하여
            # 다음은 1번째 요소와 2번쨰 요소를 지속적으로 반복하겠죠???
            print(f"----------------------\n{arr[j]}와 {arr[j+1]}를 비교합니다.")
            if arr[j] > arr[j + 1]:
                # 인접 요소가 크면 큰 것을 뒤로 보내면서 위치 바꿈 (오름차순 정렬)
                print(f"{arr[j]}와 {arr[j+1]}의 위치를 서로 바꿀게요!\n----------------------")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 예제
numbers = [5, 3, 8, 1, 2]
bubble_sort(numbers)
print(numbers)  # [1, 2, 3, 5, 8]
```

## 🟢 select 정렬

- 작동 방식: 전체 데이터 중에서 가장 작은(또는 큰) 데이터를 골라서 맨 앞(또는 맨 뒤)과 교환.
- 비교 횟수: 항상 n²번 비교.
- 장점: 메모리를 추가로 거의 사용하지 않음.
- 단점: 매우 느림. 실제로 거의 사용되지 않음.

#### 🟡 쉽게 이해하기

0번째 요소를 두고, 해당 요소의 오른쪽으로 모든 리스트를 확인해서 0번째 요소보다 작은 수라면 바꾸고, 또 다시 찾아서 더 작은 수가 있으면 또 바꾸고, 또 다시 찾아서 더 작은 수가 있으면 또 바꾸는 방식으로 가장 작은 수가 맨 앞으로 옵니다.  
이렇게 반복하면서 오름차순으로 정렬이 됩니다.

```python
a_list = [5, 3, 2, 4, 1, 8, 7, 10]

def selectSort(list):
    b_list = [s for s in list]  # ✅ 원본 리스트를 복사 (얕은 복사 X, 하드 카피)
                                # → 정렬 결과가 원본에 영향을 주지 않도록
                                # b_list는 원본과 동일한 값으로 시작

    for i in range(0, len(b_list) - 1):  # ✅ 맨 끝 전까지만 반복 (총 n-1회)
                # ❓ 왜 맨 끝 전까지만 반복하는가?
                # = 만약 길이가 5라면 마지막 자리(4번째)는 남은 하나밖에 없으니 정렬이 자동으로 확정됩니다!

        for j in range(i + 1, len(b_list)):  # ✅ i번째 다음 요소를 j로 지속적으로 넣으면서 i 다음 요소부터 끝까지 비교
            if b_list[i] > b_list[j]:        # ✅ i 위치 값보다 더 작은 값이 있으면

                # ✅ 값을 서로 바꿈 (스왑)
                b_list[i], b_list[j] = b_list[j], b_list[i]

    return b_list  # ✅ 정렬된 리스트를 반환




# 함수 호출: selectSort로 정렬된 새 리스트를 반환
b_list = selectSort(a_list)

print(a_list)  # ✅ 원본 a_list 출력 → [5, 3, 2, 4, 1, 8, 7, 10]
print(b_list)  # ✅ 정렬 결과 출력   → [1, 2, 3, 4, 5, 7, 8, 10]
```

```python
# sorted 함수를 직접 제작

def mySorted(list , key , reverse = False) :
    modify_list = [ item for item in list ]
    if reverse == False :
        for i in range(0,len(modify_list)-1) :
            for j in range(i+1,len(modify_list)) :
                if key(modify_list[i]) > key(modify_list[j]) :
                    modify_list[i] , modify_list[j] = modify_list[j] , modify_list[i]
        return modify_list

    elif reverse == True :
        for i in range(0,len(modify_list)-1) :
            for j in range(i+1,len(modify_list)) :
                if key(modify_list[i]) < key(modify_list[j]) :
                    modify_list[i] , modify_list[j] = modify_list[j] , modify_list[i]
        return modify_list

a = [
    {"name" : "C" , "age" : 16},
    {"name" : "T" , "age" : 14},
    {"name" : "A" , "age" : 22},
    {"name" : "E" , "age" : 17},
    {"name" : "Z" , "age" : 20}
     ]

print(mySorted(a,lambda x : x["name"] , True))
print(mySorted(a,lambda x : x["age"]))
```

<br><br>

# 🟩 가변 매개변수

- 함수의 매개변수 개수가 바뀌는 경우에 사용
- 변수 앞에 \* 을 붙임(튜플 타입으로 함수에서 가져감)
- 매개변수에 기본값을 줄 때는 변수 자체가 여러 개 만들어짐

| 구분        | 문법       | 설명                | 함수 내부 타입 |
| ----------- | ---------- | ------------------- | -------------- |
| 위치 인자   | `*args`    | 개수 제한 없는 인자 | `tuple`        |
| 키워드 인자 | `**kwargs` | key=value 형식 인자 | `dict`         |

## 🟢 위치인자 (\*) 예제

```python
def myadd(*args) :    # 변수 하나에 값을 여러개 전달 = 튜플 형태로 값을 전달하겠다는 의미
  print(type(args))
  for a in args :
    print(a)

myadd(1,2)
myadd(1,2,3)


def myadd2(*data) :
  s = 0
  for i in data :
    s += i
  return s

print(myadd2(1,3,5))
print(myadd2(1,3,5,7))
print(myadd2(1,3,5,7,9))
```

### 🟡 혼용 시 작성 순서 -> (일반인자 , 튜플인자 , dict 인자)

- 일반 매개변수(인자)와 튜플 매개변수(인자) 를 같이 혼용하여 사용해야 할 때는 일반 매개변수가 먼저 작성되어야 함 = 나머지 매개변수를 튜플로 받음
- 일반 매개변수와 튜플 매개변수와 dict 매개변수를 셋다 혼용하여 서용해야 할 때는 다음과 같은 순서로 작성 -> (일반인자 , 튜플인자 , dict 인자)

```python
def myadd3(n , *data) :
    print("n" , n)
    for i in data :
        print(i)

myadd3(1,2,3,4,5)   # 1 까지는 일반 매개변수로 받아지고 2 , 3 , 4 , 5 는 튜플 매개변수로 받아짐
```

## 🟢 키워드 인자 (\*\*) 예제

- dict 타입을 매개변수로 넘길수도 있음
- 이때는 매개변수의 전달 방식이 달라짐
- 함수 밖에서 dict 타입을 만들어서 함수로 매개변수로 넘겨주는 방식
- 함수 안에서는 key 값과 value 값만 매개변수로 넣어주고 함수 안에서 dict 타입으로 만들어서 출력
- 매개변수 앞에 \*\* 을 붙혀서 dict 타입으로 만들어지도록 함

### 🟡 가변 키워드 매개변수

\*\*는 가변 키워드 매개변수 (Keyword Variable Arguments)를 의미합니다.

```python
def myfunc(d) :
    print(d)

person = {"name" : "홍길동" , "age" : 12}
myfunc(person)
```

```python
# 함수 정의: 키워드 인자를 가변적으로 받기 위해 **d를 사용
def myfunc2(**d):
    # d는 딕셔너리 형태(**)로써 key=value 구조의 인자를 모두 저장
    print(d)  # {'name': '홍길동', 'age': 23} 형태로 출력됨

# 함수 호출: 키워드 인자 방식으로 전달
myfunc2(name="홍길동", age=23)
# => 내부적으로는 다음과 같은 딕셔너리로 해석됨: {'name': '홍길동', 'age': 23}
# => 이 딕셔너리가 함수 안에서 변수 d에 저장되어 사용됨
```

```
# 더 쉽게 이해하기 위해서 더 많은 dict를 넣어보겠습니다.

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} => {value}")

show_info(name="철수", age=30, job="개발자")
# 출력:
# name => 철수
# age => 30
# job => 개발자
```

```
def profile(role , *skills , **details) :
  print("role" , role)
  print("skills" , skills)
  print("details" , details)

profile("Programmer" ,
        "Python" , "react" , "Deeplearning" ,
        Salary = 100000000 , Position = "개발자")
```

<br><br>

# 🟩 4월 30일 과제

## 🟢 가위바위보 게임 (과제 같이 만들어보기)

- 컴퓨터가 1 , 2 , 3 중에 랜덤값 하나를 생각하고 있음
- 1 = 가위 , 2 = 바위 , 3 = 보
- 컴퓨터 승 , 사람 승 , 무승부
- 10 번을 해서 각 승률을 계산 / 컴퓨터 몇 번 , 사람 몇 번 , 무승부 몇 번 했는지 나오도록

```python
import random

titles = ["", "가위", "바위", "보"]
titles2 = ["", "컴퓨터승", "사람승", "무승부"]
game_list = []  # {"computer" : , "person" : , "winner" : }
# game_list = [{"computer": "홍길동", "person" : "나", "winner" : "나"}]

def isWinner(computer, person):
  # 무승부에 대해서
  if computer == person:
    return 3  # 무승부인데 3은 무슨 이유지???

  if (computer == 1 and person == 3) or \
    (computer == 2 and person == 1) or \
      (computer == 3 and person == 2):
    return 1 # 컴퓨터가 이김

  return 2 # 무승부하고 이김을 다 조건 줬는데 굳이 하나 남은 것을 if문을 써줄 필요가 없

def game_start():
  game_list.clear()
  # 계속 반복
  while True:
    computer = random.randint(1,3)
    person = int(input('1. 가위, 2. 바위, 3. 보  :' ))
    winner = isWinner(computer, person)
    print(f"컴퓨터: {titles[computer]} | 사람: {titles[person]} | 승자: {titles2[winner]}")
    game_list.append({"computer" : computer, "person" : person, "winner" : winner})
    again = input("게임을 계속하시겠습니까? y/n")
    if again != 'Y' and again != 'y':
      return


def game_statistic():
  computer_win = 0
  person_win = 0
  equal_win = 0
  for game in game_list:
    if game['winner'] == "1":
      computer_win += 1
    elif game['winner'] == "2":
      person_win += 1
    else:
      equal_win += 1

  for game in game_list:
    print(f"컴퓨터: {game['computer']}", end="\t")
    print(f"사람: {game['person']}", end="\t")
    print(f"승패: {game['winner']} \n")

def game_main():
  while True:
    print('1. 게임시작')
    print('2. 게임통계')
    print('3. 게임종료')
    sel = input('선택 : ')
    if sel == '1':
      game_start()
    elif sel == '2':
      game_statistic()
    elif sel == '3':
      print('게임을 종료합니다.')
      return

game_main()
```
