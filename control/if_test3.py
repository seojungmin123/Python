'''
today = input("요일을 입력하세요: ")

if today == "일요일":
    print("게임 세 판합시다")
print("공부 시작")



today = input("요일을 입력하세요: ")

if today == "일요일":
    print("게임 세 판합시다")
else:
    print("게임 한 판합시다")
print("공부 시작")


today = input("요일을 입력하세요: ")

if today == "일요일":
    print("게임 열 판합시다")
elif today == "토요일":
    print("게임 세 판합시다")
else:
    print("한잔해")
print("공부 시작")


total = int(input("입장인원을 입력하세요: "))

if total <= 4:
    print("추가비용없습니다")
elif total == 5:
    print(f"추가비용은 {total - 4}만원 입니다")
elif total == 6:
    print(f"추가비용은 {total - 4}만원 입니다")
elif total == 7:
    print(f"추가비용은 {total - 4}만원 입니다")
elif total == 8:
    print(f"추가비용은 {total - 4}만원 입니다")
else:
    print("입장인원은 최대 8명입니다")
'''
    

total = int(input("입장인원을 입력하세요: "))

if total <= 4:
    print("추가비용없습니다")
elif total >= 5 and total <=8:
    print(f"추가비용은 {total - 4}만원 입니다")
else:
    print("입장인원은 최대 8명입니다")











