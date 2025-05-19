from vending_machine_func import VendingMachineFunc

class VendingMachineManager:
  def __init__(self):
    self.v = VendingMachineFunc()

  def output_screen(self):
    print("[1] 자판기 실행")
    print("[2] 판매내역 출력")
    print("[3] 재고현황 출력")
    print("[0] 프로그램 종료")
    
  def start(self):
    record = [] # 판매내역 기록
    while True :
      self.output_screen()
      sel = input("메뉴 선택 : ")
      if sel == "1" :
        result = self.v.start()
        record.append(result)
        print('\n----- 자판기 작동 끝 -----\n')
      elif sel == "2" :
        # print(f"판매내역 : {record['select_menu']} {record['']}\n")
        print(f"📜 판매내역: {record}")
        print('\n----- 판매내역 출력 끝 -----\n')
          # [{
            # 'select_money': 1000, 
            # 'select_menu': '콜라', 
            # 'menu_price': '1000', 
            # 'menu_quentity': 9, 
            # 'select_quentity': 1, 
            # 'is_possible_buy': True, 
            # 'out_chage': 0
          # }] 
      elif sel == "3" :
        self.v.output_inventory()
        print('\n----- 재고현황 출력 끝 -----\n')
      elif sel == "0" :
        print('- 정상적으로 종료되었습니다.-\n')    
        return
      else :
        print('잘못 입력하셨습니다. 다시 입력해주세요.')

if __name__ == '__main__':
  v = VendingMachineManager()
  v.start()