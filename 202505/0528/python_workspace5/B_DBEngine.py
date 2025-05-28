from sqlalchemy import create_engine

theEngine = create_engine(
    "mysql+pymysql://root:비밀번호@localhost:3306/mydb",
    pool_size=10,  # 최대 연결 수
    max_overflow=5,  # 초과 시 추가 연결 수
    pool_recycle=3600,  # 재활용 시간
)
