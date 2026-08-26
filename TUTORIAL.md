# Tutorial de Logo em Python

Este é um pequeno "Logo" (a linguagem clássica de ensino de programação, criada
nos anos 1960) escrito em Python. Você dá comandos para uma tartaruga que
desenha na tela, e no caminho aprende geometria, ângulos, multiplicação,
frações e até um pouco de álgebra e recursão.

## 1. Preparando o computador

Você precisa do Python 3 instalado (o Logo em Python não usa nenhuma
biblioteca extra — só o Python "puro", que já traz o módulo `turtle`).

Para verificar se já está instalado, abra o terminal (PowerShell) e digite:

```
python --version
```

Se aparecer algo como `Python 3.x.x`, está tudo certo. Se não, instale o
Python em https://www.python.org/downloads/ (marque a opção "Add Python to
PATH" durante a instalação).

## 2. Rodando o programa

Dentro da pasta `logo`, há duas formas de usar:

**Modo interativo** (digitar comandos um a um e ver o desenho na hora):

```
python logo.py
```

**Rodando um arquivo pronto** (os exemplos ficam na pasta `exemplos`):

```
python logo.py exemplos\01_quadrado.logo
```

No modo interativo, digite `SAIR` para encerrar.

## 3. Os primeiros comandos

A tartaruga começa no centro da tela, olhando para cima. Ela entende:

| Comando      | O que faz                                  |
|--------------|---------------------------------------------|
| `PF 100`     | anda **p**ara **f**rente 100 passos          |
| `PT 50`      | anda **p**ara **t**rás 50 passos             |
| `PD 90`      | gira **p**ara a **d**ireita 90 graus         |
| `PE 45`      | gira **p**ara a **e**squerda 45 graus        |

Abra o modo interativo (`python logo.py`) e experimente:

```
logo> PF 100
logo> PD 90
logo> PF 100
```

**Pergunta para pensar com seu filho/a:** quantos graus tem uma volta
completa? E meia volta? `PD 180` faz a tartaruga dar meia-volta — teste!

## 4. Desenhando um quadrado (multiplicação e ângulos)

Digitar `PF 100` e `PD 90` quatro vezes funciona, mas é repetitivo. O
comando `REPITA` repete um bloco de comandos:

```
REPITA 4 [ PF 100 PD 90 ]
```

Isso desenha um quadrado. Ligação com a matemática:

- Um quadrado tem **4 lados**, por isso `REPITA 4`.
- A tartaruga sempre gira o mesmo ângulo em cada canto, e no final ela dá
  uma volta completa: `4 x 90 = 360` graus.

Veja o arquivo [`exemplos/01_quadrado.logo`](exemplos/01_quadrado.logo).

**Desafio:** que comando desenha um triângulo com lados de 100? (Dica: um
triângulo tem 3 lados, e o giro em cada canto precisa ser `360 / 3`.)

## 5. Procedimentos com parâmetros (um poligono qualquer)

Em vez de repetir o código para cada polígono, podemos criar um
**procedimento** — como uma "receita" com nome, que pode receber números
(variáveis, escritas com `:`):

```
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [
    PF :TAMANHO
    PD 360 / :LADOS
  ]
FIM

POLIGONO 6 50    ; um hexágono (6 lados) de tamanho 50
POLIGONO 3 80    ; um triângulo de tamanho 80
```

Aqui aparece uma ideia bem importante da matemática: `:LADOS` e `:TAMANHO`
são como **incógnitas** — o mesmo procedimento funciona para qualquer
número de lados, porque a fórmula `360 / :LADOS` sempre calcula o ângulo
externo certo (é o mesmo princípio por trás da fórmula da soma dos ângulos
de um polígono!).

Veja [`exemplos/02_poligonos.logo`](exemplos/02_poligonos.logo).

## 6. Cores e velocidade (só para deixar bonito)

```
COR "vermelho
VELOCIDADE 3      ; de 1 (devagar) a 10 (rápido), ou 0 (instantâneo)
ESPESSURA 3        ; grossura do traço
```

Cores disponíveis: `preto`, `branco`, `vermelho`, `verde`, `azul`,
`amarelo`, `laranja`, `roxo`, `rosa`, `cinza`, `marrom`, `ciano`, `magenta`.

## 7. Estrelas (mais ângulos)

Se, em vez de girar `360 / :PONTAS`, a tartaruga girar o **dobro** disso,
a linha "pula" uma ponta e cruza por dentro — e vira uma estrela:

```
PARA ESTRELA :PONTAS :TAMANHO
  REPITA :PONTAS [
    PF :TAMANHO
    PD 360 * 2 / :PONTAS
  ]
FIM

ESTRELA 5 150
```

Veja [`exemplos/03_estrela.logo`](exemplos/03_estrela.logo). Desafio:
tente `ESTRELA 7 150` — o que muda?

## 8. REPCOUNT: contando as voltas (sequências)

Dentro de um `REPITA`, a palavra `REPCOUNT` vale o número da repetição
atual (1, depois 2, depois 3, ...). Isso permite criar sequências que
crescem:

```
REPITA 60 [
  PF REPCOUNT * 2
  PD 91
]
```

A cada volta, o lado fica um pouco maior (`REPCOUNT * 2`: 2, 4, 6, 8...) —
e o resultado é uma espiral! Veja
[`exemplos/04_espiral.logo`](exemplos/04_espiral.logo).

