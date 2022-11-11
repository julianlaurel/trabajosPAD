import math
radio=int(input("pon el radio del circulo"))
profundidad=int(input("pon profundidad"))
area=math.pi*(radio**2)
volumen=area*profundidad
print(round(volumen,3))

