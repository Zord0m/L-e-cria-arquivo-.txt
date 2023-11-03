#Arquivo criação 1
arquivo = open("numero.txt", "w")
for linha in range(1,101):
    arquivo.write(f"{linha}\n")
arquivo.close()

#saída:
#numeros.txt ==> arquivo gerado na mesma pasta