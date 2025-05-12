from db import DataBase
import random

class Sign:
  def __init__(self):
    self.database = DataBase()
    self.sign_up_count = 0
    self.is_logged_in = False
    self.logged_member_number = None

  def sign_up(self):
    # validation 없음
    member_number = random.sample(range(1000, 9999), 1)
    userid = (input('가입 ID: '))
    userpawssword = (input('가입 Password: '))
    name = (input('이름: '))
    phone = (input('전화번호: '))
    email = (input('이메일: '))
    self.database.db_member(member_number, userid, userpawssword, name, phone, email)
    self.sign_up_count += 1
    print('🙋🏻‍♀️ 회원가입이 완료 되었습니다.')

  def sign_in(self):
    if self.sign_up_count == 0:
      print('⛔️ 회원가입을 먼저 해주세요.')
      return
    # validation 없음
    userid = (input('ID : '))
    userpawssword = (input('Password : '))
    for i in self.database.database_member:
      if i['id'] == userid and i['pw'] == userpawssword:
        self.is_logged_in = True
        self.logged_member_number = i['member_number']
        print('🔑 성공적으로 로그인 되었습니다.')
      else:
        print('⛔️ 로그인에 실패하였습니다.')
    return self.is_logged_in, self.logged_member_number

  def sign_out(self):
    self.is_logged_in = False
    self.logged_member_number = ''
    return self.is_logged_in, self.logged_member_number

  def list_person_info(self):
    print('---------------------------------')
    print("🔍 회원님의 정보를 검색중입니다.")
    for i in self.database.database_member:
      if i['member_number'] == self.logged_member_number:
        print(f"{i['name']}님의 정보입니다.")
        print(f"회원번호: {i['member_number']} | ID: {i['id']} | PW: {i['pw']}")
        print(f"핸드폰: {i['phone']} | 이메일: {i['email']}")
    if self.logged_member_number == None:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
    print('---------------------------------')
        