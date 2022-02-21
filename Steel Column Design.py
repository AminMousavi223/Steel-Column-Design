
D = 700 ; L =10  ; Pu = 0
if Pu == 0:
    Pu1 = 1.4*D
    Pu2 = 1.4*D+1.6*L
    Pu = max(Pu1, Pu2)
    D = 0 ; L = 0
print(float(Pu))


