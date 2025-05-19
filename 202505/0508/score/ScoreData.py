# 이 파일에서는 한 명만 처리할 수 있으면 됩니다.

# 한 사람 정보 - 데이터 베이스 레코드 하나
# 파이썬의 경우는 파일명과 클래스명은 아무 관계 없다.

class ScoreData:
  def __init__(self, name = '홍길동', kor = 0, eng = 0, mth = 0):  # 일반 인자는 항상 defaut 값보다 앞에 온다.
    self.name = name
    self.kor = kor
    self.eng = eng
    self.mth = mth 
    self.process()

  def process(self):   # 계산하는 친구
    self.total = self.kor + self.eng + self.mth
    self.avg = self.total/3
    if self.avg >= 90:
      self.grade = '수'
    elif self.avg >= 80:
      self.grade = '우'
    elif self.avg >= 70:
      self.grade = '미'
    elif self.avg >= 60:
      self.grade = '양'
    else:
      self.grade = '가'

  def print(self):
    print(f"이름: {self.name}", end='\t')
    print(f"국어: {self.kor}", end='\t')
    print(f"영어: {self.eng}", end='\t')
    print(f"수학: {self.mth}", end='\t')
    print(f"합계: {self.total}", end='\t')
    print(f"평균: {self.avg: .2f}%", end='\t') # 여기 ': .2f' 에 대해서 공부해야합니다.
    print(f"등급: {self.grade}")


if __name__ == '__main__':
  s = ScoreData(10, 20, 30)
  s.print()