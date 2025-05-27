import pymysql
import pymysql.cursors

conn = pymysql.connect(
    host="localhost",  # MySQL 서버 주소 (로컬 PC면 'localhost' 또는 '127.0.0.1')
    user="root",  # MySQL 사용자 이름 (기본은 'root')
    password="",  # MySQL 사용자 비밀번호 (여기에 실제 패스워드를 입력해야 함)
    db="mydb",  # 접속하려는 데이터베이스 이름 (예: 'mydb')
    port=3306,  # MySQL 포트 번호 (기본값 3306)
)

# 연결이 성공되었으면 다음 메시지를 출력한다.
print("접속 성공")

# 연결된 데이터베이스에서 SQL 명령을 실행할 수 있는 '커서'를 만든다.
cursor = conn.cursor()

# ==============================================================
# ???? 미완성.....
# print("======== SQL ========")
# cousor = conn.cursor(pymysql.cursors.DictCursor)
# sql = "select empno, ename, sal from emp"
# cursor.execute(sql)
# rows = cursor.fetchall()
# print("데이터 개수", len(rows))
# for row in rows:
#     print(row["EMPNO"], row["ENAME"], row["SAL"])


# ==============================================================
print("======== INSERT ========")
# sql = """
#   insert into emp(empno, ename, sal)
#   values(%s, %s, %d)
# """

cursor = conn.cursor(pymysql.cursors.DictCursor)  # 딕셔너리로 쓰기 위해서 정의.
# cursor.execute(sql, (9000, "백승빈", 6000))   # 근데 이렇게 하면 한번밖에 못들어갑니다.
# 고쳐보기
# max함수가 데이터가 한건도 없을 때 null을 갖고 온다.
sql = "select ifnull(max(empno),0 )+1 id from emp"  # id는 alicing입니다.
cursor.execute(sql)
row = cursor.fetchone()
print(row)
sql = """
  insert into emp(empno, ename, sal)
  values(%s, %s, %s)
"""
cursor.execute(sql, (row["id"], "백승빈", 6000))
conn.commit()  # 연결 객체로 커밋을 반드시 해줘야 데이터에 반영이 된다.


# 데이터베이스 연결을 종료한다.
conn.close()
