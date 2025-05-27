from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# https://soogoonsoogoonpythonists.github.io/sqlalchemy-for-pythonist/tutorial/1.%20%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC%20%EA%B0%9C%EC%9A%94.html#%E1%84%80%E1%85%A2%E1%84%8B%E1%85%AD

# SQLAlchemyrk PyMySQL을 내부적으로 사용하며 pool 지원
engine = create_engine(
    "mysql+pymysql://root:qhfkal0513@localhost/mydb",
    pool_size=10,  # 최대 연결 수
    max_overflow=5,  # 초과 시 추가 연결 수
    pool_recycle=3600,  # 재활용 시간
)

try:
    conn = engine.connect()
    print("데이터베이스 연결 성공")
except SQLAlchemyError as e:
    print("데이터베이스 연결 실패:", e)

# ------------------------------------
# tuple로 출력
result = conn.execute(text("select * from emp"))
# for row in result:
#     print(row)

# ------------------------------------
# dict type으로 출력
rows = result.mappings().all()
for row in rows:
    print(dict(row))
conn.close()

# ------------------------------------
# 데이터 추가하기 - 파라미터 처리 방식
conn = engine.connect()
sql = text(
    """
        insert into emp (empno, ename, sal)
        values(:empno, :ename, :sal)
        """
)
conn.execute(sql, [{"empno": 10001, "ename": "우즈2", "sal": 8000}])
# 여기 dict에 여러개 넣어서 만들어도 됩니다.
conn.commit()
conn.close()
