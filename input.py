# input value
import numpy as np


def input_value():
    # calculating pu with dead load and live load or directly
    try:
        D = float(input('enter dead load (kg)'))
        L = float(input('enter live load (kg)'))
        Pu = None
    except:
        D = None
        L = None

    if D is None or L is None:
        try:
            Pu = float(input('enter  critical load (kg)'))
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
    opening = 0

    # frame setting

    frame = input('enter what is kind of your system ? 1D, 2D or 3D ?').lower()
    if frame in ['2d', '3d']:
        levels = int(input('how many levels exist ?'))

        if frame == '2d':
            opening = int(input('how many opening exist ?'))
        else:
            opening = [int(input('how many opening exist in xy dimension '))
                , int(input('how many opening exist in xz  dimension '))]

    # length calculator
    def length_cal(frame):
        lengthColumn = []
        lengthOpening = []
        if frame == '1d':
            lengthColumn.append(float(input('enter length of column column (m) ')))

        else:

            for i in range(1, levels + 1):
                lengthColumn.append(float(input(f'length of column level {i} (m)')))
        return lengthColumn

    lengthColumn = length_cal(frame)

    E = float(input('enter E of your steel '))
    Fy = float(input('enter Fy of your steel '))

    return [frame, Pu, lengthColumn, E, Fy]


input_value()
