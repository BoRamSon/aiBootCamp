# 2025년 5월 9일 금요일 (10일차)

- 날씨 : 비

<br><br>

# 📜 목차

- class 더 이해하기
- 파일 읽고 쓰기 (open())
  - txt 파일 읽기
  - txt 파일 쓰기
  - txt 파일 파일 데이터를 읽고, 평균 구하는 문제 풀어보기
  - 성적이 적힌 txt 파일을 가지고 성적처리하는 문제 풀어보기
  - iris.csv 파일을 가지고 데이터 가공하는 문제 풀어보기
  - mpg.csv 파일을 가지고 데이터 가공하는 문제 풀어보기
  - with 구문
  - pickle
    - 직렬화
    - 역직렬화

<br><br>

# 🟩 class 더 이해하기

- 5명이 소속된 스타트업 회사가 있다고 해보자! (class)
  - 그 회사 안에서 돈도 주고, 사람 일도 시키고, 계산도 하고, 영업도 하고, 하는 모든 것들을 묶어놓은 것이라고 보면 됩니다.
  - 사원이 1만명이 되었다... (회사가 커져서 class를 더 분리한다.)
    - 회사를 쪼개고, 각 회사에 사람과 돈과 일을 준다.

<br><br>

# 🟩 파일 읽고 쓰기

[https://wikidocs.net/26](https://wikidocs.net/26)

- 컴퓨터는 모든 것을 파일로 봅니다. 키보드나 마우스도 파일입니다.
- 회귀선을 그을 때, 계산을 통해 최적을 찾는데, 이 때 그래픽카드로 계산을 하게 되는데, 애초에 그래픽카드(hardware)부터 공부를 해야합니다.
- 파이썬의 입출력의 기본은 파일 입출력입니다.
- c언어가 처음응로 모든 장비의 입출력 기본을 파일입출력으로 한 이후 나온 언어들은 C규칙을 따른다.
- 파일은 여러개가 있어서 특정파일과 연결하는 작업이 필요하다.

```python
f = open("데이터파일.txt", 'w') # 반환대상은 파일 객체
f.write("Hello")  # 파일 쓰기 / 출력이 파일로 된다.
f .close()
```

- 첫번째 매개변수
  - 파라미터는 경로를 포함한 파일명이다.
- 두번째 매개변수
  - w는 write용으로 파일을 만들겠다는 의미이다.
  - 만일 파일이 없으면 새로 만든다. 기존에 파일이 존재하면 내용을 모두 지운다.
- 동일 프로세스에서 파일을 연달아서 못 열어요. 열고 닫고, 열고 닫고는 계속 할 수 있지만...
- 프로그램이 가동되면 프로세스

## 🟢 Practice 1 - 쓰기(w)

```python
# newfile.py
# project file / newfile.py 폴더와 파일을 하나 만들어주세요! (저는 안 만들게요!)


f = open("데이터파일.txt", 'w')   # 이 파일을 실행하면 해당 이름으로 파일을 생성합니다.
print(f.closed)  # False (아직 닫히지 않음)

f.write("Hello")  # 출력이 파일로 된다.

f.close()
print(f.closed)  # True (닫힘)
```

### 🟡 터미널 명령어

- 🔥 dir을 통해서 파일을 찾을 수 있다.
- dir \*.txt - 확장자가 txt란 파일 목록만 확인
- type 파일명 파일 내용 확인하기

### 🟡 text파일과 binary파일 2종류가 있습니다.

#### 🔵 text 파일 -> 저장 시 가공

- ..

#### 🔵 binary 파일 -> 주기억장치 내용을 가공하지 않고 그대로 저장한다.

- ex) 이미지, 동영상, 엑셀 프로그램, pdf 등등
- 내부 구조가 일정하지 않고 다 다르기 때문에 별도의 특정 프로그램이 있어야 문서를 열 수 있습니다.

### 🟡 파일 경로에 대해서

- 파일의 경로에 Linux는 OS /(슬래시)를 사용한다.
- 파일의 경로에 Windows는 OS (역슬래시, 한글폰트의 경우 원화표시)를 사용한다.
  - c:\\temp\\test c:탭emp탭est 특수문자로 인식하기 때문에
  - c:\\temp\\test r"c:탭temp탭test" 이렇게 역슬래시를 2개 붙여줘야합니다.
  - rstring은 문자열 앞에 r을 붙이면 excape키()를 무력화 시킨다.

