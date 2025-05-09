# 2025년 4월 29일 화요일 (5일차)

## 🟢 스스로 보충 수업

예비창업패키지 발표로 인해 빠지게된 날 1일차

<br><br>

## 📜 목차 (요약)

- Call by Value / Call by Reference
- 함수 default 매개변수
- 함수 분리하기
  - 함수는 하나의 역할만 하도록 만든다.
  - 함수는 15줄을 넘지 않도록 한다.
  - 재사용성이 유용하도록 만든다.
- validation input (에러처리하기)
- lambda : 한줄짜리 함수를 의미하며 함수를 쓰고 버림(일회용 함수)
- filter()
- map()
- sort() / sorted()
- 4월 29일 과제

<br><br>

# 🟩 def() 함수 활용 1

## 🟢 주급계산 문제

- 주급 계산 - 함수를 사용해서 코드 작성 (강사님 작성)
- 함수 안의 코드는 기본적으로 15 ~ 20 줄 이내에서 작성해야하는 것이 좋음 / 아무리 많아도 A4 용지 한장은 넘지 않게 해야함
- 필요하다면 최대한 함수를 쪼개는 것이 좋음
- dictionary type과 def를 사용하는 것이 좋다고 판단됨
- <진짜 문제>  
  주급계산 이름, 근무시간, 시간당급여액 - ex) 5명에 대해서
- name: / work_time: / per_wage:  
  홍길동 40 10000  
  임꺽정 30 20000  
  장길산 20 20000  
  홍경래 10 15000  
  이징옥 20 30000

```
# --------------------------------------------------------------
# 입력
workers2 = []

def input_worker_list():
  name = input('이름을 입력해주세요! :')
  per_wage = int(input('시급을 입력해주세요! :'))
  work_time = int(input('일한 시간을 입력해주세요! :'))
  workers2.append({'name': name, 'per_wage': per_wage, 'work_time': work_time})

# --------------------------------------------------------------
# 계산
def calcul_weekly_pay2(name, per_wage, work_time):
  week_pay2 = int(per_wage) * int(work_time)
  return print(f"{name}님의 시급은 {per_wage}이며, 일한 시간은 {work_time}입니다. 따라서 주급은 총 {week_pay2}입니다.")

# --------------------------------------------------------------
# 출력
for i in range(0, 2):
  input_worker_list()
  calcul_weekly_pay2(workers2[i]['name'], workers2[i]['per_wage'], workers2[i]['work_time'])
```

## 🟢 주급계산 같이 풀어보기 (함수 역할 분리)

```
worker_list = [
                {"name" : "홍길동" , "work_time" : 30 , "per_pay" : 20000} ,              #공용변수로 존재 , 테스트용 데이터 선 입력
                {"name" : "고길동" , "work_time" : 20 , "per_pay" : 30000} ,
                {"name" : "김길동" , "work_time" : 50 , "per_pay" : 20000}
               ]



def append() : #데이터 추가 함수 작성
    worker = {}
    worker["name"]      =     input("이름 : ")
    worker["work_time"] = int(input("근무 시간 : "))
    worker["per_pay"]   = int(input("시간 당 급여액 : "))
    worker["pay"]       = 0     # 주급 계산을 위해서 입력

    worker_list.append(worker)  # 목록에 추가하기

def process(worker) :       # 주급 계산 함수 (dic 타입 데이터를 가져와서 반환하는 방법) , 매개변수로 값을 받아오면 외부로 전달 안되는 것이 원칙
    worker["pay"] = worker["work_time"] * worker["per_pay"]

def process_main() :        # process 함수는 한 명분에 대한 처리 함수이기에 별도로 함수를 만들어 리스트 내의 전체 계산을 위한 함수를 별도 작성
    for w in worker_list :
        process(w)

def output() :
    for w in worker_list :
        print(f"{w["name"]}" , end="\t")
        print(f"{w["work_time"]}" , end="\t")
        print(f"{w["per_pay"]}" , end="\t")
        print(f"{w["pay"]}" , end="\t")
        print() # 줄바꿈 코드

def main_menu() :
    while(True) :              # while(True) : 무한 루프 코드 - 종료를 하지 않는다. 종료를 원하면 break 문을 쓰거나 return 구문을 사용
        print("[1] 추가")       # return - 함수를 종료하면서 함수의 작업 내용을 함수 외부로 전달함
        print("[2] 출력")       # return 을 쓰고 값을 안주면 그냥 함수가 종료됨(함수 종료를 의미함)
        print("[3] 계산")
        print("[0] 종료")
        sel = input("선택 : ")
        if sel   == "1" :       # 사용자가 1 을 입력했을 때
            append()            # 데이터 추가 함수 호출
        elif sel == "2" :       # 사용자가 2 를 입력했을 때
            output()            # 출력 함수 호출
        elif sel == "3" :       # 사용자가 3 을 입력했을 때
            process_main()      # 계산 함수 호출
        elif sel == "0" :       # 사용자가 0 을 입력했을 때
            print("프로그램을 종료합니다.")
            return              # 함수 자체를 종료
        else :
            print("잘못 선택하셨습니다.")   # 입력 오류 체크


main_menu()
```

