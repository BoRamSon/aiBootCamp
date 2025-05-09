# 2025년 5월 7일 수요일 (8일차)

### 🔵 오늘의 수업

- 복습 2일차
- 함수를 아직 복습하지 못했기 때문에 먼저 함수부터 하겠습니다.
- class까지 나가고,
- 객체지향까지 나아가겠습니다.

# 📜 목차

- 함수 총 정리
  - 세대정리
  - 전역변수, 지역변수 (복습)
  - 함수의 매개변수 기본값 (복습)
  - python function 'Generator'
- 문제 풀기 (면적 구하기)
- 문제 풀기 (중복데이터 제거, 숫자문자열 정수로 바꾸기)
- class
  - 생성자 \_\_init\_\_(self): 활용하기
  - 주급계산을 생성자를 활용하여 1명 처리해보기
- module
  - WeekPay.py
  - WeekPayManager.py
  - \_\_init\_\_.py
- 5월 7일 과제

<br><br>

# 🟩 함수 총 정리

## 🟢 세대 정리

- 1세대
- 2세대
  - 고급언어(사람의 말과 유사한), 코볼, 포트란, 범용 언어(다목적용 언어를 못 만들음)
    - 코볼 - 데이터 처리 전문(시장은 끝났다.).
    - 포트란 - 과학기술계산용(물리학과, 원자력발전소)
    - 스파게티 코드 - 대충 의식의 흐름대로 프로그램을 함
    - goto문 - 아무데로나 막 점프한다. 현재는 시스템프로그램 분야 외에는 거의 안쓰는 걸로....
- 3세대
  - C, algol, pascal 등등...
    - 스파게티 코드에 대한 반성이 시작됨 그러면서 구조적 프로그래밍이라는 단어가 등장함
    - 구조적 프로그래밍 특징
      - 1.  top -> down 설계방식 : 기본부터 -> 아래로 내려가는 방식
      - 2.  설계라는 개념을 처음 시도를 한다.
      - 3.  순서도
      - 4.  모듈화 (함수와 프로시저로 프로그램을 작은 단위로 나누어서 프로그램을 한다.)
      - 5.  주석을 열심히
      - 6.  소프트웨어 공학
- 4세대

  - 객체지향 프로그래밍, 3세대의 반성

    - 1.  bottom -> up : 3세대의 경험을 바탕으로 부품화 (부품들을 모으면 하나의 제품이 되더라)
    - 2.  객체지향

      - 1. 추상화: 내부의 상세한 내용을 몰라도 사용에 아무 제한사항이 없는 성격을 말합니다. 추상화가 극대화 될 수록 사용자가 편해집니다.
        - ex. list, tuple, dict, map, filter 등등의 내부구조를 몰라도 된다.
      - 2. 은닉성: 데이터를 감춥니다.
        - 컴퓨터의 case가 없으면 오염으로부터 취약하다.
        - 데이터를 보호하자.
        - 접근 권한을 만들어서 외부로 접근을 막는다.
        - 최근에는 이 성격이 약화되고 있다.
        - 특히 파이썬의 경우 전부 사용가능하다.
      - 3. 상속성 : 코드의 재활용도를 높인다. 프레임워크
        - 코드를 처음부터 짜는게 아니라 이미 만들어놓은 클래스들 중에서 유사한거 골라서 상속 받아서 만든다.
      - 4. 다형성 : 이름은 같은데 형태가 여러개
        - overloading(자바), 매개변수 기본값(파이썬)
        - overriding(상속) - 상속 받아서 다시 정의할 때 사용

## 🟢 함수의 규칙 (복습)

```
def 함수이름():
  ....
  ....
```

- 함수이름 규칙은 변수 규칙과 동일하다.
  1.  영문자로 시작하고 \_ 가능
  2.  대소문자 구분
  3.  예약어 안됨
  4.  (암묵적으로) 소문자로 시작한다.
  5.  (암묵적으로) 스네이크 표기법을 사용한다.

### 🟡 전역변수, 지역변수 (복습)

- 전역변수 (global)
  - 함수 안에서 변수를 사용하면 값을 읽는게 아니고 값을 할당하면, 외부에 있는 전역변수를 가려버린다.

```python
global_x = 10 # 1. 함수 외부에 변수를 선언함

def myfunc1():
  global global_x  # 6. 🔥 예외적으로 외부 변수를 같이 사용하고 싶다면 global을 앞에 붙인다.
  global_x = 30  # 2. 현재 이 친구는 함수 내부에만 존재하는 지역변수
      # 3. 함수 내부에서 변수에 값을 할당하는 순간 변도의 변수가 만들어진다.

  y = 20
  print(global_x, y)

global_x = 100
myfunc1()  # 4. 지역변수를 우선적으로 가져오는 것을 볼 수 있습니다.
print(global_x)  # 5. 얘는 가장 마지막에 있는 global_x 변수를 가져오겠죠.
                # 7. 함수 내부의 변수가 global이 붙으니, 전역변수로 변했다!!
```