### 🟡 '절대적 경로' / '상대적 경로' 개념

절대적 경로와 상대적 경로가 있는데요~

#### 절대적 경로

- 루트부터 시작한다.
- c:\\test\\test
- 이건 사용하는게 위험하다. 파일이 바뀌면 위험해진다.
- 특별한 경우를 제외하고 잘 안쓰는 것이 좋습니다. 그래서 가급적 쓰지 말자.

#### 상대적 경로

- 현재 프로그램이 가동중인 폴더 기준으로
- . : 내 폴더
- .. : 부모 폴더
- "./test.txt" 와 "test.txt" 는 동일한 의미
- "../test.txt" 현재 이 폴더보다 하나 위로 올라가서 파일을 만들어라

#### 리눅스와 윈도우의 파일명 차이

- 리눅스는 폴더나 파일에 공백 안되고, 대소문자를 구분한다.
- 파일 확장자가 의미 없음.
- 윈도우는 폴더나 파일에 공백가능, 대소문자 구분 안함
- 윈도우 OS에서 TEST -> test 로 바꿔도 보이기는 하지만 인식을 못한다.
  - 대소문자 바꾼 것을 인식을 시키려면 TEST -> 1 -> test 이런 식으로 바꿔야 인식이 됩니다.
- C: D: 같은 드라이브명은 windows만 있는 것이며, 리눅스에는 없습니다.

## 🟢 Practice 2 - 쓰기(w)

```python
f = open("데이터파일2.txt", "w")    # 이 파일을 쓰기 모드(w)로 엽니다. 파일이 없으면 새로 생성되고, 있으면 기존 내용을 모두 지웁니다.
                                 # 이때, open 함수는 파일 객체(file object)를 반환하며, 그걸 변수 f에 저장합니다.

for i in range(1, 11):           # 1부터 10까지 숫자 i를 하나씩 반복합니다.
  print(f"i={i}", file=f)        # print 함수는 기본적으로 화면(모니터)에 출력하지만,
                                 # file이라는 키워드 파라미터에 파일 객체 f를 주면,
                                 # 화면이 아니라 해당 파일(f)에 내용을 출력하게 됩니다.
                                 # 즉, 파일에 "i=1", "i=2", ..., "i=10" 이 한 줄씩 저장됩니다.

f.close()                        # 파일을 닫습니다. 파일을 닫지 않으면, 데이터가 완전히 저장되지 않거나 파일이 손상될 수 있습니다.
                                 # 괄호()를 꼭 붙여서 함수를 호출해야 실제로 닫힙니다.
                                 # print 함수의 기본 출력장치가 모니터인데 file이라는 파라미터에
                                 # file 객체를 주면 화면에 출력이 안되고 파일로 출력한다.

print('작업완료')                  # 이 줄은 화면에 출력됩니다. 파일과는 관계없으며, 작업이 끝났다는 표시입니다.
```

## 🟢 Practice 3 - 쓰기(w)

```python
f = open("데이터파일3.txt",'w')
for i in range(1, 11):
    s = "i = %d" % (i)  # 파이썬 2부터 있던 코드
    f.write(s)

f.close()

print('작업완료')
```

## 🟢 Practice 4 - 쓰기(w)

```python
f = open("데이터파일4.txt",'w')
for i in range(1, 11):
    s = "i = %d" % (i)  # 파이썬 2부터 있던 코드
    f.writelines(s)

f.close()

print('작업완료')
```

## 🟢 Practice 5 - 이번에는 읽기(r)

- 파일을 열때는 파일이 반드시 존재해야합니다.

```python
f = open("데이터파일.txt", 'r')
data = f.read()   #파일을 통으로 읽는다.
print(data)
f.close()
```

```python
f = open("데이터파일.txt", 'r')

# data = f.read()   #파일을 통으로 읽는다.
data = f.readlines()    # 🔥 모든 라인들을 읽습니다. / 얘는 반환값이 list타입이다.
print(type(data))       # 타입 확인해보기!!!

print(data)

f.close()
```

```python
f = open("데이터파일2.txt", 'r')

line = f.readline()    # 🔥 readline = 줄 하나만 읽습니다.
print(type(line))       # 타입 확인해보기!!!

print(line)

f.close()
```

