# MNIST 손글씨 인식 실습

3Blue1Brown 딥러닝 1편 참고,
784-64-16-10 구조로 신경망을 만들어서 손글씨 숫자 판별


## 파일

- `01_neuron.ipynb` : 뉴런 하나를 numpy로 직접 계산 (가중합 + 편향 + 시그모이드)
- `02_mnist_pytorch.ipynb` : MNIST 학습, 가중치 그림 그리기, 판별 과정 보기


## 실행 방법

VS Code 터미널에

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install numpy torch torchvision matplotlib ipykernel
```

PowerShell에서 활성화가 막히면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` 를 한 번 실행

그다음 노트북을 열고 오른쪽 위에서 커널을 `.venv`로 고른 뒤 위에서부터 차례로 실행한다


## 모델

```
Flatten(784) → Linear(784,64) → Sigmoid → Linear(64,16) → Sigmoid → Linear(16,10)
```

가중치와 편향 합쳐서 51,450개


## 결과

| 첫 번째 층 뉴런 수 | 정확도 (5 epoch) |
|---|---|
| 16 | 0.924 |
| 64 | 0.959 |

뉴런수가 64개일 때 정확도가 높게 찍혔다



## 참고

- 3Blue1Brown, But what is a neural network? (유튜브)
- PyTorch 문서 https://pytorch.org/docs/