<br><br>

# 🟩 Call by Value / Call by Reference

## 🟢 함수 - Call by Value

- 함수에 **값을 복사해서 전달**
- 함수 내부 변경 → **원본에 영향 없음**
- `int`, `float`, `str` 같은 **immutable 타입**

```
def toDouble(x) :   # x 라는 매개변수를 이용해서 a 에 값을 전달함
    x = x * 2       # x 값이 2배가 되었는데 함수 외부로 값이 전달이 되는가(?)
#    return x        # 값을 받으려면 return 코드를 사용하면 됨

a = 10              # a 라는 변수와 toDouble(x) 에서의 x 변수는 서로 다른 공간
toDouble(a)         # x 라는 변수에 값을 복사해서 함수를 수행하면서 수정된 x 값은 함수 외부에 있는 a 와는 아무런 관계가 없음 ( = call by value : 함수를 값 복사로 호출함)
print(a)
```

## 🟢 함수 - Call by Reference

- 함수에 **객체 참조(주소)를 전달**
- 함수 내부 변경 → **원본에도 영향 있음**
- `list`, `dict`, `set` 같은 **mutable 타입**
- call by referance = 함수에 값 복사가 아닌 값이 저장된 주소를 불러와 호출함
- 리스트 타입 , 딕 타입 , 클래스 타입의 변수들은 함수에서 호출 시 call by value 가 아닌 call by referance 로 자동으로 실행되어 값이 변경됨
- 상기 타입들은 내부 구조가 다르기에 함수 내에서 값 변환이 가능(함수에 값을 복사하여 전달하는 것이 아니고 값이 저장된 주소를 전달하기 때문에 가능)

```
def toDouble(mydic) :
    mydic["x"] *= 2
    mydic["y"] *= 2

mydic = {"x" : 1 , "y" : 2}
toDouble(mydic)
print(mydic)
```

<br><br>

# 🟩 def() - 매개변수 default value

## 🟢 오버로딩

파이썬의 경우는 오버로딩을 지원하지 않음  
오버로딩 - 동일한 이름의 함수인데 매개변수 등의 개수나 타입등을 이용해서 동일한 이름의 함수를 여러개 만드는 것  
오버로딩의 장점 : 사용자가 편함

파이썬에서는 상기 오버로딩을 지원하지 않음 , 왜냐하면 변수에 특정한 타입을 지정해서 사용하지 않기 때문에 매개변수의 개수나 타입으로 호출할 함수의 구분이 안됨  
하지만 매개변수에 기본값을 줄 수 있어서 마치 오버로딩과 같은 효과를 줄 수 있음

매개 변수 기본값 설정

