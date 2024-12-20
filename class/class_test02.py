#변수 컨테이너변
#함수
#클래스 메소드 - 객체 지향
'''
class Stu_Score:
    def __init__(self,name,kor,eng,math): #생성자
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def sum_score(self): #총점을 구하는 메소드
        return self.kor+self.eng+self.math
    def avg_score(self): #평균을 구하는 메소드
        return int(self.sum_score()/3)
    def print_score(self): #출력하는 메소드
        print(self.name, self.sum_score(), self.avg_score(), sep='\t')

students = [
    Stu_Score('김윤후',87,90,82), #객체생성
    Stu_Score('김운후',66,90,82),
    Stu_Score('김휸우',23,90,82),
    Stu_Score('긴윰후',34,90,82),
    Stu_Score('긴유훈',100,90,82),
    Stu_Score('힘윤구',63,90,82)
    ]

print('이름', '총점', '평균', sep='\t')
for student in students: #6번 실행
    student.print_score()
'''

class Car:
    def __init__(self,type,speed):
        self.type = type
        self.speed = speed

    def move(self):
        print(self.type + "가 "+ str(self.speed) + " 속도로 움직입니다.")

    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount


c = Car("스포츠카", 100)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move(
