import numpy as np
# [ 인덱싱, 슬라이싱 ]

# # 리스트
# lst = [1, 2, 3, 4, 5]          # 배열 생성
# lst2 = lst[1:4]                # 배열 슬라이싱
# lst2[0] = 999                  # 배열 수정
# print(lst)                     # [1, 2, 3, 4, 5]  리스트는 그대로 (copy)

# # NumPy
# a = np.array([1, 2, 3, 4, 5])  # 배열 생성
# b = a[1:4]                     # 배열 슬라이싱
# b[0] = 999                     # 배열 수정
# print(a)                       # [ 1 999 3 4 5 ]  a가 바뀜 (view)

# # NumPy는 성능을 위해 "복사 안 함"을 기본값으로 택함

# b = a[1:4].copy()    # 복사가 필요하면 .copy()
# b[0] = 999
# print(a)             # [1 2 3 4 5]  원본 그대로


'''
슬라이싱	   a[1:4], a[:, 0]	 뷰
불리언 인덱싱	a[a > 2]	      복사
팬시 인덱싱	    a[[0, 2, 4]]	  복사 
astype 등 변환  a.astype(float)	  복사 


.base로 원본 확인하기
b = a[1:4]
print(b.base is a)     # True  → b는 a의 뷰

c = a[[0, 2]]
print(c.base is a)     # False → c는 독립된 복사본

'''

# 1
# (a) 슬라이싱(뷰) -> 변함
a = np.arange(5); b = a[2:]; b[:] = 0; print(a)  # [0 1 0 0 0]
# (b) 불리언 인덱싱(복제) -> 안변함
a = np.arange(5); b = a[a % 2 == 0]; b[:] = 0; print(b.base is a) # [0 1 2 3 4]
# (c) 복제 -> 안변함 
a = np.arange(5); b = a[1:4].copy(); b[0] = 99; print(a) # [0 1 2 3 4]


# 2
m = np.arange(12).reshape(3,4)
row = m[0]    # m[0, :] -> [0 1 2 3]
row[0] = 999  # [999 1 2 3]
print(m)      # 슬라이싱(뷰) 이라서 변함


# 3
scores = np.array([88, 92, 79, 95, 85])
b = scores[[3,1,0]] + 5 # 팬시 인덱싱(복제)이라 안변함
print(b)


'''
[요약]
1. 불리언, 팬시인덱싱으로 복제하는 방법과 슬라이싱(뷰)로 원본 수정이 가능한 방법이있다 뷰가 속도는 훨씬 빠름
2. b.base is a로 원본을 확인 가능하다 True = 뷰 , False = 복제
3. 뷰를 만들고 대입 ( = ) 할때 원본이 오염되는 것이고 연산을 할때는 안전
'''
