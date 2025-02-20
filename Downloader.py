from httpx import Client
from bs4 import BeautifulSoup

    
def download(pesquisa:str, caminho_pasta:str, quantidade_imagens: int):
    
    #criando uma conexão com o site
    url = f"https://danbooru.donmai.us"
    cliente = Client(base_url=url)

    #vai em todas os previews
    downloads=0
    i = 0
    page = 0

    while(True):
        
        page+=1
        resposta = cliente.get(f"/posts?page={page}&tags={pesquisa}")
        
        #salva o html da página do tema pesquisado
        html = resposta.text
        soup = BeautifulSoup(html, 'html.parser')

        #lista as divs pertencentes a classe post preview link
        imagensComLinks = soup.find_all("a",attrs={"class":"post-preview-link"})
        if(imagensComLinks == []):
            break

        #para navegar em cada preview de post
        for imgLinks in imagensComLinks:

            if(downloads == quantidade_imagens):
                print("Você baixou todas as imagens dessa pesquisa") 
                break

            post = cliente.get(imgLinks.get("href"))
            htmlPost = post.text
            soup = BeautifulSoup(htmlPost, 'html.parser')
            imagemDoPost = soup.find("img",attrs={"class":"fit-width"})

            #caso ele não de get em uma imagem do post
            if not imagemDoPost:
                continue

            caminhoDaImagem = imagemDoPost.get("src")
            
            if not caminhoDaImagem: continue

            #da get numa conexão com a src da imagem
            cliente_2 = Client()
            response = cliente_2.get(caminhoDaImagem.__str__())
            nome_arquivo = caminhoDaImagem.split('/')[-1]
            salvar_imagem(response.content, caminho_pasta, nome_arquivo)
            downloads+= 1
            print(f"{downloads} imagens baixadas")
            
            

def salvar_imagem(arquivo, caminho_pasta, nome):
    with open(f"{caminho_pasta}/{nome}", "wb") as file:
                file.write(arquivo)

