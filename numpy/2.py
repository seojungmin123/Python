import numpy as np
# [ 배열 생성 ]

np.zeros(5)        # [0. 0. 0. 0. 0.] 결과를 담을 공간을 미리 확보
np.ones(5)         # [1. 1. 1. 1. 1.] 전부 켜진 스위치판
np.full(5, 7)      # [7 7 7 7 7] 기본값으로 채워놓고 시작


a = np.array([[0,1,2],[3,4,5]])
np.zeros_like(a)   # a와 똑같은 모양(2행 3열)의 0 배열   _like


np.arange(0, 10, 2)       # 간격(2)을 알 때: 0 2 4 6 8            끝을 미포함
np.linspace(0, 10, 5)     # 개수(5)를 알 때: 0. 2.5 5. 7.5 10.    끝을 포함


# 부동소수점 오차
print(0.1 + 0.2 == 0.3)    # False
print(0.1 + 0.2)           # 0.30000000000000004

print(np.arange(0, 1, 0.1)) 
'''
오차가 누적되면서 마지막 값이 1.0 직전에서 애매하게 걸려, 끝값이 포함되거나 안 되거나가 불안정해짐
정수 간격 -> arange / 실수 수열 -> linspace (linspace는 개수 기준이라 오차 누적이 없음)

결과를 확인해야하면
np.isclose(a, 0.3)
'''

# dtype 지정
np.zeros(5, dtype=np.int64)     # 0. 이 아닌 정수 0으로
np.arange(5, dtype=np.float32)  # 딥러닝용 float32로

# 이미 있는 배열을 변환 : astype
a = np.array(["1", "2", "3"])   
b = a.astype(int)               # [1 2 3]

# astype 성질 1: 원본은 안 바뀐다
a.astype(int)
print(a.dtype)    

# astype 성질 2: float → int는 반올림이 아니라 "버림"
np.array([3.9, -1.7]).astype(int)    # [3, -1]



# 연습
# 1. 그래프 x축용으로 -5부터 5까지 정확히 100개의 점
print(np.linspace(-5,5,100))

# 2. 1부터 100까지 7의배수 전부
print(np.arange(7,100,7))

# 3. 0초부터 2초까지 0.01초 간격의 시간축
print(np.linspace(0,2,201))

# 4. 오류
# np.array(["1.5", "2.5"]).astype(int)

# 5. 수정
np.array(["1.5", "2.5"]).astype(float).astype(int)


'''
[요약]

1. zeros(0으로 채우기), ones(1로 채우기), full(지정한 숫자로 채우기) arange(정수 간격) linspace(정해진 개수)로 배열생성가능
2. 소수끼리 연산하면 숫자가 아주조금 어긋나는 부동소수점 오차 발생 -> "=="말고 "np.isclose()"
3. dtype으로 미리 지정, astype으로 이미 있는 배열을 변환하며 복제 b = a.astype(...)
'''