```python
f = open("데이터파일2.txt", 'r')

line = f.readline()

while line !="":      # readline만 사용할 때에는 이렇게 반복문으로 출력한다.
  print(type(line))
  print(line)
  line = f.readline()

f.close()
```

<br><br>

# 🟩 문제 - 특정 파일을 읽어서 평균값 출력하기

- 읽어야할 데이터 파일 내부에는
  - 이렇게 값이 들어있습니다.

(txt 파일 내용)  
10  
20  
30  
40  
50  
4  
5  
11  
12  
14  
27

- 이걸 읽어서 평균을 구하시오!

```python
average_target =  []   # list 변수


f = open("데이터파일5(문제).txt", 'r')
line = f.readline()
while line !="":      # readline만 사용할 때에는 이렇게 반복문으로 출력한다.
  # print(type(line))
  average_target.append(int(line))
  print(f"{line}을 리스트에 넣었습니다.")
  line = f.readline()
f.close()


average_result = sum(average_target) / len(average_target)

print(f"평균 결과 : {average_result}")
```

### 🟡 위 문제를 클래스로 만들어 보기

```python
class ReadFileAndPrint:
  def __init__(self):
    self.average_target =  []  # list 변수
    # self.read_file()
    # self.calcul_average()
    # self.output()

  def read_file(self):
    f = open("데이터파일5(문제).txt", 'r')
    line = f.readline()
    while line !="":
      self.average_target.append(int(line))
      print(f"{line}을 리스트에 넣었습니다.")
      line = f.readline()
    f.close()

  def calcul_average(self):
    average_result = sum(self.average_target) / len(self.average_target)
    return average_result

  def output(self):
    print(f"평균 결과 : {self.calcul_average()}")


r = ReadFileAndPrint()
r.read_file()
r.calcul_average()
r.output()
```

<br><br>

# 🟩 문제 - iris.csv 파일을 통해 읽고 쓰기 등등

- ChatGPT를 통해서 "iris.csv 파일 주세요."라고 합니다.
- 해당 iris.csv 파일을 다운로드 받아서 나의 datas폴더에 넣어 VSCode로 열어줍니다.
  - 추천 vscode extensions : Rainbow CSV (만든이: mechatroner)

### 🟡 직접 쉬운 방식으로 풀어보았습니다.

```python
# 어떤 데이터를 가지고 나오는지 확인한다.
# f = open("datas/iris.csv", 'r')
# lines = f.readlines()
# print(lines)
# f.close()


class ReadFileAndPrint:
  def __init__(self):
    self.sepal_length = []
    self.sepal_width = []
    self.petal_length = []
    self.petal_width = []

  def read_file(self):
    f = open("datas/iris.csv", 'r')
    lines = f.readlines()
    for i in lines:
      seperator = i.split(',')
      self.sepal_length.append(seperator[0])
      self.sepal_width.append(seperator[1])
      self.petal_length.append(seperator[2])
      self.petal_width.append(seperator[3])
    f.close()

    # print(f"추출 완료 sepal_length: {self.sepal_length.pop(0)}")
    # print(f"추출 완료 sepal_length: {self.sepal_length}")
    # print(f"추출 완료 sepal_width: {self.sepal_width}")
    # print(f"추출 완료 petal_length: {self.petal_length}")
    # print(f"추출 완료 petal_width: {self.petal_width}")

  def calcul_average(self, list):
    name = list[0]
    list.pop(0)  # list에 영향을 미칩니다. 실제 list에 영향을 미치고 가져와서 반환합니다.
    new_list = []
    for i in list:
      new_list.append(float(i))
    average = sum(new_list) / len(list)
    print(f"\"{name}\"의 평균은 {average:.2f}")
    return average

  def calcul_average_result(self):
    self.calcul_average(self.sepal_length)
    self.calcul_average(self.sepal_width)
    self.calcul_average(self.petal_length)
    self.calcul_average(self.petal_width)

    # print(f"추출 완료 sepal_length: {self.sepal_length}")
    # print(f"추출 완료 sepal_width: {self.sepal_width}")
    # print(f"추출 완료 petal_length: {self.petal_length}")
    # print(f"추출 완료 petal_width: {self.petal_width}")

  def menu(self):
    print(f"1. 파일 데이터 추출")
    print(f"2. 출력")
    print(f"0. 종료")

  def start(self):
    print(self.menu())
    while True:
      sel = input('메뉴 번호를 입력하세요. : ')
      if sel == '1':
        self.read_file()
      if sel == '2':
        self.calcul_average_result()
      if sel == '0':
        return print(' 👋 정상적으로 종료되었습니다.')

r = ReadFileAndPrint()
r.start()
```

