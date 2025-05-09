# 2025년 5월 8일 목요일 (9일차)

### 🔵 수업 내용

객체지향에 대해서 배우고, class에 대해서 반복적으로 학습하며 적응해 나아간다.

<br><br>

# 📜 목차

- class에 대한 이론 설명
- 5월 7일 과제 - 가위바위보(class) 과제 같이 풀어보기
- 성적처리 문제 class module로 바꿔보기 / 같이 풀어보기
- 5월 2일 과제 - 야구 게임(class module) 같이 풀어보기

<br><br>

# 🟩 class에 대한 이론 설명

## 🟡 객체지향 - 클래스 (사용자가 만드는 데이터 타입)

- int, str, float : 파이썬의 기본 타입들하고 마찬가지
- 기본 타입과 다른 것은
  - 변수 = 클래스명()
    - 클래스를 가지고 객체를 만든다. 객체는 heap 공간에 저장되고, 객체의 주소(참조)를 변수에 전달한다.
    - 메모리가 부족하면 none을 전달.
  - 객체 내부의 변수나 함수에 접근하려면 .(도트 연산자)를 이용해 접근한다.
  - 생성자 **init**라는 이름을 갖고 기본적으로 파이썬에는 개체의 자신의 주소를 전달하기 위해서 self라는 매개변수를 첫번째 매개변수로 가지고 다녀야 한다.
  - 변수명이 self일 필요는 없다. 그런데 남들도 self를 사용하니깐 self를 사용하자

## 🟡 추상화 - 클래스 : 내부 구조를 몰라도 쓰는데 지장 상황이 없다.

- 추상화와 <-> 구체화는 반대되는 말
- 추상화 될수록 사용자는 편하다...
- 하지만 반대로 추상화를 할 수록 만드는 사람은 없다.
- 누군가 한사람을 죽도록 고생시켜서 모두가 행복해진다.
- 클래스 설계 패턴 - 32가지(디자인패턴)

## 🟡 은닉화 -

- 다른 언어에서는 은닉화를 많이 지원한다.
- 접근권한을 만들어서 특정변수나 함수에 외부로 부터 접근불가 상황이 기본 외부에서 접근하게 별도로 권하능 루저야한다.
- private와 public이 있는데, python은 기본이 public 입니다.
  - 만약에 일부 변수가 외부에 노출되기 싫다면 \_\_(언더바 2개)를 변수나 함수 앞에 붙이면 private 된다.
  - weekpay module 예제 중: 함수 하나도 안만들고 변수만 있어도 충분하다.
  - weekpaymanger: 이 클래스를 통해서 접근 여기서만
    - worker_list만 보호하면 된다.
- 결론적으로 python은 굉장히 줄어들었다.

## 🟡 상속성 (x 아직 안배움)

## 🟡 다형성 - \_\_init\_\_ 매개변수 기본값

<br><br>

# 🟩 가위바위보 과제 같이 풀어보자!!!

- 컴퓨터가 1 , 2 , 3 중에 랜덤값 하나를 생각하고 있음
  - 1 = 가위 , 2 = 바위 , 3 = 보
- 사용자가 1, 2, 3 중에 하나를 입력함
  - 1 = 가위 , 2 = 바위 , 3 = 보
- 출력 : 컴퓨터 승 , 사람 승 , 무승부
- 10 번을 해서
  - 컴퓨터 몇 번 , 사람 몇 번 , 무승부 몇 번 했는지 나오도록
  - 마지막 승률을 계산