```
def myadd(x = 0 , y = 0 , z = 0) :  # 함수의 매개 변수에 기본 값을 주면 값을 전달하지 않으면 기본값이 적용됨
    return x + y + z

result = myadd(1,2,3)   # 매개변수를 넣었을 때
print(result)

result = myadd()        # 매개변수를 안 넣었을 때 - 오류 발생(함수의 매개변수에 기본 값이 적용되어 있지 않으면)
print(result)           # 매개변수를 안 넣었을 때 - 기본 값으로 출력(함수의 매개변수에 기본 값이 적용되어 있으면)

# 함수의 매개변수에 기본값이 설정되어 있기에 매개변수를 생략하거나 적게 넣을 수 있어서 오버로딩과 같은 효과를 볼 수 있음
print(myadd())
print(myadd(1))
print(myadd(1,2))
print(myadd(1,2,3))
```

#### 🟡 주의할 점

모든 매개변수에 기본값을 주어야하는 것은 아니지만, 기본값을 주기 시작한 부분부터 나머지 매개변수도 다 기본값을 주어야 한다.

```
def myfunction(a , b , c = 0 , d = 0) : # 해당 함수는 오류 미발생(단, 호출시 최소한 2개의 매개 변수는 주어야함, 그래야 오류가 뜨지 않음)
    return a + b + c + d

print(myfunction(1,2))                  # 호출 시 최소 2개의 매개변수를 주지 않으면 호출 오류 발생됨

def myfunction_2(a = 0 , b , c , d) :  # 해당 함수는 오류 발생 , 기본값을 주기 시작한 부분부터 끝까지 매개변수가 설정되어있지 않음
    return a + b + c + d
```

#### 🟡 매개변수 기본값 예제

```
def sigma(limit = 10) :
    sum = 0
    for i in range(0,limit) :
        sum += i
    return sum

print(sigma())
print(sigma(5))
print(sigma(100))
```

<br><br>

# 🟩 수업 중 과제 1

### 🔵 성적 처리해주는 프로그램 만들기

- 함수 구조 기반으로 성적 처리 프로그램 작성
  - 기본 출력을 위해서 기본값 입력
  - 없을 때 바로 출력 함수를 호출하면 오류 발생
  - dict 타입의 구조가 문법적으로 javascript 의 JSON 데이터 구조하고 동일
  - MySQL 의 속도가 너무 느려서 빅데이터에 사용하기 어려워서 몽고디비를 주로 사용 , 몽고디비가 JSON 형태로 데이터 저장을 하기에 빅데이터쪽은 몽고디비 쪽을 사용해야 함
  - 판다스에 데이터프레임이라는 구조가 있음 , dataframe <-> dict 변환이 쉬움

### 🔵 문제 내용

- 반에 5명이 존재한다. 이 인원을 대상으로
- <입력>
  - 이름
  - 국어
  - 영어
  - 수학
- <계산>

  - 1.  총점
  - 2.  평균
  - 3.  평균 결과에 대해서

    - 수(90)
    - 우(80)
    - 미(70)
    - 양(60)
    - 가(60미만)

- <출력>

  - 1.  총점
  - 2.  평균
  - 3.  평균 결과에 대해서

    - 수(90)
    - 우(80)
    - 미(70)
    - 양(60)
    - 가(60미만)

```python
student_list = [
    {"name" : "홍길동" , "kor_score" : 85 , "eng_score" : 70 , "mth_score" : 87 , "score_sum" : 242 , "score_aver" : 80 , "grade" : "A"}
]

def append() :
    student = {}
    student["name"]      =     input("학생의 이름을 입력하세요 :")
    student["kor_score"] = int(input("국어 성적을 입력하세요 : "))
    student["eng_score"] = int(input("영어 성적을 입력하세요 : "))
    student["mth_score"] = int(input("수학 성적을 입력하세요 : "))

    student_list.append(student)

def cal_score(student) :
    student["score_sum"] = student["kor_score"] + student["eng_score"] + student["mth_score"]
    student["score_aver"] = student["score_sum"] // 3

def cal_grade(student) :
    if student["score_aver"] >= 80 :
        student["grade"] = "A"
    elif student["score_aver"] >= 70 :
        student["grade"] = "B"
    elif student["score_aver"] >= 60 :
        student["grade"] = "C"
    else :
        student["grade"] = "D"

def cal_main() :
    for i in student_list :
        cal_score(i)
        cal_grade(i)

def output() :
    for i in student_list :
        print(f"이름 : {i["name"]}\t총 점수 : {i["score_sum"]}\t평균 점수 : {i["score_aver"]}\t등급 : {i["grade"]}")

def menu() :
    while (True) :
        print("[1] 학생 입력")
        print("[2] 성적 계산")
        print("[3] 기록 출력")
        print("[0] 프로그램 종료")
        sel = input("메뉴 선택 : ")

        if sel == "1" :
            append()
        elif sel == "2" :
            cal_main()
        elif sel == "3" :
            output()
        elif sel == "0" :
            return
        else :
            print("잘못 입력하셨습니다.")

menu()
```

