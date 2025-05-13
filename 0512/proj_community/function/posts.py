from db import DataBase
import datetime

class Posts:
  def __init__(self, is_logged_in=False, logged_member_number=None):
    self.database = DataBase()
    self.is_logged_in = is_logged_in
    self.logged_member_number = logged_member_number
    self.is_collect_user = False

  def is_collect_password(self, db_member_dict_list): # 작성하는 사람이 해당 계정 주인인지 확인
    if self.is_logged_in == False:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
      return False
    # validation 없음
    again_input_userpassword = (input('🔑 Password를 한번 더 입력해주세요 : '))
    for i in db_member_dict_list:
      if self.logged_member_number == i['member_number'] and \
        i['pw'] == again_input_userpassword:
        self.is_collect_user = True
        print('🔑 password가 일치합니다.')
        return True
      else:
        print('⛔️ password가 일치하지 않습니다.')
        
  def post_write(self, db_member_dict_list, db_post_dict_list):  # 작성
    self.is_collect_password(db_member_dict_list) 
    if self.is_collect_user == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
      return
    else:   # post db 입력하는 부분
      print('---------------------------------------------')
      writing_number = len(db_post_dict_list) + 1
      member_number = self.logged_member_number
      created_date = datetime.datetime.now().strftime("%Y-%m-%d")
      created_time = datetime.datetime.now().strftime("%H:%M:%S")
      title = (input('제목: '))
      print(title)
      content = (input('내용: '))
      print(content)
      print('---------------------------------------------')
      return self.database.db_posts(
        writing_number,
        member_number, 
        created_date, 
        created_time, 
        title, 
        content
      )
  
  def inquiry_post(self, db_post_dict_list):   # 전체 모든 목록 조회
    for i in db_post_dict_list:
      print(f"{i['writing_number']}번", end='\t')
      print(f"회원번호: {i['member_number']}", end='\t')
      print(f"제목: {i['title']}", end='\t')
      print(f"작성일: {i['created_date']} {i['created_time']}", end='\t')
      print(f"조회수: {i['hits']}")
      
  def read_post(self, db_post_dict_list):
    print('---------------------------------------------')
    self.inquiry_post(db_post_dict_list)
    print('---------------------------------------------')
    select = int(input('조회하고 싶은 Post 번호를 입력해주세요'))
    for i in db_post_dict_list:
      if i['writing_number'] == select:
        print(f"{i['writing_number']}번", end='\t')
        print(f"회원번호: {i['member_number']}", end='\t')
        print(f"조회수: {i['hits']}")
        print(f"작성일: {i['created_date']} {i['created_time']}")
        print(f"수정일: {i['modify_date']} {i['modify_time']}")
        print(f"제목: {i['title']}")
        print(f"내용: {i['content']}")
        print('끝')
        i['hits'] += 1     # 조회수 증가   # 🔥🔥🔥🔥🔥 이게... db_post_dict_list를 update 해야하는데요
        break
    print('---------------------------------------------')
    return db_post_dict_list 

  # 🔥🔥🔥🔥🔥
  def modify_post(self, db_post_dict_list, logged_member_number):   #수정
    if self.is_logged_in == False:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
      return
    self.is_collect_password()
    if self.is_collect_user == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
      return
    print('---------------------------------------------')
    print("✏️ 회원님께서 수정할 수 있는 게시물을 보여드릴게요!")
    for i in db_post_dict_list:
      if logged_member_number == i['member_number']:
        print(f"{i['writing_number']}번", end='\t')
        print(f"회원번호: {i['member_number']}", end='\t')
        print(f"제목: {i['title']}", end='\t')
        print(f"작성일: {i['created_date']} {i['created_time']}", end='\t')
        print(f"조회수: {i['hits']}")
    
    # validation 없음
    select = int(input('수정하고 싶은 번호를 입력해주세요')) - 1

    # 🔥🔥🔥🔥🔥 여기 if 문 있어야함 회원번호가 post 회원번호와 같아야 수정을 할 수 있음
    # 그냥 모두 수정하는 것으로...
    db_post_dict_list[select]['modify_date'] = datetime.now().strftime("%Y-%m-%d")
    db_post_dict_list[select]['modify_time'] = datetime.now().strftime("%H:%M:%S")
    db_post_dict_list[select]['title'] = (input('tile: '))
    print(f"수정됨: {db_post_dict_list[select]['title']}")
    db_post_dict_list[select]['content'] = (input('content: '))
    print(f"수정됨: {db_post_dict_list[select]['content']}")
    print('---------------------------------------------')

    # return db_post_dict_list  # 🔥🔥🔥🔥🔥 여기도 이런거 있어야 한다.


  # 🔥🔥🔥🔥🔥
  def delete_post(self, db_post_dict_list, logged_member_number):  #삭제
    if self.is_logged_in == False:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
      return
    self.is_collect_password() 
    if self.is_collect_user == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
      return
    for i in db_post_dict_list:
      if logged_member_number == i['member_number']:
        print(f"{i})")

    # validation 없음
    select = int(input('수정하고 싶은 번호를 입력해주세요')) - 1

    # 🔥🔥🔥🔥🔥 삭제를 구현 시켜야합니다.
    # 삭제할 인덱스만 return 해야하는가?
    return db_post_dict_list.pop(select)   # 이거 return 되면 이게 곧 dict list 가 되게 만들면 되는것?
