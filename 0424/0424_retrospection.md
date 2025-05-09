# 2025년 4월 24일 (2일차)

9시부터 python 기초 강의가 시작되었다.

<br><br>

# 📜 목차

- print
- variable
- breakpoint
- 문자열 연습
- 진법 변환
- 복합연산자
- 리스트
- 과제

<br><br>

# 🟩 print

```python
print("출력을 하고자 할 때 사용한다. 출력이 잘 되는 것을 볼 수 있습니다.")

# seperator를 사용해봅시다!!!!
print("red", "green", "blue", sep="*")
print("yellow", "cyan", "magent", sep=",")

# 이렇게도 사용할 수 있습니다.
print("red", "green", "blue", sep="\t", end="")
print("yellow", "cyan", "magent", sep=",")
```

<br><br>

# 🟩 변수 (variable) 01

## 🟢 변수에 대한 설명

1. 컴퓨터의 기억장소에 이름을 부여한 것을 말한다.
1. 컴퓨터의 기억공간에 이름을 부여하고 그 공간에 값을 저항하거나 읽어올 수 있다.
1. 0과 1로 구성되어 있다.
1. 사람은 숫자보다 단어를 기억하기 쉽다
1. 우리가 직접 컴퓨터 공간을 지적하면, 그 메모리가 비어있는지 용가능한지 중요한 내용일 수도 있어서 직접적으로 기억공간에 접근할 수 없다.

#### 🟡 이름을 어떻게 정하면 좋을까???

1번지에 값 3을 넣고, 2번지에 값 4를 넣고
그런데 IP로만 되어있으면, 숫자를 외우기가 너무 어렵다. 그래서 도메인을 사용하는 것과 같이
기억 공간에 이름을 붙인다.

JAVA 라면 변수를 미이 선언해야한다. >>> int a;
int 형의 데이터가 저장될 공간을 확보하고 이름을 a라고 해라
보통의 인터프리터 언어는 변수를 미리 선언하지 않는다.
필요할 떄 만들어서 쓰면 된다.

1. 규칙 :

- 영어 대소문자
- \_(언더바)
- 숫자가능(시작은 반드시 영어나 \_로만 가능하다)

##### - 예약어 사용 불가

1. int = 4 #(X)
1. ints = 4 #(O)

1. 대문자까지 구분을 해야합니다.

```python
ex.
  >>> friend = 10
  >>> Friend = 1
  >>> friend
  10
  >>> Friend
  1
```

#### 🟡 암묵적인 룰

- 변수를 만들 때
- 가급적 긴단어로 어떤 값을 저장하는 건지 용도를 알려주는 것이 좋다
- 표기법
  - 1. 스네이크 표기법 : student_name
  - 2. 카멜표기법 : studentName
  - 3. 헝가리안 표기법 : szStudentName (sz는 type으로 string이라는 의미) (현재 안씀)
-

#### 🟡 타입에 대해서~~

###### int

int - 정수, 소수점 이하가 없는 수를 정수

###### float

우리나라 국가예산 600조를 정수를 정수로 4byte

컴퓨터에 실제 음수는 없다!!!

#### 🟡 리터럴 (literal) 이 무었인가???

<갑 그 자체>
5, 4.5 , "Hello"
print(4\*5)
a = 4
b = 5

<br>

## 🟢 문제 풀기

### 🟡 문제 1