### 🟡 강사님 코드 - 강사님 코드가 너무 어렵습니다... 😭

```python
#한글처리 cp949-윈도우방식, 표준-utf-8,vscode가 utf-8
irisList = [] #1차원데이타가 들어갈 list
f = open("datas/iris.csv", "r", encoding="utf-8")
lines = f.readlines()

for i in range(1, len(lines)):
    line = lines[i]
    line = line[:len(line)-1]
    print(i, line)
    values = line.split(",")
    data =[float(values[0]), float(values[1]), float(values[2]),
           float(values[3])]
    irisList.append(data)
f.close()

for iris in irisList:
    print(iris)
#print(irisList)

result = [0,0,0,0]
for j in range(0, 4):
    for i in range(0, len(irisList)):
        result[j] = result[j] + irisList[i][j]

print(result[0]/150, result[1]/150, result[2]/150, result[3]/150)

count = len(irisList)
for i in range(0,4):
    print(f"{result[i]/count:.2f}", end="\t"),
print()
```

<br><br>

# 🟩 문제 - mpg.csv 파일로 문제 풀기

- seaborn 사이트에서 dataset을 다운로드 받겠습니다.
- seaborn 사이트에서 search "load_dataset"
- 위 쪽에 있는 것 클릭
- 깃허브로 접속

  - https://github.com/mwaskom/seaborn-data
  - mpg.csv 파일을 다운로드

- 문제
  - 실린더개수 8, 6, 4, 5 종류별로 카운트 하기

```python
# 어떤 데이터를 가지고 나오는지 확인한다.
# f = open("datas/mpg.csv", 'r')
# for i in range(0, 10):
#   line = f.readline()
#   print(line)
# f.close()


class ReadFileAndPrint:
  def __init__(self):
    self.cylinders = []
    self.count_eight = 0
    self.count_six = 0
    self.count_five = 0
    self.count_four = 0
    self.count_three = 0

  def read_file(self):
    f = open("datas/mpg.csv", 'r')
    lines = f.readlines()
    for i in lines:
      seperator = i.split(',')
      self.cylinders.append(seperator[1])
    f.close()

  def calcul_count_number(self):
    for i in self.cylinders:
      if i == '8':
        self.count_eight += 1
      elif i == '6':
        self.count_six += 1
      elif i == '5':
        self.count_five += 1
      elif i == '4':
        self.count_four += 1
      else:
        self.count_three += 1

  def output(self):
    print(f"실린더 배열의 길이 : {len(self.cylinders)}")
    print(f"결과 : 8은 {self.count_eight}개 | 6은 {self.count_six}개 | 5는 {self.count_five}개 | 4는 {self.count_four}개 | 3은 {self.count_three}개가 있습니다.")
    print(f"실제 출력된 것들으리 합 : {self.count_eight + self.count_six + self.count_five + self.count_four + self.count_three}")

  def menu(self):
    print(f"1. 파일 데이터 추출")
    print(f"2. 계산")
    print(f"3. 출력")
    print(f"0. 종료")

  def start(self):
    print(self.menu())
    while True:
      sel = input('메뉴 번호를 입력하세요. : ')
      if sel == '1':
        self.read_file()
      if sel == '2':
        self.calcul_count_number()
      if sel == '3':
        self.output()
      if sel == '0':
        return print(' 👋 정상적으로 종료되었습니다.')

r = ReadFileAndPrint()
r.start()
```

### 🟡 같이 풀어보기

```python
f = open('datas/mpg.csv', 'r')
lines = f.readlines()
f.close()

lines = lines[1:]  # 🔥 1번 리스트부터 끝까지 복사해서 다시 덮어쓴다.
print(lines[:4]) # 0번째 이름들 잘 날라간 것을 확인함.

cylinder_count = {}

for line in lines:
  line = line[:len(line)-1]   # 마지막에 있는 \n 지우기
  values = line.split(',')
  if values[1] in cylinder_count.keys():
    cylinder_count[values[1]] += 1
  else:
    cylinder_count[values[1]] = 1

print(cylinder_count)
```

