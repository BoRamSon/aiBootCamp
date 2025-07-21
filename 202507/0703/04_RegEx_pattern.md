## 🟢 정규표현식 - 패턴


```python
import re

# pattern = r"abc"
# pattern = r"^abc"
pattern = r"abc$"

text = ["abc", "abcd", "abc15", "dabc", "", "s"]
repattern = re.compile(pattern)

for item in text:
    result = repattern.search(item)
    if result:
        print(item, "- O" )
    else:
        print(item, "- X" )

```

    abc - O
    abcd - X
    abc15 - X
    dabc - O
     - X
    s - X
    

## 🟢 문제 풀어보기

사업자 번호는 앞3자리 가운데 2자리 뒤 5자리로 구성되어 있습니다. 문서에서 사업자 번호만 추출하여 그중 개인 사업자 관련 번호만 추출하고자 합니다. 사업자 번호의 각 자릿수의 의미는 다음과 같습니다.  
  
사업자번호의 의미 : 000-00-00000
  앞 3자리 - 관할세무서 번호 
  가운데 2자리 - 사업자의 성격을 나타냄(개인사업자 : 90~99)
  마지막 5자리 - 사업자용4자리+검증용1자리 
  다음 데이터들로 부터 사업자 번호들을 추출하고 그 중에 개인 면세 사업자에 해당하는 사업자 번호만 출력하기 바랍니다 
  


```python
import re

contents = """
    우리커피숍 100-90-12345
    영풍문고 101-91-12121
    영미청과 102-92-23451
    황금코인 103-89-13579
    우리문구 104-91-24689
    옆집회사 105-82-12345
"""

name_pattern = r"[가-힣]{1,}"
name_result = re.findall(name_pattern, contents)
print(name_result)

number_pattern = r"\d{3}-\d{2}-\d{5}"
number_result = re.findall(number_pattern, contents)
print(number_result)

print("\n-------- 결과 --------")
for i in range(len(name_result)):
    if re.search(r"\d{2}-9[0-9]-", number_result[i]):
        print(name_result[i], '= 개인사업자')


```

    ['우리커피숍', '영풍문고', '영미청과', '황금코인', '우리문구', '옆집회사']
    ['100-90-12345', '101-91-12121', '102-92-23451', '103-89-13579', '104-91-24689', '105-82-12345']
    
    ----- 결과 -----
    우리커피숍 = 개인사업자
    영풍문고 = 개인사업자
    영미청과 = 개인사업자
    우리문구 = 개인사업자
    