### 🟡 함수의 매개변수 기본값 (복습)

```python
def myfunc2(name = '홍길동', age = '21', phone = '010-0000-0000'):
  print(name)
  print(age)
  print(phone)

myfunc2()  # default value가 그대로 나옵니다.
myfunc2('임꺽정', 123)  # name과 age만 변경해보았습니다.
myfunc2(name = '둘리')  # 이렇게도 매개변수를 줄 수 있습니다.
myfunc2(age = 23)  # 이렇게도 매개변수를 줄 수 있습니다.
myfunc2(phone='8-4833')  #

# 정적결정: 함수를 미리 만들어놓고 호출하는 것
# 동적결정: 실행될 때 함수가 결정되는 것
# 컴파일시간에 결정되면 '정적할당'
# 실행시간에 결정되면 '동적할당'이라고 합니다.
# Java는 컴파일러임에도 불구하고 동적할당,
# 파이썬은 모든 것이 실행시간에 결정된다. 불나방 같이 실행할 때 결정됨.
```

### 🟡 python function 'Generator'

- 제너레이터
  - (개념만 알아두기)
  - 우리가 막 만들어 써야 하는 것은 아니고, 용어 자체가 중요함
  - 값을 하나씩 생성해서 순회할 수 있는 함수나 객체, range나 filter가 해당된다.
- 함수 안에서 값을 반환하려면 return과 yield(얄드)가 있다.
  - return 은 값을 반환하면서 함수를 바로 종료시켜버림.
  - yield 는 값을 반환하는데 함수를 종료하지 않고 대기상태에 들어감.

```
print(range(1,6)) # range라는 함수는 for문 안에 호출하면 데이터 한개씩 만들어서 던져준다.

for i in range(1,6):
  print(i)
```

```python
def myrange(start=1, end=5):
  i=start
  while i <= end:
    yield i  # 이 구문을 만나는 순간 값을 하나 반환하고 멈춘다. (대기 상태)
              # 즉, while문에 끝날 때 끝나게 되는 존재
    i = i + 1


gen = myrange()  # 함수를 호출해서 저장해놓고,
# 실행은 next나 for문으로 실행해야 합니다.
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# = 이것이 바로 generator라고 합니다.
```

```
# 직접 만든 myrange 함수를 사용해보겠습니다.

for i in myrange(1, 10):
  print(i)
```

- 사용성
  1.  데이터가 너무 커서 한방에 생성할 수 없을 때
  2.  무한한 작업이 필요할 때
  3.  파일을 계속 읽어서 처리하고자 할 때

<br><br>

# 🟩 문제

## 🟢 문제 1 (면적구하기)

- 입력화면
  - 1.  원의 면적
  - 2.  사각형 면적
  - 3.  사다리꼴 면적
  - 0.  종료
- 계산 방식

  - 1.  원의 면적

    - 반지름 : 5인 경우 면적은 78.5입니다.

  - 2.  사각형 면적

    - 가로 5, 세로 7인 경우, 면적은 35입니다.

  - 3.  사다리꼴 면적

    - 아랫변 \* 윗변 \* 높이, 면적은 OO입니다.

  - 0.  종료

