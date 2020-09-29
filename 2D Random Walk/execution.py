#!/usr/bin/env python
# coding: utf-8

# In[126]:


import numpy as np
import random as rand
import matplotlib.pyplot as plt


class RandomWalk ():
    
    def __init__ (self, stepestNumber = 2000):
        
        self.stepestNumber = stepestNumber
        self.widthAxis = np.zeros(stepestNumber)
        self.heighAxis = np.zeros(stepestNumber)
        
    def simulation (self):
        
        """
        몬테카를로 방법을 이용하여 자유입자의 random walk 시뮬레이션
        """
        for k in range (1, self.stepestNumber) : 
            randomValue = rand.randint(1, 4)
            # 1, 2, 3, 4 중 하나를 랜덤으로 던진다.

            if randomValue == 1 : 
                self.widthAxis[k] = self.widthAxis[k - 1] + 1
                self.heighAxis[k] = self.heighAxis[k - 1]
            # RandomValue가 1이면 X 좌표의 값을 1 늘린다.
            elif randomValue == 2 : 
                self.widthAxis[k] = self.widthAxis[k - 1] - 1
                self.heighAxis[k] = self.heighAxis[k - 1] 
            # RandomValu가 2이면 X좌표의 값을 1 뺀다.
            elif randomValue == 3 : 
                self.widthAxis[k] = self.widthAxis[k - 1] 
                self.heighAxis[k] = self.heighAxis[k - 1] + 1
            # RandomValu가 2이면 Y좌표의 값을 1 뺀다.
            else : 
                self.widthAxis[k] = self.widthAxis[k - 1] 
                self.heighAxis[k] = self.heighAxis[k - 1] - 1
                
        plt.figure(figsize = (8, 8))
        plt.plot(self.widthAxis, self.heighAxis, 
                linewidth = 1.2, color = 'darkred', alpha = 1.0)
        plt.show()
        
        
if __name__ == '__main__':
    
    model = RandomWalk()
    model.simulation()