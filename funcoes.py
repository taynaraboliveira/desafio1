# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_tres_numeros(a, b, c):
    soma = a + b + c
    return soma

# Solicita os três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chama a função e imprime o resultado
resultado = soma_tres_numeros(numero1, numero2, numero3)
print(f"A soma dos três números é: {resultado}")


# 2.Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso_numero(numero):
    numero_str = str(numero)
    numero_reverso = int(numero_str[::-1])
    return numero_reverso

 #Solicita um número ao usuário
numero_informado = int(input("Digite um número inteiro: "))

# Chama a função e imprime o reverso
resultado = reverso_numero(numero_informado)
print(f"O reverso do número {numero_informado} é {resultado}")


# 3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de graus Celsius para Fahrenheit
# ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada,
#  onde esse menu chama a função de conversão correta.

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu_conversao():
    print("Escolha uma opção:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {resultado} °F")

    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"A temperatura em Celsius é: {resultado} °C")

    else:
        print("Opção inválida!")

# Chamando o menu
menu_conversao()
