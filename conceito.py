# 1. Faça um Programa que peça um número e então mostre a mensagem: >0 número informado foi [número].

num= int(input ("Digite um número: "))
print(f"O número informado foi: {num}")

# 2. Faça um Programa que peça dois números e imprima a soma.

num1 = int(input ("Digite um número: "))
num2 = int(input ("Digite um número: "))
soma = num1 + num2
print (soma)

# 3. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura = int(input("Qual a temperatura hoje: "))
temperaturaF = temperatura * (9 / 5) + 32
print(f'Valor em Fahrenheit: {temperaturaF}')

# 4. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês

valorHora = float(input ("Qual o valor da sua hora trabalhada: "))
horasTrabalhadas= float (input("Quantas horas você trabalhou esse mês: "))
salario = float(valorHora * horasTrabalhadas) 
print (f'Seu salário esse mês é: ({salario}')