## 9. Variáveis, condições e a tabuada

`FACA "nome valor` guarda um valor em uma variável, e `SE condição [ ... ]`
executa um bloco só se a condição for verdadeira (`=`, `<`, `>`, `<=`,
`>=`, `<>` de "diferente"):

```
FACA "idade 10
SE :idade > 8 [ MOSTRE "crescendo ]
```

O comando `MOSTRE valor` imprime um número (ou o resultado de uma conta)
no terminal — ótimo para "ver" contas em vez de só desenhar. O exemplo
[`exemplos/05_tabuada.logo`](exemplos/05_tabuada.logo) desenha um gráfico
de barras da tabuada de 7 **e** imprime cada resultado (`1x7=7`, `2x7=14`,
...) — uma forma visual de estudar a tabuada.

## 10. Bônus avançado: recursão (uma árvore)

Um procedimento pode chamar **a si mesmo** — isso se chama recursão. É
uma ideia poderosa (e um pouco mais avançada; bacana para uma criança
mais grande ou para explorar junto):

```
PARA ARVORE :TAMANHO
  SE :TAMANHO < 10 [
    SAIA
  ]
  PF :TAMANHO
  PD 25
  ARVORE :TAMANHO * 0.7
  PE 50
  ARVORE :TAMANHO * 0.7
  PD 25
  PT :TAMANHO
FIM
```

Cada galho é `0.7` vezes menor que o anterior (uma multiplicação por uma
fração/decimal), até ficar menor que 10 — aí o `SE` para a recursão. Sem
essa "condição de parada", o procedimento chamaria a si mesmo para
sempre! Veja [`exemplos/06_arvore.logo`](exemplos/06_arvore.logo).

## 11. Desafios para praticar

1. Desenhe um retângulo (lados diferentes: 150 e 80).
2. Faça um procedimento `RETANGULO :BASE :ALTURA`.
3. Desenhe uma "casa": um quadrado com um triângulo em cima.
4. Mude `ESTRELA` para desenhar várias estrelas de cores diferentes ao
   redor da tela, usando `VAIPARA x y` para mudar de lugar entre uma e
   outra.
5. Crie `TABUADA` para outro número (`TABUADA 4`, `TABUADA 9`...) e
   compare os gráficos de barras — qual cresce mais rápido?

## 12. Referência rápida de comandos

| Comando | Sinônimos | O que faz |
|---|---|---|
| `PF n` | `FORWARD`, `FD` | anda para frente |
| `PT n` | `BACK`, `BK` | anda para trás |
| `PD n` | `RIGHT`, `RT` | gira para a direita (graus) |
| `PE n` | `LEFT` | gira para a esquerda (graus) |
| `LP` | `PENUP` | levanta a caneta (anda sem desenhar) |
| `AP` | `PENDOWN` | abaixa a caneta (volta a desenhar) |
| `LT` | `CLEARSCREEN`, `LIMPA` | limpa a tela |
| `MT` / `ET` | `SHOWTURTLE` / `HIDETURTLE` | mostra/esconde a tartaruga |
| `OP` | `HOME` | volta para o centro, olhando para cima |
| `VAIPARA x y` | `SETXY` | vai direto para a posição (x, y) |
| `DEFINARUMO n` | `SETHEADING` | aponta para a direção n (0 = cima) |
| `COR "nome` ou `COR r g b` | `SETCOLOR` | muda a cor do traço |
| `ESPESSURA n` | `PENSIZE` | muda a grossura do traço |
| `VELOCIDADE n` | `SPEED` | 0 (instantâneo) a 10 (rápido) |
| `RAPIDO` | `TURBO` | desliga a atualização da tela a cada passo (desenhos pesados ficam quase instantâneos) |
| `NORMAL` | | volta a mostrar o desenho sendo feito passo a passo |
| `ZOOM n` | | aproxima (n > 1) ou afasta (0 < n < 1) a visão da tela; `ZOOM 1` volta ao normal |
| `REPITA n [ ... ]` | `REPEAT` | repete o bloco n vezes |
| `REPCOUNT` | | número da repetição atual dentro do REPITA |
| `PARA nome :a :b ... / FIM` | `TO` / `END` | define um procedimento |
| `SE condição [ ... ] [ ... ]` | `IF` | executa um bloco se for verdade (segundo bloco = senão) |
| `FACA "nome valor` | `MAKE` | guarda um valor numa variável |
| `MOSTRE valor` | `PRINT`, `SHOW` | imprime um número no terminal |
| `SAIA` | `STOP` | sai do procedimento atual |
| `PARE` | | para o programa inteiro |

Operadores matemáticos nas expressões: `+ - * / %` (`%` é o resto da
divisão) e parênteses `( )` para agrupar contas, por exemplo
`PF (10 + 5) * 2`. Use `RAIZ n` (ou `SQRT n`) para raiz quadrada, por
exemplo `PF 100 * RAIZ 2` anda a diagonal de um quadrado de lado 100.
`PI` vale o número π (3.14159...) — útil para desenhar circunferências,
por exemplo `REPITA 360 [ PF 2 * PI * 100 / 360   PD 1 ]` desenha um
círculo de raio 100.

Divirta-se explorando junto com seu filho ou filha!
