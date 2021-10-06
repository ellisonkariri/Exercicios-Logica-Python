horas_mes = float(160)
salario_hora = float(input("Digite quanto ganha por hora :  "))
salario_bruto = salario_hora * horas_mes
print("Salario Bruto é de :  ", salario_bruto)

ir = (11.0 / 100) * salario_bruto
print("Desconto do IR:  ", ir)

inss = (8.0 / 100) * salario_bruto
print("Desconto do INSS:  ", inss)

sindicato = (5.0 / 100) * salario_bruto
print("Desconto do SINDICATO:  ", sindicato)

salario_liquido = salario_bruto - ir - inss - sindicato
print("Salário líquido é de  ", salario_liquido)
