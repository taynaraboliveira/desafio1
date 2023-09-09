# 1. Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int (input("Digite um número: "))
numero2 = int(input("Digite um número: "))

if(numero1 > numero2):
  maior = numero1
else:
  maior = numero2
print(f"O maior número informado foi: {maior}")

# 2. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input ("Em que turno você estuda? Digite M-matutino, V-Vespertino ou N- Noturno: ")
if turno == "M":
   mensagem = "Bom dia!"
elif turno == "V":
  mensagem = "Boa tarde!"
elif turno == "N":
   mensagem = "Boa noite!"
else:    
   mensagem = "Valor Inválido"
print(mensagem)    

# 3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

while True:
  nota = int(input ("Digite uma nota entre 0 e 10: "))
  if 0 <= nota <= 10:
   break
  else:
   print("Valor inválido. Digite novamente")
      
print("Nota válida:", nota)