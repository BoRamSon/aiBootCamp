from B_DBEngine import theEngine
from sqlalchemy import text
from C_ScoreData import ScoreData


class ScoreManager:
    def __init__(self):
        self.scoreList = []

    def output(self):
        sql = "select * from tb_score"
        self.getList(sql)
        for s in self.scoreList:
            s.output()  # ???????

    def getList(self, sql):
        with theEngine.begin() as conn:
            result = conn.execute(text(sql))
            for (
                r
            ) in (
                result.mappings().all()
            ):  # 근데 이거는 DB 것을 가져올 때나 dict로 바꾸는 거잖아
                s = ScoreData(r["sname"], r["kor"], r["eng"], r["mat"])
                self.scoreList.append(s)
        return

    # insert 직접 만들기
    def insert_data(self):
        # sname = input("이름 : ")
        # kor = int(input("국어 : "))
        # eng = int(input("영어 : "))
        # mat = int(input("수학 : "))
        sname = "재사용"
        kor = 10
        eng = 20
        mat = 30
        s = ScoreData(sname, kor, eng, mat)
        score_insert_taget = [s.make_dict()]
        print(f"print: {score_insert_taget}")

        with theEngine.connect() as conn:
            sql = """
                insert into tb_score(sname, kor, eng, mat, regdate)
                values(:sname, :kor, :eng, :mat, now())
            """
            # sql = """
            #     insert into tb_score(sname, kor, eng, mat, total, average, grade)
            #     values(:sname, :kor, :eng, :mat, :total, :average, :grade)
            # """  # 없잖아...........
            conn.execute(text(sql), score_insert_taget)
            conn.commit()

    def statistics(self):
        # 문제 - 통계를 내보시오~
        # 전체인원 : 45
        # 수: 12
        # 우:
        # 미:
        # 양:
        with theEngine.begin() as conn:
            sql = """
                SELECT '전체' grade,  count(*) cnt
                FROM tb_score
                union all
                SELECT grade, count(*) cnt
                FROM 
                    (SELECT 
                        CASE  
                            WHEN (kor+eng+mat)/3 >= 90 THEN '수'
                            WHEN (kor+eng+mat)/3 >= 80 THEN '우'
                            WHEN (kor+eng+mat)/3 >= 70 THEN '미'
                            WHEN (kor+eng+mat)/3 >= 60 THEN '양'
                            ELSE '가'
                        END AS grade
                    FROM tb_score) A
                GROUP BY grade
                ORDER BY field(grade, '전체', '수', '우', '미', '양', '가');
            """
            result = conn.execute(text(sql)).mappings().all()  # dict로 가져온다.
            for i in result:
                print(f"{i['grade']} : {i['cnt']}명")


if __name__ == "__main__":
    sm = ScoreManager()
    sm.statistics()