#### 🔴 점수 입력 시 오류 체크가 필요

- 지역변수 - 변수 선언 시 함수 내에서 선언된 변수는 해당 함수 내에서만 존재
- 전역변수 - 함수 외부에서 선언된 함수는 모든 함수에서 사용할 수 있음
- 함수를 만들때는 최대한 함수가 하나의 기능에만 집중하도록 만드는 것이 중요!!
- 에러가 발생하면 에러처리를 먼저할 것!!

```python
""" EX:))
def myfunc() :
    if error1 :
        return -1
    if error2 :
        return -2
"""


score_list = []

# ================================================
# 입력 + validation

def getNumber(subject) :
    number = input(f"{subject} : ")
    while isDigit(number) == False :
        print("숫자만 입력해주세요.")
        number = input("정수를 입력하세요 : ")
    return int(number)

# input 으로 받는 모든 데이터는 string 타입
# ord 함수를 통해서 숫자인지 아닌지 판단 가능
# 문자열을 받아서 한글자씩 "0" 과 "9" 사이에 있는 지 확인
# 글자 중에 하나라도 0 - 9 사이에 존재하지 않으면 에러(숫자가 아닌 것으로 판단)
def isDigit(number) :
    for i in range(0,len(number)) :
        if ord(number[i]) < ord("0") or ord(number[i]) > ord("9") :
            return False

    return True


# 입력한 점수가 0 ~ 100 사이에 있는 숫자인지 확인
def getScore(subject = "국어" , limit = 100) :
    n = getNumber(subject)
    while n < 0 or n > limit :
        print(f"0 ~ {limit} 사이의 값을 입력하세요")
        n = getNumber(subject)
    return n

# 국어 , 영어 , 수학 성적 합산
def getSum(s) :
    return s["kor"] + s["eng"] + s["mth"]

# 합산 성적의 평균 계산
def getAvg(s) :
    return s["sum"] // 3

# 성적 평균에 따른 등급 설정
def getGrade(s) :
    if   s["avg"] >= 80 :
        return "수"
    elif s["avg"] >= 70 :
        return "우"
    elif s["avg"] >= 60 :
        return "미"
    elif s["avg"] >= 50 :
        return "양"
    else :
        return "가"

def append() :
    s = {}

    s["name"]  = input("이름 입력 : ")
    s["kor"]   = getScore("국어")
    s["eng"]   = getScore("영어")
    s["mth"]   = getScore("수학")
    s["sum"]   = getSum(s)
    s["avg"]   = getAvg(s)
    s["grade"] = getGrade(s)

    score_list.append(s)


# ================================================
# 출력
def output() :
    for s in score_list :   # score_list 로부터 하나씩 s 라는 변수에 전달
        print(f"이름 : {s["name"]}",end="\t")
        print(f"국어 성적 : {s["kor"]}",end="\t")
        print(f"영어 성적 : {s["eng"]}",end="\t")
        print(f"수학 성적 : {s["mth"]}",end="\t")
        print(f"총 점 : {s["sum"]}",end="\t")
        print(f"평 균 : {s["avg"]:.0f}",end="\t")
        print(f"등 급 : {s["grade"]}")


def start() :
    while True :
        print("[1] 추가")
        print("[2] 출력")
        print("[0] 종료")
        sel = input("메뉴 선택 : ")
        if sel == "1" :
            append()
        elif sel == "2" :
            output()
        elif sel == "0" :
            print("프로그램을 종료합니다.")
            return
        else :
            print("메뉴 입력을 잘못하셨습니다.")

start()
```

