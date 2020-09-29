import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns
from scipy.stats import norm

plt.figure (figsize = [12, 6])

# 근사하고 싶은 Target Distribution을 정의 
TargetDistribution = lambda x : norm.pdf(x)

# 던질 난수가 따르는 분포 (초기 샘플링 이후로 던져질 난수는 이 분포를 따른다.)
Delta = 0.5 ; ProposalDistribution = lambda x : x + np.random.uniform() * 2 * Delta - Delta

CountNumber = 100000

InitialSample = np.random.uniform() 
PreviousSample = InitialSample
SampleList = np.zeros (CountNumber)

"""
1. 근사하고 싶은 임의의 확률분포를 적어준다.
2. 계산을 반복할 횟수를 정한다. (n)
3. 구간 내에서 초기값 하나를 샘플링한다. 그리고 표준편차 Sigma를 따르는 제안분포를 정의한다.
    (Normal Distribution (PreviousSample, Sigma))
"""

i = 0
while i < CountNumber :
    
    # 초기 샘플링을 평균으로 가지는 제안분포에서 다음 샘플링에 쓸 값 하나를 추출한다.
    NextSample = ProposalDistribution (PreviousSample)
    
    # 다음 샘플링 값을 Target 함수에 넣었을 때의 값을 NextProb라 하고,
    # 이전 샘플링 값을 Target 함수에 넣은 값을 PreviousProb라 하자.
    NextProb = TargetDistribution (NextSample)
    PreviousProb = TargetDistribution (PreviousSample)
    
    # 임의의 샘플링 값을 하나 다시 던지고
    U =  np.random.uniform()
    
    # 1하고 Prob Ratio 중에서 더 작은 값을 택한다.
    Alpha =  np.min ((1, NextProb / PreviousProb))
    
    if U < Alpha :
        SampleList[i] = NextSample
        PreviousSample = NextSample
        i = i + 1
        # 위와 같이 NextSample을 SampleList에 넣고 그 조건을 승인한 상태이다.
        # 이제 이전 샘플은 필요가 없어졌으니, 다음 샘플을 이제 이전 샘플로 되돌린다.
        # 샘플링 값이 Alpha보다 크다면 그 조건은 기각한다. (else 문)
        
    else :
        SampleList[i] = PreviousSample
        PreviousSample = SampleList[i]
        i = i + 1
        
        
# Plotting Graph 
plt.subplot (1, 2, 1)
fig = plt.hist (SampleList, 30, alpha = 0.3)
fig = plt.hist (SampleList [300 : ], 30, alpha = 0.3)

plt.subplot (1, 2, 2)
plt.plot(SampleList)