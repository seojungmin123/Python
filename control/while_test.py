'''
for i in range(1,101):
    print(i)

i = 1

while i <= 100:
    print(i)
    i = i + 1

i = 3

while i <= 5:
    print(i)
    i = i + 1


for i in range(1,14):
    print(f"{i}. 파이썬 최고")
    
i = 1

while i <= 13:
    print(f"{i}. 파이썬 최고")
    i = i + 1

i = 1

while i <= 100:
    if i % 5 == 0:
        print(i)
        i = i+1
    else:
        print(i, end=' ')
        i = i+1

while True:
    a = int(input("첫번째 값: "))
    b = int(input("두번째 값: "))
    print(f"두수의 합은 {a+b}입니다")
    if a == 0 and b == 0:
        break

x = 3
while x < 6:
    print(x)
    x += 1
'''
echo = input()
while echo != "exit":
    print(echo)
    echo = input()

echo = input()
while True:
    if echo =="exit":
        break
    print(echo)
    echo = input()

                                                         
    



