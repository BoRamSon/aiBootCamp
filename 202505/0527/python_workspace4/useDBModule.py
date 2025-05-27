from DBModule import Database

# cursor(커서)는 DB와 연결된 상태에서 SQL을 실행하고, 결과를 가져오는 객체


# -------------------------------------------
# 전체 출력
def output():
    db = Database()  # 객체 만들면 이미 디비 접근
    sql = "select * from tb_member"
    rows = db.excuteAll(sql)
    for row in rows:
        print(row)
    db.close()


# -------------------------------------------
# 회원가입 함수 만들기

# def member_refister():
#     db = Database()  # 객체 만들면 디비 접근
#     user_id = input("아이디 : ")
#     password = input("패스워드 : ")
#     user_name = input("이름 : ")
#     email = input("이메일 : ")
#     phone = input("전화 : ")
#     sql = """
#         INSERT INTO tb_member(user_id, password, user_name, email, phone, regdate)
#         values(%s, %s, %s, %s, %s, now())
#     """
#     db.excute(
#         sql, (user_id, password, user_name, email, phone)
#     )  # 여기 안의 괄호는 tuple을 의미합니다.


def validate_id(id):
    db = Database()  # 객체 만들면 이미 디비 접근
    sql = """
            SELECT
                user_id, password, user_name, email, phone, regdate,
                date_format(regdate, '%Y-%m-%d %H:%i') regdate
            FROM tb_member;
        """
    db.cursor.execute(sql)
    rows = db.cursor.fetchall()
    for row in rows:
        if row["user_id"] == id:
            return True
    return False


def member_register():
    db = Database()  # 객체 만들면 이미 디비 접근
    user_id = input("아이디 : ")
    if validate_id(user_id) == True:
        return print("🚫 이미 존재하는 ID입니다. 다시 실행해주세요.")
    else:
        password = input("패스워드 : ")
        user_name = input("이름 : ")
        email = input("이메일 : ")
        phone = input("전화 : ")
        sql = """
                INSERT INTO tb_member(user_id, password, user_name, email, phone, regdate)
                values(%s, %s, %s, %s, %s, now())
            """
        db.excute(
            sql, (user_id, password, user_name, email, phone)
        )  # 여기 안의 괄호는 tuple을 의미합니다.