m를 km와 m로 전환하기  
2300미터는 2km와 300m 입니다.
미터를 입력받아서 각각 km와 m로 전환해서 출력하세요.  
(힌트 - 몫 구하는 연산자 // , 나머지를 구하는 연산자 % )

```python
input_meter = int(input('m 값을 입력하시오 : '))

kilo_meter_value = input_meter // 1000
print(kilo_meter_value)

again_convert_to_meter = input_meter - (kilo_meter_value * 1000)
print(again_convert_to_meter)

print(f"{kilo_meter_value}km와 {again_convert_to_meter}m 입니다.")

# ------------------------

meter = int(input("미터는? "))

km = meter // 1000
m = meter % 1000

print(f"{meter}는 {km}km와 {m}m 입니다.")

```

<br><br>

# 🟩 index

```python
s = 'Python String'
s2 = 'hello'
s3 = '''
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
'''

print(s)
print(s2)
print(s3)
```

<br><br>

# 🟩 slicing

```python
print(s[0:3]) #0,1,2개만 출력
print(s[0:6]) #0,1,2,3,4,5, Python, 증감치를 생략하면 +1 생각한다.
print(s[0:6:2]) #0,1,2개만 출력

print(s[7:0]) # 7번방부터 마지막까지

print(s[len(s) -1:0:-1])
print(s[len(s) -1:-1:-1]) # 파이썬 버전에 따라서 에러메세지가 뜨기도 하고, 지금처럼 아무것도 출력이
print(s[len(s) -1::-1]) # 정답이다.
print(s[::-1]) # 생략하면 알아서 처리한다.  - 역순으로 출력한다
```

<br><br>

# 🟩 진법

```python
"""
컴퓨터는 이진수 체계

1100001100101100011111111111100000

8진수 -> 2진수를 3개씩 묶는다. 01,2,3,4,5,6,7 10

000 0
001 1
010 2
011 3
100 4
101 5
110 6
111 7

0000 0
0001 1
0010 2
0011 3
0100 4
0101
0110
0111
1000
1001 9
1010 A
1011 B
1100 C
1101 D
1110 E
1111 F
"""
```

```python
a = 0o45 #8진수라서 0 1 2 3 4 5 6 7 10 11 12 13 .. 17 20
print(a) #10진수로 출력한다 4\*8 + 5
a = 0xFF
print(a)

#복합연산자
a = 5
a = a + 1
print(a)
a += 1
print(a)

a -= 1
print(a)

a \*= 3
print(a)

진짜 사칙연산만 조금 복잡하게 해도 나에게는 살짝 시간이 걸리는 느낌이 들었다...
```

<br><br>

# 🟩 오후 6시 수업이 끝나기 전 과제를 주셨다.

<문제는 다음과 같다.>

5-1. 변수에 값 "홍길동, 임꺽정, 장길산, 최영, 윤관, 강감찬, 서희, 이순신, 남이"  
5-2. => list 타입으로 전환  
5-3. => '서희' 가 몇번쨰에 있는지  
5-4. '이순신', '장영실' 존재여부 확인  
5-5. 추가할 사람 : '정도전', '정약용', '최지원' ....  
5-6. '서희' => '김종서'로 바꾸기  
5-7. 장길산 => 김길산 첫글자만 바꾸기

모두 푸는데 20분정도 걸렸던 것 같다.

### 🟡 같이 풀어보기

```python
# 🟩 5-1. 변수에 값 "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
names = "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
print(names,type(names))


# 🟩 5-2. => list 타입으로 전환
nameList = names.split(',')
print(nameList, len(nameList))


# 🟩 5-3. => '서희' 가 몇번쨰에 있는지
# indexing practice
# print(f"\n{nameList[0]}")

seohee_location = nameList.index('서희')
print(f'5-3. 리스트 내에 {seohee_location + 1}번째에 존재합니다.')

# slicing
print(nameList[3:]) # 3번째 이후로 출력
print(nameList[:3]) # 처음부터 3번째 전까지 출력
print(nameList[::-1]) # 역순


# 🟩 5-4. '이순신', '장영실' 존재여부 확인
print('5-4.')
# def is_in_the_list() :  # 내가 했던 방식

# 🟡 if문과 count를 사용한 방식
if nameList.count('이순신') > 0 :  # nameList안에 '이순신'이 있으면
  print('이순신이 존재한다.')
else :
  print('이순신이 존재하지 않습니다.')

# 🟡 if문과 in을 사용한 방식
if "장영실" in nameList :  #nameList안에 '장영실'이 있으면
  print('장영실이 존재한다.')
else :
  print('장영실이 존재하지 않습니다.')




# 5-5. 추가할 사람 : '정도전', '정약용', '최지원' ....
print('5-5.')

# 🟡 append


# 🟡 extend (요소를 합치는 형식으로 )
# 예제로 보겠습니다.
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6, 7, 8]
# c = a.extend(b)  # 이건 안됩니다.

a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8]

# 🔥 +와 extend의 차이점 : +는 원본이 바뀌지 않고, extend는 원본이 바뀌어버립니다.


# 🟡 insert (특정 위치에 추가하는 형식으로 )



# 5-6. '서희' => '김종서'로 바꾸기
pos = nameList.index('서희')
nameList[pos] = '김종서'
print(f'5-6. {nameList}')



# 5-7. 장길산 => 김길산 첫글자만 바꾸기

# 🟡 replace
pos2 = nameList.index('장길산')

# 🔥 반드시 여기서 해당 변수 (nameList[pos2] 변수)를 대체해줘야지 값이 바뀌는 것입니다.
nameList[pos2] = nameList[pos2].replace(nameList[pos2][0], '김')

print(f'5-7. {nameList}')
```
