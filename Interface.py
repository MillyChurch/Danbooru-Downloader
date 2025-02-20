from pathlib import Path
from tkinter import filedialog
import Finder
import Downloader
import os

def run():

    print("Escolha onde suas imagens serão baixadas")
    caminho = filedialog.askdirectory()

    os.system('cls')

    pesquisa = input("Você deseja baixar imagens de quê?: ")
    sugestoes = Finder.search(pesquisa)

    os.system('cls')

    i = 1
    for sugestao in sugestoes:
        print(f"[{i}] - [{sugestao}]")
        i+=1

    pesquisa = input("Selecione, pelo número, sua busca\n")

    while int(pesquisa) > len(sugestoes) or int(pesquisa) < 0:  
        pesquisa = input("Insira um número válido")

    pesquisa_texto = sugestoes[int(pesquisa)-1]

    os.system('cls')

    quantidade_imagens = int(input("Você deseja baixar quantas imagens?"))

    Downloader.download(pesquisa_texto, caminho, quantidade_imagens)