<br><br>

# 🟩 lambda (람다)

- 람다란, 한줄짜리 함수를 의미하며 함수를 쓰고 버림(일회용 함수)
- 일회용 함수이기 때문에 메모리 효율성이 높아짐
- 파이썬에서 람다는 2줄 이상 코드 작성할 수 없음 - 1줄 밖에 작성할 수 없음(현재 버전)

## 🟢 함수는 그 자체가 '주소' 이다

- 변수에 함수가 있는 곳의 '주소' 를 저장할 수 있음

```
def add(a = 0 , b = 0 , c = 0) :
    return a + b + c
myadd = add             # myadd 라는 변수에 add 라는 함수 주소를 입력하고
print(myadd(3,4,5))     # myadd 변수를 이용해서 add 라를 함수를 실행할 수 있음
```

## 🟢 함수의 매개변수로 함수를 줄 수 있음

```

def myfunc(x,y,callback) :      # 세번째 매개변수(callback) 이 함수 - 함수 주소를 가져옴
    result = callback(x,y)
    print(x,y,result)

def add(x,y) :
    return x + y

myfunc(4,5,add)     # 함수 주소를 전달

myfunc(4,5, lambda x,y : x-y)   #람다로 임시 함수를 만듦. lambda 로 시작해야 하고 이름은 없으며 매개변수 설정은 호출자에 따라감 , ":" 뒤에는 함수의 내용을 기술하면 되고 return 은 생략한다

fuc_list = [        # 리스트에 다양한 람다 함수를 만들어서 리스트[인덱스] 호출을 사용하여 가능
    lambda x,y : x-y ,
    lambda x,y : x+y ,
    lambda x,y : x*y ,
    lambda x,y : x/y
]

for f in fuc_list :
    print(f(9,7))
```

<br><br>

# 🟩 filter()

### 🟡 형태

```
filter(함수, 반복가능한_객체)
```

### 🟡 특징

- 파이썬의 내장함수
- 함수: 각 요소에 적용될 True/False를 반환하는 함수
- 반복 가능한 객체: 리스트, 튜플, 문자열 등
- 앞에 함수 , 두번째 인자에 iterable 변수가 옴
  - 이렇게 iterable한 존재는 자동으로 for문인 듯 함수에 하나씩 들어갑니다.
- 반환값은 filter 객체 → list()로 감싸야 출력됨
- 특정 조건에 부합하는 데이터의 iterable 타입을 반환
- 주로 lambda하고 간편하게 같이 쓰입니다.
- lambda도 한번쓰고 버리는 것이였는데, filter도 한번 쓰고 버리는 느낌입니다.

### 🟡 작동방식

```
words = ["hi", "hello", "yes", "python"]

# 1. filter가 iterable한 것을 함수에 하나씩 넣어서 뽑아내면,
# 2. 결과들을 long_words는 filter라는 타입으로 값들을 저장하고 있음.
long_words = filter(lambda x: len(x) >= 3, words)
print(type(long_words))

# 3. 그래서 여기서 type을 list로 바꿔준 것입니다.
# (특히, 리스트로 형변환을 하지 않으면 값을 볼 수 없습니다.)
# filter객체는 메모리에 모든 값을 저장하지 않고, 필요할 때 하나씩 꺼내는 "게으른 평가 (lazy evaluation)"방식.
print(list(long_words))     # ['hello', 'yes', 'python']
print(list(long_words), '다시 출력하면 빈 리스트이다. 이미 소모되어버림')     # 🔥 다시 출력하면 빈 리스트 → 이미 소모됨

# 4. 애초에 이렇게 list로 감싸서 사용한다면 애초에 리스트에 저장해서 주기 때문에 날라가는 filter형이 아닌 list형으로 저장해버립니다.
long_words2 = list(filter(lambda x: len(x) >= 3, words))    # 🔥 사라지지 않습니다. no lazy!
print(list(long_words))     # ['hello', 'yes', 'python']
print(list(long_words))     # 사라지지 않고 잘 출력될 것입니다.

# 5. for문을 쓰는 경우
# 즉 filter형도 iterable이기 때문에 filter가 계산이 다 끝나고 하나씩 for문으로 집어넣는다.
for person in filter(lambda e : e["name"] == keyname , person_list) :
    print(f"이름 : {person["name"]}\t나이 : {person["age"]}\t연락처 : {person["phone"]}\t ")
# 어차피 iterable한 filter가 for문에 잘 들어가기 때문에 여기서는 list로 감싸주지 않아도 값을 충분히 볼 수 있음.

find_list = (list(filter(lambda e : e["name"] == keyname , person_list)))
print(find_list)
```

