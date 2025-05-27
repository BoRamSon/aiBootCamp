# -- ======================================================
# -- <문제 풀기>
# -- 전체보기
# -- 추가 : 입력 받아서
# -- 수정
#   -- update 테이블명 set 필드1='값1', 필드2='값2' where절
# -- 삭제
#   -- delete from 테이블명 where id = 1
# -- 검색 (구현 안함)
# 마지막으로 메뉴로 선택할 수 있도록 하세요.


import pymysql
import pymysql.cursors


class MysqlBasic:
    def __init__(self):
        # MySQL server에 접속하여 데이터를 조작할 수 있다.
        self.conn = self.mysql_conn()
        # 연결된 데이터베이스에서 SQL 명령을 실행할 수 있는 '커서'를 만든다.
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

        # - <문제 풀기>
        #   - 전체보기
        #   - 추가 : 입력 받아서
        #   - 수정
        #     - update 테이블명 set 필드1='값1', 필드2='값2' where절
        #   - 삭제
        #     - delete from 테이블명 where id = 1
        #   - 검색

    def mysql_conn(self):
        conn = pymysql.connect(
            host="localhost",  # MySQL 서버 주소 (로컬 PC면 'localhost' 또는 '127.0.0.1')
            user="root",  # MySQL 사용자 이름 (기본은 'root')
            password="",  # MySQL 사용자 비밀번호 (여기에 실제 패스워드를 입력해야 함)
            db="mydb",  # 접속하려는 데이터베이스 이름 (예: 'mydb')
            port=3306,  # MySQL 포트 번호 (기본값 3306)
        )
        # 연결이 성공되었으면 다음 메시지를 출력한다.
        print("접속 성공")

        return conn

    def all_view_data(self):
        # 1. 실행할 SQL문을 문자열로 작성한다.
        # 여기서는 tb_score 테이블의 모든 행(row)을 가져오는 SELECT 문이다.
        sql = "select * from tb_score"
        # 2. cursor를 이용해 SQL문을 실행한다.
        # self.cursor는 pymysql의 DictCursor이므로 결과가 딕셔너리로 반환된다.
        self.cursor.execute(sql)
        # 3. 실행한 SELECT 쿼리 결과를 모두 가져온다.
        # fetchall()은 조회된 모든 행을 리스트로 반환한다.
        rows = self.cursor.fetchall()
        # 4. 결과 행(row)의 개수를 출력한다.
        print("데이터 개수", len(rows))
        # 5. 가져온 각 행(row)을 하나씩 출력한다.
        # row는 딕셔너리 형태이며, 예: {'id': 1, 'sname': '홍길동', 'kor': 90, ...}
        for row in rows:
            print(row)

    def insert_data(self):
        # 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
        # 여기서 input으로 db 입력 받기를 해야합니다...
        name = input("이름 : ")
        kor = input("국어 : ")
        eng = input("영어 : ")
        mat = input("수학 : ")
        # ----- insert example -----
        sql = """
          INSERT INTO tb_score(sname, kor,  eng, mat, regdate)
          values(%s, %s,%s,%s, now())
        """
        self.cursor.execute(
            sql, (name, kor, eng, mat)
        )  # 🔥 진짜 이렇게 해줘야 합니다!!!
        self.conn.commit()
        print("INSERT 완료")
        # insert 내역 확인
        self.cursor.execute("SELECT * FROM tb_score ORDER BY id DESC LIMIT 1")
        row = self.cursor.fetchone()
        print("방금 추가된 데이터:", row)

    def update_data(self):
        # 🔥 이것도 입력 받아서 수정을 해주는 방식으로 고쳐야 합니다.
        sql = """
          UPDATE tb_score
          SET mat = %s
          WHERE sname = %s
        """
        self.cursor.execute(sql, (97, "김민지"))
        self.conn.commit()
        print("수정 완료")

    def delete_data(self):
        # 🔥 이것도 입력 받아서 삭제 해주는 방식으로 고쳐야 합니다.
        # ---- 여기가 진짜 삭제되는 곳 ----
        sql = """
          DELETE FROM tb_score WHERE sname = '테스트'
        """
        self.cursor.execute(sql)
        self.conn.commit()
        print("삭제 완료")
        # 전체 리스트 파악

    # def search_data(self):
    #     sql = """
    #       SELECT
    #         sname, kor, eng, mat, (kor+eng+mat) AS total,
    #         date_format(regdate, '%Y-%m-%d %H:%i') regdate
    #       FROM tb_score;
    #     """
    #     self.cursor.execute(sql)
    #     rows = self.cursor.fetchall()
    #     print("데이터 개수", len(rows))
    #     for row in rows:
    #         print(row)

    def start(self):
        while True:
            print(f"1.전체보기  |  2.추가  |  3.수정  |  4.삭제  |  0.종료")
            select = input("🔢 번호 선택: ")

            if select == "1":
                self.all_view_data()
            elif select == "2":
                self.insert_data()
            elif select == "3":
                self.update_data()
            elif select == "4":
                self.delete_data()
            elif select == "0":
                break


if __name__ == "__main__":
    m = MysqlBasic()
    m.start()
