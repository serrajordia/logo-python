# Trilha 1 - Básico

**O que você vai aprender:** dar comandos para o computador em sequência,
ângulos e polígonos, e o primeiro (e mais importante) jeito de evitar
repetir código: o laço `REPITA`.

Pré-requisito: ter o Python instalado e saber abrir o modo interativo.
Veja a seção "Preparando o computador" do [TUTORIAL.md](TUTORIAL.md) se
ainda não fez isso.

---

## Lição 1 - A tartaruga e os primeiros passos

Abra o modo interativo (`python logo.py`). A tartaruga aparece no centro
da tela, olhando para cima. Ela entende quatro comandos de movimento:

| Comando  | O que faz |
|----------|-----------|
| `PF n`   | anda **p**ara **f**rente n passos |
| `PT n`   | anda **p**ara **t**rás n passos |
| `PD n`   | gira **p**ara a **d**ireita n graus |
| `PE n`   | gira **p**ara a **e**squerda n graus |

Experimente:

```
logo> PF 100
logo> PD 90
logo> PF 100
```

**Ideia de programação:** um programa é uma **sequência de instruções**
executadas uma depois da outra, na ordem em que você escreve. Trocar a
ordem muda o resultado - tente escrever `PD 90` antes de `PF 100` e veja
a diferença.

**Ideia de geometria:** uma volta completa tem 360 graus. Meia volta,
180. Um quarto de volta (como em `PD 90`), 90. Teste `PD 360` - a
tartaruga dá uma volta inteira e fica olhando para a mesma direção de
antes.

**Desafio 1:** faça a tartaruga desenhar a letra "L" (duas linhas retas
com um cantinho de 90 graus).

**Desafio 2:** faça a tartaruga desenhar um triângulo **sem usar
`REPITA`** (você ainda não aprendeu, mas dá pra fazer digitando `PF` e
`PD` três vezes cada). Dica: o giro em cada canto é `360 / 3 = 120`
graus.

---

## Lição 2 - REPITA: não repita você mesmo

Fazer `PF 100` e `PD 90` quatro vezes é cansativo de digitar. O
`REPITA` faz isso por você:

```
REPITA 4 [ PF 100 PD 90 ]
```

Isso desenha um quadrado perfeito. Veja
[`exemplos/basico/01_quadrado.logo`](exemplos/basico/01_quadrado.logo).

**Por que funciona:** um quadrado tem 4 lados iguais. Em cada canto, a
tartaruga vira o mesmo ângulo, e depois das 4 viradas ela deu uma volta
completa: `4 × 90 = 360`.

**Ideia de programação:** isso é um **laço** (*loop*, em inglês) - o
bloco entre colchetes `[ ]` roda várias vezes. É a ferramenta mais
importante para evitar copiar e colar o mesmo comando repetidamente.

**Ideia de geometria:** essa mesma ideia funciona para QUALQUER
polígono regular (todos os lados e ângulos iguais): o ângulo de giro é
sempre `360 / numero_de_lados`. Veja
[`exemplos/basico/02_poligonos_diretos.logo`](exemplos/basico/02_poligonos_diretos.logo),
que desenha um triângulo, um pentágono e um hexágono, cada um com seu
próprio ângulo calculado dessa forma.

**Desafio 3:** desenhe um octógono (8 lados). Qual é o ângulo de giro?

**Desafio 4:** o que acontece se você usar `REPITA 4 [ PF 100 PD 91 ]`
(91 em vez de 90)? Tente e observe o desenho. Por que ele não fecha?

---

## Lição 3 - Cores e velocidade

Deixe os desenhos mais bonitos com:

```
COR "azul
VELOCIDADE 5      ; de 1 (devagar) a 10 (rapido), ou 0 (instantaneo)
ESPESSURA 3        ; grossura do traco
```

Cores disponíveis: `preto`, `branco`, `vermelho`, `verde`, `azul`,
`amarelo`, `laranja`, `roxo`, `rosa`, `cinza`, `marrom`, `ciano`,
`magenta`. Veja
[`exemplos/basico/04_cores.logo`](exemplos/basico/04_cores.logo).

Para andar **sem** desenhar (por exemplo, para mover a tartaruga para
outro lugar da tela antes de começar um novo desenho), levante a
caneta:

```
LP          ; levanta a caneta - anda sem desenhar
PF 100
AP          ; abaixa a caneta - volta a desenhar
```

---

## Lição 4 - REPCOUNT: contando as voltas

Dentro de um `REPITA`, a palavra especial `REPCOUNT` vale o número da
repetição atual: 1 na primeira volta, 2 na segunda, e assim por diante.
Isso permite criar desenhos que **mudam** a cada repetição, não só
desenhos que se repetem identicos:

```
REPITA 60 [
  PF REPCOUNT * 2
  PD 91
]
```

A cada volta, o lado fica um pouquinho maior (2, 4, 6, 8...) - e o
resultado é uma espiral! Veja
[`exemplos/basico/03_espiral.logo`](exemplos/basico/03_espiral.logo).

**Ideia de programação:** `REPCOUNT` é a sua primeira variável "de
graça" - um valor que muda sozinho a cada volta do laço. Na próxima
trilha você vai aprender a criar suas próprias variáveis.

**Desafio 5:** troque `PD 91` por `PD 90` na espiral - o que muda? E se
for `PD 89`?

**Desafio 6:** crie sua própria espiral que cresce mais rápido, usando
`REPCOUNT * 3` em vez de `REPCOUNT * 2`.

---

## O que você aprendeu

- Mover e girar a tartaruga (`PF`, `PT`, `PD`, `PE`).
- Que um algoritmo é uma sequência de passos, executados em ordem.
- Repetir comandos com `REPITA`, em vez de copiar e colar.
- Que a soma dos ângulos externos de qualquer polígono regular é 360°.
- Usar `REPCOUNT` para criar padrões que mudam a cada repetição.
- Cores, espessura e velocidade do traço.

## Pronto para a próxima trilha?

Na [Trilha 2 - Intermediário](trilha-2-intermediario.md) você vai
aprender a **criar seus próprios comandos** (procedimentos), guardar
valores em variáveis, tomar decisões com `SE`, e um novo tipo de laço
(`PARACADA`) que conta com uma variável de verdade.
