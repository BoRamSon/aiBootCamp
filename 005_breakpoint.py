pay_money = 100000

things_total_price = int(input('총 물건의 금액을 입력해주세요.'))

change = pay_money - things_total_price

temp = change

fifty_thousand_won = temp // 50000
temp = temp % 50000   # 🔥 temporary 임시의 변수라는 의미

ten_thousand_won = temp // 10000
temp = temp % 10000

five_thousand_won = temp // 5000
temp = temp % 5000

one_thousand_won = temp // 1000
temp = temp % 1000

five_hundred_won = temp // 500
temp = temp % 500

one_hundred_won = temp // 100
temp = temp % 100

fifty_won = temp // 50
temp = temp % 50

ten_won = temp // 10


# 🔥 이렇게 별도로 빼주는 것이 더 일관성 있습니다.
print(f"거스름돈은 {change}원입니다.")
print(f"5만원권 ==> {fifty_thousand_won}장")
print(f"1만원권 ==> {ten_thousand_won}장")
print(f"5천원권 ==> {five_thousand_won}장")
print(f"1천원권 ==> {one_thousand_won}장")
print(f"500원 ==> {five_hundred_won}개")
print(f"100원 ==> {one_hundred_won}개")
print(f"50원 ==> {fifty_won}개")
print(f"10원 ==> {ten_won}개")


# 이 예제를 실행할 때 python debug를 사용한다면, 