from sklearn.datasets import load_iris

iris = load_iris()
print(iris.keys())

iris_data = iris['data']
print(iris_data[:5])
print(type(iris_data))

a1 =  iris_data[ :,0]
a2 =  iris_data[ :,1]
a3 =  iris_data[ :,2]
a4 =  iris_data[ :,3]

print(len(a1))
#각각 행의 평균과 중간값 구하기 


