from tkinter import *
from tkinter import ttk
from turtle import pu


# Clear Button
def cls():
    Lis.delete(0, END)
    # plt.cla()

#Start GUI by Tkinter
# Window settings
W = Tk()
W.title("Steel Column Design")
W.geometry('600x500')

# Scrollbar
Scr = Scrollbar(W)
Scr.pack(side=RIGHT, fill=BOTH)
frame1 = Frame(W)
frame1.pack(expand=True, fill=BOTH)
# Scr.config(command=frame1.yview)

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
# Radio1 = [("Positive", "Tension (+)"), ("Negative", "Compression (-)")]
# c1 = StringVar()
# c1.set("Positive")
# for a1,b1 in Radio1:
#    Radiobutton(C_S,value=a1,text=b1,variable=c1,).pack()
Label(C_S, text='E - Modulus of Elasticity').pack()
E = Entry(C_S)
E.pack()
# Radio2 = [("Positive", "Tension (+)"), ("Negative", "Compression (-)")]
# c2 = StringVar()
# c2.set("Positive")
# for a2,b2 in Radio2:
#    Radiobutton(C_S,value=a2,text=b2,variable=c2).pack()
Label(C_S, text='\u03C3 y - Yield Strength').pack()
Fy = Entry(C_S)
Fy.pack()


#Combo Box
CH = LabelFrame(frame2, text='Section Selection')
val = ['IPE' , 'IPB' , 'Bosted IPE' , 'Bosted IPB' , '2IPE' , 'HSS' , 'HSS']
Co = ttk.Combobox(CH,values=val)
Co.set('Section')
Co.pack()



xyd = LabelFrame(frame2, text='xy direction')
Label(xyd, text='Shear Stress').pack()
En3 = Entry(xyd)
En3.pack()
Radio3 = [("Negative", "CW on x face (-)"), ("Positive", "CCW on x face (+)")]
c3 = StringVar()
c3.set("Negative")
# for a3,b3 in Radio3:
#    Radiobutton(xyd,value=a3,text=b3,variable=c3).pack()

Tetaa = LabelFrame(frame2, text='Angel')
Label(Tetaa, text='Angel from X axis').pack()
teta2 = Entry(Tetaa)
teta2.pack()
Radio4 = [("Positive", "Tension (+)"), ("Negative", "Compression (-)")]
c4 = StringVar()
c4.set("Positive")
# for a4,b4 in Radio1:
#    Radiobutton(Tetaa,value=a4,text=b4,variable=c4,).pack()

Lis = Listbox(frame2, width=20, height=5)

"""
# Button
but1 = Button(frame2, text='Compute', command=Calculations)
but2 = Button(frame2, text='Mohr Circle', command=ploot)
but3 = Button(frame2, text='Clear', command=cls)
but4 = Button(frame2, text='State of stress', command=stf)

# Combo Box
val = ['MPa', 'kPa', 'kg/cm^2', 'N/mm^2', 'N/cm^2']
combo = ttk.Combobox(frame2, values=val)
combo.set('Select Unit')
"""

# Check Button
# AbsMax = IntVar()
# ch1 = Checkbutton(frame2,text='Show Absolute Maximum Shear Stress',variable=AbsMax)

# plot
frame3 = Frame(frame2)

# Pack-grid
frame2.grid(row=0, column=0)
frame3.grid(row=2, column=1)
Lo.grid(row=0, column=0, pady=10)
# C_S.grid(row=1, column=0, pady=10)
C_S.grid(row=2, column=0, pady=10)
CH.grid(row=3, column=0, pady=10)
Tetaa.grid(row=4, column=0, pady=10)

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
