import random

class InputValidator:
    def __init__(self, user_input):
        self.user_input = user_input

    def validate_number(self):
      if self.is_empty():
        raise ValueError("빈 값입니다. 다시 입력해주세요.")
      if self.is_not_numeric():
        raise ValueError("숫자만 입력할 수 있습니다. 다시 입력해주세요.")
      if self.is_negative():
        raise ValueError("음수는 허용되지 않습니다. 다시 입력해주세요.")
      if self.is_three_number():
        raise ValueError("반드시 3자리를 입력하셔야 합니다. 다시 입력해주세요.")
      if self.is_duplicate():
        raise ValueError("중복된 숫자를 함께 입력하실 수 없습니다. 다시 입력해주세요.")
        
    def validate_answer(self):
      if self.is_answer():
        raise ValueError("Y or N 값이 입력되지 않았습니다. 다시 입력해주세요.")

    def is_answer(self):
      return self.user_input not in ['Y', 'y', 'N', 'n']

    def is_empty(self):
      return self.user_input == ""

    def is_not_numeric(self):
      return not self.user_input.isnumeric()

    def is_negative(self):
      return int(self.user_input) < 0

    def is_three_number(self):
      return len(self.user_input) != 3
    
    def is_duplicate(self):
      return len(set(self.user_input)) != 3


class BaseballGame():
  def __init__(self):
    self.play_baseball_game()

  def computer_random_numbers(self):
    random_three_number = random.sample(range(1,10), 3)
    random_three_number = [str(i) for i in random_three_number] 
    return random_three_number

  def user_input_numbers(self):
    for i in range(1,11):
      input_three_number = input('숫자 3개를 입력하세요 (예: 123): ')
      validate_number = input_three_number.replace(' ', '')

      try:
        validator = InputValidator(validate_number)
        validator.validate_number()
      except ValueError as e:
        print("검증 실패:", e)
      else:
        print(f"------------------------ \n{validate_number}를 입력하셨습니다.")
        break

      if i == 10:
        print('\nError: 3개의 숫자를 10번 이상 잘 못된 값을 입력하여 종료되었습니다.\n')
        break
    print(list(str(validate_number)))
    return list(str(validate_number))
    
  def is_collect_number(self, random_number, user_number):
    strike = 0
    ball = 0
    out = 0

    for i in range(0, 3):
      if random_number[i] == user_number[i]:
        strike += 1
      elif user_number[i] == random_number[0] or \
          user_number[i] == random_number[1] or \
          user_number[i] == random_number[2]:
        ball += 1
      else:
        out += 1
      print(f"계산 과정 보자 {strike}, {ball}, {out}")
    return strike, ball, out
  
  def collect_number_result(self):
    random_number = self.computer_random_numbers()

    try_count = 0
    write_result_history = []

    while True:
      user_number = self.user_input_numbers()
      strike, ball, out = self.is_collect_number(random_number, user_number)
      try_count += 1
      write_result_history.append({'try':  try_count,'strike': strike, 'ball': ball, 'out': out})
      
      if strike == 3:
        print('3 strike!!! 🎉축하 드립니다!🎉')
        print(f"컴퓨터가 선택한 랜덤 숫자는 {random_number}였습니다.")
        print(f"{try_count}번만에 맞추셨습니다.\n============================\n")
        break
      else:
        print(f'결과 : {strike}strike, {ball}ball, {out}out \n------------------------')

      if try_count == 10:
        print('10번의 시도가 끝났습니다. 이번 게임은 종료되었습니다. \n')
        return '실패'
        
    return try_count

  def play_baseball_game(self):      
    print('⚾️ 야구 게임이 시작되었습니다! \n게임당 맞출 수 있는 기회는 10번 입니다.\n')
    play_count = 0
    collect_history = []

    for i in range(1,11): 
      game_try_count = self.collect_number_result()
      play_count += 1
      fail_count = 0
      collect_history.append({'game_play_count': play_count, 'game_try_count': game_try_count})
      
      for i in range(1,11):
        is_continue = input('🎮 게임을 계속 진행하시겠습니까?? \n(진행 = \'Y\'입력 / 끝내기 = \'N\'입력)')

        try:
          validator = InputValidator(is_continue)
          validator.validate_answer()
        except ValueError as e:
          print("검증 실패:", e)
        else:
          if is_continue == 'N' or is_continue == 'n':
            # 통계
            print(f"\n총 {play_count}번 게임을 실시 했습니다.")
            print(f"야구 게임이 완전히 종료되었습니다. 아래 통계를 확인해보세요! \n< 통계 >")
            for i in collect_history:
              print(f"- {i['game_play_count']}번째 게임에서 {i['game_try_count']}번째만에 맞췄습니다.")
            # 승률
            for i in collect_history:
              if i['game_try_count'] == '실패':
                fail_count += 1
            wining_rate = ((play_count-fail_count)/play_count) * 100
            print (f"🏆 승률은 {wining_rate}% 입니다.")
            return wining_rate
          else:
            print('⚾️ 야구 게임을 다시 시작하셨습니다.\n')
            break

        if i == 10:
          return print('\nError: 10번 이상 잘 못된 값을 입력하여 종료되었습니다.\n')

baseball_game = BaseballGame()
