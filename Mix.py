# design column object
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk
from turtle import pu


IPB = pd.read_excel('Steel Full.xlsx', 'IPB')
IPE = pd.read_excel('Steel Full.xlsx', 'IPE')

class designColumn():

    def __init__(self, inputValue):
        ''' input value in this class is a list that is
        1)frame
        2)Pu
        3)length of column
        4)E
        5)Fy
        6)K
        7) (if it's exist) length of bay '''

        self.frame = inputValue[0]
        self.Pu = inputValue[1]
        self.lengthColumn = inputValue[2]
        self.E = inputValue[3]
        self.Fy = inputValue[4]
        self.K = inputValue[5]
        self.IPB = inputValue[6]
        self.IPE = inputValue[7]
        try:
            self.lengthOpening = inputValue[8]
        except:
            None

    def SingleColumn_IPB(self):
        A = self.IPB.loc[3:, 'مساحت']
        r_x = self.IPB.loc[3:, 'شعاع ژیراسیون حول محور x-x']
        r_y = self.IPB.loc[3:, 'شعاع ژیراسیون حول محور y-y']
        Fy = self.IPB.loc[3:3, 'تنش تسلیم']
        E = self.IPB.loc[3:3, 'مدول الاستیسیته']
        FS_list = []
        j = 0
        for i in range(3, 27):
            r_min = min(r_y[i], r_x[i])
            landa = (self.K * self.lengthColumn * 100) / r_min
            Fe = ((np.pi ** 2) * E) / (landa ** 2)
            if landa <= 139:
                Fcr = (0.658 ** (Fy / Fe)) * Fy
            else:
                Fcr = 0.877 * Fe
            Pn = Fcr * A[i]
            FS = self.Pu / (0.9 * Pn)
            FS_list.append(list(FS)[0])
            if 0.75 <= list(FS)[0] <= 1:
                return IPB.loc[i, 'IPB']
        # if FS wasn't between 1 and 0.75 we choose nearest FS to 0.75
        distance = []
        for i in FS_list:
            distance.append(abs(i - 0.75))
        j = distance.index(min(distance)) + 3
        return IPB.loc[j, 'IPB']

    def SingleColumn_IPE(self):
        A = self.IPE.loc[3:, 'مساحت']
        r_x = self.IPE.loc[3:, 'شعاع ژیراسیون حول محور x-x']
        r_y = self.IPE.loc[3:, 'شعاع ژیراسیون حول محور y-y']
        Fy = self.IPE.loc[3:3, 'تنش تسلیم']
        E = self.IPE.loc[3:3, 'مدول الاستیسیته']
        FS_list = []
        j = 0
        for i in range(3, 27):
            r_min = min(r_y[i], r_x[i])
            landa = (self.K * self.lengthColumn * 100) / r_min  
            Fe = ((np.pi ** 2) * E) / (landa ** 2)
            if landa <= 139:
                Fcr = (0.658 ** (Fy / Fe)) * Fy
            else:
                Fcr = 0.877 * Fe
    
            Pn = Fcr * A[i]
            FS = self.Pu / (0.9 * Pn)
            FS_list.append(list(FS)[0])
            if 0.75 <= list(FS)[0] <= 1:
                return IPE.loc[i, 'IPE']
         # if FS wasn't between 1 and 0.75 we choose nearest FS to 0.75
        distance = []
        for i in FS_list:
            distance.append(abs(i - 0.75))
        j = distance.index(min(distance)) + 3
        return IPE.loc[j, 'IPE']
    
    def Doublecolumn_IPE(self):
        A1 = self.IPE.loc[3:, 'مساحت']
        b = self.IPE.loc[3:, 'عرض بال']
        r_x1 = self.IPE.loc[3:, 'شعاع ژیراسیون حول محور x-x']
        r_y1 = self.IPE.loc[3:, 'شعاع ژیراسیون حول محور y-y'] # اضافه
        I_x1 = self.IPE.loc[3:, 'ممان اینرسی حول محور x-x']
        I_y1 = self.IPE.loc[3:, 'ممان اینرسی حول محور y-y']
        Fy = self.IPE.loc[3:3, 'تنش تسلیم']
        E = self.IPE.loc[3:3, 'مدول الاستیسیته']
        FS_list = []
        j = 0
        for i in range(3, 27):
            A = 2*A1[i]
            I_x = 2*I_x1[i] # اضافه
            I_y = 2*(I_y1[i] + A1[i]*(b[i]/2)**2)
            r_x = r_x1[i]
            r_y  = (I_y/A)**0.5
    
            r_min = min(r_y, r_x)
            landa = (self.K * self.lengthColumn * 100) / r_min

            Fe = ((np.pi ** 2) * E) / (landa ** 2)
            if landa <= 139:
                Fcr = (0.658 ** (Fy / Fe)) * Fy
            else:
                Fcr = 0.877 * Fe
    
            Pn = Fcr * A
            FS = self.Pu / (0.9 * Pn)
            FS_list.append(list(FS)[0])
            if 0.75 <= list(FS)[0] <= 1:
    
                return IPE.loc[i , 'IPE']

