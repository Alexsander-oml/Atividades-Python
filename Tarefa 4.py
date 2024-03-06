# Alex Santos
# Atividade 4

#1
idade = int(input('Qual é sua idade?'))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#2
nome_animal = input('Digite o nome do animal. ')

if nome_animal.lower() == 'gato':
    print('O animal é um gato')
    
elif nome_animal.lower() == 'cachorro':
    print('O animal é um cachorro')
    
else:
    print('O animal não é um gato nem um cachorro')
    
#3
for i in range(1, 100, 2):
    print(i)


#4
lista = []
med = 0
contador = 0

while True:
    entrada = input("Digite um número ou -1 para encerrar o processo: ")

    if entrada == "-1":
        break  

    if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
        num = int(entrada)
        lista.append(num)
        med += num
        contador += 1
    else:
        print("Entrada inválida. Por favor, digite apenas números.")

if contador > 0:
    media = med / contador
    print("Processo encerrado.")
    print("Lista final:", lista)
    print("Média:", media)
else:
    print("Nenhum número foi digitado.")
 
 
 
 #5
 
 #6