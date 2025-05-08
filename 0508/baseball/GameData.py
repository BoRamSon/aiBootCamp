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
        'person': [x for x in self.person],  # 🔥🔥🔥 이것은 Hard Copy 입니다.
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
