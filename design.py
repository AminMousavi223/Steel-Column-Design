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
            I_y = 2*(I_y1[i] + A1[i]*(b[i]/2))
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
    
                return IPE.loc[i , '2IPE']

    # def Battend_member(self):
    #     A1 = self.IPE.loc[3:, 'مساحت']
    #     b = self.IPE.loc[3:, 'عرض بال']
    #     r_x1 = self.IPE.loc[3:, 'شعاع ژیراسیون حول محور x-x']
    #     r_y1 = self.IPE.loc[3:, 'شعاع ژیراسیون حول محور y-y'] # اضافه
    #     I_x1 = self.IPE.loc[3:, 'ممان اینرسی حول محور x-x']
    #     I_y1 = self.IPE.loc[3:, 'ممان اینرسی حول محور y-y']
    #     Fy = self.IPE.loc[3:, 'تنش تسلیم']
    #     E = self.IPE.loc[3:, 'مدول الاستیسیته']
    #     FS_list = []
    #     j = 0
    #     for i in range(3, 27):
    #         A = 2*A1[i]
    #         I_x = 2*I_x1[i] # اضافه
    #         I_y = 2*(I_y1[i] + A1[i]*(b[i]/2))
    #         r_x = r_x1[i]
    #         r_y  = (I_y[i]/A[i])**0.5
    #
    #         r_min = min(r_y, r_x)
    #         landa = (self.K * self.lengthColumn) / r_min
    #         Fe = ((np.pi ** 2) * E) / (landa ** 2)
    #         if landa <= 139:
    #             Fcr = (0.658 ** (Fy / Fe)) * Fy
    #         else:
    #             Fcr = 0.877 * Fe
    #
    #         Pn = Fcr * A
    #         FS = self.Pu / (0.9 * Pn)
    #         FS_list.append(FS)
    #         if 0.75 <= FS <= 1:
    #
    #             return IPE.loc[i , '2IPE']


inputValue = ['2d', 50300, 2.7, 2100000, 2400, 1, IPB, IPE]
column = designColumn(inputValue)
a = column.SingleColumn_IPB()
print(a)
b = column.SingleColumn_IPE()
print(b)
c = column.Doublecolumn_IPE()
print(c)
# print(column)
# print(a, b, c)
