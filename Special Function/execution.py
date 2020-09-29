import math
import random
import numpy as np
import matplotlib.pyplot as plt

# plt.plot을 위한 기본 설정
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams['axes.grid'] = True 

# 감마 함수의 몬테카를로 계산기를 구현
# 컴퓨터에서는 무한대 적분을 구현할 수 없기에, 치환적분을 하여 적분 구간을 (0, 1)로 변환해주었다.
def build_GaamaFunction (beta, NUMBER):
    
    result = 0
    
    for index in range (NUMBER):
        random_numbers = random.uniform (0.00000, 1.00000)
        body = (1-random_numbers)/random_numbers
        Single_Result = (body ** (beta - 1)) * math.exp(-body) * (1/random_numbers ** 2)
        result = Single_Result + result
        
    result = result / NUMBER
    return result
        
# 시행횟수가 많아지면 값이 어떻게 수렴하는지 알고싶다.
# 그래서 서로 다른 시행횟수의 결과값들을 저장
Summation_List = []

# 원하는 감마함수의 인자를 지정
beta = math.pi

# 몬테카를로 방법 N = 1부터, N = 10000까지 반복 시행
for index in range (1, 10000):
    result = 0
    result = build_GaamaFunction(beta, index)
    Summation_List.append (result)
    
    # Gaama(math.pi)의 값은 2.276819287919715로 굉장히 잘 수렴한다.
    
plt.plot(Summation_List, color = "maroon", linewidth = 1.0)
print (Summation_List[10000-2])

