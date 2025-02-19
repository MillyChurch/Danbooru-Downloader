from pathlib import Path
from tkinter import filedialog
import Finder
import Downloader

print("Escolha onde suas imagens serão baixadas")
caminho = filedialog.askdirectory()

pesquisa = input("Você deseja baixar imagens de quê?: ")
sugestoes = Finder.search(pesquisa)

i = 1
for sugestao in sugestoes:
    print(f"[{i}] - [{sugestao}]")
    i+=1

pesquisa = input("Selecione, pelo número, sua busca\n")

while int(pesquisa) > len(sugestoes) or int(pesquisa) < 0:  
    pesquisa = input("Insira um número válido")

pesquisa_texto = sugestoes[int(pesquisa)-1]
primeira_pagina = int(input("Você deseja baixar a partir de qual página?"))
quantidade_paginas = int(input("Você deseja baixar quantas páginas?"))
Downloader.Downloader.download(primeira_pagina, quantidade_paginas, pesquisa_texto,caminho)
