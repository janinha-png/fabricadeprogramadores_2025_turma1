import os

try:
    for n in range(1,51):
        os.mkdir("pasta_d%" % n)
    os.chdir('pasta_1')
    arquivo = open("arquivo_1.txt", "w")
    arquivo.write("oi")
    arquivo.close()
except FileNotFoundError:
    print('Arquivo nao encontrado!')

arquivo_path = "w"
try:
    os.rmdir(arquivo_path)
    print(f"""\033[0;32m Pasta '{arquivo_path}' 
    removida com sucesso! ;D""")
except FileNotFoundError:
    print(f"""\033[0;33m Pasta '{arquivo_path}'
    não encontrada... @@""")
except OSError:
    print(f"""\033[0;34m '{arquivo_path}' 
    é um arquivo, não uma pasta!!! + +""")

lafufu = "50_arquivos"
if not os.path.exists(lafufu):
    os.mkdir(lafufu)
    
for i in range(1,51):
    arquivo = f"arquivo_{i:03d}.txt"
    jok = os.path.join(lafufu,arquivo)
    try:
        with open(jok,"w") as f:
            f.write(f"Conteudo do arquivo numero {i}\n")
        print(f"Arquivo'{arquivo}' criado com sucesso.")
    except IOError as e:
        print(f"Erro ao criar o arquivo'{arquivo}': {e}")
    print("Criação e arquivos concluida.")
