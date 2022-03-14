# design column object
import pandas as pd

IPB = pd.read_excel('Steel Full.xlsx','IPB' )
IPE = pd.read_excel('Steel Full.xlsx','IPE' )


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
        try:
            self.lengthOpening = inputValue[7]
        except:
            None

    def SinglColumn(self):
        Ag = self.Pu / 1500
        A = self.IPB.loc[3:, 'مساحت']
        r_x = self.IPB.loc[3:, 'مساحت']
        r_y = self.IPB.loc[3:, 'مساحت']
        Fy = self.IPB.loc[3:, 'مساحت']
        E = self.IPB.loc[3:, 'مساحت']
#
# inputValue = ['2d',10000,4,2100000,2400,1,5]
# column = designColumn(inputValue)
# print(column)
