# 과제1. 정수를 받아가서 짝수이면 True / 짝수가 아니면 False를 반환하는 함수

def even_num(num):
  if num % 2 == 0:
    return True
  else:
    return False

print(even_num(2))
print(even_num(3))
print(even_num(4))



# - 과제2. 4년마다 윤년인데,
  # - 100년에 한번씩은 윤년이 아닙니다.
  # - 400년에 한번씩 윤년이다.
  # - 함수를 만들어서 연도를 주면 윤년일 경우 True / 윤년이 아니면 False를 반환해라.

def leap_year(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
      return True
  else:
    return False

print(leap_year(2024))
print(leap_year(2028))
print()
print(leap_year(1900))
print(leap_year(2100))
print()
print(leap_year(1600))
print(leap_year(2000))


