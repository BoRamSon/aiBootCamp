words = ["assembly" , "java" , "rain" , "notebook" , "north" , "south" , "hospital" , "programming" , "house" ,"hour"]


# 1. filter 함수를 사용하여 글자수가 6 글자 이상인 단어만 출력하기 (컴프리헨션 X)
for i in filter(lambda is_six_text : len(is_six_text) >= 6, words):
  print(f"filter 함수를 이용하여 6글자 이상인 것만 출력하기 = {i}")


# 2. map 함수를 사용해서 글자를 대문자로 바꾸어서 출력 (컴프리헨션 X)
# for i in map(lambda convert_upper : upper(convert_upper), words):
for i in map(lambda convert_upper : convert_upper.upper(), words):
  print(f"map 함수를 활용하여 모두 대문자로 바꿔버리기 = {i}")


# 3. sorted 함수를 사용해서 단어들의 길이순으로 오름차순으로 정렬하여 출력하기
sorted_words_list = sorted(words, key=len)
print(sorted_words_list)


# 4. sorted 함수를 사용해서 알파벳 순으로 내림차순으로 정렬하여 출력하기
sorted_words_list2 = sorted(words, reverse=True)
print(sorted_words_list2)


# 5. 단어 중에 o 가 포함되는 단어가 모두 몇개인지 카운트하기 ( 힌트 , filter 를 사용 )
o_variable = list(filter(lambda text : 'o' in text, words))
print(f"o가 포함되는 단어는 모두 몇개인가? = {len(o_variable)}개")
