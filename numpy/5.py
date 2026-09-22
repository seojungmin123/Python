import numpy as np
# [ 브로드캐스팅 ]

# : 자동으로 크기를 맞춰서 연산

arr = np.arange(1,6)    # [1 2 3 4 5]

arr * 2  # [1 2 3 4 5] * [2 2 2 2 2]


m = np.array([[1, 2, 3],[4, 5, 6]])   # shape(2,3)
v = np.array([10,20,30])              # shape(3,)

print(m + v)    # [1 2 3] + [10 20 30]     
                # [4 5 6] + [10 20 30]


'''
브로드캐스팅이 안되는경우

같다 / 한쪽이 1이다 / 한쪽에 없다(자릿수 부족) - 1이거나 없는 쪽이 상대에 맞춰 늘어남

m + np.array([100, 200, 300]) O 

m: (2, 3)
v:    (3,)      뒤에서부터: 3 vs 3 같음 -> v가 2행으로 늘어남


m + np.array([100, 200]) X
# ValueError: operands could not be broadcast together with shapes (2,3) (2,)

m: (2, 3)
w:    (2,)      뒤에서부터: 3 vs 2 다름 -> 에러
'''

# 형태 바꿔서 계산하기
w = np.array([100, 200]).reshape(-1, 1)    # shape (2, 1) — 세로로 세움
print(m + w)

# 비교: 뒤에서부터 3 vs 1 -> 1이 늘어남 O, 2 vs 2 같음 O
# [[101 102 103]
#  [204 205 206]]      0행엔 +100, 1행엔 +200



# 연습
a = np.ones((3, 4))

a + np.ones(4)          # (O)  shape(4,)
# a + np.ones(3)          # (X)  shape(3,)
a + np.ones((3, 1))     # (O)  shape(3,1)
a + 5                   # (O)  shape(3,4)


data = np.array([[3, 7, 1, 9],
                 [4, 2, 8, 5],
                 [6, 0, 3, 2]])     

print(data - data.mean(axis=1, keepdims=True))


print(np.arange(1,10) * np.arange(1,10).reshape(9,1))


'''
[요약]
shape를 같은 자리끼리 비교해서 같다 / 한쪽이 1이다 / 한쪽에 없다 인경우 자동으로 크기를 맞춰 연산한다
'''