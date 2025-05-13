from db import DataBase
import random

class Sign:
  def __init__(self, member_number_set):
    self.database = DataBase()  
    self.member_number_set = member_number_set   # 만들어진 회원번호 set을 받아옵니다.

  def make_member_number(self):   # 회원 가입 시 회원번호 4자리를 랜덤으로 생성함 / 중복은 생성하지 못함
    while True:
      random_member_number = random.randint(1000, 9999)
      if random_member_number not in self.member_number_set:
        self.member_number_set.add(random_member_number)
        return random_member_number

  def sign_up(self): 
    member_number = self.make_member_number() 
    # validation 없음
    userid = (input('가입 ID: '))
    userpawssword = (input('가입 Password: '))
    name = (input('이름: '))
    phone = (input('전화번호: '))
    email = (input('이메일: '))
    print('🙋🏻‍♀️ 회원가입이 완료 되었습니다.')
    return self.database.db_member(member_number, userid, userpawssword, name, phone, email)

  def sign_in(self, db_member_dict_list, is_logged, logged_member):
    if len(db_member_dict_list) == 0:
      print('⛔️ 회원가입을 먼저 진행해주세요.')
      return False, None
    if is_logged == True:
      print('⛔️ 이미 로그인 되어있습니다. 로그아웃을 먼저 해주세요.')
      return is_logged, logged_member
    # validation 없음
    userid = (input('ID : '))
    userpawssword = (input('Password : '))
    for i in db_member_dict_list:
      if i['id'] == userid and i['pw'] == userpawssword:
        is_logged_in = True
        logged_member_number = i['member_number']
        print('🔑 성공적으로 로그인 되었습니다.')
      else:
        print('⛔️ 로그인에 실패하였습니다.')
    return is_logged_in, logged_member_number
  
  def list_person_info(self, db_member_dict_list, is_logged_in, logged_member_number):
    if is_logged_in == False:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
      return
    print('------------------------------------------')
    print("🔍 회원님의 정보를 검색중입니다.\n")
    for i in db_member_dict_list:
      if i['member_number'] == logged_member_number:
        print(f"\'{i['name']}\'님의 정보입니다.")
        print(f"회원번호: {i['member_number']} | ID: {i['id']} | PW: {i['pw']}")
        print(f"핸드폰: {i['phone']} | 이메일: {i['email']}")
    print('------------------------------------------')

  def modify_person_info(self, db_member_dict_list, is_logged_in, logged_member_number):
    if is_logged_in == False:
      return print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
    print('------------------------------------------')
    print('✏️ 회원님의 정보를 수정합니다.')
    for i in db_member_dict_list:
      if logged_member_number == i['member_number']:
        print(f"\'name: {i['name']}\' | member_number: {i['member_number']}")
        print(f"ID: {i['id']} | PW: {i['pw']}")
        print(f"phone: {i['phone']} | email: {i['email']}")

        # validation 없음
        select = input('변경할 것을 입력해주세요 : ')
        new_value = input(f'{select}에 대해서 변경할 내용을 입력하세요 : ')
        i[select] = new_value  
        print('✏️ 회원님의 정보 수정이 완료되었습니다.')
        print('------------------------------------------')
        break
    return db_member_dict_list

  def quit_member(self, db_member_dict_list, is_logged_in, logged_member_number):
    if is_logged_in == False:
      print('⛔️ 로그인 상태가 아닙니다. 먼저 로그인 해주세요.')
      return
    print('------------------------------------------')
    print('⍈ 회원탈퇴를 진행합니다.')
    for i in db_member_dict_list:
      if logged_member_number == i['member_number']:
        print(f"\'name: {i['name']}\' | member_number: {i['member_number']}")
        select = input('정말로 회원을 탈퇴하시겠습니까? (Y / N) : ')
        if select == 'Y' or select == 'y':
          db_member_dict_list.remove(i)
          print('⍈ 회원탈퇴가 성공적으로 이루어졌습니다.')
          print('------------------------------------------')
          break
        else:
          print('⍈ 회원탈퇴가 취소되었습니다.')
          print('------------------------------------------')
          break
    return db_member_dict_list



  def sign_out(self):
    is_logged_in = False
    logged_member_number = None
    print('------------------------------------------')
    print('🔑 로그아웃 되었습니다.')
    print('------------------------------------------')
    return is_logged_in, logged_member_number


        