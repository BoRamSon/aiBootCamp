from db import DataBase
from function.sign import Sign
from function.posts import Posts

class CommunityManger:
    def __init__(self):
        self.database = DataBase()
        self.sign = Sign()
        self.is_logged_in = False
        self.logged_member_number = None
        self.posts = Posts(self.is_logged_in, self.logged_member_number)

    def display(self):
        print("\n1. 회원가입")
        print("2. 로그인")
        if self.is_logged_in:
            print("3. 회원정보 조회")
            print("4. 로그아웃")
            print("5. 게시글 작성")
            print("6. 게시글 전체 목록")
            print("7. 게시글 보기")  # 생각보다 어려울 것 같다.
            print("8. 게시글 수정")
            print("9. 게시글 삭제")
        print("0. 종료")
  
    def start(self):  
        while True:
            self.display()
            select = input("번호 선택: ")
            if select == "1":
                # 회원가입
                self.sign.sign_up()
            elif select == "2":  # 로그인
                self.is_logged_in, self.logged_member_number = self.sign.sign_in()
                self.posts = Posts(self.is_logged_in, self.logged_member_number)
            elif select == "3":  # 회원정보 조회
                self.sign.list_person_info()
            elif select == "4":  # 로그아웃
                self.is_logged_in, self.logged_member_number = self.sign.sign_in()
                self.posts = Posts(self.is_logged_in, self.logged_member_number)
            elif select == "5":  # 게시글 작성
                self.posts.post_write()
            elif select == "6":  # 게시글 목록 조회
                self.posts.post_inquiry()
            elif select == "7":  # 게시글 보기
                # self.posts.post_write()
                print('아직 없습니다.')
            elif select == "8":  # 게시글 수정
                self.posts.post_modify()
                

            # elif select == "3":
            #     if current_user_id:  # 로그인된 경우에만 게시글 목록 보기
            #         list_posts()
            #     else:
            #         print("로그인이 필요합니다.")

            # elif select == "4":
            #     if current_user_id:  # 로그인된 경우에만 게시글 작성
            #         title = input("제목: ")
            #         content = input("내용: ")
            #         write_post(current_user_id, title, content)
            #     else:
            #         print("로그인이 필요합니다.")

            # elif select == "5":
            #     if current_user_id:  # 로그인된 경우에만 게시글 보기
            #         post_id = int(input("게시글 번호 입력: "))
            #         read_post(post_id)
            #     else:
            #         print("로그인이 필요합니다.")

            # elif select == "6":
            #     if current_user_id:  # 로그인된 경우에만 게시글 수정
            #         post_id = int(input("게시글 번호: "))
            #         password = input("비밀번호 확인: ")
            #         new_title = input("새 제목: ")
            #         new_content = input("새 내용: ")
            #         edit_post(post_id, current_user_id, password, new_title, new_content)
            #     else:
            #         print("로그인이 필요합니다.")

            # elif select == "7":
            #     if current_user_id:  # 로그인된 경우에만 게시글 삭제
            #         post_id = int(input("게시글 번호: "))
            #         password = input("비밀번호 확인: ")
            #         delete_post(post_id, current_user_id, password)
            #     else:
            #         print("로그인이 필요합니다.")

            elif select == "0":
                print("🚪 종료합니다.")
                break

            else:
                print("올바른 번호를 입력하세요.")


if __name__ == "__main__":
    c = CommunityManger()
    c.start()