```python
class InputValidator():
  def __init__(self, user_input):
      self.user_input = user_input

  def validate_number(self):
    if self.is_empty():
      raise ValueError('빈 값입니다. 다시 입력해주세요.')
    if self.is_number_type():
      raise ValueError('숫자만 입력할 수 있습니다. 다시 입력해주세요.')
    if self.is_negative():
      raise ValueError('음수는 허용되지 않습니다. 다시 입력해주세요.')

  def is_empty(self):
    return self.user_input == ''

  def is_number_type(value):
    return isinstance(value, (int))

  def is_negative(self):
    return int(self.user_input) < 0


class InputDataAndValidate():
  def __init__(self):
    self.INPUT_MESSAGES_CIRCLE = {'circle_extent': '원의 반지름 값을 입력해주세요. :' }
    self.INPUT_MESSAGES_RACTANGLE = {'ractangle_width': '사각형의 가로 값을 입력해주세요. :',
                                  'ractangle_langth': '사각형의 세로 값을 입력해주세요. :'
    }
    self.INPUT_MESSAGES_TRAPEZOID = {'trapezoid_width': '사다리꼴의 가로 값을 입력해주세요. :',
                                  'trapezoid_langth': '사다리꼴의 세로 값을 입력해주세요. :',
                                  'trapezoid_height': '사다리꼴의 높이를 입력해주세요. :'
    }

  def input_number(self, number_dict):
    dict_list = {}
    for key, message in number_dict.items():
      for i in range(1,11):
        dict_list[key] = int(input(message))
        try:
          validator = InputValidator(dict_list[key])
          validator.validate_number()
        except ValueError as e:
          print('ERROR:', e)
          if i == 10: return print('종료되었습니다. 다시 시도하세요.')
        else:
          break
      print(f"입력값 확인: \'{key}\': \'{dict_list[key]}\'")
    return dict_list

  def input_result(self, input_select):
    if input_select == '1':
      return self.input_number(self.INPUT_MESSAGES_CIRCLE)
    elif input_select == '2':
      return self.input_number(self.INPUT_MESSAGES_RACTANGLE)
    else:
      return self.input_number(self.INPUT_MESSAGES_TRAPEZOID)


class CalculData():

  def cal_circle_extent(self, dict_list):
    for i in dict_list:
      i['circle_extent_result'] = i['circle_extent'] * i['circle_extent'] * 3.14

  def cal_ractangle_extent(self, dict_list):
    for i in dict_list:
      i['ractangle_extent_result'] = i['ractangle_width'] * i['ractangle_langth']

  def cal_trapezoid_extent(self, dict_list):
    for i in dict_list:
      i['trapezoid_extent_result'] = i['trapezoid_width'] * i['trapezoid_langth'] * i['trapezoid_height']




class OutputData():

  def output_menu(self):
    print("[1] 원의 면적 구하기")
    print("[2] 사각형 면적 구하기")
    print("[3] 사다리꼴 면적 구하기")
    print("[0] 프로그램 종료")

  def output_result(self, dict_list) :
    for i in dict_list :
      print (f"결과: {i}")
      # print(f"{i['name']}",end="\t")


class Controller():
  def __init__(self):
    self.input = InputDataAndValidate()
    self.calcul = CalculData()
    self.output = OutputData()
    self.circle_dict_list = []
    self.ractangle_dict_list = []
    self.trapezoid_dict_list = []


  def start(self):
    while (True) :
      self.output.output_menu()
      sel = input("1 ~ 3번까지 메뉴를 골라주세요. : ")
      if sel == "1" :
          self.circle_dict_list.append(self.input.input_result('1'))
          self.calcul.cal_circle_extent(self.circle_dict_list)
          self.output.output_result(self.circle_dict_list)
      elif sel == "2" :
          self.ractangle_dict_list.append(self.input.input_result('2'))
          self.calcul.cal_ractangle_extent(self.ractangle_dict_list)
          self.output.output_result(self.ractangle_dict_list)
      elif sel == "3" :
          self.trapezoid_dict_list.append(self.input.input_result('3'))
          self.calcul.cal_trapezoid_extent(self.trapezoid_dict_list)
          self.output.output_result(self.trapezoid_dict_list)
      elif sel == "0" :
          print('정상적으로 종료되었습니다.')
          return
      else :
          print('잘못 입력하셨습니다.')


controller = Controller()
controller.start()
```

### 🟡 같이 풀어보기

```python
def circle():
  r = int(input("반지름 :") )
  s = r* r* 3.14
  print(f"면적은 {s} 입니다")


def rectangle():
  width = int(input("가로 : "))
  height = int(input("세로 : "))
  s = width * height
  print(f"면적은 {s} 입니다")


def sadari():
  width = int(input("아랫변 : "))
  width2 = int(input("윗변 : "))
  height = int(input("높이 : "))
  s = (width + width2)*height/2
  print(f"면적은 {s} 입니다")


# def main1():
#   while True:
#     select = input("1.원의면적 2.사각형면적 3.사다리꼴면적 4.종료 ")

#     if select=="1":
#         circle()
#     elif select=="2":
#         rectangle()
#     elif select=="3":
#         sadari()
#     elif select=="4":
#         return
#     else:
#         print("쫌!!!")


# if문을 사용하지 않고 dict로 만들어보기
def main2():
  myfunctions ={"1":circle, "2":rectangle, "3":sadari}
  while True:
    select = input("1.원의면적 2.사각형면적 3.사다리꼴면적 4.종료 ")
    if select in myfunctions.keys() :
      myfunctions[select]() #함수호출
    else:
      return


main2()
```

<br><br>

## 🟢 문제 2

- 리스트를 받아가서 리스트 안에 중복된 데이터를 제거하고 중복되지 않는 데이터 리스트만 반환하는 함수 만들기

```python
test_list = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,12,12,18,18,22,22]

def remove_duplicate():
  return set(test_list)

remove_duplicate()
```

