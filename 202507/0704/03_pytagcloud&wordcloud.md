<br><br><br>

# 🟩 pytagcloud & wordcloud 라이브러리

<br>

## 🟢 pytagcloud 한글폰트 설정

#### pytagcloud 패키지 font경로에 한글폰트 넣기 
C:\Users\user\.conda\envs\conda환경명칭\Lib\site-packages\pytagcloud\fonts

#### Windows 기준 파일 찾기
C:\Users\user\.conda\envs\conda환경명칭\Lib\site-packages\pytagcloud\fonts에 있는 `fonts.json` 파일을 visual studio code 에서 열고 맨 앞에 한글 폰트를 추가해야 합니다. 

#### 예시
{
	"name": "korean", 
	"ttf": "H2GTRE.TTF",
	"web": "http://fonts.googleapis.com/css?family=Nobile"
},

#### 예시 설명
이름은 제 마음대로 정하면 됩니다.  
ttf에는 복사해온 한글폰트 파일명을 작성하면 됩니다.  
여러분 컴퓨터에 저 폰트가 없을 수도 있습니다.  
가지고 있는 한글 폰트를 사용하면 됩니다.  
web은 현재 위치에 폰트가 없을 경우 web으로부터 다운받으라는 url인데 그냥 아래에 있는 web url  하나를 복사해 왔습니다.  
파일의 내용을 삭제하는게 아니라 위에 추가하는 겁니다 




### 🟡 필요한 모듈 설치하기

#### ⚫ 워드클라우드 지원 라이브러리
pip install pytagcloud   
pip install pygame 

#### ⚫ 워드 클라우드 지원 라이브러리(만든사람이 다름)
pip install WordCloud

#### ⚫ JSON 데이터를 파싱하거나 생성하는 기능을 제공하는 파이썬 라이브러리
pip install simplejson


<br>

## 🟢 pytagcloud 사용해보기


```python
import pytagcloud 
import webbrowser 

tag = [
    ('school', 30),
    ('rainbow', 70),
    ('cloud', 12),
    ('world', 300),
    ('peach', 130),
    ('pink', 39),
    ('image', 110),
    ('python', 70),
    ('computer', 60),
    ('game', 210),
    ('한글임', 500),
    ('한글임2', 500),
    ('한글임3', 500),
    ('한글임4', 600),
    ('한글임5', 600),
    ('한글임6', 600),
    ('한글임7', 600),
    ('한글임8', 600),
]
taglist = pytagcloud.make_tags(tag, maxsize=50)
print(taglist)
pytagcloud.create_tag_image(taglist, 
                            'wordcloud_test.jpg',
                            size=(600,600),
                            fontname='korean',   # 한글 폰트로 지정
                            rectangular=True)
webbrowser.open('wordcloud_test.jpg')

# import os 
# os.startfile('wordcloud_test.jpg')

```

    [{'color': (15, 96, 16), 'size': 7, 'tag': 'school'}, {'color': (181, 23, 204), 'size': 11, 'tag': 'rainbow'}, {'color': (10, 125, 50), 'size': 5, 'tag': 'cloud'}, {'color': (11, 127, 16), 'size': 30, 'tag': 'world'}, {'color': (97, 36, 56), 'size': 17, 'tag': 'peach'}, {'color': (35, 73, 180), 'size': 8, 'tag': 'pink'}, {'color': (64, 135, 42), 'size': 15, 'tag': 'image'}, {'color': (118, 15, 28), 'size': 11, 'tag': 'python'}, {'color': (182, 193, 170), 'size': 10, 'tag': 'computer'}, {'color': (103, 217, 24), 'size': 23, 'tag': 'game'}, {'color': (49, 112, 184), 'size': 44, 'tag': '한글임'}, {'color': (15, 163, 38), 'size': 44, 'tag': '한글임2'}, {'color': (160, 167, 63), 'size': 44, 'tag': '한글임3'}, {'color': (68, 143, 155), 'size': 50, 'tag': '한글임4'}, {'color': (115, 140, 138), 'size': 50, 'tag': '한글임5'}, {'color': (54, 50, 192), 'size': 50, 'tag': '한글임6'}, {'color': (22, 217, 201), 'size': 50, 'tag': '한글임7'}, {'color': (17, 133, 74), 'size': 50, 'tag': '한글임8'}]
    




    True



