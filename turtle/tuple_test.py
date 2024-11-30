'''
my_tuple = ("사과","메론","포도","토마토","사과")
#my_tuple.append ("수박") 튜플은 값 추가 불가
#my_tuple.remove ("사과") 튜플은 값 삭제 불가
print(my_tuple[:3])
print(len(my_tuple))
print("샤인머스캣" not in my_tuple)
'''

my_tuple = ("사과","메론","포도")
(f1,f2,f3) = my_tuple
number = (1,2,3,4,5,6,7,8,9,10)
(*others,n9,n10) = number
print(n10)
print(n9)
print(others)