```python
def duplicate_remove(aList):
    temp = []
    for i in aList:
        if i not in temp:  #temp안에 존재안할때
            temp.append(i)
    return temp

a = [4,3,5,8,1,2,56,4,1,2,8]
b = duplicate_remove(a)
print(b)
```

<br><br>

## 🟢 문제 3

- myint 함수 숫자로 입력한 문자열을 받아가서 정수로 바꾸어서 반환하기.
  - 122을 넣었을 경우에는 123을 반환하고, 123A 라는 잘 못된 데이터를 입력하면 -1을 반환하자.

```python
test_string = '123'

def convert_int(input_number):
  try:
    int(input_number)
  except:
    return -1
  else:
    return int(input_number)

convert_int(test_string)
```

### 🟡 같이 풀어보기

```python
# ord를 통해서 유니코드 사용하여 풀어보기

def myint(s):
  sum = 0  # 123  1 2  =>  1*10 + 2 => 123 => 12*10+3
  for c in s:
    if ord(c) < ord('0') or ord(c) > ord('9'):  # 즉, 숫자 '0'부터 '9'까지의 유니코드(ASCII 코드)는 48~57입니다.
      return -1
    sum = sum * 10 + ord(c)-ord('0')   # 문자1 -> 숫자 1로 빠구려먼 '1'-'0'
  return sum

print(myint('123') + myint('345'))
```

<br><br>

## 🟢 문제 4

- 문장을 받아가서 문자열 뒤집어서 보내는 함수
- hint: reverse

### 🟡 같이 풀어보기

```python
def reverse(s):
  result="";
  for i in range(len(s)-1, -1, -1):
      result += s[i]
  return result

print( reverse("korea"))
```

<br><br>

# 🟩 class

### class 설명

- 사용자가 정의하는 데이터 타입이다.
- 객체를 만들기 위한 설계도라고 한다.
  - 예시: 붕어빵틀 = 클래스 / 붕어빵 = 객체
- 관련 있는 데이터와 함수들의 집합니다.
- 때로는 데이터만 존재하는 클래스도 있고
- 때로는 함수만 존재하는 클래스도 있다.
- 그리고 대부분의 경우에는 데이터와 함수가 같이 존재한다.
- 클래스는 데이터 타입이다. 타입은 메모리가 없다.
- 객체를 만들어야 비로소 메모리가 확보된다.

#### 🟡 클래스는 불러오는 방법

```python
class Person:   # 클래스는 첫글자를 대문로 시작한다. 문법이 아니고, 암묵적인 것이다.
  name='홍길동'  # name이라는 클래스 변수가 있다.
  age=12       # age라는 클래스 변수가 있다.

  # 클래스는 데이터 타입이다. 타입은 메모리가 없다.
  # 객체를 만들어야 비로소 메모리가 확보된다.

p1 = Person()  # 객체 또는 개체
print(p1.name)
print(p1.age)

# 이것도 에러가 안나고 잘 출력이 되고 있다....
# 🔥 왜 잘 나오는 것인가??? 이건 말이 안되는데???,
print(Person.name)
print(Person.age)
```

#### 🟡 클래스 생성자 **init**(self)

```python
class Person:   # 클래스는 첫글자를 대문로 시작한다. 문법이 아니고, 암묵적인 것이다.
  name = '홍길동'  # name이라는 클래스 변수가 있다.
  age = 12       # age라는 클래스 변수가 있다.
  # 객체 만들 때마다 호출되는 영역이 아니고 클래스 처음에 딱 한번 호출되는 영역
  # 변수는 생성자에서 만들어야 한다.
  # 생성자는 객체가 생성될 때마다 호출되는 함수
    # 객체가 생성 될 때마다 준비작업을 진행한다.
    # 생성자의 호출자는 시스템이다.
     # 파이썬의 생성자는 __init__() 입니다. (절대 못바꿈.. 정해짐)
    # 첫번째 매개변수는 무조건 self / self가 객체 주소를 전달한다.
    # 자바에서는 this에 해당하는 요소가 self이다.

  # 클래스는 데이터 타입이다. 타입은 메모리가 없다.
  # 객체를 만들어야 비로소 메모리가 확보된다.

  def __init__(self):
    print('생성자 호출')   # 이 때 p1 = Person() 그냥 바로 호출되는 친구


p1 = Person()  # 객체 또는 개체
print(p1.name)
print(p1.age)

# 이것도 에러가 안나고 잘 출력이 되고 있다....
# 🔥 왜 잘 나오는 것인가??? 이건 말이 안되는데??
print(Person.name)
print(Person.age)
# = 만약 name이라는 객체 하나만 생성시켜서 썼다면 모든 class의 애들이 메모리에 다 잡혀버리는 문제가 있다.
# <정리>
  #  → p1.name = ...을 하면 클래스 변수를 덮어쓰지 않고, p1 객체에 자기만의 name을 새로 만듦.
  #  하지만 반대로, 클래스 변수 자체를 수정하면 모든 인스턴스에 영향이 생깁니다.

p2 = Person()
print(p2.name)
print(p2.age)

p2.name = '임꺽정'  # 이 때 별도의 메모리 공간이 만들어진다.
```