<br><br>

# 🟩 with 구문

- 그저 close를 안하는 것 때문에 생겼다고 생각하자.
- with 구문 안에 넣으면, 일이 끝나면 자동으로 닫아준다.
- 파이썬 버전이 낮을 경우에 거듭해서 파일을 여는 것은 안된다.

```python
# 원래 안 닫고 열면 에러가 나야하는데.... 나지 않습니다.

f = open('datas/mpg.csv', 'r')
lines = f.readlines()
print(lines[:3])

f = open('datas/mpg.csv', 'r')
lines = f.readlines()
print(lines[:3])
```

```python
# 🟡 이렇게 사용한다는 것을 알 수 있습니다.
with open('datas/mpg.csv', 'r') as f:
  lines = f.readlines()
  print(lines[:3])
```

<br><br>

# 🟩 직렬화 및 역직렬화

### 🟡 pickle이 무엇인가?

- Python 표준 라이브러리입니다. (설치 필요 없음)
- 직렬화(serialize), **역직렬화(deserialize)**를 위한 모듈입니다.
- 거의 모든 파이썬 객체를 저장하고 복원할 수 있습니다.

## 🟢 직렬화

- 상자를 포장하는 것
  객체 자체를 파일이나 네트워크로 메모리 그대로 저장한다.

```python
import pickle

data = {
  'name' : '홍길동',
  'age' : 23,
  'phone' : ["010-0000-0001", "010-0000-0002"]
  }   # 🔥 딕셔너리 person을 파일로 저장

# 직렬화
with open('datas/datas.bin', 'wb') as f:    # 🔥 wb: write binary (바이너리 파일로 저장)
  pickle.dump(data, f)
```

## 🟢 역직렬화

- 상자를 열고 다시 꺼내는 것

```python
import pickle

data = {
  'name' : '홍길동',
  'age' : 23,
  'phone' : ["010-0000-0001", "010-0000-0002"]
  }

# 역직렬화
with open('datas/datas.bin', 'rb') as f:   # 🔥 rb: read binary
  data2 = pickle.load(f)

print(data2)
```

<br><br>

# 🟩 직렬화, 역직렬화 문제

- 어제 했던 성적처리 class module이 있습니다.

- 이 파일에 직렬화, 역질렬화를 이용하여 성적처리 결과에 대해서 binary 파일을 만들어 저장하고, 불어와서 내용을 볼 수 있도록 만들어 보세요!!!

```python

class ScoreManager:  # 이 클래스 내부에

  # ==================================================
  # binary 파일 저장 코드 추가
  def save(self):
    with open('datas/score.bin', 'wb') as f:
      pickle.dump(self.scoreList, f)

  # binary 파일 불러오기 코드 추가
  def load(self):
    with open('datas/score.bin', 'rb') as f:
      self.scoreList = pickle.load(f)
    self.printAll()
# ==================================================
```

