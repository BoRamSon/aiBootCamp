import pandas as pd

series1 = pd.Series([ '사과', '망고', '바나나', '수박', '딸기'] )
print( series1[2:])

series2 = pd.Series({'red':'빨간색', 'green':'초록색', 'blue':'파란색', 'black':'검은색'})
print( series2['red':'blue'])

data = {
    'name':['Tom', 'Brown', 'Jane', 'Stepany', 'John'],
    'month1':[1200, 2000, 3000, 1800, 4500],
    'month2':[2400, 2300, 4300, 2800, 4200],
    'month3':[1800, 2700, 3500, 3800, 4300]
}

data = pd.DataFrame(data)

data['quater1'] = data['month1'] + data['month2'] + data['month3']

print( data )

data = data.append({'name':'Bread', 'month1':3400, 'month2':4000, 'month3':5000}, ignore_index=True)
print(data)

print( data.iloc[3, 3])

print( data.loc[4, 'month2'])

data = data.drop('month2', axis=1)
data = data.drop(2, axis=0)

print(data)