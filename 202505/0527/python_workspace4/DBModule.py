import pymysql
import pymysql.cursors


class Database:
    def __init__(self):
        # db 연결
        self.conn = self.mysql_conn()
        # cursor(커서)는 DB와 연결된 상태에서 SQL을 실행하고, 결과를 가져오는 객체
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    # init 해줄것을 이렇게 만들었습니다.
    def mysql_conn(self):
        conn = pymysql.connect(
            # 원래는 이 값들도 별도 input으로 넣어줘야 좋습니다.
            host="localhost",
            user="root",
            password="",
            db="project1",
            port=3306,
        )
        print("접속 성공")
        return conn

    # execute = 실행하다.
    # insert, update, delete 할 때 사용할 수 있게 이렇게 만들었다.
    def execute(self, query, args=()):
        # args - tuple 기본값
        print(args)
        self.cursor.execute(query, args)
        self.conn.commit()

    # 데이터 딱 1개만 가져오기
    # scalar 쿼리 포함,  select count(*) from tb_member
    def executeOne(self, query, args=()):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row  # 결과를 반환해야하낟. 첫번째 레코드값 하나만 가져간다.

    # 데이터 여러개 가져오기
    def executeAll(self, query, args=()):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return rows

    # 닫기
    def close(self):
        if self.conn.open:
            self.conn.close


if __name__ == "__main__":
    m = Database()
