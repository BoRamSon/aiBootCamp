a = ["탕수육", "치킨", "두루치기", "콩국수", "회냉면"]

#복사 - 얕은 카피 
#파이썬의 모든 변수는 참조(주소, 번지)만 저장한다
#실제 데이터는 heap 공간이라는 곳에 두고 만들어진 데이터의 
#주소(참조,번지) 만 변수에 저장한다  그래서 모든 변수가 
#특정 타입의 변수만 저장하는게 아니고 모든 타입의 객체를 다 
#저장할 수 있다. (c언어라면 모두 포인터형 변수임)
#  ["탕수육", "치킨", "두루치기", "콩국수", "회냉면"] 이 공간은
#  힙에 있고 변수 a에는 이 공간 주소값만 저장 
# b = a 를 하면 b에는 a의 주소만 저장 즉, 두 변수는 
# 같은 데이터 공간을 공유한다 

#b를 새로 만들지 않고 a를 같이 바라본다
b = a  #얖은카피, soft copy, 둘의 데이터 공간은 같다 
a[0]="짜장면"
print(a)
print(b)



#깊은 복사
a = ["탕수육", "치킨", "두루치기", "콩국수", "회냉면"]
from copy import deepcopy 
b = deepcopy(a) #새로 만든다 

a[0]="소갈비찜"

print(a)
print(b)

#def myDeepCopy(a):

import numpy as np 
a = np.array([1,3,5,7,9])
b = a  #이것도 softcopy이다 샴쌍둥이
a[0]=100
print(a)
print(b)

b = a.copy()  #numpy의 deepcopy , 분리시키고 싶을때 
a[0]=333
print(a)
print(b)

b = a #무조건 소프트 카피, 주소 복사 
#복사 할 경우 

food1 = ["탕수육", "치킨", "두루치기", "콩국수", "회냉면"]

food2 = [] # food2 = list(), list타입 객체 생성 
for item in food1:
    food2.append(item)

food1[0] = "전과복"
print(food1)
print(food2)

#파이썬의 모든 변수는 참조 변수다 , dict, list는 말할것도 없음
person1 = {"name":"홍길동","age":25, "phone":"010-0000-0000"}
person2 = deepcopy(person1) 
person2['name']="임꺽정"
print(person1)
print(person2)


#일반적으로 파이썬에서 대입연산자를 이용한 대입은 소프트카피를 
#기본으로 한다. 특히나 list, dict, numpy.array등등 
#그래서 별도의 메모리 복사를 원하면 하드(deep)카피를 해야 한다 

