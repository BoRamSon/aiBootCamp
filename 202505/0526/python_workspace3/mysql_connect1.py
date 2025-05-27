import pymysql
import pymysql.cursors


# MySQL 서버에 연결을 설정한다.
# pymysql.connect()는 MySQL 서버에 접속할 때 필요한 정보들을 넣는다.
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
print("======== 기본적으로 전체 tuple로 가져온다 ========")

# SQL 쿼리문을 문자열로 작성한다.
# 여기서는 'emp' 테이블의 모든 데이터를 가져오는 쿼리이다.
sql = "select * from emp"

# 작성한 SQL 쿼리를 실행한다.
cursor.execute(sql)
# 이 시점에서 select 결과는 cursor 내부에 임시 저장된다.


# cursor에 저장된 결과 전체를 가져온다.
rows = cursor.fetchall()

# 결과를 한 줄씩 반복하면서 출력한다.
for row in rows:
    print(type(row), row)
    # 각 row는 tuple 형태로 출력된다. (예: (8001, '홍길동', 'MANAGER', ...))


# ==============================================================
print("======== 하나만 가져오기 ========")
sql = "select * from emp where empno=8001"
cursor.execute(sql)
row = cursor.fetchone()
print(row)


# ==============================================================
print("======== 앞에 3개만 가져오기 ========")
sql = "select * from emp where empno<8000"
cursor.execute(sql)
rows = cursor.fetchmany(3)  # 앞에 3개만
for row in rows:
    print(row)


# ==============================================================
# 데이터를 tuple 타입으로 가져오면서 인덱싱과 슬라이싱만 지원
# row["ename"]   ->   데이터를 가져올 떄 dict 타입으로 가져오기
print("======== dict type로 가져오기 ========")
cousor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)


# 데이터베이스 연결을 종료한다.
conn.close()
