import pickle

class WeekPayCalculator:
  def __init__(self):
    self.worker_list = []   # 원래 빈 값으로 만든 상태에서 input을 받아서 사용한다.
    # self.worker_list = [  
    #   {"name" : "홍길동" , "work_time" : 10 , "per_pay" : 10000},
    #   {"name" : "고길동" , "work_time" : 21 , "per_pay" : 10000},
    #   {"name" : "김길동" , "work_time" : 10 , "per_pay" : 10000}
    # ]

  def input_data(self):
      worker = {}
      worker["name"]      =     input("이름 : ")
      worker["work_time"] = int(input("근무 시간 : "))
      worker["per_pay"]   = int(input("시간 당 급여액 : "))
      self.worker_list.append(worker) 

  def calcul_data(self): 
    for w in self.worker_list:
      w["pay"] = w["work_time"] * w["per_pay"]
      if w["work_time"] > 20:
        w['pay'] += (w["work_time"] - 20) * (w["per_pay"] * 1.5)

  def output_result(self):
    for w in self.worker_list:
      print(f"이름: {w['name']}" , end="\t")
      print(f"근무시간: {w['work_time']}" , end="\t")
      print(f"시급{w['per_pay']}" , end="\t")
      print(f"주급{w['pay']}" , end="\t")
      print()

  def output_menu(self):
    print("[1] 추가")       
    print("[2] 계산")       
    print("[3] 출력")
    print("[4] 파일 저장")
    print("[5] 파일 오픈")
    print("[0] 종료")               

  # binary 파일 저장 코드 추가
  def save(self):
    with open('datas/weekpay.bin', 'wb') as f:
      pickle.dump(self.worker_list, f)
  
  # binary 파일 불러오기 코드 추가
  def load(self):
    with open('datas/weekpay.bin', 'rb') as f:
      self.worker_list = pickle.load(f)
    self.output_result()

  def start(self) :
    while(True) :              
      self.output_menu()              
      sel = input("선택 : ")
      if sel   == "1" :       
          self.input_data()            
      elif sel == "2" :       
          self.calcul_data()      
      elif sel == "3" :       
          self.output_result()            
      elif sel == "4" :       
          self.save()            
      elif sel == "5" :       
          self.load()            
      elif sel == "0" :       
          return print("프로그램을 종료합니다.")
      else :
          print("❌ 잘못 선택하셨습니다. 다시 입력해주세요.")

if __name__ == '__main__':
  c1 = WeekPayCalculator()
  c1.start()

