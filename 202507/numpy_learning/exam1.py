#내장리스트.py 


#한바구니에 작두콩과 서리태가 있다 -분리하자 
a = [-3, -5, 10, 9, 8, 12, 15, 27, -5, 26]
#음수리스트 양수리스트 
#리스트 분리 - 작두콩 담을 바구니 먼저 만들기 
negList = list()     # negList = [] 동일한 문법 새로 list개체를 만들겠다 
for item in a: #콩바구니로부터 콩을 하나씩 가져와라 
    if item < 0:
        negList.append(item) #작두콩 바구니에 작두콩을 담아라 


posList = list()  #서리태 바구니 준비 
for item in a:    #콩을 하나씩 줏어러 
    if item>=0:   #서리태면 
        posList.append(item) #서리태 바구니에 담자 

print(negList)
print(posList)



#내장리스트 
#   [  변수명  for 변수명 in 리스트명 if 조건식] 

negList = [ x for x in a if x<0 ]
posList = [ x for x in a if x>=0]

print(negList)
print(posList)


#문제, 짝수,홀수리스트 분리  
evenList = [x for x in a if x%2==0]  #2로 나누어서 나머지가 0인 숫자 - 짝수 
oddList = [x for x in a if x%2==1]   #2로 나누어서 나머지가 1인 숫자 - 홀수 

print(evenList)
print(oddList)


#문제 : words 를 분리,  table에 단어 있는 것과 
#      table에 포함되지 않는 단어 분리 
table =["호박", "고구마", "감자", "양배추"]
words = ["호박", "감자", "토마토", "고구마", "상추", "베리"]

inList = [ k for k in words  if k in table]
outList = [ w for w in words  if w not in table] 

print( inList)
print( outList)
"""
m = {"호박":2000, "감자":4000, "고구마":3000, "양파":1000}
print(m.keys())
selkeys = [  m[key] for key in m.keys() if key in table]

table2 = [2000, 4000]
selkeys = [  key for key in m.values() if key in table2]
print(selkeys)


#파이썬과 numpy의 차이점--분산구하기 
#분산 (평균값 - 오차) 의 제곱의 합/개수
#데이터의 흩어짐의 정도를 보고자 한다. 
def myVar( data ):
    mean = sum(data)/len(data)
    var_sum=0
    for item in data:
        var_sum += (mean-item)**2 

    return var_sum/len(data)

print( myVar( [1,3,5,7,9] ))

import numpy as np 
print( np.var( np.array( [1,3,5,7,9] )))
"""