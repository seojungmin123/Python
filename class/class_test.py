'''
#클래스와 

class Monster: #클래스 정의
    def __init__(self,name,age,speed):#생성자
        self.name = name
        self.speed = speed
        self.age = age
    def say(self):
        print(f"내 이름은 {self.name}이고 내 나이는 {self.age}살임")
    def run(self):
        print(f"{self.name}의 속도는 {self.speed}임")
    def level(self):
        print(f"{self.name}의 속도는 {self.speed}임")

wolf = Monster('늑대',10,30)#객체
shark = Monster('상어',1,100)
king = Monster('제왕',17,3)

wolf.say()
shark.say()
king.say()

wolf.run()
shark.run()
king.run()



#성적 프로그램 (총점 평균 구하기) - 절차형언어

#학생성적리스트
students = [
    {'name':'유우진','korean':90,'english':89,'math':80},
    {'name':'우유진','korean':20,'english':69,'math':70},
    {'name':'유운지','korean':30,'english':39,'math':60},
    {'name':'우윤지','korean':10,'english':49,'math':50},
    {'name':'우이쥰','korean':40,'english':19,'math':40},
    {'name':'진우유','korean':25,'english':29,'math':30}
    ]


print('이름','총점','평균',sep = '\t')
for student in students:
    score_sum = student['korean'] + student['english'] + student['math']
    score_avg = score_sum/3
    print(student['name'], score_sum, score_avg,sep='\t')


#성적 프로그램 (총점 평균 구하기) - 절차형언어(함수)  


#학생성적리스트
students = [
    {'name':'유우진','korean':90,'english':89,'math':80},
    {'name':'우유진','korean':20,'english':69,'math':70},
    {'name':'유운지','korean':30,'english':39,'math':60},
    {'name':'우윤지','korean':10,'english':21,'math':50},
    {'name':'우이쥰','korean':40,'english':19,'math':40},
    {'name':'진우유','korean':25,'english':29,'math':30}
    ]


def score_sum(student):
    return student['korean'] + student['english'] + student['math']
def score_avg(student):
    return int((score_sum(student))/3)
def score_print(student):
    print(student['name'], score_sum(student), score_avg(student),sep='\t')

  


print('이름','총점','평균',sep = '\t')
for student in students:
    score_print(student)
'''
#성적 프로그램 (총점 평균 구하기) - 객체지향형언어(함수)
    
class Stu:
    def __init__(self,name,korean,english,math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
    def score_sum(student):
        return student['korean'] + student['english'] + student['math']
    def score_avg(student):
        return int((score_sum(student))/3)
    def score_print(student):
        print(student['name'], score_sum(student), score_avg(student),sep='\t')
        
print('이름','총점','평균',sep = '\t')
for student in students:
    score_print(student)
        
