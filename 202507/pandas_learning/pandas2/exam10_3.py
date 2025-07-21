#파일명 : exam10_3.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/score_header.csv", header=3)
print(data)

print("컬럼명 : ", data.columns)
print("인덱스 : ", data.index)

#총점, 평균 구하기 
data['total'] = data['kor'] + data['eng']+data['mat']
data['avg'] = data['total']/3

#excel이 인코딩을 cp949를 사용한다. 한글 안깨지고 엑셀서 열어보려면 cp949로 인코딩을 해야 한다 
#index = False 옵션이 없으면 index까지 저장되면서 필드가 늘어난다. 
data.to_csv("score_result.csv",  mode='w', encoding="cp949", index=False)
print( data )