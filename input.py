# input value
import numpy as np


def input_value():
    # calculating pu with dead load and live load or directly
    try:
        D = float(input('Enter dead load (kg)'))
        L = float(input('Enter live load (kg)'))
        Pu = None
    except:
        D = None
        L = None

    if D is None or L is None:
        try:
            Pu = float(input('Enter  critical load (kg)'))
        except:
            Pu = None

    # combined loading
    def Load(D, L, Pu):
        if Pu == 0 or Pu == None:
            Pu1 = 1.4 * D
            Pu2 = 1.4 * D + 1.6 * L
            Pu = max(Pu1, Pu2)

        return Pu

    Pu = Load(D, L, Pu)
    Bay = 0

    # frame setting

    frame = input('Enter what is kind of your system ? 1D, 2D or 3D ?').lower()
    if frame in ['2d', '3d']:
        levels = int(input('How many levels exist ?'))

        if frame == '2d':
            opening = [int(input('how many opening exist ?'))]
        else:
            Bay = [int(input('How many bay exist in xy dimension '))
                , int(input('How many bay exist in xz dimension '))]

    # length calculator
    def length_cal(frame):
        lengthColumn = []
        lengthOpening_xy = []
        lengthOpening_xz = []
        # length of column
        if frame == '1d':
            lengthColumn.append(float(input('enter length of column column (m) ')))
            return [lengthColumn]
        else:

            for i in range(1, levels + 1):
                lengthColumn.append(float(input(f'length of column level {i} (m)')))
            # length of opening
            for i in range(1, opening[0] + 1):
                lengthOpening_xy.append(float(input(f'length of opening in xy plate {i}'
                                                    f' (m) (start from left)')))
            if frame == '3d':
                for i in range(1, opening[1] + 1):
                    lengthOpening_xz.append(float(input(f'length of opening in xz plate {i}'
                                                        f' (m) (start from left)')))
                return [lengthColumn, lengthOpening_xy, lengthOpening_xz]

            return [lengthColumn, lengthOpening_xy]

    length= length_cal(frame)
    lengthColumn = length[0]
    try:
        lengthOpening = [length[1], length[2]]
    except:
        lengthOpening = [length[1]]

    E = float(input('Enter E of your steel '))
    Fy = float(input('Enter Fy of your steel '))

    return [frame, Pu, lengthColumn, E, Fy]


input_value()
