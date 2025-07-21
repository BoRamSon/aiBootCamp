import numpy as np

# np.zeros( 크기 ) 0으로 채워진 배열을 만든다. 크기만큼 
# np.zeros( 크리를 tuple 타입으로 )   np.zeros( (2,3,4) )
print( np.zeros(10) ) # 0으로 채워진 공간 10개를 만든다 
print( np.zeros( (2, 10) ) ) #0으로 채워진 공간 2 by 10 - 20개 
print( np.ones( (3, 10) ) )  #ones 함수는 데이터를 1로 채운다 

print( np.zeros( (3,4,2) ) )


#랜덤값 생성하기 
#np.random.seed(1) #seed  함수를 호출해서 값을 넣어주면, 그 다음 랜덤값이 동일하게나온다
                  #아무 정수나 
a= np.random.rand( 5 ) #0~1사이의 균일한 실수 난수  
print(a)
print(type(a))

#3차원으로 랜덤값 달라 - 튜플로 줘야 하는게 아니라서 괄호 없음 
a= np.random.rand( 5,4,3 ) 
print(a)
print(type(a))



#가우스 분포를 따른다. -정규분포를 따른다 
a= np.random.randn( 5 )
print(a)


a= np.random.randint(10 ) # 정수값 1개 0~ 9 에 이르는 범위
print(a)
