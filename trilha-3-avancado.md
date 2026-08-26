# Trilha 3 - Avançado

**O que você vai aprender:** recursão, funções que devolvem um valor
(`DEVOLVA`), o laço `ENQUANTO`, `QUEBRA`/`CONTINUA`, e geometria mais
avançada (círculos, o Teorema de Pitágoras, fractais).

Pré-requisito: ter feito a [Trilha 2 - Intermediário](trilha-2-intermediario.md).

---

## Lição 1 - Recursão: um procedimento que chama a si mesmo

Um procedimento pode chamar **a si mesmo**. Isso se chama recursão, e é
uma das ideias mais poderosas (e mais divertidas) de programação:

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

ARVORE 100
```

Veja [`exemplos/avancado/01_arvore_recursiva.logo`](exemplos/avancado/01_arvore_recursiva.logo).

**Como isso funciona:** cada galho é `0.7` vezes menor que o galho de
onde ele saiu. Como o tamanho vai encolhendo, mais cedo ou mais tarde
ele fica menor que 10 - e o `SE :TAMANHO < 10 [ SAIA ]` para a
recursão ali. Essa é a **condição de parada**: toda recursão precisa de
uma, ou ela chamaria a si mesma para sempre (até o programa travar).

**Ideia de matemática:** os tamanhos formam uma sequência geométrica
(100, 70, 49, 34.3, ...) - cada termo é o anterior vezes 0.7. É a mesma
ideia por trás de juros compostos ou meia-vida radioativa.

**Desafio 1:** troque `0.7` por `0.5` ou `0.8`. O que muda na árvore?

---

## Lição 2 - Funções: procedimentos que devolvem um valor

Até agora, seus procedimentos sempre desenhavam algo ou imprimiam algo
com `MOSTRE`. Uma **função** é um procedimento que devolve um número
para ser usado numa conta, com `DEVOLVA`:

```
PARA DOBRO :X
  DEVOLVA :X * 2
FIM

MOSTRE DOBRO 21        ; mostra 42
PF DOBRO 10             ; anda 20 passos para frente
```

Um exemplo com geometria de verdade - o Teorema de Pitágoras, para
calcular a distância entre dois pontos:

```
PARA DISTANCIA :X1 :Y1 :X2 :Y2
  DEVOLVA RAIZ ((:X2 - :X1) * (:X2 - :X1) + (:Y2 - :Y1) * (:Y2 - :Y1))
FIM

MOSTRE DISTANCIA 0 0 3 4     ; mostra 5 (o classico triangulo 3-4-5)
```

Veja [`exemplos/avancado/04_pitagoras.logo`](exemplos/avancado/04_pitagoras.logo),
que também desenha o triângulo e confere a conta.

> **Dica de sintaxe:** quando você combina **duas** chamadas de função
> numa mesma conta (por exemplo, somando o resultado de duas), coloque
> cada chamada entre parênteses - veja a Lição 3 para entender por quê.

**Desafio 2:** escreva uma função `AREA_RETANGULO :BASE :ALTURA` que
devolve a área (base × altura), e use `MOSTRE` para testar.

---

## Lição 3 - Recursão que devolve valor: fatorial e Fibonacci

Juntando `DEVOLVA` com recursão, você pode escrever funções matemáticas
clássicas:

```
PARA FATORIAL :N
  SE :N <= 1 [ DEVOLVA 1 ]
  DEVOLVA :N * FATORIAL :N - 1
FIM

PARA FIBONACCI :N
  SE :N <= 1 [ DEVOLVA :N ]
  DEVOLVA (FIBONACCI :N - 1) + (FIBONACCI :N - 2)
FIM

MOSTRE FATORIAL 5        ; 5! = 5x4x3x2x1 = 120
MOSTRE FIBONACCI 10       ; 10º numero da sequencia de Fibonacci
```

Veja [`exemplos/avancado/05_fatorial_fibonacci.logo`](exemplos/avancado/05_fatorial_fibonacci.logo).

Repare que `FATORIAL :N - 1` **não** precisa de parênteses (só existe
uma chamada de função ali, então o Logo consegue descobrir sozinho que
o `- 1` faz parte do número que vai para dentro de `FATORIAL`). Mas em
`FIBONACCI`, como há **duas** chamadas somadas, os parênteses
`(FIBONACCI :N - 1) + (FIBONACCI :N - 2)` são necessários para o Logo
não se confundir sobre onde termina uma chamada e começa a soma. Na
dúvida, **use parênteses** - nunca atrapalham.

**Ideia de algoritmo:** `FATORIAL` e `FIBONACCI` são exemplos de
**recursão** onde cada chamada resolve um pedacinho do problema e
devolve o resultado para quem chamou - até chegar no caso mais simples
(`:N <= 1`), que é resolvido diretamente, sem precisar chamar de novo.

**Desafio 3:** o que acontece se você chamar `FATORIAL -3` (um número
negativo)? Por quê? Como você mudaria o procedimento para evitar isso
(dica: `SE`)?

---

## Lição 4 - ENQUANTO: repetir até que algo mude

`REPITA` e `PARACADA` já sabem, antes de começar, quantas vezes vão
rodar. O `ENQUANTO` é diferente: ele repete **enquanto uma condição for
verdadeira**, e você não sabe de antemão quantas vezes vai rodar.

```
FACA "lado 10
ENQUANTO :lado < 150 [
  REPITA 6 [ PF :lado PD 60 ]
  FACA "lado :lado + 12
]
```

Veja [`exemplos/avancado/07_enquanto_crescente.logo`](exemplos/avancado/07_enquanto_crescente.logo)
- ele desenha hexágonos cada vez maiores, até o lado passar de 150.

**Cuidado:** se a condição nunca ficar falsa, o `ENQUANTO` roda para
sempre (um "loop infinito")! Por segurança, este Logo interrompe um
`ENQUANTO` sozinho depois de 200.000 voltas e mostra um aviso - mas o
ideal é sempre garantir que alguma coisa dentro do bloco (como o
`FACA "lado :lado + 12` acima) caminhe na direção de tornar a condição
falsa.

