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

# Start GUI by Tkinter
def input_output():
    global IPB, IPE
    # calculating pu with dead load and live load or directly
    try:  
        Pu = float(pu.get())
    except:
        D = float(d.get())
        Li = float(li.get())
        Pu1 = 1.4 * D
        Pu2 = 1.4 * D + 1.6 * Li
        Pu = max(Pu1, Pu2)
  
    inputValue = ['1d', Pu, float(L.get()), int(E.get()) ,int(Fy.get()), float(k.get()), IPB, IPE]
    column = designColumn(inputValue)
    Lis.insert(END, f'Best performance for IPB sections: IPB{int(column.SingleColumn_IPB())}' )
    Lis.insert(END, f'Best performance for IPE sections: IPE{int(column.SingleColumn_IPE())}' )
    Lis.insert(END, f'Best performance for 2IPE sections: 2IPE{int(column.Doublecolumn_IPE())}' )
    
def cls():
    Lis.delete(0, END)
    # plt.cla()

# Window settings
W = Tk()
W.title("Steel Column Design")
W.geometry('550x400')

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
pu = Entry(Lo)
pu.pack()
Label(Lo, text='Dead Load').pack()
d = Entry(Lo)
d.pack()
Label(Lo, text='Live Load').pack()
li = Entry(Lo)
li.pack()

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
Label(C_S, text='K').pack()
k = Entry(C_S)
k.pack()

#Combo Box
CH = LabelFrame(frame2, text='Section Selection')
val = ['IPE' , 'IPB' , 'Bosted IPE' , 'Bosted IPB' , '2IPE' , 'HSS' , 'HSS']
Co = ttk.Combobox(CH,values=val)
Co.set('Section')
Co.pack()

Bu = LabelFrame(frame2, text='')
but1 = Button(Bu, text='Compute', command=input_output).pack(pady=20,ipadx=40)
but2 = Button(Bu, text='Clear', command=cls).pack(pady=20,ipadx=40)
Lis = Listbox(frame2, width=35, height=5)

# Pack-grid
frame2.grid(row=0, column=0)
Lo.grid(row=0, column=0, padx=50, pady=20)
C_S.grid(row=1, column=0, pady=20)
Bu.grid(row=1, column=1, pady=20,ipadx=40)
Lis.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=20)

# Run Tkinter
W.mainloop()