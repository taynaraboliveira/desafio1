# 1. "Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene numa lista a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0.

# Inicializando listas
listaNotas = []
listaMedias = []

quantidadeAlunos = 10
quantidadeNotas = 4

# Loop para coletar as notas e calcular as médias
# range gera uma lista de 10 até 0
# append vai incluir o item no fim da lista

# Coleta de notas
for aluno in range(quantidadeAlunos):
    listaNotas.append([])
    for nota in range(quantidadeNotas):
       nota_inserida = float(input(f"Digite a nota {nota+1} do aluno {aluno+1}: "))
    listaNotas[aluno].append(nota_inserida)

# Cálculo das médias
for notas in listaNotas:
    listaMedias.append(sum(notas) / len(notas))

# Conta quantos alunos têm média maior ou igual a 7.0
alunos_aprovados = sum(1 for media in listaMedias if media >= 7.0)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")


# 2.Programa nome ao contrário em maiúsculas. Faça um programa que 
#permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para 
#frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário 
#pode digitar letras maiúsculas ou minúsculas.

def inverte_nome(nome):
    nome_invertido = nome[::-1]
    nome_maiusculo = nome_invertido.upper()
    return nome_maiusculo

# Solicita o nome ao usuário
nome = input("Digite o seu nome: ")

# Chama a função e imprime o nome invertido em maiúsculas
nome_invertido = inverte_nome(nome)
print(nome_invertido)


# 3.Escreva um programa em Python que onde todos os valores em um dicionário são emitidos.
# Se sim, imprima True. Caso contrário, imprima Falso.

dicionario = {"banana": 'fruta', "casa": 'imovel', "laranja": 'fruta'}
print(dicionario)

# Verifica se todos os valores no dicionário são emitidos
valores_emitidos = all(valores for valores in dicionario.values())

if valores_emitidos:
   print("True")
else:
   print("False")
   

# 4.Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 perguntas ela deve ser classificada como "Suspeita", 
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ela será classificada como "Inocente".

# Fazendo as perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Inicializa a contagem de respostas positivas
respostas_positivas = 0

# Pergunta para o usuário e verifica a resposta
for pergunta in perguntas:
    resposta = input(pergunta + " (Sim ou Não): ").lower()
    if resposta == "sim":
        respostas_positivas += 1

# Classificação final
if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente") 
