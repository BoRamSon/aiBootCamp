from db import DataBase
import datetime

class Posts:
  def __init__(self, is_logged_in=False, logged_member_number=None):
    self.database = DataBase()
    self.is_logged_in = is_logged_in
    self.logged_member_number = logged_member_number
    self.is_collect_user = False

  def is_collect_password(
      self, logged_member_number, db_member_dict_list
    ): # 작성하는 사람이 해당 계정 주인인지 확인
    if self.is_logged_in == False:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
      return False
    # validation 없음
    again_input_userpassword = (input('🔑 Password를 한번 더 입력해주세요 : '))
    for i in db_member_dict_list:
      if logged_member_number == i['member_number'] and \
        i['pw'] == again_input_userpassword:
        self.is_collect_user = True
        print('🔑 password가 일치합니다.')
        return True
    print('⛔️ 비밀번호가 일치하지 않습니다.')
    return False
        
  def post_write(
      self, logged_member_number, db_member_dict_list, db_post_dict_list
    ):  # 게시물 작성
    collect_pw = self.is_collect_password(logged_member_number, db_member_dict_list) 
    if collect_pw == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
      return 
    elif collect_pw == True:
      print('---------------------------------------------')
      writing_number = len(db_post_dict_list) + 1
      member_number = self.logged_member_number
      now = datetime.datetime.now()
      created_date = now.strftime("%Y-%m-%d")
      created_time = now.strftime("%H:%M:%S")
      title = (input('제목: '))
      # print(title)
      content = (input('내용: '))
      # print(content)
      print('---------------------------------------------')
      return self.database.db_posts(
        writing_number, member_number, created_date, created_time, title, content
      )
  
  def inquiry_post(self, db_post_dict_list):   # 전체 모든 목록 조회
    print('---------------------------------------------')
    for i in db_post_dict_list:
      if i != None:
        print(f"{i['writing_number']}번 -", end='\t')
        print(f"회원번호: {i['member_number']}", end='\t')
        print(f"제목: {i['title']}", end='\t')
        print(f"작성일: {i['created_date']} {i['created_time']}", end='\t')
        print(f"조회수: {i['hits']}")
    print('---------------------------------------------')  

  def read_post(self, db_post_dict_list):
    self.inquiry_post(db_post_dict_list)
    select = int(input('𝌞 조회하고 싶은 Post 번호를 입력해주세요 : '))
    not_in_list = True
    for i in db_post_dict_list:
      if i != None and i['writing_number'] == select:
        print(f"\n{i['writing_number']}번 -", end='\t')
        print(f"회원번호: {i['member_number']}", end='\t')
        print(f"조회수: {i['hits'] + 1}")
        print(f"작성일: {i['created_date']} {i['created_time']}")
        print(f"수정일: {i['modify_date']} {i['modify_time']}")
        print(f"제목: {i['title']}")
        print(f"내용: {i['content']}")
        print(' -- 끝 --')
        i['hits'] += 1
        not_in_list = False
        break
    if not_in_list:
      print(f"⛔️ 존재하지 않는 번호를 입력하셔서 종료되었습니다. 다시 실행해주세요.")
    print('---------------------------------------------')
    return db_post_dict_list 

  def modify_post(
      self, db_member_dict_list, db_post_dict_list, logged_member_number
    ):   #수정
    collect_pw = self.is_collect_password(logged_member_number, db_member_dict_list)
    if collect_pw == False:
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
    elif len(db_post_dict_list) == 0:
      print('⛔️ 작성된 게시글이 없습니다.')
    else:
      print('---------------------------------------------')
      print("✏️ 회원님께서 수정할 수 있는 게시물을 보여드릴게요!\n")
      for i in db_post_dict_list:
        if i != None and logged_member_number == i['member_number']:
          print(f"{i['writing_number']}번", end='\t')
          print(f"회원번호: {i['member_number']}", end='\t')
          print(f"제목: {i['title']}", end='\t')
          print(f"작성일: {i['created_date']} {i['created_time']}", end='\t')
          print(f"조회수: {i['hits']}")
      # validation 없음
      select = int(input('수정하고 싶은 번호를 입력해주세요 : '))
      for i in db_post_dict_list:
        if i != None and select == i['writing_number']:
          now = datetime.datetime.now()
          i['modify_date'] = now.strftime("%Y-%m-%d")
          i['modify_time'] = now.strftime("%H:%M:%S")
          i['title'] = (input('제목: '))
          print(f"수정됨: {i['title']}")
          i['content'] = (input('내용: '))
          print(f"수정됨: {i['content']}")
          print('---------------------------------------------')
    return db_post_dict_list

  def delete_post(
      self, db_member_dict_list, db_post_dict_list, logged_member_number
    ):  #삭제
    collect_pw = self.is_collect_password(logged_member_number, db_member_dict_list)
    if collect_pw == False:   
      print('⛔️ 비밀번호를 먼저 입력하시고 시도해주세요.')
    elif len(db_post_dict_list) == 0:
      print('⛔️ 작성된 게시글이 없습니다.')
    else:
      print('---------------------------------------------')
      print("✏️ 회원님께서 삭제할 수 있는 게시물을 보여드릴게요!\n")
      for i in db_post_dict_list:
        if i != None and logged_member_number == i['member_number']:
          print(f"{i['writing_number']}번", end='\t')
          print(f"회원번호: {i['member_number']}", end='\t')
          print(f"제목: {i['title']}", end='\t')
          print(f"작성일: {i['created_date']} {i['created_time']}", end='\t')
          print(f"조회수: {i['hits']}")
      # validation 없음
      select = int(input('삭제하고 싶은 번호를 입력해주세요')) - 1
      db_post_dict_list.pop(select) 
    return db_post_dict_list
