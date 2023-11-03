# Abra os arquivos 'pares.txt' e 'impares.txt' e leia as linhas
with open('pares.txt', 'r') as f:
    pares = [int(line.strip()) for line in f]
with open('impares.txt', 'r') as f:
    impares = [int(line.strip()) for line in f]

# Combine as listas e ordene
todos_numeros = sorted(pares + impares)

# Escreva os números ordenados no arquivo 'paresimpares.txt'
with open('paresimpares.txt', 'w') as f:
    for num in todos_numeros:
        f.write(str(num) + '\n')
