#파일명 : exam10_3.py

import pandas as pd 

data = pd.read_excel("./data/score.xlsx")

data['total'] = data['kor'] + data['eng']+data['mat']
data['avg'] = data['total']/3
print(data)

data.to_excel("score_result1.xlsx")
data.to_excel("score_result2.xlsx", index=False)
