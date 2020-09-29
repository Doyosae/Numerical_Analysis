import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns

pd.set_option ('display.width', 500)
pd.set_option ('display.max_column', 100)

TargetDistribution = lambda x : 6*x*(1-x)
sigma = 0.1
CountNumber = 100000

InitialSample = np.random.uniform() 
PreviousSample = InitialSample
SampleList = []

"""
1. 근사하고 싶은 임의의 확률분포를 적어준다.
2. 만족할때까지 샘플링하여 계산을 반복할 횟수를 정한다. (n)
3. 정의역 내에서 초기값 하나를 샘플링한다. 그리고 표준편차 Sigma를 따르는 제안분포를 정의한다. (Normal Distribution (PreviousSample, Sigma))
4. 이미 샘플링한 값을 평균으로 하는 제안분포를 따르는 다음 샘플링 값 하나를 다시 추출한다.
5. 이미 샘플링한 값을 PreviousSample, 다음에 샘플링한 값을 NextSample이라 부르자.
이 과정은 아래의 While 문에서 구현하였다.
"""

i = 0

while i < CountNumber :
    NextSample = np.random.normal(PreviousSample, sigma)
    
    while  (NextSample <0) | (NextSample > 1) :
        NextSample = np.random.normal(PreviousSample, sigma)
        
        # 다음 샘플링 값이 0보다 작거나, 1보다 크면 버리고 다시 샘플링하여 값을 추출한다.
        # (왜냐하면 확률 분포의 값이 0 ~ 1에서 정의되기 때문)
        # 매우 중요한 사실, 추정하고자 하는 확률분포의 정의역에 따라 채택하는 범위는 달라질 수 있음
    
    NextProb = TargetDistribution (NextSample)
    PreviousProb = TargetDistribution (PreviousSample)
    Alpha =  NextProb / PreviousProb
    U =  np.random.uniform()
    
    # NextSample을 확률분포에 넣어서 그 값에 해당하는 Prob를 계산
    # PreviousSample을 확률분포에 넣어서 그 값에 해당하는 Prob를 계산
    # 그리고 0 ~ 1 사이의 균등분포를 가지는 임의의 값 하나를 추출 (다음 표본이 기각될지 안될지를 결정하는 변수)
    # Metropolis Hastings 알고리즘에 따라서, 사후 확률 / 사전 확률의 비인 Acceptance Prob를 정의한다.
    # 확률로써 작동하는 Alpha와의 크기 비교를 하고 U가 Alpha보다 작다면 승인
    
    if U < Alpha :
        SampleList.append (NextSample)
        PreviousSample = NextSample
        i = i + 1
        
        # 위와 같이 NextSample을 SampleList에 넣고 그 조건을 승인한 상태이다.
        # 이제 이전 샘플은 필요가 없어졌으니, 다음 샘플을 이제 이전 샘플로 되돌린다.
        # 샘플링 값이 Alpha보다 크다면 그 조건은 기각한다.     
    else :
        SampleList.append(PreviousSample)
        SampleList[i] = PreviousSample
        i = i + 1
        
e, q, h = plt.hist(SampleList, 1000, alpha=0.5, color = 'darkred')
PartitionSpace = np.linspace(0, 1, 100)
plt.plot (PartitionSpace, 0.55 * np.max(e) * TargetDistribution(PartitionSpace), alpha = 20, color = 'black')
plt.show ()