<br><br>

# 🟩 class 생성자에 대해서

```python
class Person:
  # 이 공간은 클래스 공간이다. 크래스 정의할 때 딱 한번 싱행된다.
  # 객체 만들 때마다 실행되지 않는다. 그래서 list타입이나 dict타입 등을 함부러 여기에 선언하면 안된다.

  # ❌ 잘 못된 변수 설정 (공통변수 선언하는 곳)
  # name = '홍길동'
  # age = '12'
  # phone = ['010-0000-0001', '010-0000-0002']   # 공통공간...

  # ✅ 잘 된 예시 - 파이썬은 생성자에 변수 만들기
  def __init__(self):
    self.name = ''
    self.age = 0
    self.phone = []

  # 이 함수는 생성자의 변수 내용을 변경하고 있습니다.
  def append(self, name = '임꺽정', age = 13, phone='010-0000-0001'):
    self.name = name
    self.age = age
    self.phone.append(phone)

  def output(self):
    print(self.name, self.age, self.phone)

p1 = Person()
p1.append('장길산', 11, '010-0000-0003')

p2 = Person()
p2.append('김종서', 13, '010-0000-0004')

p1.output()
p2.output()
```

<br><br>

## 🟢 문제 (주급계산)

```python
class WeekPayCalculator:
  def __init__(self):
    self.worker_list = []   # 원래 빈 값으로 만든 상태에서 input을 받아서 사용한다.
    # self.worker_list = [
    #                 {"name" : "홍길동" , "work_time" : 30 , "per_pay" : 20000},
    #                 {"name" : "고길동" , "work_time" : 20 , "per_pay" : 30000},
    #                 {"name" : "김길동" , "work_time" : 50 , "per_pay" : 20000}
    #               ]

  def input_data(self):
      worker = {}
      worker["name"]      =     input("이름 : ")
      worker["work_time"] = int(input("근무 시간 : "))
      worker["per_pay"]   = int(input("시간 당 급여액 : "))
      self.worker_list.append(worker)

  def calcul_data(self) :
    for w in self.worker_list:
      w["pay"] = w["work_time"] * w["per_pay"]

  def output(self) :
    for w in self.worker_list:
      print(f"{w['name']}" , end="\t")
      print(f"{w['work_time']}" , end="\t")
      print(f"{w['per_pay']}" , end="\t")
      print(f"{w['pay']}" , end="\t")
      print()

  def main_menu(self) :
    while(True) :
      print("[1] 추가")
      print("[2] 계산")
      print("[3] 출력")
      print("[0] 종료")
      sel = input("선택 : ")
      if sel   == "1" :
          self.input_data()
      elif sel == "2" :
          self.calcul_data()
      elif sel == "3" :
          self.output()
      elif sel == "0" :
          print("프로그램을 종료합니다.")
          return
      else :
          print("❌ 잘못 선택하셨습니다. 다시 입력해주세요.")   # 입력 오류 체크

c1 = WeekPayCalculator()
c1.main_menu()
```

### 🟡 같이 풀어보기 (한명의 주급만 처리하기)

```python
class WeekPay1():
  def __init__(self, name='', work_time = 20, per_pay = 10000):
    self.name = name
    self.work_time = work_time
    self.per_pay = per_pay
    self.process()

  def process(self):
    self.pay = self.work_time * self.per_pay

  def output(self):
    print(f"이름: {self.name} | 근무한 시간: {self.work_time} | 시급: {self.per_pay} | 주급: {self.pay}")


c2 = WeekPay1('홍길동')
c2.output()
```

### 🟡 같이 풀어보기 (여러명의 주급만 처리하기)

