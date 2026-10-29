# Trilha 1 - Básico

**O que você vai aprender:** dar comandos para o computador em sequência,
ângulos e polígonos, cores, coordenadas e o primeiro (e mais importante)
jeito de evitar repetir código: o laço `REPITA`.

**Formato:** 10 aulas de **20 minutos** cada, com dificuldade crescente.
Pré-requisito: nenhum. É só abrir a [versão web](https://serrajordia.github.io/logo-python/web/)
(roda no navegador) ou, no computador, `python logo.py` (veja a seção
"Preparando o computador" do [TUTORIAL.md](TUTORIAL.md)).

## Como funciona cada aula

| Tempo | Etapa | O que fazer |
|-------|-------|-------------|
| 3 min | 🔥 **Aquecimento** | rever a aula anterior com uma pergunta rápida |
| 5 min | 💡 **Ideia nova** | ler a explicação e testar os exemplos |
| 7 min | 🛠️ **Mão na massa** | fazer o desenho principal da aula |
| 5 min | 🎯 **Exercícios** | resolver os exercícios (⭐ fácil, ⭐⭐ médio, ⭐⭐⭐ difícil) |

Cada aula tem ainda um **🚀 Desafio extra** opcional (fica fora dos 20
minutos) e as **respostas** dos exercícios escondidas no fim — tente
primeiro, espie depois! Se um exercício não couber nos 5 minutos, deixe
para o começo da próxima aula.

> **Dica:** na versão web, o controle 🐢—🐇 no topo da página ajusta a
> velocidade da tartaruga (e **∞** desenha tudo de uma vez). No
> computador, o comando `VELOCIDADE` faz o mesmo (veja a Aula 5).

---

## Aula 1 - A tartaruga e os primeiros passos

### 🔥 Aquecimento (3 min)

Abra o Logo. A tartaruga aparece no centro da tela, olhando para
**cima**. Digite `PF 100` e aperte Enter. Para onde ela foi? Quantos
"passos" você acha que ela andou?

### 💡 Ideia nova (5 min)

A tartaruga entende quatro comandos de movimento:

| Comando  | O que faz |
|----------|-----------|
| `PF n`   | anda **p**ara **f**rente n passos |
| `PT n`   | anda **p**ara **t**rás n passos |
| `PD n`   | gira **p**ara a **d**ireita n graus |
| `PE n`   | gira **p**ara a **e**squerda n graus |

**Ideia de programação:** um programa é uma **sequência de instruções**
executadas uma depois da outra, na ordem em que você escreve. Trocar a
ordem muda o resultado — escreva `PD 90` antes de `PF 100` e compare.

**Ideia de matemática:** uma volta completa tem 360 graus. Meia volta,
180. Um quarto de volta (um "canto reto"), 90. Teste `PD 360`: a
tartaruga dá uma volta inteira e fica olhando para o mesmo lado de antes.

### 🛠️ Mão na massa (7 min)

Digite os três comandos, um de cada vez, e veja o que aparece:

<!-- exemplo: basico/05_primeiros_passos.logo -->
```logo
; sobe, vira a direita (canto de 90 graus) e anda de lado
PF 100
PD 90
PF 100
```

*(Este programa está pronto em [`exemplos/basico/05_primeiros_passos.logo`](exemplos/basico/05_primeiros_passos.logo).)*

Agora faça um **canto diferente**: use `PD 45` no lugar de `PD 90`.
Repare que 45 é a *metade* de 90 — o canto fica mais "aberto".

### 🎯 Exercícios (5 min)

- **1.1** ⭐ Desenhe a letra **L** de pé (uma linha vertical e uma
  linha curta na horizontal, formando um canto de 90°).
- **1.2** ⭐ Desenhe uma **escada de 3 degraus** (sobe, vira, anda, vira
  para o outro lado...).
- **1.3** ⭐⭐ Desenhe um **quadrado** de lado 80 usando só `PF` e `PD`
  (sem `REPITA`, você ainda não aprendeu).
- **1.4** ⭐⭐ Desenhe um **triângulo** de lado 100 sem `REPITA`. Dica:
  o giro em cada canto é `360 / 3 = 120` graus.
- **1.5** ⭐⭐⭐ Desenhe uma **seta apontando para cima**: uma haste
  vertical e duas "asinhas" na ponta. Dica: as asinhas formam um ângulo
  de 150° com a haste (180° − 30°).

### 🚀 Desafio extra

Escreva as suas iniciais com os comandos que já conhece (letras feitas
só de linhas retas e cantos de 90°, como L, T, H, E).

<details>
<summary>Ver respostas</summary>

**1.1**

```logo
PF 100
PT 100
PD 90
PF 60
```

**1.2** (sobe, vai para a direita, sobe, vai para a direita...)

```logo
PF 30
PD 90
PF 30
PE 90
PF 30
PD 90
PF 30
PE 90
PF 30
PD 90
PF 30
PE 90
```

**1.3**

```logo
PF 80
PD 90
PF 80
PD 90
PF 80
PD 90
PF 80
PD 90
```

**1.4**

```logo
PF 100
PD 120
PF 100
PD 120
PF 100
PD 120
```

**1.5**

```logo
PF 100
PD 150
PF 30
PT 30
PE 300
PF 30
```

(Depois de desenhar a asinha da direita, a tartaruga volta à ponta com
`PT 30` e gira 300° para a esquerda — o mesmo que 60° para a direita —
para apontar na direção da asinha da esquerda.)

</details>

---

## Aula 2 - Girando: o mundo dos ângulos

### 🔥 Aquecimento (3 min)

Sem usar o computador: quantos graus tem uma volta completa? E meia
volta? Se a tartaruga girar `PD 90` quatro vezes seguidas, para onde ela
fica olhando?

### 💡 Ideia nova (5 min)

Um **ângulo** mede quanto você gira. Alguns ângulos têm nome:

| Ângulo | Nome | Parece com... |
|--------|------|---------------|
| 90°  | ângulo reto | o canto de uma folha de papel |
| 45°  | metade de um reto | a diagonal de um quadrado |
| 180° | meia volta | uma linha reta (fica de costas) |
| 360° | volta completa | volta ao mesmo lugar, olhando igual |

`PD` e `PE` giram para lados opostos, então um **desfaz** o outro:
`PD 30` seguido de `PE 30` deixa a tartaruga olhando para o mesmo lado de
antes. Isso também funciona entre `PF` e `PT`.

### 🛠️ Mão na massa (7 min)

Vamos desenhar a letra **Z** — ela precisa de um ângulo que não é reto:

<!-- exemplo: basico/06_letra_z.logo -->
```logo
; a barra de cima, a diagonal, a barra de baixo
PD 90
PF 60
PD 135
PF 85
PE 135
PF 60
```

*(Este programa está pronto em [`exemplos/basico/06_letra_z.logo`](exemplos/basico/06_letra_z.logo).)*

Por que **135**? Depois de girar `PD 90` a tartaruga olha para a direita.
Para descer na diagonal (45° do chão), ela ainda precisa girar
`180 - 45 = 135` graus. A diagonal de um quadrado de lado 60 mede cerca
de 85 (veremos o motivo na Trilha 3).

### 🎯 Exercícios (5 min)

- **2.1** ⭐ Faça a tartaruga dar uma volta completa e voltar a olhar
  para cima, usando só `PD 90` (quantas vezes?).
- **2.2** ⭐ Desenhe a letra **T** (haste vertical de 100 e uma barra de
  80 em cima, centrada).
- **2.3** ⭐⭐ Se a tartaruga girou `PD 30`, quanto ela precisa girar
  para a **esquerda** para voltar ao rumo original? Teste no computador.
- **2.4** ⭐⭐ Desenhe a letra **V** (duas linhas de 100 que se encontram
  numa ponta, abertas num ângulo de 60° entre si).
- **2.5** ⭐⭐⭐ Desenhe um **losango** de lado 80: os giros alternam
  entre 60° e 120°. Some os quatro giros: dá 360°?

### 🚀 Desafio extra

Desenhe um **paralelogramo** com lados 100 e 50. Os giros são os mesmos
do losango (60° e 120°)? Por quê?

<details>
<summary>Ver respostas</summary>

**2.1** Quatro vezes (4 × 90 = 360):

```logo
PD 90
PD 90
PD 90
PD 90
```

**2.2**

```logo
PF 100
PE 90
PF 40
PT 80
```

**2.3** `PE 30` (os giros em sentidos opostos se cancelam).

**2.4** (a tartaruga sobe pela perna da esquerda até a ponta de baixo e
sobe pela da direita; usamos `PT` para ir "para baixo")

```logo
PE 30
PF 100
PT 100
PD 60
PF 100
```

**2.5** 60 + 120 + 60 + 120 = 360 — sim!

```logo
PF 80
PD 60
PF 80
PD 120
PF 80
PD 60
PF 80
PD 120
```

**Desafio:** sim, os giros são os mesmos: um paralelogramo tem os lados
opostos paralelos, então os ângulos de giro se alternam do mesmo jeito.

```logo
PF 100
PD 60
PF 50
PD 120
PF 100
PD 60
PF 50
PD 120
```

</details>

---

## Aula 3 - REPITA: não repita você mesmo

### 🔥 Aquecimento (3 min)

Na aula passada você desenhou um quadrado digitando `PF` e `PD` quatro
vezes cada. Cansativo, né? Quantas linhas de código foram? (Resposta: 8.)

### 💡 Ideia nova (5 min)

O `REPITA` faz o trabalho chato por você:

```
REPITA 4 [ PF 100 PD 90 ]
```

Tudo o que está entre os colchetes `[ ]` roda 4 vezes. Isso desenha um
quadrado perfeito (veja também
[`exemplos/basico/01_quadrado.logo`](exemplos/basico/01_quadrado.logo)).

**Ideia de programação:** isso é um **laço** (*loop*): um bloco de
comandos que roda várias vezes. É a ferramenta mais importante para
evitar copiar e colar.

**Ideia de matemática:** depois dos 4 giros de 90°, a tartaruga deu uma
volta completa: `4 × 90 = 360`. Por isso o quadrado fecha.

### 🛠️ Mão na massa (7 min)

Um retângulo tem dois pares de lados diferentes, então o bloco repetido
tem *dois* lados:

<!-- exemplo: basico/07_retangulo.logo -->
```logo
; 2 voltas de (lado comprido + canto + lado curto + canto)
REPITA 2 [ PF 120 PD 90 PF 60 PD 90 ]
```

*(Este programa está pronto em [`exemplos/basico/07_retangulo.logo`](exemplos/basico/07_retangulo.logo).)*

Conte: 2 repetições × 2 cantos = 4 cantos de 90°.

### 🎯 Exercícios (5 min)

- **3.1** ⭐ Desenhe um quadrado de lado 80 com `REPITA`.
- **3.2** ⭐ Desenhe um triângulo de lado 100 com `REPITA` (giro de 120°).
- **3.3** ⭐⭐ Desenhe um retângulo de 150 por 50.
- **3.4** ⭐⭐ Desenhe **dois quadrados lado a lado**, de lado 60. Dica:
  depois do primeiro, ande 60 para a direita (`PD 90`, `PF 60`, `PE 90`)
  e desenhe o segundo.
- **3.5** ⭐⭐⭐ Desenhe uma **escadinha de 5 degraus** usando um único
  `REPITA` (cada degrau: sobe 20, vira para a direita, anda 20, vira
  para a esquerda).

### 🚀 Desafio extra

Por que `REPITA 4 [ PF 100 PD 90 ]` fecha o quadrado, mas
`REPITA 3 [ PF 100 PD 90 ]` não? Quantas repetições fariam a tartaruga
voltar ao ponto de partida **olhando para o mesmo lado**?

<details>
<summary>Ver respostas</summary>

**3.1**

```logo
REPITA 4 [ PF 80 PD 90 ]
```

**3.2**

```logo
REPITA 3 [ PF 100 PD 120 ]
```

**3.3**

```logo
REPITA 2 [ PF 150 PD 90 PF 50 PD 90 ]
```

**3.4**

```logo
REPITA 4 [ PF 60 PD 90 ]
PD 90
PF 60
PE 90
REPITA 4 [ PF 60 PD 90 ]
```

**3.5**

```logo
REPITA 5 [ PF 20 PD 90 PF 20 PE 90 ]
```

**Desafio:** com 3 repetições ela só gira 270°, faltando 90° para a
volta completa. Com 4 (4 × 90 = 360) ela fecha. Qualquer múltiplo de 4
também fecha (8, 12...).

</details>

---

## Aula 4 - Polígonos: a regra dos 360 graus

### 🔥 Aquecimento (3 min)

Desenhe um quadrado e um triângulo com `REPITA`. Qual foi o giro de cada
um? (90° e 120°.) Multiplique o giro pelo número de lados. O que deu?

### 💡 Ideia nova (5 min)

Nos dois casos deu **360**. Isso vale para **qualquer polígono regular**
(lados e ângulos todos iguais): o giro em cada canto é

```
giro = 360 / numero_de_lados
```

| Lados | Polígono | Giro | Ângulo de dentro (180 − giro) |
|-------|----------|------|-------------------------------|
| 3  | triângulo | 120° | 60°  |
| 4  | quadrado  | 90°  | 90°  |
| 5  | pentágono | 72°  | 108° |
| 6  | hexágono  | 60°  | 120° |
| 8  | octógono  | 45°  | 135° |
| 10 | decágono  | 36°  | 144° |
| 12 | dodecágono | 30° | 150° |

Você pode até deixar o Logo fazer a conta: `PD 360 / 5` gira 72.

### 🛠️ Mão na massa (7 min)

Veja três polígonos desenhados de uma vez (é o exemplo
[`exemplos/basico/02_poligonos_diretos.logo`](exemplos/basico/02_poligonos_diretos.logo)).
Agora faça o seu, o pentágono:

<!-- exemplo: basico/08_pentagono.logo -->
```logo
; 5 lados, giro de 360 / 5 = 72 graus
REPITA 5 [ PF 80 PD 360 / 5 ]
```

*(Este programa está pronto em [`exemplos/basico/08_pentagono.logo`](exemplos/basico/08_pentagono.logo).)*

### 🎯 Exercícios (5 min)

- **4.1** ⭐ Desenhe um hexágono de lado 60.
- **4.2** ⭐ Desenhe um octógono de lado 50. Qual é o giro?
- **4.3** ⭐⭐ Desenhe um decágono (10 lados) de lado 40, deixando o
  Logo calcular o giro (`PD 360 / 10`).
- **4.4** ⭐⭐ Desenhe um polígono de **20 lados** de lado 20. Qual o
  giro? Ele se parece com o quê?
- **4.5** ⭐⭐⭐ Complete a tabela de cabeça: qual o giro de um polígono
  de 9 lados? E de 15? E de 18? E de 36? (Depois confira desenhando.)

### 🚀 Desafio extra

Teste `REPITA 4 [ PF 100 PD 91 ]`. Por que o desenho não fecha? Quantos
graus faltam (ou sobram) depois de 4 giros?

<details>
<summary>Ver respostas</summary>

**4.1**

```logo
REPITA 6 [ PF 60 PD 60 ]
```

**4.2** O giro é 360 / 8 = 45°.

```logo
REPITA 8 [ PF 50 PD 45 ]
```

**4.3**

```logo
REPITA 10 [ PF 40 PD 360 / 10 ]
```

**4.4** Giro de 360 / 20 = 18°. Fica quase um círculo.

```logo
REPITA 20 [ PF 20 PD 18 ]
```

**4.5** 9 lados: 360 / 9 = 40°. 15 lados: 24°. 18 lados: 20°. 36 lados:
10°.

```logo
REPITA 9 [ PF 40 PD 40 ]
REPITA 15 [ PF 30 PD 24 ]
```

**Desafio:** 4 × 91 = 364°, passou 4° da volta. Na próxima volta o
desenho se desloca um pouquinho e nunca fecha de verdade.

</details>

---

## Aula 5 - Caneta, cor e espessura

### 🔥 Aquecimento (3 min)

Qual é o giro de um hexágono? E de um octógono? Desenhe os dois. (60° e
45°.)

### 💡 Ideia nova (5 min)

Hora de dar vida aos desenhos:

```
COR "azul          ; muda a cor do traço
ESPESSURA 4        ; grossura do traço
LP                 ; levanta a caneta: anda sem desenhar
AP                 ; abaixa a caneta: volta a desenhar
```

Cores disponíveis: `preto`, `branco`, `vermelho`, `verde`, `azul`,
`amarelo`, `laranja`, `roxo`, `rosa`, `cinza`, `marrom`, `ciano`,
`magenta`, `dourado`, `prata`. Você também pode misturar a sua, com três
números de 0 a 255 (quanto de vermelho, verde e azul): `COR 255 128 0`
é laranja. Veja
[`exemplos/basico/04_cores.logo`](exemplos/basico/04_cores.logo).

**Velocidade:** no computador, `VELOCIDADE n` vai de 1 (devagar) a 10
(rápido), e `0` é instantâneo. Na versão web, use o controle 🐢—🐇 do
topo da página.

### 🛠️ Mão na massa (7 min)

Uma linha tracejada, alternando "desenha" e "pula":

<!-- exemplo: basico/09_tracejado.logo -->
```logo
COR "vermelho
ESPESSURA 3
REPITA 12 [ PF 10 LP PF 10 AP ]
```

*(Este programa está pronto em [`exemplos/basico/09_tracejado.logo`](exemplos/basico/09_tracejado.logo).)*

### 🎯 Exercícios (5 min)

- **5.1** ⭐ Desenhe um quadrado vermelho com espessura 4.
- **5.2** ⭐ Desenhe um triângulo com cada lado de uma cor diferente
  (vermelho, azul e verde).
- **5.3** ⭐⭐ Desenhe um quadrado azul, depois **levante a caneta**,
  vá 100 passos para a direita e desenhe um quadrado vermelho.
- **5.4** ⭐⭐ Desenhe um quadrado cujos lados são tracejados (cada lado
  de 60 feito com 3 traços e 3 pulos de 10).
- **5.5** ⭐⭐⭐ Desenhe um **semáforo**: três quadrados de lado 50
  empilhados (vermelho embaixo, amarelo no meio, verde em cima), com um
  espacinho entre eles.

### 🚀 Desafio extra

Misture cores com `COR r g b` e desenhe um quadrado "laranja queimado".
Qual combinação você usou?

<details>
<summary>Ver respostas</summary>

**5.1**

```logo
COR "vermelho
ESPESSURA 4
REPITA 4 [ PF 80 PD 90 ]
```

**5.2**

```logo
COR "vermelho
PF 100
PD 120
COR "azul
PF 100
PD 120
COR "verde
PF 100
PD 120
```

**5.3**

```logo
COR "azul
REPITA 4 [ PF 50 PD 90 ]
LP
PD 90
PF 100
PE 90
AP
COR "vermelho
REPITA 4 [ PF 50 PD 90 ]
```

**5.4**

```logo
REPITA 4 [ REPITA 3 [ PF 10 LP PF 10 AP ] PD 90 ]
```

**5.5**

```logo
COR "vermelho
REPITA 4 [ PF 50 PD 90 ]
LP
PF 60
AP
COR "amarelo
REPITA 4 [ PF 50 PD 90 ]
LP
PF 60
AP
COR "verde
REPITA 4 [ PF 50 PD 90 ]
```

**Desafio:** por exemplo `COR 200 80 0`.

```logo
COR 200 80 0
REPITA 4 [ PF 80 PD 90 ]
```

</details>

---

## Aula 6 - Laço dentro de laço: flores e rosáceas

### 🔥 Aquecimento (3 min)

Quanto dá `36 × 10`? E `12 × 30`? E `18 × 20`? (Todas dão 360 — guarde
isso na cabeça.)

### 💡 Ideia nova (5 min)

Dá para colocar um `REPITA` **dentro** de outro. O de dentro desenha
uma figura; o de fora **gira um pouquinho** e repete a figura:

```
REPITA 36 [
  REPITA 4 [ PF 80 PD 90 ]   ; um quadrado
  PD 10                       ; gira um pouquinho
]
```

São 36 quadrados, cada um girado 10° em relação ao anterior. Como
`36 × 10 = 360`, no final o desenho dá uma volta completa e fecha
lindamente — uma **rosácea**.

### 🛠️ Mão na massa (7 min)

<!-- exemplo: basico/10_rosacea_de_quadrados.logo -->
```logo
COR "roxo
REPITA 36 [
  REPITA 4 [ PF 80 PD 90 ]
  PD 10
]
```

*(Este programa está pronto em [`exemplos/basico/10_rosacea_de_quadrados.logo`](exemplos/basico/10_rosacea_de_quadrados.logo).)*

Tente trocar o quadrado por um triângulo (`REPITA 3 [ PF 80 PD 120 ]`).
O que acontece?

### 🎯 Exercícios (5 min)

- **6.1** ⭐ Faça uma rosácea de **triângulos**: 12 triângulos de lado
  70, girando 30° entre eles.
- **6.2** ⭐ Faça uma rosácea de **quadrados** com só 18 quadrados.
  Qual deve ser o giro entre eles?
- **6.3** ⭐⭐ Faça uma rosácea de **hexágonos** com 10 hexágonos de lado
  40. Qual o giro entre eles?
- **6.4** ⭐⭐ Dê **uma cor** ao desenho e aumente a espessura para 2.
- **6.5** ⭐⭐⭐ Detetive: este código deveria fechar, mas não fecha. Por
  quê? Como consertar?
  `REPITA 10 [ REPITA 4 [ PF 60 PD 90 ] PD 10 ]`

### 🚀 Desafio extra

Descubra três pares `(quantidade, giro)` diferentes que funcionam além
de `(36, 10)`. Qual é a regra?

<details>
<summary>Ver respostas</summary>

**6.1**

```logo
REPITA 12 [ REPITA 3 [ PF 70 PD 120 ] PD 30 ]
```

**6.2** Giro de 360 / 18 = 20°.

```logo
REPITA 18 [ REPITA 4 [ PF 80 PD 90 ] PD 20 ]
```

**6.3** Giro de 360 / 10 = 36°.

```logo
REPITA 10 [ REPITA 6 [ PF 40 PD 60 ] PD 36 ]
```

**6.4**

```logo
COR "azul
ESPESSURA 2
REPITA 18 [ REPITA 4 [ PF 80 PD 90 ] PD 20 ]
```

**6.5** `10 × 10 = 100`, que não é 360, então o desenho não dá a volta
completa. Para consertar, o giro deve ser `360 / 10 = 36`:

```logo
REPITA 10 [ REPITA 4 [ PF 60 PD 90 ] PD 36 ]
```

**Desafio:** (12, 30), (18, 20), (20, 18), (24, 15), (30, 12), (45, 8),
(60, 6)... A regra: `quantidade × giro = 360`.

</details>

---

## Aula 7 - REPCOUNT: contando as voltas

### 🔥 Aquecimento (3 min)

Desenhe a rosácea da aula anterior. Ela é **sempre igual** a cada volta
do laço de fora. E se cada volta fosse diferente da anterior?

### 💡 Ideia nova (5 min)

Dentro de um `REPITA`, a palavra `REPCOUNT` vale o **número da volta
atual**: 1 na primeira, 2 na segunda, 3 na terceira...

```
REPITA 40 [ PF REPCOUNT * 5 PD 90 ]
```

A cada volta o lado cresce (5, 10, 15, 20...) — e o resultado é uma
**espiral**! Veja
[`exemplos/basico/03_espiral.logo`](exemplos/basico/03_espiral.logo).

**Ideia de programação:** `REPCOUNT` é a sua primeira "variável de
graça": um valor que muda sozinho a cada volta.

**Ideia de matemática:** os lados 5, 10, 15, 20... formam uma
**sequência** (uma lista de números com uma regra: "soma 5").

### 🛠️ Mão na massa (7 min)

<!-- exemplo: basico/11_espiral_quadrada.logo -->
```logo
COR "azul
REPITA 40 [ PF REPCOUNT * 5 PD 90 ]
```

*(Este programa está pronto em [`exemplos/basico/11_espiral_quadrada.logo`](exemplos/basico/11_espiral_quadrada.logo).)*

Troque `PD 90` por `PD 91`, `PD 89` e `PD 120`. O que muda no desenho?

### 🎯 Exercícios (5 min)

- **7.1** ⭐ Desenhe uma espiral quadrada com 30 voltas, em que o lado
  cresce de 8 em 8.
- **7.2** ⭐ Desenhe uma espiral **triangular**: giro de 120°, 40
  voltas, lado crescendo de 4 em 4.
- **7.3** ⭐⭐ Desenhe um **sol** de raios crescentes: 12 raios, cada um
  com comprimento `REPCOUNT * 8` (a tartaruga anda e volta pelo mesmo
  caminho), girando 30° entre eles.
- **7.4** ⭐⭐ Faça uma espiral que cresce **mais devagar**: lado
  `REPCOUNT * 2`, giro de 91°, 100 voltas.
- **7.5** ⭐⭐⭐ Desenhe uma **estrela-espiral**: 100 voltas, lado
  `REPCOUNT * 3`, giro de 144°. Depois tente 150°.

### 🚀 Desafio extra

Uma espiral "mágica": `REPITA 150 [ PF REPCOUNT * 2 PD 59 ]`. Troque o
59 por 60, 61, 119, 121 e anote o que cada giro desenha.

<details>
<summary>Ver respostas</summary>

**7.1**

```logo
REPITA 30 [ PF REPCOUNT * 8 PD 90 ]
```

**7.2**

```logo
REPITA 40 [ PF REPCOUNT * 4 PD 120 ]
```

**7.3**

```logo
REPITA 12 [ PF REPCOUNT * 8 PT REPCOUNT * 8 PD 30 ]
```

**7.4**

```logo
REPITA 100 [ PF REPCOUNT * 2 PD 91 ]
```

**7.5**

```logo
REPITA 100 [ PF REPCOUNT * 3 PD 144 ]
```

Com 150° o desenho muda de "estrela" para uma figura mais aberta.

**Desafio:**

```logo
REPITA 150 [ PF REPCOUNT * 2 PD 59 ]
```

</details>

---

## Aula 8 - Matemática com a tartaruga: MOSTRE e a tabuada

### 🔥 Aquecimento (3 min)

Sem calculadora: quanto é `7 × 3`? E `7 × 6`? Vamos fazer o computador
contar para nós.

### 💡 Ideia nova (5 min)

O comando `MOSTRE` **escreve** na tela (no painel de texto):

```
MOSTRE 7 * 3        ; escreve 21
MOSTRE "oi          ; escreve oi
MOSTRE [ola mundo]  ; escreve ola mundo
```

Juntando `MOSTRE` com `REPCOUNT`, o Logo escreve uma tabuada inteira:

```
REPITA 10 [ MOSTRE REPCOUNT * 7 ]
```

**Ideia de matemática:** `REPCOUNT * 7` dá 7, 14, 21, ... : os
**múltiplos de 7**. A tabuada é uma sequência em que se soma 7 a cada
passo.

### 🛠️ Mão na massa (7 min)

Dá para **ver** a tabuada crescendo, desenhando uma barra para cada
resultado (altura `REPCOUNT * 4 * 5`, onde o `5` só serve para "esticar"
o desenho):

<!-- exemplo: basico/12_tabuada_barras.logo -->
```logo
; tabuada do 4, escrita e desenhada
COR "verde
REPITA 10 [
  MOSTRE REPCOUNT * 4
  PF REPCOUNT * 4 * 5
  PT REPCOUNT * 4 * 5
  PD 90
  PF 20
  PE 90
]
```

*(Este programa está pronto em [`exemplos/basico/12_tabuada_barras.logo`](exemplos/basico/12_tabuada_barras.logo).)*

Qual barra é a maior? Qual a diferença de altura entre uma barra e a
próxima? (Sempre a mesma — a "razão" da sequência.)

### 🎯 Exercícios (5 min)

- **8.1** ⭐ Escreva a tabuada do 5 com `MOSTRE` e `REPITA`.
- **8.2** ⭐ Escreva a tabuada do 9. Que padrão você vê nos números
  (some os dois algarismos de cada resultado)?
- **8.3** ⭐⭐ Escreva os **quadrados perfeitos**: 1, 4, 9, 16...
  (`REPCOUNT * REPCOUNT`).
- **8.4** ⭐⭐ Escreva os **números ímpares**: 1, 3, 5, 7...
  (`REPCOUNT * 2 - 1`).
- **8.5** ⭐⭐⭐ Desenhe barras para os quadrados perfeitos de 1 a 8, com
  altura `REPCOUNT * REPCOUNT * 4`. Como a diferença entre barras vizinhas
  muda?

### 🚀 Desafio extra

Compare os ímpares (8.4) com a **diferença** entre quadrados vizinhos
(4 − 1, 9 − 4, 16 − 9...). Que relação você descobre?

<details>
<summary>Ver respostas</summary>

**8.1**

```logo
REPITA 10 [ MOSTRE REPCOUNT * 5 ]
```

**8.2** 9, 18, 27, 36, 45...: 1+8 = 9, 2+7 = 9, 3+6 = 9... Sempre 9!

```logo
REPITA 10 [ MOSTRE REPCOUNT * 9 ]
```

**8.3**

```logo
REPITA 10 [ MOSTRE REPCOUNT * REPCOUNT ]
```

**8.4**

```logo
REPITA 10 [ MOSTRE REPCOUNT * 2 - 1 ]
```

**8.5**

```logo
COR "azul
REPITA 8 [
  MOSTRE REPCOUNT * REPCOUNT
  PF REPCOUNT * REPCOUNT * 4
  PT REPCOUNT * REPCOUNT * 4
  PD 90
  PF 20
  PE 90
]
```

As diferenças entre barras vizinhas **crescem** (3, 5, 7, 9...), ao
contrário da tabuada, onde eram sempre iguais.

**Desafio:** a diferença entre dois quadrados vizinhos é sempre um
número ímpar: 4 − 1 = 3, 9 − 4 = 5, 16 − 9 = 7...

</details>

---

## Aula 9 - O mapa da tartaruga: coordenadas

### 🔥 Aquecimento (3 min)

Se você quisesse explicar a um amigo onde está um tesouro no pátio da
escola, que informações daria? (Um "mapa" precisa de pontos de
referência e de distâncias.)

### 💡 Ideia nova (5 min)

A tela é um **plano cartesiano**. O centro é o ponto `(0, 0)`:

- o primeiro número (**x**) diz quanto andar para a direita (positivo)
  ou esquerda (negativo);
- o segundo (**y**) diz quanto subir (positivo) ou descer (negativo).

```
VAIPARA 100 50      ; vai para x = 100, y = 50 (desenha a linha até lá)
LP                  ; com a caneta levantada, ele pula sem desenhar
DEFINARUMO 0        ; aponta para cima (0 = cima, 90 = direita, 180 = baixo)
```

### 🛠️ Mão na massa (7 min)

Desenhe os **eixos** (as duas linhas que se cruzam no centro) e o
quadrado de lado 100 no primeiro quadrante:

<!-- exemplo: basico/13_eixos_e_quadrado.logo -->
```logo
; eixos
COR "cinza
LP
VAIPARA -200 0
AP
VAIPARA 200 0
LP
VAIPARA 0 -150
AP
VAIPARA 0 150
; quadrado ligando pontos
COR "azul
LP
VAIPARA 0 0
AP
VAIPARA 100 0
VAIPARA 100 100
VAIPARA 0 100
VAIPARA 0 0
```

*(Este programa está pronto em [`exemplos/basico/13_eixos_e_quadrado.logo`](exemplos/basico/13_eixos_e_quadrado.logo).)*

Repare como cada `VAIPARA` liga o ponto anterior ao próximo: é o jogo de
**ligar os pontos**.

### 🎯 Exercícios (5 min)

- **9.1** ⭐ Desenhe uma linha da origem `(0, 0)` até `(100, 100)`. Que
  ângulo ela faz com o eixo horizontal?
- **9.2** ⭐ Desenhe um quadrado de lado 80 ligando os pontos
  `(0,0)`, `(80,0)`, `(80,80)`, `(0,80)`.
- **9.3** ⭐⭐ Desenhe um **triângulo** com vértices `(-50, 0)`,
  `(50, 0)` e `(0, 87)`. (Levante a caneta para ir ao primeiro ponto.)
- **9.4** ⭐⭐ Desenhe o contorno de uma **casa** ligando
  `(0,0)`, `(100,0)`, `(100,80)`, `(50,130)`, `(0,80)` e de volta a `(0,0)`.
- **9.5** ⭐⭐⭐ Desenhe uma **estrela de 5 pontas** ligando, nesta ordem,
  `(0,100)`, `(59,-81)`, `(-95,31)`, `(95,31)`, `(-59,-81)` e de volta
  a `(0,100)`.

### 🚀 Desafio extra

Desenhe numa folha quadriculada uma figura sua (um barco, um peixe) com
pontos de coordenadas inteiras; depois escreva a lista de `VAIPARA` que
a reproduz no Logo.

<details>
<summary>Ver respostas</summary>

**9.1** A linha faz 45° (x e y crescem igual).

```logo
VAIPARA 100 100
```

**9.2**

```logo
VAIPARA 80 0
VAIPARA 80 80
VAIPARA 0 80
VAIPARA 0 0
```

**9.3**

```logo
LP
VAIPARA -50 0
AP
VAIPARA 50 0
VAIPARA 0 87
VAIPARA -50 0
```

**9.4**

```logo
VAIPARA 100 0
VAIPARA 100 80
VAIPARA 50 130
VAIPARA 0 80
VAIPARA 0 0
```

**9.5**

```logo
LP
VAIPARA 0 100
AP
VAIPARA 59 -81
VAIPARA -95 31
VAIPARA 95 31
VAIPARA -59 -81
VAIPARA 0 100
```

</details>

---

## Aula 10 - Projeto final: o meu desenho

### 🔥 Aquecimento (3 min)

Revisão-relâmpago, sem computador:

1. Qual o giro de um pentágono regular? (72°)
2. O que `REPCOUNT` vale na terceira volta de um `REPITA`? (3)
3. Para que serve `LP`? (levanta a caneta, para andar sem desenhar)
4. Qual é o ponto `(0, 0)`? (o centro da tela)

### 💡 Ideia nova (5 min)

Todo desenho complicado é uma **colagem de formas simples**. O truque
dos programadores é **planejar antes de digitar**:

1. **Esboce** no papel.
2. **Quebre** o desenho em formas (quadrados, triângulos, círculos).
3. **Escreva** uma forma por vez e **teste** cada uma antes da próxima.
4. **Pinte** no final.

### 🛠️ Mão na massa (7 min)

Uma casa com sol, montada em peças. O sol é um polígono de 36 lados
(quase um círculo):

<!-- exemplo: basico/14_casa_e_sol.logo -->
```logo
; paredes
COR "marrom
ESPESSURA 3
REPITA 4 [ PF 100 PD 90 ]
; telhado (um triangulo em cima do quadrado)
LP
PF 100
PD 90
AP
PE 60
COR "vermelho
PF 100
PD 120
PF 100
; porta
COR "azul
LP
VAIPARA 35 0
DEFINARUMO 0
AP
REPITA 2 [ PF 50 PD 90 PF 30 PD 90 ]
; sol
COR "dourado
LP
VAIPARA 170 170
DEFINARUMO 0
AP
REPITA 36 [ PF 5 PD 10 ]
```

*(Este programa está pronto em [`exemplos/basico/14_casa_e_sol.logo`](exemplos/basico/14_casa_e_sol.logo).)*

### 🎯 Exercícios (5 min)

**Projeto:** escolha **um** e faça (use uma folha de rascunho!):

- **10.1** ⭐ Um **barco** (casco = trapézio ou semicírculo, vela =
  triângulo).
- **10.2** ⭐⭐ Um **foguete** (corpo = retângulo, bico = triângulo,
  duas aletas, uma janela redonda).
- **10.3** ⭐⭐⭐ Uma **cidade**: três prédios de alturas diferentes
  (retângulos), com janelas (quadradinhos) e um sol.

**Checklist de autoavaliação:** ✅ usei pelo menos um `REPITA`, ✅ usei
cores, ✅ levantei a caneta (`LP`) para mudar de lugar, ✅ o desenho
fecha direitinho, ✅ expliquei a um adulto como ele foi montado.

### 🚀 Desafio extra

Adicione uma **rosácea** (Aula 6) ao seu desenho como se fosse uma flor
ou uma estrela no céu.

<details>
<summary>Ver uma resposta para o barco (10.1)</summary>

```logo
; casco (mais largo em cima)
COR "marrom
PD 90
PF 100
PE 60
PF 40
PE 120
PF 140
PE 120
PF 40
PE 60
; mastro
COR "preto
LP
VAIPARA 50 35
AP
VAIPARA 50 135
; vela
COR "azul
VAIPARA 105 55
VAIPARA 50 55
```
(Há muitas respostas certas: o importante é que o seu desenho tenha as
partes planejadas e testadas.)

</details>

---

## O que você aprendeu

- Mover e girar a tartaruga (`PF`, `PT`, `PD`, `PE`) e que um programa é
  uma sequência de passos.
- Medir ângulos (90°, 180°, 360°) e a regra do giro de um polígono
  regular: `360 / numero_de_lados`.
- Repetir com `REPITA` (inclusive um dentro do outro) e contar voltas
  com `REPCOUNT`.
- Cores, espessura e caneta (`COR`, `ESPESSURA`, `LP`, `AP`).
- Escrever números com `MOSTRE`, e descobrir sequências (tabuada,
  quadrados, ímpares).
- Usar coordenadas (`VAIPARA`, `DEFINARUMO`) e planejar um desenho em
  partes.

## Pronto para a próxima trilha?

Na [Trilha 2 - Intermediário](trilha-2-intermediario.md) você vai
**criar seus próprios comandos** (procedimentos), guardar valores em
variáveis, tomar decisões com `SE`, e usar um laço (`PARACADA`) que
conta com uma variável de verdade.
