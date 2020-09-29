"""
Simplely Ising model
"""
import os, random
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


class ISING_Model ():
    
    def __init__ (self, number = 300, time = 2.0):
        
        self.number = number
        self.time = time
        self.beta = 1 / self.time
        
        self.iteration = 0
        self.isingState = np.ones ((number, number))
        self.deltaEnergy = np.zeros ((number, number))

        for index1 in range (self.number) : 
            for index2 in range (self.number) : 
                if random.random() > 0.5:
                    self.isingState[index1, index2] = -self.isingState[index1, index2]
                    
    def initial_plot (self):
        plt.imshow(self.isingState)
        
    def spin_Calculator(self, row, column):
        
        initial = self.isingState[row, column]
        out1 = self.isingState[(row-1)%self.number, column]
        out2 = self.isingState[(row+1)%self.number, column]
        out3 = self.isingState[row, (column-1)%self.number]
        out4 = self.isingState[row, (column+1)%self.number]

        output = initial*(out1 + out2 + out3 + out4)

        return output
    
    
    def simulation(self, end = 100):
        
        while self.iteration < end : # 총 300회를 반복할 것
            self.iteration = self.iteration + 1 
            
            for row in tqdm(range (self.number)) :       
                for column in range (self.number) :
                    self.deltaEnergy[row, column] = self.spin_Calculator(row, column)

                    # row 행에서 스핀값을 바꾸는 것, column 행에서 스핀값을 바꾸는 것
                    # DeltaEnergy를 계산한다. 나의 상태에서 주변 애들이 받는 스핀 변화를 모아서 계산한다.
                    # 이 에너지 변화량이 이전보다 커질까 작아질까???

                    if self.deltaEnergy[row, column]  < 0 or \
                        random.random() < np.exp(-2*self.beta*self.deltaEnergy[row, column]) :
                        # 에너지 변화량이 0보다 작으면 옳다.
                        # 에너지 변화량 계산식에서 전체 항의 계수가 양수이므로 에너지 감소는 마땅하고
                        # 또 그 조건에서 해당 격자점의 스핀이 뒤집혀져야 한다.
                        # 에너지 변화량이 0보다 크면 방향을 바꾸지 않는다. (기각 과정)
                        self.isingState[row, column] = -self.isingState[row, column]
                           
            plt.imshow(self.isingState)
            plt.savefig("/Users/doyosae/Desktop/ising/" + str(self.iteration) + ".jpeg")


            
# model demostatration
if __name__ == '__main__':

    plt.rcParams ["figure.figsize"] = (7, 7)
    plt.rcParams ['lines.linewidth'] = 0
    plt.rcParams ['lines.color'] = 'darkred'
    plt.rcParams ['axes.grid'] = False
    
    model = ISING_Model()
    model.initial_plot()
    model.simulation()
