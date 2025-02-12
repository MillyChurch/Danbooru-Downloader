from httpx import Client
from bs4 import BeautifulSoup

primeiraPagina = 1
quantidadePaginas = 5
pesquisa = "beatrice_(umineko)"

#criando uma conexão com o site
url = f"https://danbooru.donmai.us"
cliente = Client(base_url=url)

#vai em todas os previews
downloads=0

for x in range(primeiraPagina,quantidadePaginas+primeiraPagina):

    resposta = cliente.get(f"/posts?page={x}&tags={pesquisa}")
    
    #salva o html do site
    html = resposta.text
    soup = BeautifulSoup(html, 'html.parser')

    #lista as divs pertencentes a classe post preview link
    imagensComLinks = soup.find_all("a",attrs={"class":"post-preview-link"})


    for imgLinks in imagensComLinks:
        post = cliente.get(imgLinks.get("href"))
        htmlPost = post.text
        soup = BeautifulSoup(htmlPost, 'html.parser')

        imagemDoPost = soup.find("img",attrs={"class":"fit-width"})
        caminhoDaImagem = imagemDoPost.get("src")

        aax = Client()

        response = aax.get(caminhoDaImagem.__str__())

        with open(f"Downloads/{caminhoDaImagem.split('/')[-1]}.jpg", "wb") as file:
            file.write(response.content)
            downloads+=1

print(f"Você baixou {downloads} imagens")