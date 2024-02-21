# TPC1: Conversor de MD para HTML

## Autor

**Nome:** Henrique Nuno Marinho Malheiro

**Id:** A97455

## Descrição

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:
    <ol>
        <ol>
            <li>Cabeçalhos (linhas iniciadas por "# texto", ou "## texto" ou "### texto")
                <ol>In: # Exemplo </ol>
                <ol>Out: \<h1> Exemplo \</h1></ol>
            </li>
            <li>Bold (pedaços de texto entre "**"):
                <ol>In: Este é um \** exemplo \** ...</ol>
                <ol>Out: Este é um \<b> exemplo \</b> ...</ol>
            </li>
            <li>Itálico (pedaços de texto entre "*"):
                <ol>In: Este é um \* exemplo \* ...</ol>
                <ol>Out: Este é um \<i> exemplo \</i> ...</ol>
            </li>
            <li>Lista numerada:
                <ol>
                    In: 
                    <ol>
                        <li> Primeiro item
                        </li>
                        <li> Segundo item
                        </li>
                        <li> Terceiro item
                        </li>
                    </ol>
                    Out:
                    <ol> 
                        \<ol>
                        <ol>
                        \<li> Primeiro item
                        \</li>
                        \<li> Segundo item
                        \</li>
                        \<li> Terceiro item
                        \</li>
                        <ol>
                        \</ol>
                    </ol> 
                </ol>
            </li>
            <li>Link: [texto](endereço URL)
                <ol> In: Como pode ser consultado em [página da UC](http://www.uc.pt)</ol>
                <ol> Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a></ol>
            </li>
            <li>Imagem: ![texto alternativo](path para a imagem)
                <ol>In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ... </ol>
                <ol>Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...</ol>
            </li>
        </ol>
    </ol>