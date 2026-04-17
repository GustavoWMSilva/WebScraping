# Relatorio de Desenvolvimento - Tarefa 1

## 1. Objetivo da atividade

O objetivo desta tarefa foi aplicar tecnicas de web scraping em um ambiente controlado, utilizando a Wikipedia como fonte de dados. O artigo inicial escolhido foi `https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange`.

A partir dessa pagina inicial, o codigo deveria:
- baixar o HTML da pagina;
- identificar e baixar os HTMLs de todos os links internos no formato `/wiki/`;
- extrair o titulo da pagina;
- extrair o primeiro paragrafo do artigo;
- extrair a lista de links internos;
- extrair a lista de links das imagens;
- salvar os dados em arquivos CSV com timestamp.

## 2. Logica utilizada

O desenvolvimento foi feito com base no material disponibilizado pela professora, utilizando principalmente:
- `urllib.request` e `urllib.error` para abrir paginas e tratar erros;
- `BeautifulSoup` para analisar o HTML;
- seletores CSS com `a[href^='/wiki/']` para encontrar links internos;
- coleta de `img["src"]` para localizar imagens;
- modulo `csv` para exportar os resultados.

Primeiro, o programa baixa a pagina inicial e salva o HTML em disco. Depois, usando o BeautifulSoup, identifica todos os links internos da Wikipedia encontrados nessa pagina. Em seguida, o codigo percorre esses links, baixa os HTMLs correspondentes e salva cada arquivo localmente.

Na etapa seguinte, o programa reabre os HTMLs salvos e extrai as informacoes pedidas no enunciado. O titulo e obtido a partir da tag `<title>`, o primeiro paragrafo e identificado percorrendo as tags `<p>`, os links internos sao filtrados pelo padrao `/wiki/` e os links de imagens sao obtidos a partir da tag `<img>`.

Por fim, os dados sao salvos em dois CSVs:
- `paginas_wikipedia.csv`, contendo os dados principais de cada pagina;
- `imagens_wikipedia.csv`, contendo os links das imagens encontrados.

## 3. Resultados obtidos

O codigo produz:
- uma pasta com os HTMLs baixados;
- um CSV com os dados de cada pagina;
- um CSV com os links das imagens;
- um timestamp associado a cada coleta.

Esses arquivos permitem analisar posteriormente a estrutura das paginas e os relacionamentos entre os artigos encontrados a partir da pagina inicial escolhida.

## 4. Dificuldades e problemas encontrados

Uma dificuldade importante foi garantir que os links encontrados fossem realmente internos da Wikipedia. Para isso, foi necessario filtrar apenas links que comecam com `/wiki/` e tambem remover partes extras, como trechos com `#` e `?`, para evitar duplicidades ou links incompletos.

Outra dificuldade foi tratar os links das imagens, pois muitos deles aparecem em formato relativo, como `//...` ou `/...`. Foi necessario corrigir esses formatos para gerar links completos e utilizaveis.

Tambem foi importante organizar o salvamento dos HTMLs com nomes de arquivo validos, evitando problemas com caracteres especiais.

## 5. Analise breve

Mesmo em um ambiente controlado como a Wikipedia, a coleta exige cuidados com tratamento de erros, padronizacao dos links e organizacao dos dados exportados. A atividade mostra que o scraping nao depende apenas de baixar paginas, mas tambem de limpar e estruturar corretamente as informacoes para uso posterior.

O uso da Wikipedia facilitou a atividade por ser um ambiente mais previsivel, o que permitiu focar nos conceitos principais de crawler, parsing de HTML e exportacao de dados.
