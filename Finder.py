from bs4 import BeautifulSoup
from httpx import Client




def search(pesquisa: str):
    end_point = f"https://danbooru.donmai.us/autocomplete?search%5Bquery%5D={pesquisa}&search%5Btype%5D=tag_query&version=1&limit=20"
    #criando conexão com a url e manda a requisição com a pesquisa
    cliente = Client(base_url=end_point)
    response = cliente.get("")
    soup = BeautifulSoup(response.text, "html.parser")

    #consigo as LIs de sugestão através do html devolvido pela http response
    lis = soup.find_all("li", attrs={'class':'ui-menu-item'})
    sugestoes = [

        li.get("data-autocomplete-value")
        for li in lis
        
    ]

    return sugestoes


