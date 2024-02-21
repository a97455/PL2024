# TPC1: Conversor de MD para HTML

## Autor

**Nome:** Henrique Nuno Marinho Malheiro

**Id:** A97455

## Descrição

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

- **Cabeçalhos (linhas iniciadas por "# texto", ou "## texto" ou "### texto")**
   In: \# Exemplo
   Out: \<h1> Exemplo \</h1>

- **Bold (pedaços de texto entre "\*\*")**
   In: Este é um \*\*exemplo** ...
   Out: Este é um \<b>exemplo</b> ...

- **Itálico (pedaços de texto entre "\*")**
   In: Este é um \*exemplo* ...
   Out:  Este é um \<i>exemplo\</i> ...

- **Lista numerada:**
   In:
     
     1. Primeiro item
     2. Segundo item
     3. Terceiro item
     
   Out:
     
     1. Primeiro item
     2. Segundo item
     3. Terceiro item
     

- **Link: [texto](endereço URL)**
   In: Como pode ser consultado em \[página da UC](http://www.uc.pt)
   Out: Como pode ser consultado em \[página da UC](http://www.uc.pt)

- **Imagem: ![texto alternativo](path para a imagem)**
   In: Como se vê na imagem seguinte: !\[imagem dum coelho](http://www.coellho.com) ...
   Out: Como se vê na imagem seguinte: !\[imagem dum coelho](http://www.coellho.com) ...