```python
class WeekPay2():
  def __init__(self, name='', work_time = 20, per_pay = 10000):
    self.name = name
    self.work_time = work_time
    self.per_pay = per_pay
    self.process()

  def process(self):
    self.pay = self.work_time * self.per_pay

  def output(self):
    print(f"이름: {self.name} | 근무한 시간: {self.work_time} | 시급: {self.per_pay} | 주급: {self.pay}")

# c2 = WeekPay2('홍길동')
# c2.output()


# 🟡 1. 이것을 또 다른 class로 만들어서 여러개를 처리하는 것으로 만들 수 있습니다.
# 자주 사용하는 클래스의 구조가 있습니다.
# worker_list = [
#   WeekPay2('홍길동', 20, 20000),
#   WeekPay2('고길동', 10, 50000),
#   WeekPay2('김길동', 30, 40000),
#   WeekPay2('이길동', 40, 20000),
#   WeekPay2('장길동', 20, 20000)
# ]

# for w in worker_list:
#   w.output()


# 🟡 2. 이전 클래스를 활용해서 여러명을 처리하는 class를 만들어보겠습니다.
class WeekPayManager:
  def __init__(self):
    self.worker_list = [
      WeekPay2('홍길동', 20, 20000),
      WeekPay2('고길동', 10, 50000),
      WeekPay2('김길동', 30, 40000),
      WeekPay2('이길동', 40, 20000),
      WeekPay2('장길동', 20, 20000)
    ]

  def output(self):
    for w in self.worker_list:
      # 1) 여기에 WeekPay2('홍길동', 20, 20000) 클래스 자체가 들어와버립니다.
      # 2) 그러면서 w가 output
      w.output()


c3 = WeekPayManager()
c3.output()
```

<br><br>

# 🟩 module (py파일들의 모음)

### 🟢 1. 별도의 WeekPay.py 파일 만들고 주급계산 코드를 넣어줍니다.

이 코드는 한명의 주급을 계산해줍니다.

```python
class WeekPay():
  def __init__(self, name='', work_time = 20, per_pay = 10000):
    self.name = name
    self.work_time = work_time
    self.per_pay = per_pay
    self.process()

  def process(self):
    self.pay = self.work_time * self.per_pay

  def output(self):
    print(f"이름: {self.name} | 근무한 시간: {self.work_time} | 시급: {self.per_pay} | 주급: {self.pay}")


# w1 = WeekPay('A')
# w1.output()


# 파이썬의 모듈들은 내장변수가 있다. __name__ 을 누구나 가지고 있습니다.
  # 언더바 2개는 다 내장이다. (우리가 만든게 아닌 시스템 제공)
print(__name__)  # 이 모듈로 직접 실행하면 main이 들어온다. python Weekpay.py
# import 되서 싱행되면 파일명이 전달된다. python WeekPayManager.py

if __name__ == "__main__":
  w1 = WeekPay('A')
  w1.output()
```

### 🟢 2. 별도의 WeekPayManager.py 파일을 만들어주고, class 코드를 넣어줍니다.

```python
# 파일명 > 클래스명 순서로 이름을 적습니다.
from WeekPay import WeekPay    # 외부 파일 (모듈을) 이 파일로 불러오기

class WeekPayManager:
  def __init__(self):
    self.worker_list = [
      WeekPay('홍길동', 20, 20000),
      WeekPay('고길동', 10, 50000),
      WeekPay('김길동', 30, 40000),
      WeekPay('이길동', 40, 20000),
      WeekPay('장길동', 20, 20000)
    ]

  def output(self):
    for w in self.worker_list:
      # 1) 여기에 WeekPay2('홍길동', 20, 20000) 클래스 자체가 들어와버립니다.
      # 2) 그러면서 w가 output
      w.output()


# c3 = WeekPayManager()
# c3.output()


# 🟡 다른 파일에서 import 해올 때는 실행되지 않게 막는 용도입니다.

# 파이썬의 모듈들은 내장변수가 있다. __name__ 을 누구나 가지고 있습니다.
  # 언더바 2개는 다 내장이다. (우리가 만든게 아닌 시스템 제공)
print(__name__)  # 이 모듈로 직접 실행하면 main이 들어온다. python Weekpay.py
# import 되서 싱행되면 파일명이 전달된다. python WeekPayManager.py

if __name__ == "__main__":
  mgr = WeekPayManager()
  mgr.output()
```

### 🟢 3. 별도로 \_\_init\_\_ 파일을 만든다.

이 것은 다른 파일들을 끌어다가 한번에 실행해주는 main이다.

```python
# python 프로젝트 시작 파일 입니다.
# 파일명이 __init__으로 정해져있습니다. main.py 같은 존재입니다.

from WeekPayManager import WeekPayManager

mgr = WeekPayManager()
# mgr.output()
mgr.start()
```

### 🟢 4. WeekPayManage.py 파일 코드에 기능 추가하기 (start 기능)

차차 추가할 것입니다.

