import pandas as pd 

data = {
    'class1':{
            'name': ['박동석', '권다윤', '김민제'],
            'height':[173, 177, 183]
    },

    'class2':{
            'name': ['김민수', '이용희', '임미영'],
            'height':[179, 167, 180]
    }
}

panel = pd.Panel(data)
print(panel)

print( panel['class1'])
print( panel['class2'])

df = panel['class1']
print( df.iloc[0,0])
print( df.columns)
print("--- for ---")
for key in panel:
    item = panel[key]
    for col in item.columns:
        for row in item[col]:
            print(row, end=' ')
        print()
   