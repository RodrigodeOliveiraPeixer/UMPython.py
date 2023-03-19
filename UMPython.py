#1 - Solicitar a inserção de 5 números, ao final, imprimir os números pares, números ímpares e a média geral desses números.


numeros = []
for i in range(5):
    numero = int(input("Insira um número: "))
    numeros.append(numero)


pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


media = sum(numeros) / len(numeros)


print("Números pares:", pares)
print("Números ímpares:", impares)
print("Média geral:", media)