```python
import pickle

class ScoreData:
  def __init__(self, name = '홍길동', kor = 0, eng = 0, mth = 0):  # 일반 인자는 항상 defaut 값보다 앞에 온다.
    self.name = name
    self.kor = kor
    self.eng = eng
    self.mth = mth
    self.process()

  def process(self):   # 계산하는 친구
    self.total = self.kor + self.eng + self.mth
    self.avg = self.total/3
    if self.avg >= 90:
      self.grade = '수'
    elif self.avg >= 80:
      self.grade = '우'
    elif self.avg >= 70:
      self.grade = '미'
    elif self.avg >= 60:
      self.grade = '양'
    else:
      self.grade = '가'

  def print(self):
    print(f"이름: {self.name}", end='\t')
    print(f"국어: {self.kor}", end='\t')
    print(f"영어: {self.eng}", end='\t')
    print(f"수학: {self.mth}", end='\t')
    print(f"합계: {self.total}", end='\t')
    print(f"평균: {self.avg: .2f}%", end='\t') # 여기 ': .2f' 에 대해서 공부해야합니다.
    print(f"등급: {self.grade}")


# ==================================================

# from ScoreData import ScoreData
# ScoreData.py 파일에서부터 ScroeData클래스를 가져와라.
# import pickle

class ScoreManager:
  def __init__(self):
    self.ScoreData = ScoreData()
    self.scoreList = [
      ScoreData('조승연', 90, 80, 90),
      ScoreData('안세영', 80, 80, 90),
      ScoreData('김연아', 90, 90, 90),
      ScoreData('김연경', 100, 80, 100)
    ]

  def append(self):
    # input_name = input('이름을 입력하세요 : ')
    # input_kor = int(input('국어 점수를 입력하세요 : '))
    # input_eng = int(input('영어 점수를 입력하세요 : '))
    # input_mth = int(input('수학 점수를 입력하세요 : '))
    # sc = ScoreData() # 객체 생성
    # sc.process()
    # self.scoreList.append(ScoreData(input_name, input_kor, input_eng, input_mth))

    sc = ScoreData() # 객체 생성
    sc.name = input('이름을 입력하세요 : ')
    sc.kor = int(input('국어 점수를 입력하세요 : '))
    sc.eng = int(input('영어 점수를 입력하세요 : '))
    sc.mth = int(input('수학 점수를 입력하세요 : '))
    sc.process()
    self.scoreList.append(sc)



  def search_student(self):
    # find_name = input('찾을 이름을 입력해주세요 : ')
    # for s in self.scoreList:       # 🔥 for문과 if문으로 충분히 할 수 있을 것 같은데에....
    #   if s['name'] == find_name:
    #     find_student.append(s)
    #     print(f'찾았습니다! >>>> {s}')

    find_name = input('찾을 이름을 입력해주세요 : ')
    # filter는 두번쨰 매개변수로 전달된 list를 받아서
    # for문 돌려서 첫번째 매개변수로 전달된 함수를 호출
    # 람다 : 매개변수하나(scoreList에 저장된 객체 하나)
    #       반환은 True or False

    # 매개변수 ScoreData 객체
    # list로 둘러 쌓으면 list생성자가 호출되면서 filter가 모든 작업을 완료한다.ㅁ
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))

    # 데이터가 없을 수 있잖아~
    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.

    # 🔥🔥🔥 enumerate가 list를 전달하면 해당 리스트 내의 위치 index와 함께 결과물을 출력해줍니다.
    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()

    # print(find_student)
    # return find_student   # 🔥🔥🔥 이거를 이렇게 계속 수정 > 삭제 > 정렬 순으로 가져가면서 사용하려고 생각했었습니다.



  def edit_student(self):
    # self.search_student()

    find_name = input('수정할 이름을 입력해주세요 : ')
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))

    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.

    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()

    sel = int(input('수정할 대상의 번호를 입력해주세요 : '))
    # 수정할 대상의 참조를 가져온다.
    item = find_student[sel]   # 🔥🔥🔥 self.scoreList 원본을 바꿔줘야 할 것 같은데요
    item.name = input('이름을 입력하세요 : ')
    item.kor = int(input('국어 점수를 입력하세요 : '))
    item.eng = int(input('영어 점수를 입력하세요 : '))
    item.mth = int(input('수학 점수를 입력하세요 : '))
    item.process() # 다시 계산하기


    # print(find_student)
    # return find_student



  def delete_student(self):
    find_name = input('삭제할 이름을 입력해주세요 : ')
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))

    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.

    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()

    sel = int(input('삭제할 대상의 번호를 입력해주세요 : '))
    # 수정할 대상의 참조를 가져온다.
    item = find_student[sel]
    # ------------------------
    # 🟡 edit_student 코드에서 이 부분만 추가하였습니다.
    # del find_student[sel]  # 🔥🔥🔥 del은 삭제가 되지 않습니다.
    self.scoreList.remove(find_student[sel]) # 🔥🔥🔥 직접적으로 list.remove를 통해 삭제를 했습니다.
                                      # 🔥🔥🔥 보통 삭제에서는 remove를 사용한다고 알아두세요!!!
    # ------------------------
    item.process() # 다시 계산하기

  def sorted(self):
    # 원본을 냅두고, 정렬하여 출력하기
      # sort는 원본을 직접 정렬
      # sorted는 새로운 정령된 리스트를 반환

    # key에 전달해야할 람다는
    # 매개변수 하나 반환값 정렬을 할 수 있는 데이터 타입
    # > < 연산자 수행이 가능하다

    # s1 = ScoreData()
    # s2 = ScoreData()
    # s1 > s2
    # 파이썬이 제공하는 기본 파이썬이 제공하는 기본 타입들 int, float, str

    result_list = sorted(
        self.scoreList,
        key=lambda item : item.total,  # 🔥🔥🔥 이렇게까지는 생각을 못했다.
        reverse=True
      )

    for i in result_list:
      i.print()


  def printAll(self):
    for s in self.scoreList:
      s.print()

# ==================================================
# binary 파일 저장 코드 추가
  def save(self):
    with open('datas/score.bin', 'wb') as f:
      pickle.dump(self.scoreList, f)

# binary 파일 불러오기 코드 추가
  def load(self):
    with open('datas/score.bin', 'rb') as f:
      self.scoreList = pickle.load(f)
    self.printAll()
# ==================================================

  def menuDisplay(self):
    print("----------------")
    print("----- 메뉴 -----")
    print("[1] 학생 추가")
    print("[2] 기록 출력")
    print("[3] 검색  ") #이름
    print("[4] 수정  ") #이름
    print("[5] 삭제  ") #이름
    print("[6] 정렬  ") #총점 내림차순으로
    print("[7] 파일 저장  ")
    print("[8] 파일 오픈  ")
    print("[0] 프로그램 종료")
    print("----------------")

  def start(self):
    funcList = [
      None,
      self.append,
      self.printAll,
      self.search_student,
      self.edit_student,
      self.delete_student,
      self.sorted,
      self.save,
      self.load
    ]
    while True:
      self.menuDisplay()
      choise = int(input('선택 : '))
      if choise > 0 and choise < len(funcList):
        funcList[choise]()
      else:
        return


if __name__ == '__main__':
  sm = ScoreManager()
  sm.start()
  # sm.printAll()
```

