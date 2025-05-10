import re
from vending_machine_constants import OUTPUT_MESSAGES_STRING

class InputValidator:  
  def __init__(self):
    self.OUTPUT_MESSAGES_STRING = OUTPUT_MESSAGES_STRING

  def input_price(self,MESSAGE_DICT):
    for key, message in MESSAGE_DICT.items():
      for i in range(1,11):
        validate_target = input(message)
        try:
          self.validate_price(validate_target)
        except ValueError as e:
          print('ERROR:', e)
          if i == 10: return print('종료되었습니다. 다시 시도하세요.')
        else:
          print(f"✅ <검증완료> \'{key}\': \'{validate_target}\'")
          return validate_target

  def input_sequence(self, MESSAGE_DICT):
    for key, message in MESSAGE_DICT.items():
      for i in range(1,11):
        validate_target = input(message)
        try:
          if self.is_valid_int(validate_target):
            self.validate_string(validate_target)
          else:
            self.validate_number(validate_target)
        except ValueError as e:
          print('ERROR:', e)
          if i == 10: return print('종료되었습니다. 다시 시도하세요.')
        else:
          print(f"✅ <검증완료> \'{key}\': \'{validate_target}\'")
          return validate_target
  
  def input_quentity(self,MESSAGE_DICT):
    for key, message in MESSAGE_DICT.items():
      for i in range(1,11):
        validate_target = input(message)
        try:
          self.validate_quentity(validate_target)
        except ValueError as e:
          print('ERROR:', e)
          if i == 10: return print('종료되었습니다. 다시 시도하세요.')
        else:
          print(f"✅ <검증완료> \'{key}\': \'{validate_target}\'")
          return validate_target

  def validate_string(self, input):
    if self.is_empty(input):
      raise ValueError('빈 값입니다. 다시 입력해주세요.')
    if self.is_numeric(input):
      raise ValueError('숫자가 입력될 수 없습니다. 다시 입력해주세요.')
    if self.is_korean_string(input):
      raise ValueError('한글만 입력할 수 있어요. 다시 입력해주세요.')
    if self.is_in_the_menu(input, self.OUTPUT_MESSAGES_STRING):
      raise ValueError('메뉴에 존재하지 않습니다. 다시 입력해주세요.')
    
  def is_numeric(self, input):
    return input.isnumeric()
  
  def is_korean_string(self, input):
    return not bool(re.fullmatch(r"[가-힣]+", input))
  
  def is_in_the_menu(self, input, OUTPUT_MESSAGES_STRING):
    validate_menu = []
    for i in OUTPUT_MESSAGES_STRING:
      validate_menu.append(i['menu'])
    return not (input in validate_menu)

  def validate_price(self, input):
    if self.is_valid_int(input):
      raise ValueError('숫자만 입력할 수 있습니다. 다시 입력해주세요.')
    if self.is_empty(input):
      raise ValueError('빈 값입니다. 다시 입력해주세요.')
    if self.is_negative(input):
      raise ValueError('음수는 허용되지 않습니다. 다시 입력해주세요.') 
    if self.is_price_limit(input):
      raise ValueError('최소 200원이상 넣어주세요. 다시 입력해주세요.')
    
  def validate_quentity(self, input):
    if self.is_empty(input):
      raise ValueError('빈 값입니다. 다시 입력해주세요.')
    if self.is_negative(input):
      raise ValueError('음수는 허용되지 않습니다. 다시 입력해주세요.') 
    if self.is_limit_quentity_range(input):
      raise ValueError('과도한 수량을 입력하셨습니다. 다시 입력해주세요.') 

  def validate_number(self, input):
    if self.is_empty(input):
      raise ValueError('빈 값입니다. 다시 입력해주세요.')
    if self.is_negative(input):
      raise ValueError('음수는 허용되지 않습니다. 다시 입력해주세요.') 
    if self.is_limit_range(input):
      raise ValueError('메뉴가 1 ~ 9까지 있습니다. 다시 입력해주세요.') 
    
  def is_empty(self, input):
    return input == ''
  
  def is_valid_int(self, input):
    try:
        int(input)
        return False
    except ValueError:
        return True

  def is_negative(self, input):
    return int(input) < 0
  
  def is_limit_range(self, input):
    return int(input) < 0 or 10 <= int(input)
  
  def is_price_limit(self, input):
    return int(input) < 200
  
  def is_limit_quentity_range(self, input):
    return int(input) < 0 or 30 <= int(input)
  