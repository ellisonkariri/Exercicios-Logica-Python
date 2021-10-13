a = int(input("digite o primeiro numero "))
b = int(input("digite o segundo numero "))
c = int(input("digite o terceiro numero "))

maior = a
menor = 0

if b > maior:
    maior = b
    menor = a
else:
    menor = b

if c > maior:
    maior = c
else:
    menor = c


print(" Maior número é " f'{maior}')
print(" Menor número é " f'{menor}')
