<br>

## 🟢 정규표현식 - 함수




<br>

### 🟡 기본 예시


```python
import re
 
pattern = r'비'
text = "하늘에 비가 오고 있습니다.  어제도 비가 왔고 오늘도 비가 오고 있습니다"

# 1단계 - re 사용하기
regex = re.compile(pattern)   # 패턴을 컴파일 시킨다.

# 2단계 - regex 사용하기
result = regex.findall(text)  # matiching 이 이루어진 모든 문자열의 리스트를 반환합니다 

print( result )
print( f"\'{pattern}\'에 대해서 {len(result)} 개를 찾았다." )

```

    ['비', '비', '비']
    '비'에 대해서 3 개를 찾았다.
    

<br>

### 🟡 우편번호 형식 맞추기 정규식


◈ 우편번호 형식 맞추기 정규식 예제

우리나라의 우편번호는 6자리에서 5자리로 체계가 바뀌었습니다. 정수 값을 입력을 받아서 이 데이터가 우편번호 형식에 맞는지 확인해보는 예제를 만들어 보겠습니다. 
우편번호 패턴 방식 : \d{5}$      <- 정수 5개만 가능하다 

파일명 : exam13_1.py





```python
import re
 
# zipcode = input("우편번호를 입력하세요")
zipcode = '12345'

# pattern = r'\d{5}'    # 5자리로 끝나야한다는 조건을 위해서 뒤에 $ 를 붙여준다.
pattern = r'\d{5}$'     # 5자리로 끝나야한다는 조건을 위해서 뒤에 $ 를 붙여준다.
regex = re.compile(pattern)

# match 함수가 패턴이 반드시 시작위치에 있어야 한다.  ex) a1234
result = regex.match(zipcode)   # 형식이 일치하는게 없으면 None 반환

if result != None:
    print("형식이 일치합니다.")
else:
    print("잘못된 형식입니다.")    


# 이렇게 쓰는 것이 가장 베스트입니다.
print(re.match(pattern, zipcode))

```

    형식이 일치합니다.
    <re.Match object; span=(0, 5), match='12345'>
    

<br>

### 🟡 match


```python
import re

text1 = "I like star"
text2 = "star is beautiful"

pattern = "star"
print (re.match( pattern, text1))
print (re.match( pattern, text2))


matchObj = re.match( pattern, text2)
print(f"group: {matchObj.group()}" )
print(f"start: {matchObj.start()}" )
print(f"end: {matchObj.end()}" )
print(f"span: {matchObj.span()}" )

print(f"text2[:4] : {text2[:4]}")


```

    None
    <re.Match object; span=(0, 4), match='star'>
    group: star
    start: 0
    end: 4
    span: (0, 4)
    text2[:4] : star
    

<br>

### 🟡 search


```python
import re

text1 = "I like star"
text2 = "star is beautiful"

pattern = "star"
print (re.search( pattern, text1))
print (re.search( pattern, text2))      


matchObj = re.match( pattern, text2)
print(f"group: {matchObj.group()}" )
print(f"start: {matchObj.start()}" )
print(f"end: {matchObj.end()}" )
print(f"span: {matchObj.span()}" )

print(f"text2[:4] : {text2[:4]}")


```

    <re.Match object; span=(7, 11), match='star'>
    <re.Match object; span=(0, 4), match='star'>
    group: star
    start: 0
    end: 4
    span: (0, 4)
    text2[:4] : star
    

<br>

### 🟡 findall & finditer


```python
import re

text = """
    phone : 010-0000-0000 email:test1@nate.com
    phone : 010-1111-1111 email:test2@naver.com
    phone : 010-2222-2222 email:test3@gmail.com
    """
print()

# ================================================

print("--- 이메일 추출하기 ---") 
# pattern_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emailpattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b"

matchObj = re.findall( emailpattern, text)

for item in matchObj:
    print( item)


print("\n--- 이메일 추출하기 finditer---") 
matchObj = re.finditer( emailpattern, text)

for item in matchObj:
    print( item)

# ================================================

print("\n--- 전화번호 추출하기 ---")
# pattern_phone = r"^\d{2,3}-\d{3,4}-\d{4}$"
phonepattern = r"\d{3}-\d{4}-\d{4}"

matchObj = re.findall( phonepattern, text)

for item in matchObj:
    print( item)


print("\n--- 전화번호 추출하기 finditer---")
matchObj = re.finditer( phonepattern, text)

for item in matchObj:
    print( item)




```

    
    --- 이메일 추출하기 ---
    test1@nate.com
    test2@naver.com
    test3@gmail.com
    
    --- 이메일 추출하기 finditer---
    <re.Match object; span=(33, 47), match='test1@nate.com'>
    <re.Match object; span=(80, 95), match='test2@naver.com'>
    <re.Match object; span=(128, 143), match='test3@gmail.com'>
    
    --- 전화번호 추출하기 ---
    010-0000-0000
    010-1111-1111
    010-2222-2222
    
    --- 전화번호 추출하기 finditer---
    <re.Match object; span=(13, 26), match='010-0000-0000'>
    <re.Match object; span=(60, 73), match='010-1111-1111'>
    <re.Match object; span=(108, 121), match='010-2222-2222'>
    

<br>

### 🟡 sub
`re.sub(pattern, repl, string, count=0, flags=0)` | 패턴을 **repl 문자열로 교체**하여 반환


```python
import re

text1 = "I like stars, red star, yellow star"

print("\n---- 기본 사용 ----")
pattern = "star"
result = re.sub( pattern, "moon", text1)
print(result)   # 문자열을 전체 체인지

print("\n---- count=2 옵션 사용 ----")
result2 = re.sub( pattern, "moon", text1, count=2)
print(result2)   # 특정 문자 2개까지만 체인지


```

    
    ---- 기본 사용 ----
    I like moons, red moon, yellow moon
    
    ---- count=2 옵션 사용 ----
    I like moons, red moon, yellow star
    
