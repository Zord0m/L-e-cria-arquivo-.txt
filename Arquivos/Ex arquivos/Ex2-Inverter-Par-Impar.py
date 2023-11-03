with open ("pares.txt", "r") as f:
    pares = [int(line.strip()) for line in f]
with open ("impares.txt", "r") as f:
    impares = [int(line.strip()) for line in f]

# Inverta a ordem dos números em cada lista
pares_invertidos = pares[::-1]
impares_invertidos = impares[::-1]

# Escreva os números invertidos nos arquivos 'invertidopares.txt' e 'invertidoimpares.txt'
with open("invertidopares.txt", "w") as f:
    for num in pares_invertidos:
        f.write(str(num)+ '\n')

with open("invertidoimpares.txt", "w") as f:
    for num in impares_invertidos:
        f.write(str(num)+ '\n')     