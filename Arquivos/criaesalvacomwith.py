#Arquivo criação com with
#with open("impares.txt","w") as impares, with open("pares.txt","w") as pares: -> pode ser assim

with open("impares.txt","w") as impares:
    with open("pares.txt","w") as pares:
        for n in range(0,1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")

#a estrutura with garante o fechamento do arquivo 