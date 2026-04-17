from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import unquote
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os
import time

URL_INICIAL = "https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange"
BASE_URL = "https://en.wikipedia.org"
PASTA_HTML = "htmls_lab1_vancouver"
CSV_PAGINAS = "paginas_wikipedia.csv"
CSV_IMAGENS = "imagens_wikipedia.csv"
HEADERS = {"User-Agent": "aula-cpa"}


def get_pagina(url):
    # Funcao baseada no exemplo da professora usando urllib + tratamento de erros.
    try:
        req = Request(url, headers=HEADERS)
        html = urlopen(req)
    except HTTPError as erro:
        print("Houve um erro na obtencao da pagina!", erro)
        return None
    except URLError as erro:
        print("Ocorreu um erro no servidor!", erro)
        return None
    else:
        print("Consegui abrir a pagina:", url)
        return html.read()


def corrigir_nome_arquivo(nome):
    # Remove caracteres problematicos para salvar os HTMLs no Windows.
    nome = unquote(nome)
    nome = nome.replace("/", "_")
    nome = nome.replace("\\", "_")
    nome = nome.replace(":", "_")
    nome = nome.replace("*", "_")
    nome = nome.replace("?", "_")
    nome = nome.replace("\"", "_")
    nome = nome.replace("<", "_")
    nome = nome.replace(">", "_")
    nome = nome.replace("|", "_")
    return nome


def salvar_html(url, conteudo, pasta=PASTA_HTML):
    # Salva o HTML da pagina em disco para o scraping posterior.
    os.makedirs(pasta, exist_ok=True)

    nome_arquivo = url.split("/")[-1]
    nome_arquivo = corrigir_nome_arquivo(nome_arquivo) + ".html"
    caminho = os.path.join(pasta, nome_arquivo)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo.decode("utf-8", errors="ignore"))

    print("HTML salvo com sucesso:", caminho)
    return caminho


def extrair_links_internos(soup):
    # Coleta apenas links internos da Wikipedia no formato /wiki/,
    # exatamente como foi pedido no enunciado.
    links_internos = []

    for link in soup.select("a[href^='/wiki/']"):
        href = link.get("href")

        if href is None:
            continue

        if "#" in href:
            href = href.split("#")[0]

        if "?" in href:
            href = href.split("?")[0]

        if href == "/wiki/":
            continue

        link_completo = BASE_URL + href

        if link_completo not in links_internos:
            links_internos.append(link_completo)

    return links_internos


def extrair_links_imagens(soup):
    # Coleta os src das imagens e corrige os links relativos.
    links_imagens = []

    for img in soup.select("img"):
        if img.has_attr("src"):
            src = img["src"]

            if src.startswith("//"):
                src = "https:" + src
            elif src.startswith("/"):
                src = BASE_URL + src

            if src not in links_imagens:
                links_imagens.append(src)

    return links_imagens


def extrair_primeiro_paragrafo(soup):
    # Percorre os paragrafos e retorna o primeiro que tenha texto.
    paragrafos = soup.find_all("p")

    for paragrafo in paragrafos:
        texto = paragrafo.get_text(" ", strip=True)
        if texto != "":
            return texto

    return ""


def extrair_titulo(soup):
    # Usa o title da pagina, como mostrado nos exemplos da professora.
    if soup.head and soup.head.title and soup.head.title.string:
        return soup.head.title.string.strip()

    return "Sem titulo"