```python
import random

class GameData:
  # 변수 선언을 생성자에 하자
    # 이유: 그래야 객체가 생성될 때마다 새로운 메모리를 만들어준다.
  def __init__(self):
    self.computer = 0
    self.person = 0
    self.winner = 0

  def gameStart(self):
    self.computer = random.randint(1,3)
    self.person = int(input('1.가위, 2.바위, 3.보 중 선택 숫자 입력 :  '))
    self.winner = self.isWinner()

  def isWinner(self):  # 🔥 나한테는 calcul 부분
    s = self
    if s.computer == s.person:
      return 3

    # 명령어 한문장 이상일 때 연결하는 기호 '\' (양 쪽으로 공백이 필요합니다.)
    if (s.computer == 1 and s.person==3) or \
        (s.computer == 2 and s.person==1) or \
        (s.computer == 3 and s.person==2):
      return 1 # 컴퓨터 승

    return 2 # 사람 승

  def printLog(self):
    print(f"컴퓨터: {self.computer} | 사람: {self.person} | 승부: {self.winner}")



class Game:
  title1 = ["", "가위", "바위", "보"]
  title2 = ["", "컴퓨터승", "사람승", "무승부"]

  def __init__(self):
    self.gameList = []  # game 정보를 저장한다.

  def start(self):
    while True:
      g = GameData()
      g.gameStart()
      # g.printLog()
      # self.printLog(g)
      self.gameList.append( g )

      agein = input('1. 계속? | 0. 종료? : ')
      if agein != '1':
        return

  def printLog(self, g):
    print(f"컴퓨터: {self.title1[g.computer]}", end='\t')
    print(f"사람: {self.title1[g.person]}", end='\t')
    print(f"승부: {self.title2[g.winner]}")

  def printResult(self):
    print(f"{len(self.gameList)}번 수행함")
    for g in self.gameList:
      self.printLog(g)

  def mainStart(self):
    self.start()
    self.printResult()

# 습관적으로 해당 if문을 써주자!!
if __name__ == '__main__':
#   g = GameData()
#   g.gameStart()
#   g.printLog() # class 내에서 호출해놓는 것이 아닌 이렇게 호출하면 나중에 지우기도 좋겠다.
  game = Game()
  game.mainStart()
```

<br><br>

# 🟩 문제(성적처리 문제를 클래스로 만들어보세요.)

### class module 형태로 만들어야 합니다.

1.  먼저 score라는 폴더를 생성하고,
2.  파일을 2개를 만들어서 각각 class를 넣어놓고
3.  import를 통해서 다른 파일의 class를 가져다가 사용합니다.

### class를 만들 때는 하나만 처리하는 class 1개를 먼저 만듭니다.

```python
# ScoreData.py

# 이 파일에서는 한 명만 처리할 수 있으면 됩니다.

# 한 사람 정보 - 데이터 베이스 레코드 하나
# 파이썬의 경우는 파일명과 클래스명은 아무 관계 없다.

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


if __name__ == '__main__':
  s = ScoreData(10, 20, 30)
  s.print()
```

### 1개의 동작을 하는 class를 가지고 원하는 값을 도출해 낼 수 있도록 만들어줍니다.

```python
# ScoreDataManager.py

from ScoreData import ScoreData
# ScoreData.py 파일에서부터 ScroeData클래스를 가져와라.

class ScoreManager:
  def __init__(self):
    self.scoreList = [
      ScoreData('조승연', 90, 80, 90),
      ScoreData('안세영', 80, 80, 90),
      ScoreData('김연아', 90, 90, 90),
      ScoreData('김연경', 100, 80, 100)
    ]

  def append(self):
    sc = ScoreData() # 객체 생성
    sc.name = input('이름을 입력하세요 : ')
    sc.kor = int(input('국어 점수를 입력하세요 : '))
    sc.eng = int(input('영어 점수를 입력하세요 : '))
    sc.mth = int(input('수학 점수를 입력하세요 : '))
    sc.process()
    self.scoreList.append(sc)


  def search_student(self):
    find_name = input('찾을 이름을 입력해주세요 : ')
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))

    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.

    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()


  def edit_student(self):
    find_name = input('수정할 이름을 입력해주세요 : ')
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))

    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.

    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()

    sel = int(input('수정할 대상의 번호를 입력해주세요 : '))
    item = find_student[sel]
    item.name = input('이름을 입력하세요 : ')
    item.kor = int(input('국어 점수를 입력하세요 : '))
    item.eng = int(input('영어 점수를 입력하세요 : '))
    item.mth = int(input('수학 점수를 입력하세요 : '))
    item.process() # 다시 계산하기


  def delete_student(self):
    find_name = input('삭제할 이름을 입력해주세요 : ')
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))

    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return

    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()

    sel = int(input('삭제할 대상의 번호를 입력해주세요 : '))
    item = find_student[sel]
    self.scoreList.remove(find_student[sel])
    item.process() # 다시 계산하기


  def sorted(self):
    result_list = sorted(
        self.scoreList,
        key=lambda item : item.total,
        reverse=True
      )

    for i in result_list:
      i.print()


  def printAll(self):
    for s in self.scoreList:
      s.print()


  def menuDisplay(self):
    print("----------------")
    print("----- 메뉴 -----")
    print("[1] 학생 추가")
    print("[2] 기록 출력")
    print("[3] 검색  ") #이름
    print("[4] 수정  ") #이름
    print("[5] 삭제  ") #이름
    print("[6] 정렬  ") #총점 내림차순으로
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
      self.sorted
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
  sm.printAll()
```

