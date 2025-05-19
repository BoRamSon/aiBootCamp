from convert_data_csv import ConvertData
from vending_machine_validate import InputValidator
from vending_machine_constants import (
  INPUT_MESSAGES_STRING_PRICE,
  INPUT_MESSAGES_STRING_SELECT,
  INPUT_MESSAGES_STRING_QUENTITY
)

class VendingMachineFunc:
  def __init__(self):
    c = ConvertData()
    self.vending_machine_data = c.start() # 데이터를 가진 존재
    self.input_validator = InputValidator()
    self.INPUT_MESSAGES_STRING_PRICE = INPUT_MESSAGES_STRING_PRICE
    self.INPUT_MESSAGES_STRING_SELECT = INPUT_MESSAGES_STRING_SELECT
    self.INPUT_MESSAGES_STRING_QUENTITY = INPUT_MESSAGES_STRING_QUENTITY
    self.select_money = 0
    self.select_menu = ''
    self.get_menu_price = 0
    self.get_menu_quentity = 0
    self.select_quentity = 0
    self.is_buy = bool
    self.sold_quentity = 0
    self.out_change = 0
    self.decided_data = {}
  
  def start(self):
    self.menu_screen()
    self.input_money()
    self.menu_screen()
    self.input_data()
    self.input_quentity()
    self.decided_menu()
    self.calcul_is_buy()
    self.output_data()
    self.update()
    self.output_inventory()
    return self.decided_data

  def menu_screen(self):
    print(f"--------------------------")
    for i in self.vending_machine_data:
      print(f"{i['num']}. {i['menu']} | 가격: {i['price']}원 | 재고: {'stock'}")
    print(f"--------------------------")

  def input_money(self): 
    money = self.input_validator.input_price(self.INPUT_MESSAGES_STRING_PRICE)
    self.select_money = int(money)
    print(f"💰 넣으신 금액은 \'{self.select_money}\'원 입니다.\n")
    return money

  def input_data(self):
    select_menu = self.input_validator.input_sequence(self.INPUT_MESSAGES_STRING_SELECT)
    self.select_menu = select_menu
    print(f"🤣 입력하신 메뉴는 \'{self.select_menu}\' 입니다.\n")
    return select_menu
  
  def input_quentity(self):
    select_quentity = self.input_validator.input_quentity(self.INPUT_MESSAGES_STRING_QUENTITY)
    self.select_quentity = int(select_quentity)
    print(f"🤣 입력하신 수량은 \'{self.select_quentity}\' 입니다.\n")
    return select_quentity
  
  def decided_menu(self):
    if self.select_menu.isnumeric():
      for i in self.vending_machine_data:
        if self.select_menu == i['num']:
          self.select_menu = i['menu']
          self.get_menu_price = i['price']
          self.get_menu_quentity = int(i['stock'])
    else:
      for i in self.vending_machine_data:
        if self.select_menu == i['menu']:
          self.select_menu = i['menu']
          self.get_menu_price = i['price']
          self.get_menu_quentity = int(i['stock'])
    self.decided_data = {
      'select_money' : self.select_money,
      'select_menu' : self.select_menu,
      'menu_price' : self.get_menu_price,
      'menu_quentity' : self.get_menu_quentity,
      'select_quentity' : self.select_quentity   
    }
    print(f" ✔️ 확정 데이터: {self.decided_data}\n")
  
  def calcul_is_buy(self):
    needs_money = self.decided_data['menu_price'] * self.decided_data['select_quentity']
    if int(needs_money) <= self.decided_data['select_money']:
      self.is_buy = True
      self.out_change += self.select_money - int(needs_money)
      self.get_menu_quentity -= int(self.decided_data['select_quentity'])  # 재고 update
    else:
      self.is_buy = False
    
  def output_data(self):
    if self.is_buy == True:
      print(f"🥤 {self.decided_data['select_menu']} {self.decided_data['select_quentity']}개 여기 있습니다.")
      print(f"💰 거스름돈 {self.out_change}")
    else:
      print(f"🚫 ✋ 돈이 모자라서 못 사요. 돌아가주세요.")
      print(f"😭 넣으신 금액 {self.select_money}원이 환불되었습니다.\n")

  def update(self):
    self.decided_data = {
      'select_money' : self.select_money,
      'select_menu' : self.select_menu,
      'menu_price' : self.get_menu_price,
      'menu_quentity' : self.get_menu_quentity,
      'select_quentity' : self.select_quentity,
      'is_possible_buy' : self.is_buy,
      'out_chage' : self.out_change
    }
    for i in self.vending_machine_data:
      if self.select_menu == i['menu']:
        i['stock'] = self.get_menu_quentity

  def output_inventory(self):
    print(f"\n< 🧮 현재 자판기 내 상품 현황 >")
    for i in self.vending_machine_data:
      print(f"{i}")


if __name__ == '__main__':
  v = VendingMachineFunc()
  v.start()