<br>

## 🟢 텍스트파일을 Okt로 단어를 추출 및 tag로 만들어 wordcloud(pytagcloud)로 만들기



```python
import pytagcloud 
import webbrowser 
from konlpy.tag import Okt
from collections import Counter #워드 카운트 단어 계수기 

file = open("./data/data1.txt", encoding="utf-8")
text = file.read() #텍스트파일 읽기 

#파일로부터 명사 추출 
okt = Okt() 
nouns = okt.nouns(text) #명사로 분해하기 

nounsCounter = Counter(nouns) #명사들 다 세서 (단어, 카운트) 형태로 데이터 전달
print(nounsCounter)

tag = nounsCounter.most_common(100) #모든 단어로 차트를 그리면 너무 정신없어서 
#빈도수를 기반으로 정렬한 다음 100개만 가져와서 차트를 그려라 

taglist = pytagcloud.make_tags(tag, maxsize=50)
print(taglist)
pytagcloud.create_tag_image(taglist, 
                            'wordcloud_test2.jpg',
                            size=(600,600),
                            fontname='korean',
                            rectangular=False)
webbrowser.open('wordcloud2.jpg')

```

    Counter({'광장': 14, '그': 13, '밀실': 8, '사람': 6, '살': 4, '것': 4, '인간': 3, '공간': 3, '다만': 3, '수': 3, '시대': 2, '달리': 2, '로부터': 2, '골목': 2, '길': 2, '거상': 2, '자결': 2, '민들레': 2, '씨앗': 2, '온': 2, '치': 2, '경로': 2, '얼마나': 2, '개인': 2, '이': 2, '때': 2, '나': 2, '표범': 1, '가죽': 1, '징': 1, '원시인': 1, '사회': 1, '끝내': 1, '동료': 1, '줄': 1, '생활': 1, '현대': 1, '산업': 1, '구조': 1, '미궁': 1, '한편': 1, '동물': 1, '혈거인': 1, '동굴': 1, '정신병원': 1, '격리': 1, '실': 1, '자기': 1, '저': 1, '무수': 1, '곳': 1, '의': 1, '목도': 1, '행방': 1, '갖가지': 1, '노정': 1, '더': 1, '소리': 1, '아주': 1, '덩치': 1, '거리': 1, '못': 1, '바보': 1, '봄': 1, '들판': 1, '속': 1, '영원': 1, '이르렀건': 1, '문제': 1, '보고': 1, '사랑': 1, '대중': 1, '가지': 1, '한쪽': 1, '폭동': 1, '피': 1, '광란': 1, '우리': 1, '분수': 1, '햇빛': 1, '아래': 1, '뭇': 1, '꽃': 1, '피고': 1, '영웅': 1, '신들': 1, '동상': 1, '치장': 1, '바다': 1, '람': 1, '합창': 1, '한몫': 1, '끼': 1, '똑': 1, '일기장': 1, '저녁': 1, '채': 1, '새벽': 1, '간': 1, '애인': 1, '장갑': 1, '침대': 1, '걸터': 1, '시간': 1, '이명': 1, '준': 1, '경우': 1, '마찬가지': 1, '패': 1, '두둔': 1, '생각': 1, '말': 1, '풍문': 1, '만족': 1, '늘': 1, '현장': 1, '태도': 1, '바로': 1, '때문': 1, '이야기': 1, '전하': 1, '저자': 1, '최인훈': 1, '서문': 1})
    [{'color': (57, 109, 28), 'size': 52, 'tag': '광장'}, {'color': (175, 206, 144), 'size': 50, 'tag': '그'}, {'color': (19, 72, 212), 'size': 34, 'tag': '밀실'}, {'color': (154, 23, 36), 'size': 28, 'tag': '사람'}, {'color': (131, 175, 210), 'size': 21, 'tag': '살'}, {'color': (134, 41, 121), 'size': 21, 'tag': '것'}, {'color': (18, 92, 97), 'size': 17, 'tag': '인간'}, {'color': (86, 172, 85), 'size': 17, 'tag': '공간'}, {'color': (188, 64, 64), 'size': 17, 'tag': '다만'}, {'color': (199, 19, 204), 'size': 17, 'tag': '수'}, {'color': (201, 15, 96), 'size': 13, 'tag': '시대'}, {'color': (48, 52, 104), 'size': 13, 'tag': '달리'}, {'color': (212, 198, 210), 'size': 13, 'tag': '로부터'}, {'color': (14, 138, 220), 'size': 13, 'tag': '골목'}, {'color': (29, 216, 117), 'size': 13, 'tag': '길'}, {'color': (82, 125, 85), 'size': 13, 'tag': '거상'}, {'color': (74, 19, 82), 'size': 13, 'tag': '자결'}, {'color': (86, 137, 14), 'size': 13, 'tag': '민들레'}, {'color': (178, 71, 28), 'size': 13, 'tag': '씨앗'}, {'color': (76, 124, 190), 'size': 13, 'tag': '온'}, {'color': (164, 142, 142), 'size': 13, 'tag': '치'}, {'color': (170, 185, 179), 'size': 13, 'tag': '경로'}, {'color': (151, 54, 101), 'size': 13, 'tag': '얼마나'}, {'color': (29, 164, 157), 'size': 13, 'tag': '개인'}, {'color': (182, 125, 169), 'size': 13, 'tag': '이'}, {'color': (119, 185, 104), 'size': 13, 'tag': '때'}, {'color': (30, 197, 202), 'size': 13, 'tag': '나'}, {'color': (167, 13, 102), 'size': 9, 'tag': '표범'}, {'color': (187, 149, 213), 'size': 9, 'tag': '가죽'}, {'color': (37, 18, 21), 'size': 9, 'tag': '징'}, {'color': (81, 143, 134), 'size': 9, 'tag': '원시인'}, {'color': (180, 208, 154), 'size': 9, 'tag': '사회'}, {'color': (145, 171, 203), 'size': 9, 'tag': '끝내'}, {'color': (140, 79, 100), 'size': 9, 'tag': '동료'}, {'color': (210, 63, 31), 'size': 9, 'tag': '줄'}, {'color': (107, 173, 29), 'size': 9, 'tag': '생활'}, {'color': (132, 216, 37), 'size': 9, 'tag': '현대'}, {'color': (174, 36, 34), 'size': 9, 'tag': '산업'}, {'color': (42, 29, 97), 'size': 9, 'tag': '구조'}, {'color': (66, 159, 206), 'size': 9, 'tag': '미궁'}, {'color': (83, 94, 49), 'size': 9, 'tag': '한편'}, {'color': (122, 64, 101), 'size': 9, 'tag': '동물'}, {'color': (45, 107, 51), 'size': 9, 'tag': '혈거인'}, {'color': (71, 14, 47), 'size': 9, 'tag': '동굴'}, {'color': (198, 178, 58), 'size': 9, 'tag': '정신병원'}, {'color': (85, 69, 213), 'size': 9, 'tag': '격리'}, {'color': (107, 148, 48), 'size': 9, 'tag': '실'}, {'color': (12, 65, 53), 'size': 9, 'tag': '자기'}, {'color': (208, 199, 131), 'size': 9, 'tag': '저'}, {'color': (59, 164, 116), 'size': 9, 'tag': '무수'}, {'color': (41, 58, 18), 'size': 9, 'tag': '곳'}, {'color': (200, 199, 99), 'size': 9, 'tag': '의'}, {'color': (91, 88, 126), 'size': 9, 'tag': '목도'}, {'color': (38, 149, 125), 'size': 9, 'tag': '행방'}, {'color': (152, 157, 102), 'size': 9, 'tag': '갖가지'}, {'color': (137, 185, 205), 'size': 9, 'tag': '노정'}, {'color': (95, 81, 216), 'size': 9, 'tag': '더'}, {'color': (110, 144, 176), 'size': 9, 'tag': '소리'}, {'color': (26, 138, 69), 'size': 9, 'tag': '아주'}, {'color': (93, 125, 186), 'size': 9, 'tag': '덩치'}, {'color': (216, 198, 91), 'size': 9, 'tag': '거리'}, {'color': (156, 215, 196), 'size': 9, 'tag': '못'}, {'color': (96, 140, 206), 'size': 9, 'tag': '바보'}, {'color': (19, 180, 92), 'size': 9, 'tag': '봄'}, {'color': (131, 203, 128), 'size': 9, 'tag': '들판'}, {'color': (160, 187, 81), 'size': 9, 'tag': '속'}, {'color': (41, 101, 76), 'size': 9, 'tag': '영원'}, {'color': (49, 193, 35), 'size': 9, 'tag': '이르렀건'}, {'color': (179, 189, 174), 'size': 9, 'tag': '문제'}, {'color': (209, 59, 66), 'size': 9, 'tag': '보고'}, {'color': (186, 86, 136), 'size': 9, 'tag': '사랑'}, {'color': (112, 16, 80), 'size': 9, 'tag': '대중'}, {'color': (76, 149, 88), 'size': 9, 'tag': '가지'}, {'color': (200, 152, 63), 'size': 9, 'tag': '한쪽'}, {'color': (23, 125, 213), 'size': 9, 'tag': '폭동'}, {'color': (138, 136, 182), 'size': 9, 'tag': '피'}, {'color': (27, 31, 166), 'size': 9, 'tag': '광란'}, {'color': (128, 93, 122), 'size': 9, 'tag': '우리'}, {'color': (193, 202, 138), 'size': 9, 'tag': '분수'}, {'color': (113, 18, 193), 'size': 9, 'tag': '햇빛'}, {'color': (40, 20, 160), 'size': 9, 'tag': '아래'}, {'color': (85, 160, 72), 'size': 9, 'tag': '뭇'}, {'color': (114, 182, 187), 'size': 9, 'tag': '꽃'}, {'color': (84, 218, 39), 'size': 9, 'tag': '피고'}, {'color': (13, 93, 55), 'size': 9, 'tag': '영웅'}, {'color': (167, 162, 109), 'size': 9, 'tag': '신들'}, {'color': (23, 42, 163), 'size': 9, 'tag': '동상'}, {'color': (55, 52, 214), 'size': 9, 'tag': '치장'}, {'color': (220, 30, 67), 'size': 9, 'tag': '바다'}, {'color': (60, 56, 68), 'size': 9, 'tag': '람'}, {'color': (166, 61, 210), 'size': 9, 'tag': '합창'}, {'color': (90, 139, 77), 'size': 9, 'tag': '한몫'}, {'color': (28, 168, 67), 'size': 9, 'tag': '끼'}, {'color': (176, 198, 147), 'size': 9, 'tag': '똑'}, {'color': (53, 208, 182), 'size': 9, 'tag': '일기장'}, {'color': (76, 25, 184), 'size': 9, 'tag': '저녁'}, {'color': (70, 40, 22), 'size': 9, 'tag': '채'}, {'color': (132, 100, 71), 'size': 9, 'tag': '새벽'}, {'color': (25, 140, 77), 'size': 9, 'tag': '간'}, {'color': (121, 121, 123), 'size': 9, 'tag': '애인'}]
    




    True



