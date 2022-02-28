import numpy as np
import openpyxl as ex

def Excel():
    IPE = ex.load_workbook('Steel Full IPE.xlsx')
    IPE = IPE.active
    Number = IPE.cell(row=5, column=1).value
    A = IPE.cell(row=5, column=10).value
    r_x = IPE.cell(row=5, column=15).value
    r_y = IPE.cell(row=5, column=19).value
    Fy = IPE.cell(row=5, column=22).value
    E = IPE.cell(row=5, column=24).value
    return [A, r_x, r_y, Fy, E]
print(Excel(A))

# # Get the K value
# def K():

#     return 

# # Get the Fcr value
# def Fcr():
#     Landa_x = (k_x*L)/r_x
#     Landa_y = (k_y*L)/r_y
#     Landa = max(Landa_x,Landa_y)
#     Fe=((np.pi**2)*E)/(Landa)**2
#     if Landa <= 139:
#         Fcr=(0.658**(Fy/Fe))*Fy
#     else:
#         Fcr=0.877*Fe
#     return


# def check():
#     Pn=Fcr*A
#     if (Pu/(0.9*Pn)) > 1:
#         Pass
#         # Return to Numbering and choose Higher one
#     elif (Pu/(0.9*Pn)) < 0.85:
#         Pass
#         # Return to Numbering and choose Lower one
#     else:
#         Pass
#         # OK




