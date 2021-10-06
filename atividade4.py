peso = float(input("digite a quantidade do peso:   "))
excedente = 50
excesso = 0

if(peso >= excedente):
    excesso = peso - excedente
    multa = excesso * 4
    print("A quantidade do excedida foi de :  ", excesso)
    print(" A multa foi de :  ", multa)

else:
    print("não teve multa")
