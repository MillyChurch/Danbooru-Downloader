from httpx import Client
from bs4 import BeautifulSoup

page = 2
pesquisa = "beatrice_(umineko)"

#criando uma conexão com o site
url = f"https://danbooru.donmai.us/posts?page={page}&tags={pesquisa}"
cliente = Client(base_url=url)
resposta = cliente.get("")

#salva o html do site
html = resposta.text
soup = BeautifulSoup(html, 'html.parser')


imagens = soup.find_all("img")
print(imagens)

with open("open.html", "w") as filex:
    filex.write(html)