limite = int(input("Digite até qual número quer contar: "))

for numero in range(1, limite + 1):
    if numero % 15 == 0:
        print("FIZZBUZZ")
    elif numero % 3 == 0:
        print("FIZZ")
    elif numero % 5 == 0:
        print("BUZZ")
    else:
        print(numero)