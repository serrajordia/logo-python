# Trilha 2 - Intermediário

**O que você vai aprender:** criar seus próprios comandos
(procedimentos), guardar valores em variáveis, tomar decisões com `SE`,
um laço `PARACADA` com uma variável de verdade, e a arte de planejar um
desenho complicado quebrando ele em partes menores.

Pré-requisito: ter feito a [Trilha 1 - Básico](trilha-1-basico.md).

---

## Lição 1 - Procedimentos: crie seus próprios comandos

Na trilha básica, você desenhou um triângulo, um pentágono e um
hexágono repetindo quase o mesmo código três vezes. Em programação,
repetir código parecido é sinal de que existe uma forma melhor: criar
um **procedimento** (uma "receita" com nome, que você pode chamar
sempre que precisar).

```
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [
    PF :TAMANHO
    PD 360 / :LADOS
  ]
FIM

POLIGONO 6 50    ; um hexagono (6 lados) de tamanho 50
POLIGONO 3 80    ; um triangulo de tamanho 80
```

`:LADOS` e `:TAMANHO` são **parâmetros**: números que você "empresta"
ao procedimento cada vez que o chama. Isso é parecido com uma incógnita
em matemática (como o `x` numa equação) - o mesmo procedimento funciona
para qualquer número de lados e qualquer tamanho, porque a conta
`360 / :LADOS` é sempre recalculada. Veja
[`exemplos/intermediario/01_poligono_funcao.logo`](exemplos/intermediario/01_poligono_funcao.logo).

**Ideia de programação:** isto se chama **abstração** - transformar um
padrão repetido em uma ferramenta reutilizável com nome. É uma das
ideias mais importantes de toda a programação.

**Desafio 1:** crie um procedimento `RETANGULO :BASE :ALTURA` (ele não
pode usar `REPITA` sozinho, porque os lados não são todos iguais - vai
precisar de 2 pares de `PF`/`PD`).

---

## Lição 2 - Variáveis com FACA

Um procedimento tem parâmetros próprios, mas às vezes você quer guardar
um valor "solto", fora de um procedimento. Para isso existe `FACA`:

```
FACA "idade 10
MOSTRE :idade
FACA "idade :idade + 1
MOSTRE :idade
```

`FACA "nome valor` guarda `valor` numa variável chamada `nome`. Depois,
`:nome` (com dois-pontos) usa esse valor em qualquer conta.

`MOSTRE valor` imprime um número no terminal (ótimo para "ver" o
resultado de uma conta sem precisar desenhar nada).

---

## Lição 3 - Estrelas e mais ângulos

Se, em vez de girar `360 / :PONTAS`, a tartaruga girar o **dobro**
disso, a linha "pula" uma ponta e cruza por dentro - e vira uma
estrela:

```
PARA ESTRELA :PONTAS :TAMANHO
  REPITA :PONTAS [
    PF :TAMANHO
    PD 360 * 2 / :PONTAS
  ]
FIM

ESTRELA 5 150
```

Veja [`exemplos/intermediario/02_estrela.logo`](exemplos/intermediario/02_estrela.logo).

**Desafio 2:** tente `ESTRELA 7 150` e `ESTRELA 4 150`. O que muda? Por
que uma estrela de 4 pontas fica esquisita?

---

## Lição 4 - SE: fazendo o programa decidir

`SE condição [ ... ]` executa um bloco só se a condição for verdadeira.
Você pode comparar números com `=`, `<`, `>`, `<=`, `>=` e `<>`
(diferente). E pode dar um segundo bloco para "senão":

```
SE :idade >= 18 [ MOSTRE [Pode dirigir] ] [ MOSTRE [Ainda nao] ]
```

Um exemplo mais matemático: classificar um triângulo pelos seus 3
lados (equilátero, isósceles ou escaleno), encadeando vários `SE`. Veja
[`exemplos/intermediario/06_condicionais.logo`](exemplos/intermediario/06_condicionais.logo).

> Este Logo ainda não tem um jeito de juntar duas condições com "E"/"OU"
> - por isso usamos um `SE` dentro do outro no lugar disso. Veja como
> fica no exemplo.

