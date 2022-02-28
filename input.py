# input value

def input_value():
    D = float(input('enter dead load (kg)'))
    L = float(input('enter live load (kg)'))
    Pu = float(input('enter  critical loading (kg)'))

    def Load(D, L, Pu):
        if Pu == 0 or Pu == None:
            Pu1 = 1.4 * D
            Pu2 = 1.4 * D + 1.6 * L
            Pu = max(Pu1, Pu2)

        return Pu
