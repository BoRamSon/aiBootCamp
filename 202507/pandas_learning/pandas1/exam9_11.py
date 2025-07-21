import pandas as pd
 
data = {
    'name':['홍길동', '임꺽정', '장길산', '홍경래', '이상민', '김수경'],
    'work_time':[40, 30, 20, 42, 28, 35],
    'per_pay':[1000, 9000, 9700, 8500, 12000, 20000],
}


print()
df = pd.DataFrame(data)
df['pay'] = df['work_time'] * df['per_pay']
print(df)
print()