**Desafio 3:** escreva um procedimento `PAR_OU_IMPAR :N` que usa
`MOSTRE` para dizer se `:N` é par ou ímpar. Dica: o resto da divisão por
2 é `:N % 2` (par quando o resto é 0).

---

## Lição 5 - PARACADA: um laço com uma variável de verdade

`REPCOUNT` (da trilha básica) só existe dentro de um `REPITA` e sempre
conta de 1 em 1. O `PARACADA` é mais poderoso: você escolhe o nome da
variável, o valor inicial, o final, e (se quiser) o passo:

```
PARACADA :i DE 1 ATE 10 [
  MOSTRE :i
]

PARACADA :i DE 10 ATE 1 PASSO -1 [   ; contagem regressiva
  MOSTRE :i
]
```

Como a variável tem nome, dá para usar **dois `PARACADA`, um dentro do
outro**, para repetir em duas dimensões - por exemplo, uma grade de
quadradinhos (linhas × colunas), como um tabuleiro:

```
PARA QUADRADINHO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

PARACADA :linha DE 0 ATE 4 [
  PARACADA :coluna DE 0 ATE 4 [
    VAIPARA (:coluna * 40 - 100) (:linha * 40 - 100)
    QUADRADINHO 30
  ]
]
```

Veja [`exemplos/intermediario/05_paracada_grade.logo`](exemplos/intermediario/05_paracada_grade.logo).

**Ideia de algoritmo:** repetir em duas dimensões (uma variável para a
linha, outra para a coluna) é a base de qualquer programa que trabalha
com tabelas, planilhas, tabuleiros de jogo ou imagens.

---

## Lição 6 - Planejamento: quebrando um desenho complicado

Uma casa parece complicada - mas é só um quadrado com um triângulo em
cima. **Planejar** um desenho é descobrir em quais formas simples ele
pode ser quebrado, e depois escrever um procedimento para cada uma:

```
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

PARA CASA :LADO
  QUADRADO :LADO
  LP
  PF :LADO
  PD 90
  AP
  PE 60
  PF :LADO
  PD 120
  PF :LADO
FIM

CASA 120
```

Veja [`exemplos/intermediario/03_casa.logo`](exemplos/intermediario/03_casa.logo)
com cores. Repare que `CASA` **reaproveita** o procedimento `QUADRADO`
que você já tinha - programadores raramente escrevem tudo do zero,
eles reaproveitam pedaços que já funcionam.

**Desafio 4 (projeto):** desenhe um "boneco de palitos" (cabeça =
círculo pequeno ou quadrado, corpo, braços, pernas), usando um
procedimento para cada parte do corpo.

---

## Bônus: tabuada em gráfico de barras

Juntando `FACA`, `REPCOUNT`, `PARA` e `MOSTRE`, dá pra "ver" a tabuada
crescendo:

Veja [`exemplos/intermediario/04_tabuada_grafico.logo`](exemplos/intermediario/04_tabuada_grafico.logo)
- ele desenha um gráfico de barras da tabuada de 7 **e** imprime cada
conta (`7, 14, 21, ...`) no terminal.

**Desafio 5:** mude para a tabuada de outro número e compare os dois
gráficos - qual cresce mais rápido?

---

## O que você aprendeu

- Criar procedimentos com parâmetros (`PARA`/`FIM`) - abstração.
- Guardar e atualizar valores com variáveis (`FACA`).
- Tomar decisões com `SE` (e simular "E" encadeando `SE`s).
- Repetir com uma variável de verdade, inclusive laços aninhados
  (`PARACADA`).
- Planejar um desenho complexo decompondo em partes reutilizáveis.

## Pronto para a próxima trilha?

Na [Trilha 3 - Avançado](trilha-3-avancado.md) você vai aprender
recursão (procedimentos que chamam a si mesmos), funções que devolvem
um valor (`DEVOLVA`), o laço `ENQUANTO`, `QUEBRA`/`CONTINUA`, e vai
desenhar fractais de verdade.
