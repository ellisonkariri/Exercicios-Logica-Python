altura = float(input("Digite sua altura:  "))
sexo = input("digite 0 para Masculino e 1 para Feminino:   ")

if(sexo == "0"):
    peso = (72.7*altura - 58)
    print("Seu peso ideal é de :  ", peso)

elif(sexo == "1"):
    peso = (62.1*altura - 44.7)
print("Seu peso ideal é de :  ", peso)
