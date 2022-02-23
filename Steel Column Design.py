from ast import Pass
from re import A
from termios import FFDLY
import numpy as np

# Specify the amount of loading
def Load():
    if Pu == 0:
        Pu1 = 1.4*D
        Pu2 = 1.4*D + 1.6*L
        Pu = max(Pu1, Pu2)

# Select the cross section number
def Numbering():

    return

# Get the K value
def K():

    return 

# Get the Fcr value
def Fcr():
    Landa = (k*L)/rmin
    Fe=((np.pi**2)*E)/(Landa)**2
    if Landa <= 139:
        Fcr=(0.658**(Fy/Fe))*Fy
    else:
        Fcr=0.877*Fe
    return


def check():
    Pn=Fcr*A
    if (Pu/(0.9*Pn)) > 1:
        Pass
        # Return to Numbering and choose Higher one
    elif (Pu/(0.9*Pn)) < 0.85:
        Pass
        # Return to Numbering and choose Lower one
    else:
        Pass
        # OK




