from db import DataBase
from function.sign import Sign
from function.posts import Posts

class CommunityManger:
  def __init__(self):
    self.database = DataBase()
    self.db_member_dict_list = [{
      'member_number': '9999',
      'id': 'admin', 
      'pw': 'admin', 
      'name': '관리자', 
      'phone': '010-1234-5678', 
      'email': 'admin@example.com'
    }]
    self.db_post_dict_list = []
    self.member_number_set = set()
    self.sign = Sign(self.member_number_set)
    self.is_admin_logged_in = False
    self.is_logged_in = False
    self.logged_member_number = None
    self.posts = Posts(self.is_logged_in, self.logged_member_number)

  def record_member_num(self):
    member_number_set2 = set()
    for i in self.db_member_dict_list:
      member_number_set2.add(i['member_number'])
    self.member_number_set = member_number_set2
    self.sign = Sign(self.member_number_set)

  def display(self):
    if self.is_logged_in == False:
      print("\n1. 회원가입")
      print("2. 로그인")
    if self.is_logged_in or self.is_admin_logged_in:
      print("\n3. 개인정보 조회")
      print("4. 개인정보 수정")
      print("5. 회원 탈퇴")
      print("6. 로그아웃")
      print("7. 게시글 작성")
      print("8. 게시글 전체 목록")
      print("9. 게시글 읽기")
      print("10. 게시글 수정")
      print("11. 게시글 삭제")
    if self.is_admin_logged_in:
      print("12. [admin] 전체 회원 조회")
    print("0. 종료")

  def start(self):  
    while True:
      self.display()
      select = input("🔢 번호 선택: ")

      if select == "1":    # 회원가입
        self.db_member_dict_list.append(self.sign.sign_up())
        print(f"(✅확인용) 현재 입력되어있는 회원 리스트 : {self.db_member_dict_list}")
        self.record_member_num()
        print(f"(✅확인용) 회원번호 기록여부 : {self.member_number_set}")

      elif select == "2":  # 로그인
        self.is_admin_logged_in, self.is_logged_in, self.logged_member_number = self.sign.sign_in(
          self.db_member_dict_list, self.is_admin_logged_in, self.is_logged_in, self.logged_member_number
        )
        print(f"(✅확인용) 로그인 여부 =   <admin login> {self.is_admin_logged_in}  |  <일반 login> {self.is_logged_in}")
        self.posts = Posts(self.is_logged_in, self.logged_member_number)

      elif select == "3":  # 개인정보 조회
        self.sign.list_person_info(
          self.db_member_dict_list, self.is_logged_in, self.logged_member_number
        )

      elif select == "4":  # 개인정보 수정
        self.db_member_dict_list = self.sign.modify_person_info(
          self.db_member_dict_list, self.is_logged_in, self.logged_member_number
        )
        print(f"(✅확인용) 현재 수정 이후 회원 리스트 : {self.db_member_dict_list}")

      elif select == "5":  # 회원 탈퇴
        self.db_member_dict_list, self.is_logged_in = self.sign.quit_member(
          self.db_member_dict_list, self.is_logged_in, self.logged_member_number
        )
        print(f"(✅확인용) 현재 탈퇴 이후 회원 리스트 : {self.db_member_dict_list}")

      elif select == "6":  # 로그아웃
        self.is_admin_logged_in, self.is_logged_in, self.logged_member_number = self.sign.sign_out()
        self.posts = Posts(self.is_logged_in, self.logged_member_number)

      elif select == "7":  # 게시글 작성
        post_write_result = self.posts.post_write(
          self.logged_member_number, self.db_member_dict_list, self.db_post_dict_list
          )
        if post_write_result is not None:
          self.db_post_dict_list.append(post_write_result)
        print(f"(✅확인용) 현재 입력되어있는 게시글 리스트 : {self.db_post_dict_list}")

      elif select == "8":  # 게시글 목록 조회
        self.posts.inquiry_post(self.db_post_dict_list)

      elif select == "9":  # 게시글 읽기
        self.db_post_dict_list = self.posts.read_post(self.db_post_dict_list)

      elif select == "10":  # 게시글 수정
        self.db_post_dict_list = self.posts.modify_post(
          self.db_member_dict_list, self.db_post_dict_list, self.logged_member_number
        )
        print(f"(✅확인용) 현재 게시글이 현황 : {self.db_post_dict_list}")

      elif select == "11":  # 게시글 삭제
        self.db_post_dict_list = self.posts.delete_post(
          self.db_member_dict_list, self.db_post_dict_list, self.logged_member_number
        )
        print(f"(✅확인용) 현재 게시글이 현황 : {self.db_post_dict_list}")

      elif select == "12" and self.is_admin_logged_in == True:  # [admin] 회원관리
        print("\n< 🚨 [admin] 전체 회원 조회 >")
        for index, i in enumerate(self.db_member_dict_list):
          print('---------------------------------------------')  
          print(f"\'{index +1}번 | name: {i['name']}\' | member_number: {i['member_number']}")
          print(f"ID: {i['id']} | PW: {i['pw']}")
          print(f"phone: {i['phone']} | email: {i['email']}")
          print('---------------------------------------------')  

      elif select == "0":
        return print("👋 bye, bye..  종료합니다.\n")
      
      else:
        print("올바른 번호를 입력하세요.")

if __name__ == "__main__":
    c = CommunityManger()
    c.start()
