import pygame
import sys
pygame.init()

white=(255,255,255)
black=(0,0,0)
red = (255,0,0)
yellow = (255,255,0)

w = 480
h = 640

pad = pygame.display.set_mode((w,h)) #화면 생성
pygame.display.set_caption("Shooting Game") #제목 설정
pad.fill(("#EFF8FB"))


#도형 그리기


#선 그리기
'''
pygame.draw.line(pad, black, (30,50),(350,500),3)
pygame.draw.line(pad, yellow, (0,320),(480,320),3)
'''


#삼각형 그리기
pygame.draw.polygon(pad, red, ((240,60),(40,240),(440,240)))


#다각형 그리기


#사각형 그리기
pygame.draw.rect(pad, black, (40,240,400,300))
pygame.draw.rect(pad, yellow, (190,320,100,220))


#원 그리기
pygame.draw.circle(pad, white, (240,170),50)


 

#선 그리기
pygame.draw.line(pad, red, (240,120),(240,220),3)
pygame.draw.line(pad, red, (190,170),(290,170),3)



pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
