# Alex Santos - 4C
# 14.03.2024

#Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se
#eles forem iguais, imprima que eles são iguais.

#1

def menor(a,b):
    if a > b:
        return b
    elif b > a:
        return a
    else:
        return "Os números são iguais"

print(menor(10,1)) #1

#2

# Escreva uma função que recebe um número n como parâmetro e imprime se n é
# positivo ou negativo.

def NP(n):
    if n > 0:
      return "Positivo"
    elif n < 0:
      return "Negativo"
    else:
      return "Neutro"

print(NP(1)) #Positivo

#3

# Escreva uma função que recebe dois números (a e b) como parâmetro e retorna
# True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def soma(a,b,limite):
    if a + b > limite:
        return: True

print(soma(a,b,limite))
    
#4

# Escreva uma função que recebe um número como parâmetro, a função imprime
# ”Fizz”se o número for múltiplo de três, imprime ”Buzz”se o número for múltiplo de
# cinco, e imprime ”FizzBuzz”se o número for múltiplo de três e cinco. Caso o
# número não seja múltiplo nem de três nem de cinco, ele deve ser impresso. Note
# que, ao contrário das funções anteriores, sua função não deve retornar nada. Ela
# precisa simplesmente imprimir o que foi pedido.

def FB(n):
    if n%3 == 0 and n%5 != 0:
     print("Fizz")
    if n%5 == 0 and n%3 != 0:
     print("Buzz")
    if n%5 == 0 and n%3 == 0:
     print("FizzBuzz")


#5
# Escreva uma função que recebe como entrada uma lista de números e retorna True
# se um número passado como parâmetro está presente na lista.

def verificar_numero(lista, num):
    for numero in lista:
     if  numero == num:
      return True
    return False

numeros = [1, 2, 3, 4, 5]
print(verificar_numero(lista, 3))  # Saída: True
print(verificar_numero(lista, 6))  # Saída: False


# Atividade 6
# Escreva uma função que recebe como entrada um número inteiro positivo n e
# retorne a soma de todos os inteiros positivos menores ou iguais a n.

def soma(n):
    soma = 0
    for contador in range(1, n + 1):
        soma+= contador
    return soma

print(soma(3)) #6
print(soma(10)) #55
print(soma(15)) #120
print(soma(25)) #325