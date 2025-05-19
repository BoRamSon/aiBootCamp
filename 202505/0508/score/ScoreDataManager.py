from ScoreData import ScoreData
# ScoreData.py 파일에서부터 ScroeData클래스를 가져와라.

class ScoreManager:
  def __init__(self):
    self.scoreList = [
      ScoreData('조승연', 90, 80, 90),
      ScoreData('안세영', 80, 80, 90),
      ScoreData('김연아', 90, 90, 90),
      ScoreData('김연경', 100, 80, 100)
    ]

  def append(self):
    # input_name = input('이름을 입력하세요 : ')
    # input_kor = int(input('국어 점수를 입력하세요 : '))
    # input_eng = int(input('영어 점수를 입력하세요 : '))
    # input_mth = int(input('수학 점수를 입력하세요 : '))
    # sc = ScoreData() # 객체 생성
    # sc.process()
    # self.scoreList.append(ScoreData(input_name, input_kor, input_eng, input_mth))

    sc = ScoreData() # 객체 생성
    sc.name = input('이름을 입력하세요 : ')
    sc.kor = int(input('국어 점수를 입력하세요 : '))
    sc.eng = int(input('영어 점수를 입력하세요 : '))
    sc.mth = int(input('수학 점수를 입력하세요 : '))
    sc.process()
    self.scoreList.append(sc)



  def search_student(self):
    # find_name = input('찾을 이름을 입력해주세요 : ')
    # for s in self.scoreList:       # 🔥 for문과 if문으로 충분히 할 수 있을 것 같은데에....
    #   if s['name'] == find_name:
    #     find_student.append(s)
    #     print(f'찾았습니다! >>>> {s}')

    find_name = input('찾을 이름을 입력해주세요 : ')
    # filter는 두번쨰 매개변수로 전달된 list를 받아서
    # for문 돌려서 첫번째 매개변수로 전달된 함수를 호출
    # 람다 : 매개변수하나(scoreList에 저장된 객체 하나)
    #       반환은 True or False

    # 매개변수 ScoreData 객체
    # list로 둘러 쌓으면 list생성자가 호출되면서 filter가 모든 작업을 완료한다.ㅁ
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))
    
    # 데이터가 없을 수 있잖아~
    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.
    
    # 🔥🔥🔥 enumerate가 list를 전달하면 해당 리스트 내의 위치 index와 함께 결과물을 출력해줍니다.
    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()

    # print(find_student)  
    # return find_student   # 🔥🔥🔥 이거를 이렇게 계속 수정 > 삭제 > 정렬 순으로 가져가면서 사용하려고 생각했었습니다.



  def edit_student(self):
    # self.search_student()

    find_name = input('수정할 이름을 입력해주세요 : ')
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))
  
    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.
    
    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()
    
    sel = int(input('수정할 대상의 번호를 입력해주세요 : '))
    # 수정할 대상의 참조를 가져온다.
    item = find_student[sel]   # 🔥🔥🔥 self.scoreList 원본을 바꿔줘야 할 것 같은데요
    item.name = input('이름을 입력하세요 : ')
    item.kor = int(input('국어 점수를 입력하세요 : '))
    item.eng = int(input('영어 점수를 입력하세요 : '))
    item.mth = int(input('수학 점수를 입력하세요 : '))
    item.process() # 다시 계산하기


    # print(find_student)
    # return find_student



  def delete_student(self):
    find_name = input('삭제할 이름을 입력해주세요 : ')
    find_student = list(filter(lambda item: find_name in item.name , self.scoreList))
  
    if len(find_student) == 0:
      print('찾으시는 데이터가 없습니다.')
      return   # else 사용하지 말고 그냥 종료시켜버려라.. 굳이 반복 시켜줄 필요도 딱히 없다.
    
    for i, s in enumerate(find_student):
      print(f"[{i}]", end=' ')
      s.print()

    sel = int(input('삭제할 대상의 번호를 입력해주세요 : '))
    # 수정할 대상의 참조를 가져온다.
    item = find_student[sel]  
    # ------------------------
    # 🟡 edit_student 코드에서 이 부분만 추가하였습니다.
    # del find_student[sel]  # 🔥🔥🔥 del은 삭제가 되지 않습니다.
    self.scoreList.remove(find_student[sel]) # 🔥🔥🔥 직접적으로 list.remove를 통해 삭제를 했습니다.
                                      # 🔥🔥🔥 보통 삭제에서는 remove를 사용한다고 알아두세요!!!
    # ------------------------
    item.process() # 다시 계산하기

  def sorted(self):
    # 원본을 냅두고, 정렬하여 출력하기
      # sort는 원본을 직접 정렬
      # sorted는 새로운 정령된 리스트를 반환

    # key에 전달해야할 람다는 
    # 매개변수 하나 반환값 정렬을 할 수 있는 데이터 타입
    # > < 연산자 수행이 가능하다

    # s1 = ScoreData()
    # s2 = ScoreData()
    # s1 > s2
    # 파이썬이 제공하는 기본 파이썬이 제공하는 기본 타입들 int, float, str

    result_list = sorted(
        self.scoreList, 
        key=lambda item : item.total,  # 🔥🔥🔥 이렇게까지는 생각을 못했다.
        reverse=True
      )

    for i in result_list:
      i.print()



# ==================================================

  def printAll(self):
    for s in self.scoreList:
      s.print()

  def menuDisplay(self):
    print("----------------")
    print("----- 메뉴 -----")
    print("[1] 학생 추가")
    print("[2] 기록 출력")
    print("[3] 검색  ") #이름
    print("[4] 수정  ") #이름
    print("[5] 삭제  ") #이름
    print("[6] 정렬  ") #총점 내림차순으로 
    print("[0] 프로그램 종료")
    print("----------------")

  def start(self):
    funcList = [
      None, 
      self.append, 
      self.printAll, 
      self.search_student,
      self.edit_student,
      self.delete_student,
      self.sorted
    ]
    while True:
      self.menuDisplay()
      choise = int(input('선택 : '))
      if choise > 0 and choise < len(funcList):
        funcList[choise]()
      else:
        return





if __name__ == '__main__':
  sm = ScoreManager()
  sm.start()
  sm.printAll()