<br><br>

# 🟩 map()

## 🟢 `map()` 기본 개념

### 🟡 정의

- **함수**와 **이터러블 객체**를 받아 각 요소에 함수를 적용한 결과를 반환하는 함수
- **지연 평가(Lazy Evaluation)**: 즉시 계산하지 않고 필요 시 결과 생성

### 🟡 기본 구조 (형태)

```
map_obj = map(function, iterable[, iterable2, ...])
```

- function: 각 요소에 적용할 함수
- iterable: 함수를 적용할 반복 가능한 객체 (리스트, 튜플 등)
- map()은 이터레이터 를 반환, 그래서 list(), tuple()로 변환해야 실제 값 확인 가능

### 🟡 작동방식

- filter하고 비슷하게 생겼다고 하는 것은 틀린 것이지만, 이해하기에는 비슷하다고 이해합시다. 하지만 map은 그저 주어진 동작을 수행하고 return 합니다.

## 🟢 예제

```python
# 이렇게 한줄로 만들어버릴 수 있습니다.
# 🔥 지연 평가(Lazy Evaluation)에 대해서 파악해봅시다.

result3 = map(lambda x, y: x + y, [10, 20], [1, 2])

# map()은 이터레이터 를 반환, 그래서 list(), tuple()로 변환해야 실제 값 확인 가능
print(list(result3))  # [11, 22]
print(list(result3))  # 🔥 요소가 사라져버림... 필요할 때 나타났다가 소모되어버림
```

```
person_list = [
    {"name" : "홍길동" , "age" : 34 , "phone" : "010-0000-0001"},
    {"name" : "정발산" , "age" : 70 , "phone" : "010-0000-0005"},
    {"name" : "강감찬" , "age" : 54 , "phone" : "010-0000-0003"},
    {"name" : "이순신" , "age" : 30 , "phone" : "010-0000-0002"},
    {"name" : "김종서" , "age" : 27 , "phone" : "010-0000-0008"},
    {"name" : "장영실" , "age" : 66 , "phone" : "010-0000-0006"},
    {"name" : "서희"   , "age" : 75 , "phone" : "010-0000-0001"},
    {"name" : "곽재우" , "age" : 41 , "phone" : "010-0000-0009"}
]

def myfunc_3(x) :
    x["age"] = x["age"] + 5
    return x

# map 사용 시 함수를 사용하지 않으면 객체가 나오지 않음
for per in map(myfunc_3, person_list) :
    print(per)
```

<br><br>

# 🟩 sort()

### 🟡 정의

- 데이터 정렬 함수
- sort()는 리스트 내부에서 직접 정렬을 수행하는 메서드입니다.
- 리스트 타입: 타입 자체로 정렬을 지니고 있음
- 즉, 원본 리스트를 정렬 상태로 변경(in-place) 합니다.
- 정렬된 새로운 리스트를 반환하지 않으며, 반환값은 None입니다.

### 🟡 기본 구조 (형태)

```
list.sort(key=None, reverse=False)
```

- key (옵션): 정렬 기준이 되는 함수
- reverse (옵션): True이면 내림차순, 기본은 False (오름차순)
- list 형태에만 사용가능 (dict의 경우 list dict '\[{}\]'여야 가능)

### 🟡 특징

