#예외처리
'''
str = "89점"
score = int(str)
print(score)


#=>예외처리
str = "89점"
try:
    score = int(str)
    print(score)
except:
    print("예외가 발생함")
print("작업완료")


while True: #무한반복문
    str = input("점수를 입력하세요: ")
    try:
        score2 = int(str)
        print("입력한 점수: ",score)
    except:
        print("점수형식이 잘못됨")
    break
'''

str = "91"
try:
    score = int(str)
    print(score)
    a = str[3]
except NameError:
    print("변수명 에러남")
except IndexError:
    print("리스트 범위 에러남")
