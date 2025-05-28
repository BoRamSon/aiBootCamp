from sqlalchemy import text
from B_DBEngine import theEngine


# if __name__ == '__main__':
#   with theEngine.begin() as conn:
#     sql = "select * from emp"
#     result = conn.execute(text(sql))
#     print(result.all())
#     # all은 쿼리 결과를 "전부 리스트로 가져오는 함수"


class ScoreData:
    def __init__(self, sname="", kor=0, eng=0, mat=0, total=0, average=0, grade=""):
        self.sname = sname
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.total = total
        self.average = average
        self.grade = grade
        self.process()

    # 갑자기 추가
    def make_dict(self):
        print(
            f"dict 변경 = sname: {self.sname} kor: {self.kor} eng: {self.eng} mat: {self.mat} total: {self.total} average: {self.average} grade: {self.grade}"
        )
        return {
            "sname": self.sname,
            "kor": self.kor,
            "eng": self.eng,
            "mat": self.mat,
            "total": self.total,
            "average": self.average,
            "grade": self.grade,
        }

    def output(self):
        print(f"{self.sname}", end="\t")
        print(f"{self.kor}", end="\t")
        print(f"{self.eng}", end="\t")
        print(f"{self.mat}", end="\t")
        print(f"{self.total}", end="\t")
        print(f"{self.average}", end="\t")
        print(f"{self.grade}")

    def process(self):  # init 중심적 코딩
        self.total = self.kor + self.eng + self.mat
        self.average = self.total / 3
        if self.average >= 90:
            self.grade = "수"
        elif self.average >= 80:
            self.grade = "우"
        elif self.average >= 70:
            self.grade = "미"
        elif self.average >= 60:
            self.grade = "양"
        else:
            self.grade = "가"

    # def read_data(salf):
    #     with theEngine.begin() as conn:
    #         sql = "select * from emp"
    #         result = conn.execute(text(sql))
    #         print(result.all())  # tuple로 가져오는데
    #         # all은 쿼리 결과를 "전부 리스트로 가져오는 함수"
    #         # dict type으로 가져오고 싶다면
    #         result = conn.execute(text(sql))
    #         for r in result.mappings().all():
    #             print(row)
    #             print(dict(row))
    #             print(row['empno'])


if __name__ == "__main__":
    # s = ScoreData()
    # s.read_data()
    with theEngine.begin() as conn:
        sql = "select * from tb_score"
        result = conn.execute(text(sql))
        print(result.all())  # tuple로 가져오는데
        # all은 쿼리 결과를 "전부 리스트로 가져오는 함수"
        # dict type으로 가져오고 싶다면
        result = conn.execute(text(sql))
        for r in result.mappings().all():
            s = ScoreData(r["sname"], r["kor"], r["eng"], r["mat"])
            s.output()
