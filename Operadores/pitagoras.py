#Teorema de Pitágoras

import math

print("\nTEOREMA DE PITÁGORAS")

b = float(input("\nA²: "))
h = float(input("\nB²: "))

p = (b**2) + (h**2)

pitagoras = math.sqrt(p) #tranformação de raiz.


print("\nHIPOTENUSA: {:.2f}".format(pitagoras))
