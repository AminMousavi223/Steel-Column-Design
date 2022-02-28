# input value

def input_value():
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

    def Load(D, L, Pu):
        if Pu == 0 or Pu == None:
            Pu1 = 1.4 * D
            Pu2 = 1.4 * D + 1.6 * L
            Pu = max(Pu1, Pu2)

        return Pu

    Pu = Load(D, L, Pu)

    frame = input('enter what is kind of your system ? 1D, 2D or 3D ?').lower()
    if frame in ['2d', '3d']:
        levels = int(input('how many levels exist ?'))

    def length_column(frame):
        length = []
        if frame == '1d':
            length.append(float(input('enter length of column (m) ')))

        else:

            for i in range(1, levels + 1):
                length.append(float(input(f'length of level {i} (m)')))
        return length

    length = length_column(frame)

    return [frame, Pu, length]


