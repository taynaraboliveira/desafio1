# 1. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,
# e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:

#Dólar Americano: R$4,91
#Peso Argentino: R$0,02
#Dólar Australiano: R$3,18
#Dólar Canadense: R$3,64
#Franco Suíço: R$0,42
#Euro: R$5,36
#Libra esterlina: R$6,21

def converte_moeda(valor, taxa):
    return valor * taxa

carteira = float(input("Quanto dinheiro você tem na carteira (em reais)? "))

moedas = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

for moeda, taxa in moedas.items():
    valor_convertido = converte_moeda(carteira, taxa)
    print(f"Com {carteira:.2f} reais, você poderia comprar {valor_convertido:.2f} {moeda}.")


# 2. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 
#R$80,00 por dia e R$0,20 por km rodado.

# Solicita a quantidade de km e dias
km_percorridos = float(input("Quantos quilômetros foram percorridos com o carro? "))
dias_alugados = int(input("Por quantos dias o carro foi alugado? "))

# Define os custos
custo_km = km_percorridos * 0.20
custo_diaria = dias_alugados * 80

# Calcula o preço total
preco_total = custo_km + custo_diaria

# Imprime o preço a pagar
print(f"O preço a pagar é R${preco_total:.2f}.")


# 3.Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. 
#Se o salário for até R$1000,00 o funcionário terá 20% de aumento. Entre R$1001,00 até R$2800,00 
#o funcionário terá 10% de aumento. Acima de R$2801,00 o funcionário terá 5% de aumento.

# Solicita o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Verifica as condições e aplica o aumento conforme o caso
if salario <= 1000:
    novo_salario = salario * 1.2
elif 1000 < salario <= 2800:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.05

# Imprime o novo salário
print(f"O novo salário do funcionário é R$ {novo_salario:.2f}")


# 4.Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um número: ').

def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, digite um valor numérico inteiro válido.")

# Exemplo de uso
n = leiaInt('Digite um número: ')
print(f'O número digitado foi: {n}')