- sort 함수가 filter처럼 별도로 존재
- sort내부에 key 라는 매개변수에 lambda 를 전달할 수도 있음.
- dict 타입은 dict 타입끼리의 비교 연산자가 없어서 .sort() 를 사용할 수 없음 - 오류 발생
- dict 타입은 대신 sort()함수 내부에 key 라고 하는 매개변수를 주고 lambda 를 사용해서 처리할 수 있습니다.
- 이 때 제공하는 lambda 는 매개변수 하나고 반환값이 > 연산자가 지원되는 반환타입만 매개변수로 사용이 가능하다.
- 오름차순이 기본값이며, reverse 값은 True 로 변경하면 내림차순으로 정렬함
- list 타입에 속한 함수 sort 는 자신의 순서가 바뀜

## 🟢 예제

```python
nums = [5, 2, 9, 1]
nums.sort()
print(nums)  # [1, 2, 5, 9]

# 🟡 reverse를 true로 설정했을 경우, 내림차순으로 정렬이 된다.
# 이거말고 없습니다.

nums.sort(reverse=True)
print(nums)  # [9, 5, 2, 1]

# 🟡 key 값 사용해보기 1
words = ["apple", "banana", "cherry", "date"]

# 문자열 길이 기준으로 정렬
words.sort(key=len)
print(words)  # ['date', 'apple', 'banana', 'cherry']

# 🟡 key 값 사용해보기 2 (lambda)

# dict list type
people = [
    {"name": "홍길동", "age": 25},
    {"name": "김철수", "age": 20},
    {"name": "이영희", "age": 30}
]

# 나이 기준 정렬
people.sort(key=lambda person: person["age"])

# 딕셔너리 리스트에 적용해보기
person_list = [
    {"name" : "홍길동" , "age" : 34 , "phone" : "010-0000-0001"},
    {"name" : "정발산" , "age" : 70 , "phone" : "010-0000-0005"},
    {"name" : "강감찬" , "age" : 54 , "phone" : "010-0000-0003"},
    {"name" : "이순신" , "age" : 30 , "phone" : "010-0000-0002"},
    {"name" : "김종서" , "age" : 27 , "phone" : "010-0000-0008"},
    {"name" : "장영실" , "age" : 66 , "phone" : "010-0000-0006"},
    {"name" : "서희"   , "age" : 75 , "phone" : "010-0000-0001"},
    {"name" : "곽재우" , "age" : 41 , "phone" : "010-0000-0009"}
]

person_list.sort(key = lambda e : e["name"])
print(person_list)

person_list.sort(key = lambda e : e["name"] , reverse = True)
print(person_list)

person_list.sort(key = lambda e : e["age"])
print(person_list)

# sorted(iterable 데이터 , key , reverse) - 첫번째 매개변수로 전달된 데이터의 원래 순서를 안 바꾸고 바뀐 순서를 list 로 만들어 전달
a = [9,3,5,1,78,1,8,0]
b = sorted(a)
print("a =" ,a)
print("b =" ,b)

```

<br><br>

# 🟩 sorted()

| 항목      | `list.sort()`               | `sorted()`                                     |
| --------- | --------------------------- | ---------------------------------------------- |
| 적용 대상 | 리스트만 가능               | 반복 가능한 모든 자료형 (`list`, `tuple`, ...) |
| 결과      | 원본을 직접 정렬 (in-place) | 새로운 정렬된 리스트를 반환                    |
| 리턴값    | `None`                      | 정렬된 새 리스트                               |

### 🟡 정의

- sorted()는 반복 가능한(iterable) 객체를 정렬된 리스트로 반환하는 내장 함수입니다.
- 원본을 변경하지 않고, 새로운 리스트를 반환합니다.

### 🟡 기본 구조 (형태)

```python
sorted(iterable, *, key=None, reverse=False)
```

| 인자       | 설명                                                 |
| ---------- | ---------------------------------------------------- |
| `iterable` | 리스트, 튜플, 문자열, 딕셔너리 등 반복 가능한 자료형 |
| `key`      | 정렬 기준 함수 (`lambda`, `len`, `str.lower` 등)     |
| `reverse`  | `True`면 내림차순, 기본은 `False` (오름차순)         |

## 🟢 예제

