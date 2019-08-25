import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
# from matplotlib import colors as cnames
# from mpl_toolkits.mplot3d import Axes3D



def Build_DrawingGraph(XS, YS, ZS):
    
    plt.rcParams["figure.figsize"] = (20, 15)
    plt.rcParams["lines.linewidth"] = 1.0
    plt.rcParams["axes.grid"] = False

    fig = plt.figure()
    ax = fig.gca(projection = "3d")

    ax.plot(XS, YS, ZS, color = "darkred")
    ax.set_title("Visualization Lorenz Equation", size = 30)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    plt.show()
    
    
def Build_CalculateEquation(class_name):
    XS = np.empty(CalculateSteps+1)
    YS = np.empty(CalculateSteps+1)
    ZS = np.empty(CalculateSteps+1)
    XS[0], YS[0], ZS[0] = (1., 1., 1.)

    for index in range(CalculateSteps):
        X_deriv, Y_deriv, Z_deriv = class_name.Build_LorenzEquation (XS[index], YS[index], ZS[index])
        XS[index+1] = XS[index] + (X_deriv * DerivTime)
        YS[index+1] = YS[index] + (Y_deriv * DerivTime)
        ZS[index+1] = ZS[index] + (Z_deriv * DerivTime)
    
    
class Lorenz_Equation():
    
    # Define List for Posiotiona information Saving
    # Define Axis Position Initialization
    DerivTime = 0.01
    CalculateSteps = 9999
    
    def __init__(self, Sigma, Beta, Rho):
    
        # Define Constant for Lorenz Equation
        # Default Value is
        # Sigma = 10
        # Beta = 8./3
        # Rho = 28
        self.Sigma = Sigma
        self.Beta = Beta
        self.Rho = Rho

    def Build_LorenzEquation(self, X,  Y,  Z):

        X_deriv = self.Sigma * (Y - X)
        Y_deriv = X * (self.Rho - Z) - Y
        Z_deriv = X * Y - self.Beta * Z
        
        outputs = X_deriv, Y_deriv, Z_deriv
        return outputs



Lorenz = Lorenz_Equation(10, 8./3, 28)
Build_CalculateEquation(Lorenz)
Build_DrawingGrph(XS, YS, ZS)