<br>

## 🟢 wordcloud - 글 내용 중 단어 빈도 기반의 워드클라우드를 생성


```python
# matplotlib의 pyplot 모듈을 가져와서 plt라는 이름으로 사용
import matplotlib.pyplot as plt

# WordCloud 클래스는 단어 빈도 기반의 워드클라우드를 생성하는 데 사용됨
from wordcloud import WordCloud 

# 텍스트 파일을 읽기 모드로 열기 (상대경로 기준: ./data/alice.txt)
file = open("./data/alice_edit.txt")  # 내요이 너무 길어서 내가 내용을 대부분 없앤 edit 파일 만듬.

# 파일의 전체 내용을 하나의 문자열로 읽음
text = file.read() 

# 텍스트 출력 (확인용)
print(text)
print("\n\n")

# WordCloud 객체 생성 후, .generate(text) 메서드로 주어진 텍스트에서 워드클라우드 생성
wordcloud = WordCloud().generate(text)

# 워드클라우드 이미지를 화면에 표시 (imshow는 이미지 데이터를 시각화함)
# interpolation='bilinear'는 픽셀을 부드럽게 보간 처리하여 좀 더 부드러운 이미지로 보이게 함
plt.imshow(wordcloud, interpolation='bilinear') 

# x, y 축 눈금과 축 이름을 제거해서 이미지만 깔끔하게 표시되게 함
plt.axis("off") 

# 최종적으로 이미지(워드클라우드)를 화면에 출력
plt.show()

```

    Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll
    
    This eBook is for the use of anyone anywhere at no cost and with
    almost no restrictions whatsoever.  You may copy it, give it away or
    re-use it under the terms of the Project Gutenberg License included
    with this eBook or online at www.gutenberg.org
    
    
    Title: Alice's Adventures in Wonderland
    
    Author: Lewis Carroll
    
    Posting Date: June 25, 2008 [EBook #11]
    Release Date: March, 1994
    [Last updated: December 20, 2011]
    
    Language: English
    
    
    *** START OF THIS PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***
    
    
    
    
    
    
    
    


    
![png](03_pytagcloud%26wordcloud_files/03_pytagcloud%26wordcloud_8_1.png)
    


<br>

## 🟢 konlpy.corpus 한국 법률 말뭉치


```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 한국 법률 말뭉치
from konlpy.corpus import kolaw
c = kolaw.open('constitution.txt').read()
print(c[:200])
```

    대한민국헌법
    
    유구한 역사와 전통에 빛나는 우리 대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에 항거한 4·19민주이념을 계승하고, 조국의 민주개혁과 평화적 통일의 사명에 입각하여 정의·인도와 동포애로써 민족의 단결을 공고히 하고, 모든 사회적 폐습과 불의를 타파하며, 자율과 조화를 바탕으로 자유민주적 기본질서를 더욱 확고히 하여 정치·경제
    

### 🟡 konlpy.corpus 법률 말뭉치 워드클라우드 생성


```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from konlpy.tag import Okt       # 추가

# 한국 법률 말뭉치
from konlpy.corpus import kolaw
c = kolaw.open('constitution.txt').read()
print(c[:200])

font_path = 'C:/Windows/fonts/malgun.ttf'
wordcloud = WordCloud(font_path=font_path, width=800, height=400).generate(c)

# 파일로 저장
wordcloud.to_file('image1.png')

# 이미지 정보를 리턴
plt.imshow(wordcloud, interpolation='bilinear')  # 이미지 좀 이뻐보이게 보간법
plt.axis('off')  # x, y 축 안보이게 제거
plt.show()


```

    대한민국헌법
    
    유구한 역사와 전통에 빛나는 우리 대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에 항거한 4·19민주이념을 계승하고, 조국의 민주개혁과 평화적 통일의 사명에 입각하여 정의·인도와 동포애로써 민족의 단결을 공고히 하고, 모든 사회적 폐습과 불의를 타파하며, 자율과 조화를 바탕으로 자유민주적 기본질서를 더욱 확고히 하여 정치·경제
    


    
![png](03_pytagcloud%26wordcloud_files/03_pytagcloud%26wordcloud_12_1.png)
    

