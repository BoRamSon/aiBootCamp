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
    print(f"\n-------- 통계 --------")
    print(f"컴퓨터 승리 수 : {winning_dict_list['computer_wins_number']}")
    print(f"사람 승리 수 : {winning_dict_list['user_wins_number']}")
    print(f"무승부 수 : {winning_dict_list['draw_game']}")
    print(f"컴퓨터의 승률 : {winning_dict_list['computer_winning_rate']}")
    print(f"사람의 승률 : {winning_dict_list['user_winning_rate']}")
    print(f"-------- 통계 --------\n")

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
