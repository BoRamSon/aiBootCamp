class WeekPay():
  def __init__(self, name='', work_time = 20, per_pay = 10000):
    self.name = name
    self.work_time = work_time
    self.per_pay = per_pay
    self.process()

  def process(self):
    self.pay = self.work_time * self.per_pay

  def output(self):
    print(f"이름: {self.name} | 근무한 시간: {self.work_time} | 시급: {self.per_pay} | 주급: {self.pay}")


# w1 = WeekPay('A')
# w1.output()

# ------------------------------------------
# 🟡 다른 파일에서 import 해올 때는 실행되지 않게 막는 용도입니다.

# 파이썬의 모듈들은 내장변수가 있다. __name__ 을 누구나 가지고 있습니다.
  # 언더바 2개는 다 내장이다. (우리가 만든게 아닌 시스템 제공)
print(__name__)  # 이 모듈로 직접 실행하면 main이 들어온다. python Weekpay.py
# import 되서 싱행되면 파일명이 전달된다. python WeekPayManager.py

if __name__ == "__main__":
  w1 = WeekPay('A')
  w1.output()