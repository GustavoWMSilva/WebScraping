# Tarefa 2 - Guia de estudo e ponto de partida

Este arquivo foi montado para te ajudar a desenvolver a Tarefa 2 com base nos materiais da professora, sem te entregar a solucao completa.

## 0. O que instalar antes de rodar

Para a Tarefa 2 voce vai precisar rodar Selenium localmente.

Voce precisa ter:
- Python instalado;
- Google Chrome instalado;
- um ambiente virtual (`venv`);
- a biblioteca `selenium`.

Bibliotecas como `json`, `re` e `time` nao precisam ser instaladas, porque ja fazem parte do Python.

### Como abrir a pasta do projeto no terminal

No PowerShell, entre na pasta onde estao os arquivos:

```powershell
cd "c:\Users\gusta\OneDrive - PUCRS - BR\2 Semestre\Documentos\Faculdade 2026\Nova pasta"
```

### Como criar o venv

Se ainda nao existir um ambiente virtual para esta tarefa:

```powershell
python -m venv .venv
```

### Como ativar o venv no Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Se der certo, normalmente o nome do ambiente aparece no inicio da linha do terminal.

### Como instalar o que precisa

Com o venv ativado:

```powershell
pip install --upgrade pip
pip install selenium notebook
```

### Como testar se esta funcionando

Teste se o Selenium foi instalado:

```powershell
python -c "import selenium; print(selenium.__version__)"
```

Se quiser testar a abertura do navegador de forma simples, use:

```powershell
python -c "from selenium import webdriver; driver = webdriver.Chrome(); driver.get('https://www.imdb.com/chart/top/'); print(driver.title); driver.quit()"
```

### Como sair do venv depois

```powershell
deactivate
```

## 1. O que a tarefa pede

Veja o enunciado em:
- `Laboratorio_1.pdf`, pagina 3

O que voce precisa entregar na Tarefa 2:
- a lista dos 250 filmes com maior avaliacao no IMDb;
- o scraping das paginas individuais desses filmes;
- os campos: titulo, ano, url do poster, imagem do poster, nota IMDb, generos e diretores;
- um arquivo JSON com os resultados.

## 2. Onde entender por que usar Selenium

Comece por aqui:
- `Orientacoes_Tarefa1.ipynb`, celulas 17 a 19
- `AULA 11.pdf`, paginas 9 a 12

Esses materiais explicam que o IMDb nao funciona bem com `requests` ou `urllib` porque o conteudo depende de JavaScript. Por isso a professora migra para Selenium.

## 3. Onde aprender a iniciar o Selenium

Estude:
- `Aula12-Selenium.ipynb`, celulas 1 a 4
- `Aula 12 - Prática com Selenium.pdf`, paginas 1 e 2

Aqui voce encontra:
- imports principais;
- `webdriver.Chrome()`;
- `WebDriverWait(driver, 10)`;
- configuracao do ambiente virtual e Jupyter.

## 4. Onde aprender a esperar o carregamento da pagina

Estude:
- `Aula12-Selenium.ipynb`, celulas 13 e 14

O ponto principal aqui e:
- `WebDriverWait`
- `EC.presence_of_all_elements_located(...)`

Isso e essencial para o IMDb, porque a pagina nao carrega tudo imediatamente.

## 5. Onde aprender a localizar elementos

Para entender os localizadores:
- `AULA 11.pdf`, pagina 27
- `AULA 11.pdf`, paginas 30 e 31
- `AULA 11.pdf`, pagina 41

Para revisar seletores CSS e busca em HTML:
- `AULA 10.pdf`, paginas 4 a 11

Use esses materiais para decidir quando vale mais usar:
- `By.CSS_SELECTOR`
- `By.XPATH`
- `find_element`
- `find_elements`

## 6. Onde esta o exemplo mais parecido com a sua tarefa

O melhor ponto de partida esta em:
- `Aula12-Selenium.ipynb`, celulas 19 a 25

Essas celulas te mostram:
- scraping de uma lista do IMDb;
- extracao de titulo, ano, nota e URL;
- abertura da pagina do filme;
- retorno para a lista;
- estrategia melhor: abrir em nova aba.

Se voce for aprender uma parte por vez, foque primeiro nessas celulas.

## 7. Como usar o notebook base que foi criado

Arquivo criado:
- `tarefa2_imdb_base.ipynb`

O que ele ja faz:
- abre a lista Top 250 do IMDb;
- coleta os cards principais da lista;
- pega titulo, ano, nota e URL do filme;
- abre paginas individuais em nova aba;
- monta uma estrutura base de dicionario;
- salva um JSON inicial.

O que falta voce desenvolver:
- completar o seletor do poster;
- completar o seletor da imagem do poster;
- completar a nota IMDb diretamente na pagina do filme;
- completar os generos;
- completar os diretores;
- aumentar o limite de teste para 250 quando estiver funcionando.

## 8. Estrategia recomendada para voce aprender melhor

Siga esta ordem:
1. Rode o notebook base com `LIMITE_LISTA = 5` e `LIMITE_DETALHES = 1`.
2. Confirme que a lista principal esta funcionando.
3. Abra manualmente a pagina de um filme e inspecione o HTML no navegador.
4. Escolha um campo por vez: primeiro titulo, depois ano, depois poster, depois generos.
5. So no final aumente para 250 filmes.

## 9. Dica final

Nao tente completar todos os campos de uma vez.

O melhor caminho para desenvolver a habilidade e:
- fazer a lista funcionar;
- testar a navegacao para a pagina do filme;
- descobrir um seletor por campo;
- validar com `print`;
- salvar em JSON no final.