```python
# 🟡 원본을 바꾸지 않는다. 바꾼 값을 따로 저장한다. 즉 return이 있다.
nums = [5, 2, 9, 1]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 5, 9]
print(nums)         # [5, 2, 9, 1] (원본 유지)

# 🟡 문자열 리스트 정렬
words1 = ['banana', 'apple', 'cherry']
print(sorted(words1))  # ['apple', 'banana', 'cherry']

# 🟡 단순 reverse=True
words2 = ['banana', 'apple', 'cherry']
print(sorted(words2, reverse=True))  # ['cherry', 'banana', 'apple']

# 🟡 문자열 길이 기준 정렬 (key 사용)
words3 = ['banana', 'apple', 'cherry']
print(sorted(words3, key=len))  # ['apple', 'banana', 'cherry']

# 🟡 문자열, 튜플에도 사용 가능

print(sorted("python"))    # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted((3, 1, 2)))    # [1, 2, 3]

# 🟡 딕셔너리 해보기

d = {'b': 2, 'c': 3, 'a': 1}

# 키 기준
print(sorted(d.items()))
# [('a', 1), ('b', 2), ('c', 3)]

# 값 기준
print(sorted(d.items(), key=lambda x: x[1]))
# [('a', 1), ('b', 2), ('c', 3)]

# 🟡 사용자 정의 객체 정렬 (딕셔너리 리스트 등)

students = [
  {"name": "홍길동", "age": 23},
  {"name": "김철수", "age": 21},
  {"name": "이영희", "age": 25}
]

# 나이 기준 정렬
sorted_students = sorted(students, key=lambda x: x["age"])

# 🟡 dict list 정렬
person_list = [
    {"name" : "홍길동" , "age" : 34 , "phone" : "010-0000-0001"},
    {"name" : "정발산" , "age" : 70 , "phone" : "010-0000-0005"},
    {"name" : "강감찬" , "age" : 54 , "phone" : "010-0000-0003"},
    {"name" : "이순신" , "age" : 30 , "phone" : "010-0000-0002"},
    {"name" : "김종서" , "age" : 27 , "phone" : "010-0000-0008"},
    {"name" : "장영실" , "age" : 66 , "phone" : "010-0000-0006"},
    {"name" : "서희"   , "age" : 75 , "phone" : "010-0000-0001"},
    {"name" : "곽재우" , "age" : 41 , "phone" : "010-0000-0009"}
]

print(person_list)  # 그냥 단순 출력

# --------------------------------------------
# 새로운 리스트를 만듭니다.
person_list_2 = sorted(person_list , key = lambda e : e["name"])

print(person_list_2)  # 정렬된 리스트를 출력
```

<br><br>

# 🟩 4월 29일 과제

5개의 문제 풀기

```python
# 주어진 list
words = ["assembly" , "java" , "rain" , "notebook" , "north" , "south" , "hospital" , "programming" , "house" ,"hour"]


# 1. filter 함수를 사용하여 글자수가 6 글자 이상인 단어만 출력하기 (컴프리헨션 X)
for i in filter(lambda is_six_text : len(is_six_text) >= 6, words):
  print(f"filter 함수를 이용하여 6글자 이상인 것만 출력하기 = {i}")


# 2. map 함수를 사용해서 글자를 대문자로 바꾸어서 출력 (컴프리헨션 X)
# for i in map(lambda convert_upper : upper(convert_upper), words):
for i in map(lambda convert_upper : convert_upper.upper(), words):
  print(f"map 함수를 활용하여 모두 대문자로 바꿔버리기 = {i}")


# 3. sorted 함수를 사용해서 단어들의 길이순으로 오름차순으로 정렬하여 출력하기
sorted_words_list = sorted(words, key=len)
print(sorted_words_list)


# 4. sorted 함수를 사용해서 알파벳 순으로 내림차순으로 정렬하여 출력하기
sorted_words_list2 = sorted(words, reverse=True)
print(sorted_words_list2)


# 5. 단어 중에 o 가 포함되는 단어가 모두 몇개인지 카운트하기 ( 힌트 , filter 를 사용 )
o_variable = list(filter(lambda text : 'o' in text, words))
print(f"o가 포함되는 단어는 모두 몇개인가? = {len(o_variable)}개")
```