**Desafio 4:** reescreva a árvore recursiva da Lição 1 usando `ENQUANTO`
em vez de recursão (dica: você vai precisar de uma variável e de
`PARACADA` ou `REPITA` no lugar das duas chamadas recursivas - é bem
mais difícil! Essa dificuldade é exatamente por que recursão existe:
alguns problemas ficam muito mais simples com ela).

---

## Lição 5 - QUEBRA e CONTINUA

Dentro de qualquer laço (`REPITA`, `ENQUANTO` ou `PARACADA`):

- `QUEBRA` sai do laço imediatamente, mesmo que ele não tenha terminado.
- `CONTINUA` pula direto para a próxima volta, sem rodar o resto do
  bloco naquela volta.

```
; para depois do sexto lado de um poligono de 10 lados
REPITA 10 [
  SE REPCOUNT > 6 [ QUEBRA ]
  PF 30
  PD 36
]

; linha tracejada: pula o desenho das partes pares
REPITA 20 [
  SE (REPCOUNT % 2) = 0 [ LP PF 15 AP CONTINUA ]
  PF 15
]
```

Veja [`exemplos/avancado/06_quebra_continua.logo`](exemplos/avancado/06_quebra_continua.logo).

**Desafio 5:** use `CONTINUA` para desenhar um polígono de 20 lados
pulando (não desenhando) todo lado cujo número seja múltiplo de 3.

---

## Lição 6 - Fractais: o Floco de Neve de Koch

Um fractal é uma forma feita de partes que se parecem com o todo. A
curva de Koch é construída assim: um segmento de nível N é, na
verdade, 4 segmentos de nível N-1 (cada um 3 vezes menor), com viradas
esquerda-direita-esquerda entre eles. No nível 0, é só uma linha reta.

```
PARA KOCH :TAMANHO :NIVEL
  SE :NIVEL = 0 [
    PF :TAMANHO
    SAIA
  ]
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PD 120
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
FIM

RAPIDO
REPITA 3 [
  KOCH 300 3
  PD 120
]
NORMAL
```

Veja [`exemplos/avancado/08_floco_de_neve.logo`](exemplos/avancado/08_floco_de_neve.logo).
Repare no `RAPIDO`/`NORMAL`: com 3 níveis de recursão, o desenho tem
muitos segmentos, e o modo rápido evita esperar.

**Desafio 6:** troque `KOCH 300 3` por `KOCH 300 4`. Quantas vezes mais
lento fica? (cada nível multiplica o número de segmentos por 4).

---

## Lição 7 - Juntando tudo: um tabuleiro de xadrez

```
PARA QUADRADINHO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

RAPIDO
FACA "lado 30
PARACADA :linha DE 0 ATE 7 [
  PARACADA :coluna DE 0 ATE 7 [
    LP
    VAIPARA (:coluna * :lado - 120) (:linha * :lado - 120)
    AP
    SE ((:linha + :coluna) % 2) = 0 [ COR "preto ] [ COR "branco ]
    QUADRADINHO :lado
  ]
]
NORMAL
```

Veja [`exemplos/avancado/09_tabuleiro.logo`](exemplos/avancado/09_tabuleiro.logo).
Esse exemplo junta praticamente tudo que você aprendeu nas 3 trilhas:
procedimentos, `PARACADA` aninhado, coordenadas (`VAIPARA`), `SE`, e o
operador `%` para decidir a cor alternada (a mesma ideia de par/ímpar
da Trilha 2, só que aplicada à soma da linha com a coluna).

---

## O que você aprendeu

- Recursão, e por que toda recursão precisa de uma condição de parada.
- Funções que devolvem valores (`DEVOLVA`), inclusive recursivas.
- `ENQUANTO`, para repetir sem saber de antemão quantas vezes.
- `QUEBRA` e `CONTINUA`, para controlar um laço por dentro.
- Círculos (fórmula da circunferência), o Teorema de Pitágoras, e
  fractais recursivos.

## Para onde ir depois

Você já tem todas as ferramentas de um "Logo completo". Algumas ideias
para continuar praticando por conta própria:

- Desenhe outros fractais (o triângulo de Sierpinski é um ótimo
  próximo desafio - pesquise como ele é construído).
- Escreva uma função `EH_PRIMO :N` que decide se um número é primo,
  usando `ENQUANTO` ou `PARACADA` para testar os divisores.
- Combine `FIBONACCI` com uma "memória" (uma lista de valores já
  calculados) para deixar a função muito mais rápida para números
  grandes - isso se chama *memoização*, uma técnica real usada em
  programas de verdade.