def baixar_htmls():
    print("=" * 60)
    print("ETAPA 1 - BAIXAR A PAGINA INICIAL")
    print("=" * 60)

    pagina_inicial = get_pagina(URL_INICIAL)

    if pagina_inicial is None:
        return []

    soup_inicial = BeautifulSoup(pagina_inicial, "html.parser")

    paginas_baixadas = []
    timestamp_inicial = datetime.now().isoformat()
    caminho_inicial = salvar_html(URL_INICIAL, pagina_inicial)

    paginas_baixadas.append(
        {
            "url": URL_INICIAL,
            "arquivo_html": caminho_inicial,
            "timestamp": timestamp_inicial,
        }
    )

    links_internos = extrair_links_internos(soup_inicial)
    print("Titulo da pagina inicial:", extrair_titulo(soup_inicial))
    print("Numero de links internos encontrados:", len(links_internos))
    print("Exemplo de 5 links internos encontrados:")
    for link in links_internos[:5]:
        print(link)

    print("=" * 60)
    print("ETAPA 2 - BAIXAR OS LINKS INTERNOS ENCONTRADOS")
    print("=" * 60)

    for indice, link in enumerate(links_internos, start=1):
        if link == URL_INICIAL:
            continue

        print(f"[{indice}/{len(links_internos)}] Baixando:", link)
        pagina = get_pagina(link)

        if pagina is not None:
            timestamp = datetime.now().isoformat()
            caminho = salvar_html(link, pagina)

            paginas_baixadas.append(
                {
                    "url": link,
                    "arquivo_html": caminho,
                    "timestamp": timestamp,
                }
            )

        time.sleep(0.5)

    return paginas_baixadas


def gerar_csvs(paginas_baixadas):
    print("=" * 60)
    print("ETAPA 3 - EXTRAIR DADOS DOS HTMLs BAIXADOS")
    print("=" * 60)

    with open(CSV_PAGINAS, "w", newline="", encoding="utf-8") as arquivo_paginas:
        escritor_paginas = csv.writer(arquivo_paginas)
        escritor_paginas.writerow(
            [
                "page_url",
                "html_file",
                "title",
                "first_paragraph",
                "internal_links",
                "image_links",
                "timestamp",
            ]
        )

        with open(CSV_IMAGENS, "w", newline="", encoding="utf-8") as arquivo_imagens:
            escritor_imagens = csv.writer(arquivo_imagens)
            escritor_imagens.writerow(
                ["page_url", "page_title", "image_url", "timestamp"]
            )

            for pagina in paginas_baixadas:
                print("Lendo arquivo HTML:", pagina["arquivo_html"])
                with open(pagina["arquivo_html"], "r", encoding="utf-8") as arquivo_html:
                    soup = BeautifulSoup(arquivo_html, "html.parser")

                titulo = extrair_titulo(soup)
                primeiro_paragrafo = extrair_primeiro_paragrafo(soup)
                links_internos = extrair_links_internos(soup)
                links_imagens = extrair_links_imagens(soup)

                print("Titulo extraido:", titulo)
                print("Primeiro paragrafo:", primeiro_paragrafo[:180])
                print("Quantidade de links internos:", len(links_internos))
                print("Quantidade de imagens:", len(links_imagens))
                print("-" * 60)

                escritor_paginas.writerow(
                    [
                        pagina["url"],
                        os.path.basename(pagina["arquivo_html"]),
                        titulo,
                        primeiro_paragrafo,
                        " | ".join(links_internos),
                        " | ".join(links_imagens),
                        pagina["timestamp"],
                    ]
                )

                for imagem in links_imagens:
                    escritor_imagens.writerow(
                        [
                            pagina["url"],
                            titulo,
                            imagem,
                            pagina["timestamp"],
                        ]
                    )


def main():
    print("LINK INICIAL ESCOLHIDO:", URL_INICIAL)
    paginas_baixadas = baixar_htmls()

    if len(paginas_baixadas) == 0:
        print("Nenhuma pagina foi baixada.")
        return

    gerar_csvs(paginas_baixadas)

    print("=" * 60)
    print("Processo finalizado.")
    print("Total de paginas baixadas:", len(paginas_baixadas))
    print("HTMLs salvos na pasta:", PASTA_HTML)
    print("CSV de paginas:", CSV_PAGINAS)
    print("CSV de imagens:", CSV_IMAGENS)


main()
