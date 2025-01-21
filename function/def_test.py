#사용자 정의 함수

'''
def hello(name="방시혁",age=52,j="학생"):
    print("안녕하세요")
    print(f"제 이름은 {name}입니다")
    print(f"저의 직업은 {j}입니다")
    print(f"제 나이는 {age}입니다\n")

hello(j="HYBE 이사회 의장")
#hello("과즙세연",23,"BJ")
#hello("민희진",44,"ADOR CEO")
'''

#두 수의 합을 구하는 함수
'''
def add_num(f,s):
    print(f"{f}, {s}을 입력받았")
    hap = f + s
    return(hap)

hap = add_num(10,30)
print(f"두수의 합은 {hap}입니다")
'''



def scoreFunc(scoreList):

    total = sum(scoreList)
    avg = total/len(scoreList)
    max_score = max(scoreList)
    min_score = min(scoreList)
    return total, avg, max_score, min_score

score = [90,80,10,50,95]
total, avg ,max_score, min_score = scoreFunc(score)

print(f"합 : {total}\n평균 : {avg}\n최고점수 : {max_score}\n최저점수 : {min_score}")
