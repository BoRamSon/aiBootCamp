import pymysql
import pymysql.cursors


class MysqlBasic:
    def __init__(self):
        self.conn = self.mysql_conn()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def mysql_conn(self):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="mydb",
            port=3306,
        )

        print("접속 성공")

        return conn

    def all_view_data(self):

        sql = """
            SELECT
                id, sname, kor, eng, mat, 
                (kor+eng+mat) AS total,
                (kor+eng+mat)/3 AS average,
                date_format(regdate, '%Y-%m-%d %H:%i') regdate
            FROM tb_score;
        """
        print(sql)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print("데이터 개수", len(rows))
        for row in rows:
            print(
                row["id"],
                row["sname"],
                row["kor"],
                row["eng"],
                row["mat"],
                row["total"],
                row["average"],
            )
        print()

    def insert_data(self):

        name = input("이름 : ")
        kor = input("국어 : ")
        eng = input("영어 : ")
        mat = input("수학 : ")

        sql = """
            INSERT INTO tb_score(sname, kor,  eng, mat, regdate)
            values(%s, %s,%s,%s, now())
        """
        self.cursor.execute(sql, (name, kor, eng, mat))
        self.conn.commit()
        print("INSERT 완료")

        self.cursor.execute("SELECT * FROM tb_score ORDER BY id DESC LIMIT 1")
        row = self.cursor.fetchone()
        print("방금 추가된 데이터:", row)
        print()

    def update_data(self):

        self.all_view_data()

        id = input("수정할 id 입력 : ")
        sname = input("이름 : ")
        kor = input("국어 : ")
        eng = input("영어 : ")
        mat = input("수학 : ")

        sql = """
            UPDATE tb_score
            SET 
                sname = %s,
                kor = %s,
                eng = %s,
                mat = %s
            WHERE id = %s
        """
        self.cursor.execute(sql, (sname, kor, eng, mat, id))
        self.conn.commit()
        print("수정 완료")

        self.all_view_data()
        print()

    def delete_data(self):

        self.all_view_data()

        sname = input("삭제할 이름을 입력하세요 : ")
        sql = """
            DELETE FROM tb_score WHERE sname = %s
        """
        self.cursor.execute(sql, sname)
        self.conn.commit()
        print("삭제 완료")

        self.all_view_data()
        print()

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
