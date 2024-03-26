#Sem repetidor 

def happy(number):
    if number == 10:
        string = str(number)
        total = int(string[0])+int(string[1])
        return total == 1

    if number == 100:
        string = str(number)
        total = int(string[0])+int(string[1])+int(string[2])
        return total == 1

    if number == 1:
        return True

    return False

assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)

#Com repetidor

def happy(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum([int(char) ** 2 for char in str(n)])
    return n == 1


assert happy(1)
assert happy(10)
assert happy(100)
assert happy(130)
assert not happy(4)
assert not happy(20)

#Meu modelo

def e_feliz_com_for(numero):
    while numero != 1 and numero != 4:  # O ciclo infinito é 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
        numero = sum(int(digito)**2 for digito in str(numero))
    return numero == 1


print(e_feliz_com_for(19))  # True
print(e_feliz_com_for(20))  # False