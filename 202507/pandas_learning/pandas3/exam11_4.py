#파일명 : exam11_4.py
#데이터표준화
#1.결측치 나 이상치 제거 
#2.단위맞추기 - 정규화(normalization)
#머신러닝중에 서포트벡터머신, 딥러닝 
#정규화 - 수식, sklearn 라이브러가 정규화 클래스를 제공하고 있는데 

import pandas as pd 

data = pd.read_csv('./data/auto-mpg.csv')
print(data.info()) #요약정보 
print(data.head()) #앞에서 5개 

#컬럼명 변경하기 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.head())

#정규화 : 1이 넘어 가는 값을 갖는 데이터들을 0~1 사이에 머무르도록 
#(정규화하고자 하는 값 - 데이터 값들 중 최소값) / (데이터 값들 중 최대값 - 데이터 값들 중 최소값)
data['mpg2'] = (data['mpg'] - data['mpg'].min())/(data['mpg'].max()-data['mpg'].min())
print(data) #['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model', 'mpg2']

#단위환산 - 한국 단위로 환산하기 
mpg_unit = 1.60934 / 3.78541

data['kpl'] = (data['mpg'] * mpg_unit).round(2)
print( data.head() )




