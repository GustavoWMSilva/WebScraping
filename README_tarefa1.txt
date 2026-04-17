Tarefa 1 - Laboratorio 1 (Wikipedia)

Este codigo foi reorganizado para seguir apenas a linha mostrada no material da professora:
- urllib.request e urllib.error
- BeautifulSoup
- seletor a[href^='/wiki/']
- coleta de img["src"]
- salvamento em CSV

Link usado no script:
- https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange

Arquivos gerados:
- tarefa1_wikipedia.py: script principal
- tarefa1_wikipedia.ipynb: versao em notebook, organizada em etapas
- relatorio_tarefa1.md: relatorio curto para apoiar a entrega
- htmls_lab1_vancouver: HTMLs baixados
- paginas_wikipedia.csv: dados de cada pagina
- imagens_wikipedia.csv: links das imagens

Como executar com o venv:
1. Abra o terminal na pasta do projeto.
2. Rode:

.\.venv\Scripts\python.exe tarefa1_wikipedia.py

O script faz:
- baixa o HTML da pagina inicial;
- coleta os links internos /wiki/ dessa pagina;
- baixa os HTMLs desses links;
- extrai titulo, primeiro paragrafo, links internos e links das imagens;
- salva dois CSVs com timestamp.

Observacoes:
- O codigo possui comentarios didaticos e prints-chave para facilitar a correcao.
- O notebook segue a mesma logica do script, mas separado em celulas para facilitar a apresentacao.
