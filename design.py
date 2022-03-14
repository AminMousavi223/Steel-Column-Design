# design column object
import pandas as pd
import numpy as np

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
        self.IPE = inputValue[6]
        try:
            self.lengthOpening = inputValue[8]
        except:
            None

    def SingleColumn(self):
        A = self.IPB.loc[3:, 'مساحت']
        r_x = self.IPB.loc[3:, 'شعاع ژیراسیون حول محور x-x']
        r_y = self.IPB.loc[3:, 'شعاع ژیراسیون حول محور y-y']
        Fy = self.IPB.loc[3:, 'تنش تسلیم']
        E = self.IPB.loc[3:, 'مدول الاستیسیته']
        FS_list = []
        j = 0
        for i in range(3, 27):
            r_min = min(r_y[i], r_x[i])
            landa = (self.K * self.lengthColumn) / r_min
            Fe = ((np.pi ** 2) * E) / (landa ** 2)
            if landa <= 139:
                Fcr = (0.658 ** (Fy / Fe)) * Fy
            else:
                Fcr = 0.877 * Fe

            Pn = Fcr * A[i]
            FS = self.Pu / (0.9 * Pn)
            FS_list.append(FS)
            if 0.75 <= FS <= 1:

                return IPB.loc[i , 'IPB']

    def Doublecolumn(self):
        A1 = self.IPB.loc[3:, 'مساحت']
        b = self.IPB.loc[3:, 'عرض بال'] 
        r_x1 = self.IPB.loc[3:, 'شعاع ژیراسیون حول محور x-x']
        r_y1 = self.IPB.loc[3:, 'شعاع ژیراسیون حول محور y-y']
        I_x1 = self.IPB.loc[3:, 'ممان اینرسی حول محور x-x']
        I_y1 = self.IPB.loc[3:, 'ممان اینرسی حول محور y-y']         
        Fy = self.IPB.loc[3:, 'تنش تسلیم']
        E = self.IPB.loc[3:, 'مدول الاستیسیته']
        FS_list = []
        A = 2*A1
        I_x = 2*I_x1
        I_y = 2*(I_y1 + A1*(b/2))
        r_x = r_x1
        r_y  = (I_y/A)**0.5
        j = 0
        for i in range(3, 27):
            r_min = min(r_y[i], r_x[i])
            landa = (self.K * self.lengthColumn) / r_min
            Fe = ((np.pi ** 2) * E) / (landa ** 2)
            if landa <= 139:
                Fcr = (0.658 ** (Fy / Fe)) * Fy
            else:
                Fcr = 0.877 * Fe

            Pn = Fcr * A[i]
            FS = self.Pu / (0.9 * Pn)
            FS_list.append(FS)
            if 0.75 <= FS <= 1:

                return IPB.loc[i , '2IPB']


inputValue = ['1d', 50300, 2.7, 2100000, 2400, 1, IPB, IPE]
column = designColumn(inputValue)
a = column.SingleColumn()
# print(column)
print(a)