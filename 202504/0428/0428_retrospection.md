# 2025년 4월 28일 월요일 (4일차)

- 4일차가 시작되었다.

<br><br>

# 🟩 오전

오전 시간을 시작하자마자 list, dictionary, for문을 사용하는 예제를 풀기 시작했다. 예제만 몇 문제 풀었는데 시간이 너무나 빨리 갔다.

```
workers = []

for i in range(0, 2):
    name = input('이름: ')
    work_time = int(input('일한 시간: '))
    per_pay = int(input('시간당 급여: '))

    # 🔥 딕셔너리 형태로 데이터를 저장
    # 아~ 딕셔너리는 괄호안에 그대로 {}를 통해 넣는구나!!!!
    workers.append({'name': name, 'work_time': work_time, 'per_pay': per_pay})


for i in workers:
  weekly_pay = i['work_time'] * i['per_wage']
  print(f"\'{i['name']}\'님의 주급은 {weekly_pay}입니다.")
```

```
## 입력

name\_list = \[\]
korean\_lang\_sub\_list = \[\]
english\_lang\_sub\_list = \[\]
math\_sub\_list = \[\]

for i in range(0, 1):
name = input('이름을 입력하시오 : ')
korean\_lang\_sub = int(input('국어 점수를 입력하시오 : '))
english\_lang\_sub = int(input('영어 점수를 입력하시오 : '))
math\_sub = int(input('수학 점수를 입력하시오 : '))

name\_list.append(name)
korean\_lang\_sub\_list.append(korean\_lang\_sub)
english\_lang\_sub\_list.append(english\_lang\_sub)
math\_sub\_list.append(math\_sub)

# ==============================================
# 계산

grade\_sum\_result = \[\]
grade\_average\_result = \[\]
grade\_average\_korean\_result = \[\]

for i in range(0, 1):
total\_grade = korean\_lang\_sub\_list\[i\] + english\_lang\_sub\_list \[i\] + math\_sub\_list\[i\]
grade\_sum\_result.append(total\_grade)
total\_grade\_average = total\_grade / 3
grade\_average\_result.append(total\_grade\_average)
if total\_grade\_average >= 90:
grade\_average\_korean\_result.append('(수)')
elif total\_grade\_average >= 80:
grade\_average\_korean\_result.append('(우)')
elif total\_grade\_average >= 70:
grade\_average\_korean\_result.append('(미)')
elif total\_grade\_average >= 60:
grade\_average\_korean\_result.append('(양)')
else:
grade\_average\_korean\_result.append('(가)')

# ==============================================
# 출력
for i in range(0, 1):
print(f"{name\_list\[i\]}님의 총점은 {grade\_sum\_result\[i\]}이고, 평균은 {grade\_average\_result\[i\]}이며, 한글점수는 {grade\_average\_korean\_result\[i\]} 입니다.")
```

<br><br>

# 🟩 오후

오후 시간에는 for문 중첩과 별만들기에 대한 문제를 풀었다. 그런데 도저히 내 머릿속으로 별만들기를 할 수 없었다. 아무리 시도해도 어떻게 해야할지 감이 오지 않고 계속 실패만 했다.. 결국 ChatGPT와 강사님을 통해서 이렇게 만들 수 있구나 알게되었지만, 또 어떻게 이 코드가 만들어지는 것인지 깊이 이해하지 못했다.

<br><br>

## 🟢 for문 - 별 만들기

```
for i in range(0, 10):
  for j in range(0, i):
    print('*', end='')
  print()
```

하지만 수업은 나가야하기 때문에 함수(def)로 넘어간다.

<br><br>

## 🟢 함수(defien)

- 함수란? 특정 기능끼리 묶어놓은 코드
  - 아주 옛날에 프로그램을 스파게티 코드(결과만 나오면 좋다.)라고 합니다.
  - 결과만 나오면 좋다. =>
  - 모듈 (일을 작게 나누어서 처리하자 나눈 일의 단위) => 기능별로 나눠서
    - 프로시저 : 일이 끝나고 값을 반환하지 않는다.
    - 함수 : 일을 끝내고 값을 반환한다.
      - 파이썬은 프로시저나 함수를 구분하지 않습니다.
      - C언어가 프로시저와 함수를 합쳐서 함수라고 부른다.
  - 파일에 저장하는게 아니라, 데이터베이스에 저장을 한다.
    - MySQL을 주로 사용하는 이유는 공짜이기 때문이고, oracle이 가장 좋습니다.()
  - 함수는 기본적으로 15줄을 넘기면 안됩니다. A4용지 한장을 넘기면 안된다.
- 파이썬의 경우는 def키워드로 시작해서
- `def 함수이름(매개변수들): ...... ...... return 값 원칙이 값 하나만 리턴한다. 파이썬도 값을 하나만 보낸다. 만일 여러개 보내면 tuple타입으로 묶어서 전달한다. # 튜플 예시 : return value1, value2`
- 장점 : 유지보수가 편해진다.
  - 반복적인 일을 처리하고자 할 때 함수를 만들면 간결하게 처리할 수 있다.
  - 구조적 프로그래밍(C언어), 객체지향 프로그램에서 필수다.

<br><br>

## 🟢 수업을 마치며, 과제

- 과제1. 정수를 받아가서 짝수이면 True / 짝수가 아니면 False를 반환하는 함수
- 과제2. 4년마다 윤년인데,
  - 100년에 한번씩은 윤년이 아닙니다.
  - 400년에 한번씩 윤년이다.
  - 함수를 만들어서 연도를 주면 윤년일 경우 True / 윤년이 아니면 False를 반환해라.

<br><br>

## 🟢 github

[https://github.com/BoRamSon/aiBootCamp/tree/001_basic](https://github.com/BoRamSon/aiBootCamp/tree/001_python_basic)
