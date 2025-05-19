# --------------------------------------------
# 입력
input_list = []
# input_list = [1,2,3,4,5,6,7,8,9,10]  # test

for i in range(1,11):
  self_input = int(input('입력해주세요 :'))
  input_list.append(self_input)

# --------------------------------------------
# 계산
even_num = []
odd_num = []

# print(input_list)  # test

for i in input_list:
  if i % 2 == 0:
    even_num.append(i)
  if i % 2 != 0:
    odd_num.append(i)

sum_even_num = sum(even_num)
average_even_num = sum(even_num) / len(even_num)

sum_odd_num = sum(odd_num)
average_odd_num = sum(odd_num) / len(odd_num)

# -----------------------------------------------
# 출력
print(f'짝수의 합 : {sum_even_num}')
print(f'홀수의 합 : {sum_odd_num}')

print(f'짝수의 평균 : {average_even_num}')
print(f'홀수의 평균 : {average_odd_num}')
