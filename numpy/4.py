import numpy as np
# [ axis ]

m = np.array([[1, 2, 3],
              [4, 5, 6]])      # shape: (2, 3)

'''
          axis 1 →  (가로: 열 번호가 바뀌는 방향)
axis 0  [1  2  3]
  ↓     [4  5  6]
(세로: 행 번호가 바뀌는 방향)

집계에 axis를 주면 그 방향으로 합침
'''

m.sum(axis=0)    # 세로로 눌러 합치기  

'''
[1  2  3]
 ↓  ↓  ↓         세로로 눌러서
[4  5  6]
─────────
[5  7  9]        열별 합계
'''

m.sum(axis=1)    # 가로로 눌러 합치기

'''
[1  2  3] → 6        가로로 눌러서
[4  5  6] → 15       행별 합계
'''


m.mean(axis=1)                   # shape(2,) 
m.mean(axis=1, keepdims=True)    # shape(2,1)  차원(형태) 유지


# 연습

data = np.array([[3, 7, 1, 9],
                 [4, 2, 8, 5],
                 [6, 0, 3, 2]])     # shape (3, 4)


print(data.sum(axis=0)) # shape (4,)
print(data.sum(axis=1)) # shape (3,)


# 최고값
print(data.max(axis=0))
# 평균
print(data.mean(axis=1))



'''
[요약]
1. axis 는 배열의 방향에 붙은 번호  axis=0 <- 세로, axis=1 <- 가로
2. 집계함수에 쓰여서 방향대로 누를 수 있다
3. axis=k로 집계하면, shape에서 k번째 숫자가 지워진다. 남는 게 결과의 shape이다 
'''

