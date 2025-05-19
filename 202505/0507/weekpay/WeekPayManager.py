# 파일명 > 클래스명 순서로 이름을 적습니다.
from WeekPay import WeekPay    # 외부 파일 (모듈을) 이 파일로 불러오기

class WeekPayManager:
  def __init__(self):
    self.worker_list = [
      WeekPay('홍길동', 20, 20000),
      WeekPay('고길동', 10, 50000),
      WeekPay('김길동', 30, 40000),
      WeekPay('이길동', 40, 20000),
      WeekPay('장길동', 20, 20000)
    ]

  def output(self):
    for w in self.worker_list:
      # 1) 여기에 WeekPay2('홍길동', 20, 20000) 클래스 자체가 들어와버립니다.
      # 2) 그러면서 w가 output
      w.output() 

  def search(self):
    name = input("찾을이름 : ")
    result_list = list(filter(lambda w : w.name == name, self.worker_list))
    if len(result_list) == 0:
        print("데이터가 없습니다")
        return 
    
    #resultList[0].output() #Weekpay의 output
    for w in result_list:
        w.output()


  def modify(self):  # 수정하다, 수식하다, 한정하다
    name = input('찾을 이름 :')
    result_list = list(filter( lambda w : name in w.name, self.worker_list)) # 포함만 되어있어도 필터링 해버리기
    if len(result_list) == 0:
      print('찾으시는 데이터가 존재하지 않습니다.')
      return

    # enumerate 함수는 인덱스랑 데이터를 한꺼번에 반환한다.
    for i, w in enumerate(result_list):
        print(i, end ="\t")
        w.output()

    sel = int(input('수정할 대상을 선택하세요. :'))
    temp = result_list[sel]
    temp.name = input('이름 : ')
    temp.work_time = int(input('근무시간 :'))
    temp.per_pay = int(input('시간당급여액 :'))
    temp.process()


  def delet(self):
    pass
    # result_list = self.search()

    # 삭제하고 싶었던 것을 dict type으로 만들어주고, 
    # for i in result_list:

    # name = input('찾을 이름 :')
    


  def start(self):
    print('start')


# c3 = WeekPayManager()
# c3.output()


# ------------------------------------------
# 🟡 다른 파일에서 import 해올 때는 실행되지 않게 막는 용도입니다.

# 파이썬의 모듈들은 내장변수가 있다. __name__ 을 누구나 가지고 있습니다.
  # 언더바 2개는 다 내장이다. (우리가 만든게 아닌 시스템 제공)
# print(__name__)  # 이 모듈로 직접 실행하면 main이 들어온다. python Weekpay.py
# import 되서 싱행되면 파일명이 전달된다. python WeekPayManager.py

# if __name__ == "__main__":
#   mgr = WeekPayManager()
#   mgr.output()