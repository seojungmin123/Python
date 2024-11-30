'''
#5
if 6>3:
    print("크다")
print("끝")

#7
if 4>3:
    print("A")
print("B")

#6
if 5==5:
    print("A")
    print("B")

#8
print("비교")
if 6==3:
    print("틀리다")

#9
if 10>4:
    print("big")
else:
    print("small")

#11
if 2+3>4:
    print("plus")
else:
    print("no")

#10
if 10 != 10:
    print("diff")
else:
    print("same")

#12
if 5< 4-1:
    print("minus")
else:
    print("no")

#

key = 5
if key <= 0:
    print("0이하")
elif key <=5:
    print("5이하")
else:
    print("10이하")
'''

import datetime
now = datetime.datetime.now()

if 3<= now.month <=5:
    print("봄입니다")
elif 6<= now.month <=8:
    print("여름입니다")
elif 9<= now.month <=11:
    print("가을입니다")
elif now.month == 12 or 1<= now.month <=2:
    print("겨울입니다")






