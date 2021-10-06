import math
a = float(input("Digite a variável a"))
b = float(input("Digite a Variavel b"))
c = float(input("Digite a Variável C"))

delta = (b**2) - 4*a*c
print(delta)

raiz_delta = math.sqrt(delta)
print(raiz_delta)

if raiz_delta < 0:
    print("delta negativo")
else:
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)

    print("as raizes são", x1, x2)
