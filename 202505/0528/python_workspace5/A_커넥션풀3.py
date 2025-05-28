from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


class Alchemy:
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:qhfkal0513@localhost:3306/mydb",
            pool_size=10,  # 최대 연결 수
            max_overflow=5,  # 초과 시 추가 연결 수
            pool_recycle=3600,  # 재활용 시간
        )

    # ------------------------------------
    # 1. 모든 데이터 가져오기
    def read_all_data(self):
        # 1. 데이터 가져오기
        # 데이터베이스 연결 객체(engine)를 통해 connect()를 호출하여 연결을 시작
        # 이게 끝나면 자동으로 닫힘.
        with self.engine.connect() as conn:
            sql = """
                select empno, ename, sal
                from emp
            """
            # [방법 1] 튜플 형식으로 결과 가져오기
            # SQL 실행: text(sql)로 SQL 문자열을 실행 가능한 객체로 변환
            result = conn.execute(text(sql))
            # result.all() → 전체 결과를 리스트 형태로 가져옴 (각 행은 튜플)
            # for now in result.all():
            #     print(now)  # 예: (7369, 'SMITH', 800)

            # [방법 2] 딕셔너리 형식으로 결과 가져오기
            # 다시 SQL 실행 (주의: 위의 result는 이미 한 번 소모되었기 때문에 새로 실행해야 함)
            result = conn.execute(text(sql))
            # result.mappings() → 각 행을 딕셔너리처럼 가져올 수 있게 함
            # .all()로 전체 결과 리스트로 변환
            rows = result.mappings().all()
            # 각 row는 Mapping 타입 (dict처럼 작동), dict(row)로 실제 딕셔너리로 변환 가능
            # for row in rows:
            #     print(dict(row))  # 예: {'empno': 7369, 'ename': 'SMITH', 'sal': 800}

    def read_all_data2(self):
        with self.engine.connect() as conn:
            sql = """
                select empno, ename, sal
                from emp
            """
            result = conn.execute(text(sql))

            for now in result.all():
                print(now)

    # ------------------------------------
    # 2. 특정 데이터 가져오기 / 검색어를 전달할 때
    def read_specific_date(self):
        with self.engine.connect() as conn:
            ename = "백승빈"  # 🔥 나중에 input 받으삼

            sql = """
                select empno, ename, sal
                from emp
                where ename = :name
            """

            # :name
            result = conn.execute(text(sql), [{"name": ename}])
            # print(list(result)) # 파악만 하고 주석처리
            temp = result.all()  # 한번 읽으면 없어지니깐, 복사해서 계속 가지고 있어라~
            # 왜 자꾸 all()을 붙이는가????  =  쿼리 결과를 "전부 리스트로 가져오는 함수
            print(temp)
            # if len(temp) == 0:
            #     print("없음")
            # else:
            #     for now in temp:
            #         print(now)

    # ------------------------------------
    # 3. insert
    def insert_data(self):
        with self.engine.connect() as conn:
            sql = """
                select ifnull(max(empno), 0) + 1
                from emp
            """
            result = conn.execute(text(sql))  # [()] 이렇게 tuple로 옵니다.

            empno = result.all()[0][0]

            sql = """
                insert into emp(empno, ename, sal)
                values(:empno, :ename, :sal)
            """

            conn.execute(
                text(sql),
                [{"empno": empno, "ename": "테스트" + str(empno), "sal": 9000}],
            )

            conn.commit()

    # ------------------------------------
    def start(self):
        while True:
            print("1.전체보기 | 2.특정데이터검색 | 3.데이터넣기 |")
            select = input("메뉴를 선택해주세요 : ")
            if select == "1":
                self.read_all_data()
            if select == "2":
                self.read_specific_date()
            if select == "3":
                self.insert_data()
            if select == "4":
                pass
            if select == "0":
                break


if __name__ == "__main__":
    s = Alchemy()
    s.start()
