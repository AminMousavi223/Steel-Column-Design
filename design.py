# design column object

class designColumn():


    def __init__(self,inputValue):
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
        try:
            self.lengthOpening = inputValue[6]
        except:
            None

inputValue = ['2d',10000,4,2100000,2400,1,5]
column = designColumn(inputValue)
print(column)