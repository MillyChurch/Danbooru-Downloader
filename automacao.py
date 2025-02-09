from playwright.sync_api import sync_playwright, Locator
from concurrent.futures import ThreadPoolExecutor
import requests
import time

def searchImage(pesquisa: str):
    with sync_playwright() as pw:
        url = f"https://danbooru.donmai.us/posts?page={5}&tags={pesquisa}"
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        x=1
        pagex = 6
        imgPage = page.locator("img").nth(x)

        while pagex < 10:
            img = page.locator("img").nth(x)

            while img.is_visible() and img.get_attribute("class")=="post-preview-image":
                #pega a imagem da pagina
                imgPage = img
                imgPage.click() 
                everOne = page.locator("img").nth(1)
                src = everOne.get_attribute("src")
                # print(f"src: {imgPage}")
                downloadImg(src,f"{pesquisa}_({pagex}-{x})")
                page.goto(url,timeout=5000)
                x=x+1
                img = page.locator("img").nth(x)
                print(url)

            x = 1
            pagex += 1
            url = f"https://danbooru.donmai.us/posts?page={pagex}&tags={pesquisa}"
            page.goto(url,timeout=5000)
            

    
def downloadImg(imageSrc:str, nomeImagem:str):
    resposta = requests.get(imageSrc)
    with open(f"Downloads/{nomeImagem}.jpg","wb") as file:
        file.write(resposta.content)

searchImage("beatrice_(umineko)")