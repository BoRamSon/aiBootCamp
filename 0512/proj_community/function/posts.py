from db import DataBase
import datetime

class Posts:
  def __init__(self, is_logged_in=False, logged_member_number=None):
    self.database = DataBase()
    self.is_logged_in = is_logged_in
    print(self.is_logged_in)
    self.logged_member_number = logged_member_number
    self.is_collect_user = False

  def is_collect_password(self): # 작성하는 사람이 해당 계정 주인인지 확인
    if self.is_logged_in == False:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
      return False
    # validation 없음
    # 🔥🔥🔥🔥🔥🔥🔥🔥🔥 지금 여기에서 안먹히고 있는데 이유를 전혀 모르겠습니다.
    print()
    again_input_userpawssword = (input('🔑 Password를 한번 더 입력해주세요 : '))
    for i in self.database.database_member:
      if self.logged_member_number == i['member_number'] and \
        i['password'] == again_input_userpawssword:
        self.is_collect_user = True
        print('🔑 password가 일치합니다.')
        return True
      else:
        print('⛔️ password가 일치하지 않습니다.')
        
  def post_write(self):  # 작성
    self.is_collect_password() 
    if self.is_collect_user == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
      return
    else:  # db 입력하는 부분
      print('---------------------------------------------')
      member_number = self.logged_member_number
      created_date = datetime.now().strftime("%Y-%m-%d")
      created_time = datetime.now().strftime("%H:%M:%S")
      title = (input('제목: '))
      print(title)
      content = (input('내용: '))
      print(content)
      print('---------------------------------------------')
      self.database.db_member(
        member_number, 
        created_date, 
        created_time, 
        title, 
        content
      )
  
  def post_inquiry(self):  # 전체 모든 목록 조회
    for i in self.database.database_posts:
      print(i)  

  def post_modify(self):  #수정
    self.is_collect_password() 
    if self.is_collect_user == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
      return
    print('---------------------------------------------')
    print("✏️ 회원님께서 수정할 수 있는 게시물을 보여드릴게요!")
    for index, value in enumerate(self.database.database_posts):
      if self.logged_member_number == value['member_number']:
        print(f"{index} : {value})")
    # validation 없음
    select = int(input('수정하고 싶은 번호를 입력해주세요'))
    # 그냥 모두 수정하는 것으로...
    self.database.database_posts[select]['modify_date'] = datetime.now().strftime("%Y-%m-%d")
    self.database.database_posts[select]['modify_time'] = datetime.now().strftime("%H:%M:%S")
    self.database.database_posts[select]['title'] = (input('tile: '))
    print(f"수정됨: {self.database.database_posts[select]['title']}")
    self.database.database_posts[select]['content'] = (input('content: '))
    print(f"수정됨: {self.database.database_posts[select]['content']}")
    print('---------------------------------------------')

  def post_delete(self):  #삭제
    self.is_collect_password() 
    if self.is_collect_user == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
      return
    for index, value in enumerate(self.database.database_posts):
      if self.logged_member_number == value['member_number']:
        print(f"{index} : {value})")
    # validation 없음
    select = int(input('수정하고 싶은 번호를 입력해주세요'))