inputValue = ['1d', 84012.05, 2.7, 2100000, 2400, 1, IPB, IPE]
column = designColumn(inputValue)

def printing():
    Lis.insert(END, f'Best performance for IPB sections: IPB{int(column.SingleColumn_IPB())}' )
    Lis.insert(END, f'Best performance for IPE sections: IPE{int(column.SingleColumn_IPE())}' )
    Lis.insert(END, f'Best performance for 2IPE sections: 2IPE{int(column.Doublecolumn_IPE())}' )

a = column.SingleColumn_IPB()
b = column.SingleColumn_IPE()
c = column.Doublecolumn_IPE()
print(a)
print(b)
print(c)


# Start GUI by Tkinter
# Clear Button
def cls():
    Lis.delete(0, END)
    # plt.cla()

# Window settings
W = Tk()
W.title("Steel Column Design")
W.geometry('350x600')

# Scrollbar
Scr = Scrollbar(W)
Scr.pack(side=RIGHT, fill=BOTH)
frame1 = Frame(W)
frame1.pack(expand=True, fill=BOTH)

# Menu 
menu = Menu(W)
M1 = Menu(menu, tearoff=0)
M1.add_command(label='New File')
M1.add_command(label='Open File...')
M1.add_command(label='Save')
M1.add_command(label='Save As...')
M1.add_command(label='Close', command=W.quit)
M2 = Menu(menu, tearoff=0)
M2.add_command(label='Undo')
M2.add_command(label='Redo')
M2.add_command(label='Cut')
M2.add_command(label='Copy')
M2.add_command(label='Pase')
M3 = Menu(menu, tearoff=0)
M3.add_command(label='Slove')
M3.add_command(label='Solution...')
M4 = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=M1)
menu.add_cascade(label='Edit', menu=M2)
menu.add_cascade(label='Solver', menu=M3)
menu.add_cascade(label='Help', menu=M4)
W.config(menu=menu)

# Labe Frame - entry
frame2 = Frame(frame1)
Lo = LabelFrame(frame2, text='Loading')
Label(Lo, text='Pu').pack()
Pu = Entry(Lo)
Pu.pack()
Label(Lo, text='Dead Load').pack()
D = Entry(Lo)
D.pack()
Label(Lo, text='Live Load').pack()
Li = Entry(Lo)
Li.pack()

C_S = LabelFrame(frame2, text='Column Specifications')
Label(C_S, text='L - Length').pack()
L = Entry(C_S)
L.pack()
Label(C_S, text='E - Modulus of Elasticity').pack()
E = Entry(C_S)
E.pack()
Label(C_S, text='\u03C3 y - Yield Strength').pack()
Fy = Entry(C_S)
Fy.pack()

#Combo Box
CH = LabelFrame(frame2, text='Section Selection')
val = ['IPE' , 'IPB' , 'Bosted IPE' , 'Bosted IPB' , '2IPE' , 'HSS' , 'HSS']
Co = ttk.Combobox(CH,values=val)
Co.set('Section')
Co.pack()

Lis = Listbox(frame2, width=40, height=5)

but1 = Button(frame2, text='Compute', command=printing)
but1.grid(row=0, column=1, pady=10, ipadx=30)

"""
# Button
but1 = Button(frame2, text='Compute', command=Calculations)
but2 = Button(frame2, text='Mohr Circle', command=ploot)
but3 = Button(frame2, text='Clear', command=cls)
but4 = Button(frame2, text='State of stress', command=stf)
"""

# Pack-grid
frame2.grid(row=0, column=0)
#frame3.grid(row=2, column=1)
Lo.grid(row=0, column=0, pady=10)
# C_S.grid(row=1, column=0, pady=10)
C_S.grid(row=2, column=0, pady=10)
CH.grid(row=3, column=0, pady=10)
"""
but1.grid(row=0, column=1, pady=10, ipadx=30)
but2.grid(row=1, column=1, pady=10, ipadx=40)
but3.grid(row=3, column=1, pady=10, ipadx=30)
but4.grid(row=2, column=1, pady=10, ipadx=30)
"""

# combo.grid(row=1,column=4,pady=0,padx=70)

# ch1.grid(row=2,column=0,ipadx=20,ipady=20)

# Lis.grid
Lis.grid(row=4, column=0, padx=100, pady=10, ipadx=20, ipady=20)



# Run Tkinter
W.mainloop()
