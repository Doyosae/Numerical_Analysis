import math
import numpy as np
import matplotlib.pyplot as plt


x = 0.00001
Scale = 100000
MaxBoundary = 800000
MaxListBoundary = MaxBoundary-1

ControlVariable = input("Enter a compelx number that you want.")

Function_list = []
Real_Parts = []
Imag_Parts = []

# 주어진 식을 계산하는 모듈
def Calculator_module (x):
    
    Chunk1 = math.exp(5.88235*(2.4-x)) + 1
    Chunk2 = x*x + x*complex(ControlVariable)
    
    Chunk1_module = 5.6j / Chunk1
    Chunk2_module = 81.1801 / Chunk2
    fraction = Chunk1_module + 8.84 - Chunk2_module
    domoniator = Chunk1_module + 11.84 - Chunk2_module
    
    outputs = fraction / domoniator
    
    return outputs


# 하나씩 다 대입한다 0.0001 단위로 1 ~ 8000 계산
for index in range (1, MaxBoundary):
    Calculating = x * index
    Function_Value = Calculator_module(Calculating)
    Function_list.append(Function_Value)
    
for index in range (0, MaxListBoundary):
    Real_Parts.append(Function_list[index].real)
    Imag_Parts.append(Function_list[index].imag)


# 주의사항, 가로축 척도를 1000으로 나누어 볼껏
# ex, 0 ~ 8000 -> 0 ~ 8
fig = plt.figure(figsize=(20, 30)) 

FONTSIZE = 40
LINEWIDTH = 2.0
NUMBERING = 1

plt.subplot(311)
plt.title("Real Value", size = FONTSIZE)
plt.plot(Real_Parts, color = 'darkred', linewidth = LINEWIDTH)

plt.subplot(312)
plt.title("Image Value", size = FONTSIZE)
plt.plot(Imag_Parts, color = 'darkred', linewidth = LINEWIDTH)

print("Print Local Maxixmum Position of Imaginary Part ")
print(max(Imag_Parts))
print("Print X Position about Local Maxixmum Position of Imaginary Part ")
print(Imag_Parts.index(max(Imag_Parts))/Scale)


# Image_Parts_WidthList = []
# Image_Parts_HeightList = []
# for index in range (500):
#     Image_Parts_WidthList.append((Imag_Parts.index(max(Imag_Parts))-250 + index)/Scale)
#     Image_Parts_HeightList.append(Imag_Parts[Imag_Parts.index(max(Imag_Parts))-250 + index])
    
# file_write = open("Log.txt", "w")
# for index in range (500):    
#     file_write.write(str(Image_Parts_WidthList[index])    +    str(Image_Parts_HeightList[index]) + "\n")
# file_write.close
