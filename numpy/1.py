import numpy as np
import time
'''
[ ndarray ]

파이썬 리스트[1,2,3]은 숫자를 직접담지않고 저장된 위치를 담은 주소록
그래서 리스트는 [1, "안녕", 3.14, [5, 6]]처럼 아무거나 섞어 담을 수 있지만 꺼내오는 과정이 매번 필요함

NumPy배열(ndarray = n-dimensional array)은 숫자들을 빈틈없이 일렬로 직접 저장
이동이 필요없고 연속된 데이터를 한꺼번에 잘 처리하도록 설계되어 통째로 계산가능

조건: 모든 데이터의 타입이 같아야한다(dtype)
'''

a = np.array([1, 2, 3])
print(a.dtype)          # int64  <- 64비트 정수


# 다를경우 bool < 정수 < 실수 < 문자열 순으로, 정보 손실 없이 담을 수 있는 넓은 쪽으로 알아서 맞춤
b = np.array([1, 2, 3.5])
print(b)          # [1.  2.  3.5]  <- 전부 실수가 됨
print(b.dtype)    # float64

c = np.array([1, 2, "셋"])
print(c)          # ['1' '2' '셋']  <- 전부 문자열이 됨
print(c.dtype)    # <U11 (문자열 타입)



# 속도 실측

n = 10_000_000
lst = list(range(n)) # 리스트
arr = np.arange(n) # NumPy 배열

start = time.time()
lst2 = [x * 2 for x in lst]
print(f"리스트 : {time.time() - start}") # 리스트 : 0.8863937854766846

start = time.time()
arr2 = arr * 2
print(f"배열 : {time.time() - start}") # 배열 : 0.02586817741394043  약 34배 차이


# nbytes 

print(np.array([1, 2, 3]).nbytes)        # 24
print(np.array([1.5, 2.5, 3.5]).nbytes)  # 24
# int64와 float64는 둘 다 64비트 = 8바이트라 칸 크기가 같음 (3개 × 8 = 24)

# dtype 이름 뒤 숫자 = 비트 수
# 칸 크기는 선택 가능 (int8, int16, int32, int64 / float32, float64)
a = np.array([1, 2, 3], dtype=np.int8)   # 1바이트짜리 칸
print(a.nbytes) 

# 오버플로우 조심
b = np.array([100], dtype=np.int8)
print(b + 100)    # 200이 아니라 -56 (-128 ~ 127)


'''
[요약]

1. 리스트는 주소록(값의 위치만 저장 -> 유연하지만 배달 비용), 
   ndarray는 연속 창고(값을 직접 일렬 저장 -> 통째 계산 가능, 실측 약 34배 빠름)

2. 창고 구조의 대가로 모든 원소는 한 타입(dtype)이어야 하며,
   섞이면 손실 없는 넓은 쪽으로 자동 통일: bool < int < float < 문자열 (True는 1이 됨)

3. 칸 크기는 선택 가능(int8~64, float32/64, 이름 뒤 숫자 = 비트 수).
   작은 칸은 메모리 절약 대신 오버플로 위험 (int8에서 100+100 = -56)
'''