```python
# 파일명 > 클래스명 순서로 이름을 적습니다.
from WeekPay import WeekPay    # 외부 파일 (모듈을) 이 파일로 불러오기

class WeekPayManager:
  def __init__(self):
    self.worker_list = [
      WeekPay('홍길동', 20, 20000),
      WeekPay('고길동', 10, 50000),
      WeekPay('김길동', 30, 40000),
      WeekPay('이길동', 40, 20000),
      WeekPay('장길동', 20, 20000)
    ]

  def output(self):
    for w in self.worker_list:
      # 1) 여기에 WeekPay2('홍길동', 20, 20000) 클래스 자체가 들어와버립니다.
      # 2) 그러면서 w가 output
      w.output()


  def start(self):
    print('start')


if __name__ == "__main__":
  mgr = WeekPayManager()
  mgr.output()
```

### 🟢 5. WeekPayManage.py 파일 코드에 기능 추가하기 (search 기능)

```python
# 파일명 > 클래스명 순서로 이름을 적습니다.
from WeekPay import WeekPay    # 외부 파일 (모듈을) 이 파일로 불러오기

class WeekPayManager:
  def __init__(self):
    self.worker_list = [
      WeekPay('홍길동', 20, 20000),
      WeekPay('고길동', 10, 50000),
      WeekPay('김길동', 30, 40000),
      WeekPay('이길동', 40, 20000),
      WeekPay('장길동', 20, 20000)
    ]

  def output(self):
    for w in self.worker_list:
      # 1) 여기에 WeekPay2('홍길동', 20, 20000) 클래스 자체가 들어와버립니다.
      # 2) 그러면서 w가 output
      w.output()

  def search(self):
    name = input('찾을 이름 :')
    result_list = list(filter(lambda w : w.name == name, self.worker_list))
    if len(result_list) == 0:
      print('찾으시는 데이터가 존재하지 않습니다.')
      return
    # return result_list[0].output()   # 여기서는 WeekPay의 output이 실행됨
                                      # 하지만 이건 1개의 데이터만 반환한다....

    for w in result_list:  # 찾는 데이터가 여러개인 경우 여러개를 출력해낼 수 있는 것
      w.output()

  def start(self):
    print('start')


if __name__ == "__main__":
  mgr = WeekPayManager()
  mgr.output()
```

### 🟢 6. WeekPayManage.py 파일 코드에 기능 추가하기 (수정 기능 추가)

```python
# 파일명 > 클래스명 순서로 이름을 적습니다.
from WeekPay import WeekPay    # 외부 파일 (모듈을) 이 파일로 불러오기

class WeekPayManager:
  def __init__(self):
    self.worker_list = [
      WeekPay('홍길동', 20, 20000),
      WeekPay('고길동', 10, 50000),
      WeekPay('김길동', 30, 40000),
      WeekPay('이길동', 40, 20000),
      WeekPay('장길동', 20, 20000)
    ]

  def output(self):
    for w in self.worker_list:
      # 1) 여기에 WeekPay2('홍길동', 20, 20000) 클래스 자체가 들어와버립니다.
      # 2) 그러면서 w가 output
      w.output()

  def search(self):
    name = input("찾을이름 : ")
    result_list = list(filter(lambda w : w.name == name, self.worker_list))
    if len(result_list) == 0:
        print("데이터가 없습니다")
        return

    #resultList[0].output() #Weekpay의 output
    for w in result_list:
        w.output()


  def modify(self):  # 수정하다, 수식하다, 한정하다
    name = input('찾을 이름 :')
    result_list = list(filter( lambda w : name in w.name, self.worker_list)) # 포함만 되어있어도 필터링 해버리기
    if len(result_list) == 0:
      print('찾으시는 데이터가 존재하지 않습니다.')
      return

    # enumerate 함수는 인덱스랑 데이터를 한꺼번에 반환한다.
    for i, w in enumerate(result_list):
        print(i, end ="\t")
        w.output()

    sel = int(input('수정할 대상을 선택하세요. :'))
    temp = result_list[sel]
    temp.name = input('이름 : ')
    temp.work_time = int(input('근무시간 :'))
    temp.per_pay = int(input('시간당급여액 :'))
    temp.process()

  def start(self):
    print('start')
```

<br><br>

# 🟩 5월 7일 과제

