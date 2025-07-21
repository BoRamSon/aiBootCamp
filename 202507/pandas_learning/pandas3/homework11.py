import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/iris.csv')
#NaN값 있는지 체크하기 - 각 필드별로 NaN값 있는 개수 출력
print( data.isnull().sum())

sepal_length_mean = data['sepal.length'].mean() 
sepal_width_mean = data['sepal.width'].mean() 
petal_length_mean = data['petal.length'].mean() 
petal_width_mean = data['petal.width'].mean() 

data['sepal.length'].fillna( sepal_length_mean, inplace=True)
data['sepal.width'].fillna( sepal_width_mean, inplace=True)
data['petal.length'].fillna( petal_length_mean, inplace=True)
data['petal.width'].fillna( petal_width_mean, inplace=True)

#data.fillna(data.mean(), inplace=True)

#정규화를 함수로 만들었음
def normalize(columnname):
    max = data[columnname].max()
    min = data[columnname].min()
    return (data[columnname]-min)/(max-min)

data['sepal.length'] = normalize('sepal.length')
data['sepal.width'] = normalize('sepal.width')
data['petal.width'] = normalize('petal.width')

print(data)

#구간 나누기 
count, bin_dividers = np.histogram(data['petal.length'], bins=3)
print( bin_dividers)

bin_names = ["A", "B", "C"]
data["petal_grade"] = pd.cut( x=data['petal.length'], bins=bin_dividers, 
    labels = bin_names, include_lowest=True)

print(data)


Y_class = np.array(data['petal_grade']).reshape(-1,1)

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(Y_class)

Y_class_onehot = enc.transform(Y_class).toarray()
Y_class_recovery = np.argmax(Y_class_onehot, axis=1).reshape(-1,1)

print(Y_class_onehot)


