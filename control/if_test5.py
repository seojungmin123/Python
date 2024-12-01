'''
money = int(input("가지고 있는 돈은 얼마인가요?: "))

if money >= 20000:
    print("탕수육")
elif money >= 10000:
    print("쟁반짜장")
elif money >= 6000:
    print("해물짬뽕")
elif money >= 4000:
    print("짜장면")
else:
    print("단무지")


a = int(input("첫번째 값: "))
b = int(input("두번째 값: "))

if a % 2 == 0 and b % 2 == 0: #둘다 짝수
    print()
elif a % 2 == 1 and b % 2 == 1: #둘다 홀수
    print()
else:                            #홀짝 하나씩
    print()


list_num = [1,2,3,4,5]
n = int(input("정수 하나 입력: "))

if n in list_num:
    print(f"{n}은 목록 안에 있습니다")
else:
    print(f"{n}은 찾을 수 없습니다")
'''
a = int(input("첫번째 값: "))
b = int(input("두번째 값: "))

if a % 2 == 1 and b % 2 == 1: #둘다 홀수
    print(a**2 + b**2)
elif a % 2 == 0 and b % 2 == 0: #둘다 짝수
    print(abs(a-b))
else:                            #홀짝 하나씩
    print(2*(a+b))