```python
import random

class InputValidator():
  def __init__(self, user_input):
      self.user_input = user_input

  def validate_number(self):
    if self.is_empty():
      raise ValueError('빈 값입니다. 다시 입력해주세요.')
    if self.is_number_type():
      raise ValueError('숫자만 입력할 수 있습니다. 다시 입력해주세요.')
    if self.is_negative():
      raise ValueError('음수는 허용되지 않습니다. 다시 입력해주세요.')
    if self.is_biger_number():
      raise ValueError('1, 2, 3 숫자 중 1개만 입력할 수 있습니다. 다시 입력해주세요.')

  def is_empty(self):
    return self.user_input == ''

  def is_number_type(value):
    return isinstance(value, (int))

  def is_negative(self):
    return int(self.user_input) < 0

  def is_biger_number(self):
    return int(self.user_input) > 3

class InputDataAndValidate():
  def __init__(self):
    self.INPUT_MESSAGES_NUMBER = {'user': '1 = 가위 , 2 = 바위 , 3 = 보 중 하나를 입력해주세요. :'}

  def input_computer_number(self):
    random_number = random.sample([1,2,3], 1)[0]
    return {'computer': random_number}

  def input_user_number(self, number_dict):
    score = {}
    for key, message in number_dict.items():
      for i in range(1,11):
        score[key] = int(input(message))
        try:
          validator = InputValidator(score[key])
          validator.validate_number()
        except ValueError as e:
          print('ERROR:', e)
          if i == 10: return print('종료되었습니다. 다시 시도하세요.')
        else:
          break
    return score

  def input_result(self):
    a = self.input_computer_number()
    b = self.input_user_number(self.INPUT_MESSAGES_NUMBER)
    computer_and_user_result = a | b
    print(computer_and_user_result)
    return computer_and_user_result

class CalculWinner():
  def cal_winner(self, input_dict_list):
    for i in input_dict_list:
      if i['computer'] == 3 and i['user'] == 1:
        i['winner'] = '사람'
      elif i['user'] == 3 and i['computer'] == 1:
        i['winner'] = '컴퓨터'
      elif i['computer'] < i['user']:
        i['winner'] = '사람'
      elif i['user'] < i['computer']:
        i['winner'] = '컴퓨터'
      elif i['user'] == i['computer']:
        i['winner'] = '무승부'
      else:
        print('ERROR: if문에 걸리지 못했습니다. 코드가 잘 못 되었습니다. 다시 확인해주세요.')
    print('\n🔥 승부 계산이 완료되었습니다.\n')

  def cal_winning_rate(self, winner_dict_list):
    played_game = len(winner_dict_list)
    computer_wins_number = 0
    user_wins_number = 0
    draw_game = 0
    for i in winner_dict_list:
      if i['winner'] == '컴퓨터':
        computer_wins_number += 1
      elif i['winner'] == '사람':
        user_wins_number += 1
      else:
        draw_game += 1

    computer_winning_rate = (computer_wins_number / played_game) * 100
    user_winning_rate = (user_wins_number / played_game) * 100
    return {'computer_wins_number' : computer_wins_number,
            'user_wins_number' : user_wins_number,
            'draw_game' : draw_game,
            'computer_winning_rate' : computer_winning_rate,
            'user_winning_rate' : user_winning_rate
    }


class OutputData():
  def output_menu(self):
    print("[1] 게임 시작")
    print("[2] 승부 계산")
    print("[3] 통계 출력")
    print("[0] 프로그램 종료")

  def output_winner(self, winner_dict_list):
    for i in winner_dict_list:
      print(f"컴퓨터 : {i['computer']}",end="\t")
      print(f"유저 : {i['user']}",end="\t")
      print(f"승자 : {i['winner']}")

  def output_winning_rate(self, winning_dict_list):
    print(f"\n<br><br><br><br>-- 통계 <br><br><br><br>--")
    print(f"컴퓨터 승리 수 : {winning_dict_list['computer_wins_number']}")
    print(f"사람 승리 수 : {winning_dict_list['user_wins_number']}")
    print(f"무승부 수 : {winning_dict_list['draw_game']}")
    print(f"컴퓨터의 승률 : {winning_dict_list['computer_winning_rate']}")
    print(f"사람의 승률 : {winning_dict_list['user_winning_rate']}")
    print(f"<br><br><br><br>-- 통계 <br><br><br><br>--\n")

class Controller():
  def __init__(self):
    self.input_user = InputDataAndValidate()
    self.calcul_winner = CalculWinner()
    self.output_game = OutputData()
    self.winner_result = []

  def start(self):
    while (True) :
      self.output_game.output_menu()
      sel = input("메뉴 선택 : ")
      if sel == "1" :
          for i in range(1, 11):
            self.winner_result.append(self.input_user.input_result())
      elif sel == "2" :
          self.calcul_winner.cal_winner(self.winner_result)
          cal_winning_rate = self.calcul_winner.cal_winning_rate(self.winner_result)
      elif sel == "3" :
          # self.output_game.output_winner(self.winner_result)
          self.output_game.output_winning_rate(cal_winning_rate)
      elif sel == "0" :
          print('정상적으로 종료되었습니다.')
          return
      else :
          print('잘못 입력하셨습니다.')


controller = Controller()
controller.start()
```
