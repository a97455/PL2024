# TPC6: Construir uma Gramática Independente de Contexto (LL1)

## Autor

**Nome:** Henrique Nuno Marinho Malheiro

**Id:** A97455

## Descrição

O TPC consiste em desenvolver uma Gramática Independente de Contexto (LL1) que permita tratar de prioridades de operações matemáticas, calculando os LA's (Look Aheads) dos diversos predicados.

Para tal o programa será composto pelos seguintes predicados:

- Expression -> Term SumorSub 

- SumorSub -> + Term SumorSub
            | - Term SumorSub
            | ε 

- Term -> Factor MultiorDiv

- MultiorDiv -> * Factor MultiorDiv 
              | / Factor MultiorDiv
              | ε

- Factor -> (Expression) | Number

Com esta gramática, a expressão 2*(5+4)+4/2 será analizada da seguinte forma:

- 2 -> Term -> Factor -> Number
- \* -> Term -> MultiorDiv -> *
    - (5+4) -> Factor -> Expression
        - 5 -> Term -> Factor -> Number
        - \+ -> SumorSub
        - 4 -> Term -> Factor -> Number
    - MultiorDiv -> ε
- \+ -> SumorSub -> +
    - 4 -> Term -> Factor -> Number
    - SumorSub -> ε
- / -> Term -> MultiorDiv -> /
    - 2 -> Factor -> Number 
    - MultiorDiv -> ε