## 🔵 출력 결과

```markdown
----- 메뉴 -----
[1] 학생 추가
[2] 기록 출력
[3] 검색
[4] 수정
[5] 삭제
[6] 정렬
[7] 파일 저장
[8] 파일 오픈
[0] 프로그램 종료


선택 : 7

----- 메뉴 -----
[1] 학생 추가
[2] 기록 출력
[3] 검색  
[4] 수정  
[5] 삭제  
[6] 정렬  
[7] 파일 저장  
[8] 파일 오픈  
[0] 프로그램 종료

---

선택 : 8
이름: 조승연 국어: 90 영어: 80 수학: 90 합계: 260 평균: 86.67% 등급: 우
이름: 안세영 국어: 80 영어: 80 수학: 90 합계: 250 평균: 83.33% 등급: 우
이름: 김연아 국어: 90 영어: 90 수학: 90 합계: 270 평균: 90.00% 등급: 수
이름: 김연경 국어: 100 영어: 80 수학: 100 합계: 280 평균: 93.33% 등급: 수

---

----- 메뉴 -----
[1] 학생 추가
[2] 기록 출력
[3] 검색  
[4] 수정  
[5] 삭제  
[6] 정렬  
[7] 파일 저장  
[8] 파일 오픈  
[0] 프로그램 종료

선택 : 0 (종료)
```

<br><br>

# 🟩 5월 9일 과제

- weekpay(주급계산)
  - class 적용
  - 연장수당 적용 : 20시간 넘어가면 수당 (얼마?)
  - pickle
    - 직렬
    - 역직렬

```python

```

<br><br>

# 🤔 회고 정리

이번주는 연휴로 인해 3일간 나왔다.  
함수를 복습하고, class를 본격적으로 들어가면서 초보자의 머릿속으로는 도저히 이해하기 힘든 많은 것을 이해하지 못했고 그냥 이렇게 쓴다라는 것만 외운다음에 쓰면서 익숙해졌다.  
그저 단순한 문제를 풀 때는 완만히 풀었으나, 조금 복잡해지거나 데이터를 특별하게 가공하는 부분에서 많이 막히면서 시간을 잡아먹고 생각을 많이하게 되었다.  
자주 활용하지 않는 문법과 난이도가 좀 있는 문제를 풀어보면서 익숙해지고 실력을 향상시켜야겠다.
이번주도 유익한 시간이였다.
