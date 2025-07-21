import pandas as pd 

file = open("data.txt", encoding="utf8")
lines = file.readlines() 
df = pd.DataFrame() #기본객체를 하나 만들고 
for line in lines:
    line = line[:len(line)-1]  #마지막에 \n 지우기 
    #print(line)
    items = line.split(" ")
    """
    items[0] = "홍길동"
    items[1] = "90"
    ....
    """
    df = df.append({"name":items[0], "kor":int(items[1]), "eng":int(items[2]),
         "mat":int(items[3])}, ignore_index=True)

file.close()

print(df)

#순서 바꾸기 - fancy index 사용 
df2 = df[ ['name', 'kor', 'eng', 'mat'] ]
print(df2)
df2['total'] = df2.kor + df2.eng + df2.mat 
df2['total'] = df2['kor'] + df2['eng'] + df2['mat']
df2['avg'] = df2['total']/3 

print(df2)

for i in range(0, df2.name.count()):
    print( df2.iloc[i, 0], df2.iloc[i, 1],df2.iloc[i, 2],df2.iloc[i, 3],df2.iloc[i, 4],df2.iloc[i, 5])



