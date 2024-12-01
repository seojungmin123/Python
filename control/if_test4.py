'''
#홀짝판별

n = int(input("정수 하나를 입력하세요: "))
if n%2 == 1:
    print(f"{n}은 홀수입니다")
else:
    print(f"{n}은 짝수입니다")



#합격 탈락 판별

score = int(input("점수를 입력하세요: "))
if score >= 60:
    print("합격")
else:
    print("탈락")


#열날때 행동요령

temp = int(input("체온을 입력하세요: "))
if temp >= 40:
    print("당장 응급실 가세요")
elif temp >= 38:
    print("해열제 먹고 병원을 가세요")
elif 37 >= temp >= 36:
    print("학교로 가세요")
else:
    print("정상입니다 당장 학교로 가세요")
'''

#학점 판별

score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A학점 입니다")
elif score >= 80:
    print("B학점 입니다")
elif score >= 70:
    print("C학점 입니다")
elif score >= 60:
    print("D학점 입니다")
else:
    print("E학점 입니다")