<br><br>

# 🟩 문제 (야구게임을 class module로 만들어보기)

```python
import random

# 하나씩만 생각하며 만드는 습관을 가져야합니다.

class Baseball:
  # 1. 변수를 이렇게 지정
  def __init__(self):
    self.computer = [-1, -1, -1, -1]
    self.person = [-1, -1, -1, -1]
    self.count = 0  # 몇 번 했는지를 저장하기 위한 변수
    self.personList = []

  # 2. 컴퓨터의 입력
  def init_computer(self):
    cnt = 1
    while cnt <= 3:
      v = random.randint(0,9)
      if v not in self.computer:  # 중복 아닐 때
        self.computer[cnt] = v
        cnt += 1

  # 3. 유저의 입력
  def init_person(self):
    s = input('숫자 3개를 입력하세요 (예시 0 1 2) : ')
    number_list = s.strip().split(' ')  # 이거는 문자열 리스트입니다.

    self.person[1] = int(number_list[0])  # 숫자로 바꿔서 넣습니다.
    self.person[2] = int(number_list[1])
    self.person[3] = int(number_list[2])

  # 4. 컴퓨터의 입력을 맞췄는지 calculator
  def get_result(self):
    strike = 0
    ball = 0
    out = 0

    for i in range(1, 4):
      if self.computer[i] == self.person[i]:
        strike += 1
      elif self.computer[i] == self.person[1] or \
            self.computer[i] == self.person[2] or \
            self.computer[i] == self.person[3]:
        ball += 1
      else:
        out += 1
      print(f"{i}번째 확인 : {strike}, {ball}, {out}")

    return strike, ball, out

  # 5. 다 했다. 이제 합치자!
  def start(self):
    # 3strike 이거나 4번의 기회를 다 사용했을 경우에 종료한다.

    flag = False # 아직 3strike가 아님을 나타내기 위한 변수

    self.init_computer()
    print(self.computer)  # 컨닝하면서 테스트하려고 합니다.

    while flag == False and self.count <= 5:
      self.init_person()
      strike, ball, out = self.get_result()
      print(f"strike: {strike} | ball: {ball} | out: {out}")

      self.personList.append({
        # 'person': self.person,
        'person': [x for x in self.person],  # 이것은 Hard Copy 입니다.
        'strike': strike,
        'ball': ball,
        'out': out
      })

      if strike == 3:
        flag = True
      else:
        self.count += 1


if __name__ == '__main__':
  b = Baseball()
  # b.init_computer()
  # b.init_person()

  # print(b.computer)
  # print(b.person)
  # b.get_result()

  b.start()
```

```python
from GameData import Baseball

class GameMain:
  def __init__(self):
    self.gameList = []

  def gamestart(self):
    b = Baseball()
    b.start()
    self.gameList.append(b)

  def showStatistics(self):
    for b in self.gameList:
      print(b.computer)
      for item in b.personList:
        print(
          item['person'],
          item['strike'],
          item['ball'],
          item['out'],
          b.count
        )

  def start(self):
    while True:
      print(f"1. 게임시작")
      print(f"2. 통계")
      print(f"0. 종료")
      sel = input('선택 : ')
      if sel == '1':
        self.gamestart()
      elif sel == '2':
        self.showStatistics()
      else:
        return


if __name__ == '__main__':
  g = GameMain()
  g.start()
```

<br><br>

# 🟩 과제 - Linux 설치하기

- Mac에 VMware를 통해서 설치를 시도해보려고 합니다.
- **[https://cdimage.ubuntu.com/releases/22.04.5/release/](https://cdimage.ubuntu.com/releases/22.04.5/release/)**

- 성공적으로 설치를 완료하였습니다.
