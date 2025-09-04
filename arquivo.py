try:
    arquivo = open("numeros.txt", "w")
    for linha in range(1,101):
        arquivo.write("%d Joaninha\n" % linha)  
    arquivo.close()
except FileNotFoundError:
    print('Arquivo não encontrado!')