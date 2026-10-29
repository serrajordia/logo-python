# Trilha 3 - Avançado

**O que você vai aprender:** funções que devolvem valores (`DEVOLVA`), o
Teorema de Pitágoras, círculos e o número π, o laço `ENQUANTO`,
`QUEBRA`/`CONTINUA`, recursão (procedimentos que chamam a si mesmos) e
fractais.

**Formato:** 10 aulas de **20 minutos** cada, com dificuldade crescente.
Pré-requisito: a [Trilha 2 - Intermediário](trilha-2-intermediario.md).

## Como funciona cada aula

| Tempo | Etapa | O que fazer |
|-------|-------|-------------|
| 3 min | 🔥 **Aquecimento** | rever a aula anterior com uma pergunta rápida |
| 5 min | 💡 **Ideia nova** | ler a explicação e testar os exemplos |
| 7 min | 🛠️ **Mão na massa** | fazer o programa principal da aula |
| 5 min | 🎯 **Exercícios** | resolver os exercícios (⭐ fácil, ⭐⭐ médio, ⭐⭐⭐ difícil) |

Cada aula tem ainda um **🚀 Desafio extra** opcional (fora dos 20
minutos) e as **respostas** escondidas no fim: tente primeiro, espie
depois! Se um exercício não couber nos 5 minutos, deixe-o para o começo da
próxima aula.

> **Dicas:** (1) alguns desenhos desta trilha têm milhares de traços. Na
> versão web, deixe o controle de velocidade em **∞** (ou clique em
> **⏩ Pular**) para vê-los prontos; no computador, use `RAPIDO` no
> início e `NORMAL` no fim. (2) Tudo que vem depois de `;` é comentário.

---

## Aula 1 - Funções: procedimentos que devolvem um valor

### 🔥 Aquecimento (3 min)

Na Trilha 2, seus procedimentos **faziam** coisas: desenhavam, escreviam.
Uma calculadora, ao contrário, **responde**: você pergunta `7 × 8` e ela
devolve 56. Como o Logo poderia ter comandos que devolvem respostas?

### 💡 Ideia nova (5 min)

Uma **função** é um procedimento que **devolve** um valor com `DEVOLVA`.
Esse valor pode ser usado em qualquer conta, como se fosse um número:

```
PARA DOBRO :X
  DEVOLVA :X * 2
FIM

MOSTRE DOBRO 21        ; escreve 42
PF DOBRO 10            ; anda 20 passos
```

**Ideia de programação:** `DEVOLVA` encerra a função na hora e "entrega"
o resultado a quem a chamou. Uma função não precisa desenhar nada.

**Ideia de matemática:** é exatamente a ideia de **função** da
matemática: `f(x) = 2x` recebe um `x` e devolve um único resultado.

### 🛠️ Mão na massa (7 min)

<!-- exemplo: avancado/10_funcoes_matematicas.logo -->
```logo
PARA DOBRO :X
  DEVOLVA :X * 2
FIM

PARA MEDIA :A :B
  DEVOLVA (:A + :B) / 2
FIM

PARA AREA_RETANGULO :BASE :ALTURA
  DEVOLVA :BASE * :ALTURA
FIM

MOSTRE DOBRO 21
MOSTRE MEDIA 8 13
MOSTRE AREA_RETANGULO 12 5

; usando funcoes dentro de comandos de desenho
PF DOBRO 40
PD 90
PF MEDIA 60 100
```

*(Este programa está pronto em [`exemplos/avancado/10_funcoes_matematicas.logo`](exemplos/avancado/10_funcoes_matematicas.logo).)*

### 🎯 Exercícios (5 min)

- **1.1** ⭐ Escreva `TRIPLO :X` e mostre o triplo de 14.
- **1.2** ⭐ Escreva `PERIMETRO_RETANGULO :BASE :ALTURA` e teste com
  12 e 5.
- **1.3** ⭐⭐ Escreva `CELSIUS :F`, que converte graus Fahrenheit em
  Celsius: `(F − 32) × 5 / 9`. Teste com 32, 50, 86 e 212.
- **1.4** ⭐⭐ Escreva `MAIOR :A :B` que **devolve** (e não só escreve) o
  maior número. Depois use-a para desenhar um quadrado cujo lado é
  `MAIOR 40 70`.
- **1.5** ⭐⭐⭐ Escreva `LADO_PARA :N`, que devolve `360 / :N`. Desenhe os
  polígonos de 3 a 8 lados com lado `LADO_PARA :n` (todos com perímetro
  360). O que acontece com os polígonos conforme `n` cresce?

### 🚀 Desafio extra

Escreva `MEDIA3 :A :B :C` e use-a para escrever a média das suas três
últimas notas.

<details>
<summary>Ver respostas</summary>

**1.1**

```logo
PARA TRIPLO :X
  DEVOLVA :X * 3
FIM
MOSTRE TRIPLO 14
```

**1.2** Resposta: 34.

```logo
PARA PERIMETRO_RETANGULO :BASE :ALTURA
  DEVOLVA 2 * (:BASE + :ALTURA)
FIM
MOSTRE PERIMETRO_RETANGULO 12 5
```

**1.3** Resultados: 0, 10, 30 e 100.

```logo
PARA CELSIUS :F
  DEVOLVA (:F - 32) * 5 / 9
FIM
MOSTRE CELSIUS 32
MOSTRE CELSIUS 50
MOSTRE CELSIUS 86
MOSTRE CELSIUS 212
```

**1.4**

```logo
PARA MAIOR :A :B
  SE :A > :B [ DEVOLVA :A ]
  DEVOLVA :B
FIM
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
MOSTRE MAIOR 40 70
QUADRADO MAIOR 40 70
```

**1.5** Conforme `n` cresce, o polígono se aproxima de um círculo (que
tem o mesmo perímetro de 360).

```logo
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [ PF :TAMANHO PD 360 / :LADOS ]
FIM
PARA LADO_PARA :N
  DEVOLVA 360 / :N
FIM
PARACADA :n DE 3 ATE 8 [ POLIGONO :n LADO_PARA :n ]
```

**Desafio:**

```logo
PARA MEDIA3 :A :B :C
  DEVOLVA (:A + :B + :C) / 3
FIM
MOSTRE MEDIA3 7 8 9
```

</details>

---

## Aula 2 - Pitágoras: a função da distância

### 🔥 Aquecimento (3 min)

Quanto mede a diagonal de um quadrado de lado 10? (Menos de 20, mais de
10... mas quanto?) Hoje vamos descobrir uma fórmula para isso.

### 💡 Ideia nova (5 min)

Num triângulo **retângulo** (com um ângulo de 90°), o lado maior
(**hipotenusa**, `c`) e os menores (**catetos**, `a` e `b`) se
relacionam assim:

```
a * a + b * b = c * c        ; Teorema de Pitagoras
c = RAIZ (a * a + b * b)
```

O clássico triângulo **3-4-5**: `9 + 16 = 25`, e `RAIZ 25 = 5`. Com ele
dá para escrever uma função que mede a **distância entre dois pontos**
`(x1, y1)` e `(x2, y2)`:

```
PARA DISTANCIA :X1 :Y1 :X2 :Y2
  DEVOLVA RAIZ ((:X2 - :X1) * (:X2 - :X1) + (:Y2 - :Y1) * (:Y2 - :Y1))
FIM
```

> **Dica de sintaxe:** repare nos parênteses depois de `RAIZ`: sem eles,
> o Logo calcularia a raiz só do primeiro número.

Veja também
[`exemplos/avancado/04_pitagoras.logo`](exemplos/avancado/04_pitagoras.logo).

### 🛠️ Mão na massa (7 min)

Desenhe um triângulo 3-4-5 ampliado 30 vezes, e confira o teorema:

<!-- exemplo: avancado/11_hipotenusa.logo -->
```logo
PARA HIPOTENUSA :A :B
  DEVOLVA RAIZ (:A * :A + :B * :B)
FIM

FACA "a 90
FACA "b 120
MOSTRE :a * :a + :b * :b                         ; soma dos quadrados dos catetos
MOSTRE HIPOTENUSA :a :b                           ; a hipotenusa: 150
MOSTRE (HIPOTENUSA :a :b) * (HIPOTENUSA :a :b)    ; o quadrado dela: igual a soma!

; desenho: catetos nos eixos, hipotenusa fechando o triangulo
VAIPARA :a 0
VAIPARA :a :b
VAIPARA 0 0
```

*(Este programa está pronto em [`exemplos/avancado/11_hipotenusa.logo`](exemplos/avancado/11_hipotenusa.logo).)*

As duas contas (`90² + 120²` e `150²`) dão `22500`: é o teorema
funcionando.

### 🎯 Exercícios (5 min)

- **2.1** ⭐ Use `HIPOTENUSA` para as medidas `(3, 4)`, `(5, 12)` e
  `(8, 15)`. Que trios de números inteiros você achou?
- **2.2** ⭐ Calcule a distância de `(0, 0)` a `(80, 60)` com `DISTANCIA`.
- **2.3** ⭐⭐ Escreva `DIAGONAL :LADO`, que devolve a diagonal do
  quadrado (`:LADO * RAIZ 2`), e desenhe um quadrado de lado 100 com a
  diagonal.
- **2.4** ⭐⭐ Escreva `E_RETANGULO :A :B :C`, que diz se um triângulo
  de lados `a`, `b` e `c` (com `c` o maior) é retângulo. Teste `3 4 5`,
  `5 12 13` e `4 5 6`.
- **2.5** ⭐⭐⭐ Escreva `PERIMETRO :X1 :Y1 :X2 :Y2 :X3 :Y3`, que devolve
  o perímetro do triângulo de vértices `(x1,y1)`, `(x2,y2)`, `(x3,y3)`,
  usando `DISTANCIA` três vezes. Teste com `(0,0)`, `(6,0)`, `(0,8)`.

### 🚀 Desafio extra

Um triângulo de lados 5, 5 e 8 tem altura 3. Desenhe-o (use `VAIPARA`) e
confirme a altura usando `DISTANCIA` entre o topo e o meio da base.

<details>
<summary>Ver respostas</summary>

**2.1** `(3,4)` → 5; `(5,12)` → 13; `(8,15)` → 17. São os **trios
pitagóricos**.

```logo
PARA HIPOTENUSA :A :B
  DEVOLVA RAIZ (:A * :A + :B * :B)
FIM
MOSTRE HIPOTENUSA 3 4
MOSTRE HIPOTENUSA 5 12
MOSTRE HIPOTENUSA 8 15
```

**2.2** Resposta: 100.

```logo
PARA DISTANCIA :X1 :Y1 :X2 :Y2
  DEVOLVA RAIZ ((:X2 - :X1) * (:X2 - :X1) + (:Y2 - :Y1) * (:Y2 - :Y1))
FIM
MOSTRE DISTANCIA 0 0 80 60
```

**2.3**

```logo
PARA DIAGONAL :LADO
  DEVOLVA :LADO * RAIZ 2
FIM
REPITA 4 [ PF 100 PD 90 ]
PD 45
PF DIAGONAL 100
```

(Resultado: 141,42... — um número com **infinitas casas decimais**, que
não é fração. É um *irracional*.)

**2.4**

```logo
PARA E_RETANGULO :A :B :C
  SE (:A * :A + :B * :B) = (:C * :C) [ MOSTRE [retangulo] ] [ MOSTRE [nao e retangulo] ]
FIM
E_RETANGULO 3 4 5
E_RETANGULO 5 12 13
E_RETANGULO 4 5 6
```

**2.5** Resposta: 24 (6 + 8 + 10).

```logo
PARA DISTANCIA :X1 :Y1 :X2 :Y2
  DEVOLVA RAIZ ((:X2 - :X1) * (:X2 - :X1) + (:Y2 - :Y1) * (:Y2 - :Y1))
FIM
PARA PERIMETRO :X1 :Y1 :X2 :Y2 :X3 :Y3
  DEVOLVA (DISTANCIA :X1 :Y1 :X2 :Y2) + (DISTANCIA :X2 :Y2 :X3 :Y3) + (DISTANCIA :X3 :Y3 :X1 :Y1)
FIM
MOSTRE PERIMETRO 0 0 6 0 0 8
```

**Desafio:**

```logo
PARA DISTANCIA :X1 :Y1 :X2 :Y2
  DEVOLVA RAIZ ((:X2 - :X1) * (:X2 - :X1) + (:Y2 - :Y1) * (:Y2 - :Y1))
FIM
LP
VAIPARA -4 0
AP
VAIPARA 4 0
VAIPARA 0 3
VAIPARA -4 0
MOSTRE DISTANCIA 0 3 0 0
```

(Aqui a base fica de `(-4,0)` a `(4,0)`: medidas ampliadas só no
desenho; use `ZOOM 10` para ver melhor.)

</details>

---

## Aula 3 - Círculos e o número π

### 🔥 Aquecimento (3 min)

Quantos lados tem um círculo? (Quase ninguém responde "infinitos" de
primeira.) Na Trilha 1 você desenhou um polígono de 36 lados que parecia
um círculo. E com 360 lados?

### 💡 Ideia nova (5 min)

Um círculo é um polígono com **muitos lados minúsculos**. Se a
circunferência mede `2 × π × raio` e a tartaruga dá 360 passos
pequenos, cada passo mede `2 × π × raio / 360` e gira 1°:

```
PARA CIRCULO :RAIO
  REPITA 360 [ PF 2 * PI * :RAIO / 360 PD 1 ]
FIM
```

`PI` é o número π ≈ 3,14159..., a razão entre a circunferência e o
diâmetro de **qualquer** círculo. Veja
[`exemplos/avancado/02_circulo_pi.logo`](exemplos/avancado/02_circulo_pi.logo).

Um **arco** é um pedaço de círculo: em vez de 360 passos, use só alguns
graus.

### 🛠️ Mão na massa (7 min)

<!-- exemplo: avancado/12_rosacea_de_circulos.logo -->
```logo
PARA CIRCULO :RAIO
  REPITA 360 [ PF 2 * PI * :RAIO / 360 PD 1 ]
FIM

COR "azul
REPITA 12 [ CIRCULO 60 PD 30 ]
```

*(Este programa está pronto em [`exemplos/avancado/12_rosacea_de_circulos.logo`](exemplos/avancado/12_rosacea_de_circulos.logo).)*

São 12 círculos girados de 30° — uma rosácea de círculos (12 × 30 = 360).

### 🎯 Exercícios (5 min)

- **3.1** ⭐ Desenhe um círculo de raio 80.
- **3.2** ⭐ Escreva a circunferência de um círculo de raio 10 e de um de
  diâmetro 1 (raio 0,5). O segundo valor é π!
- **3.3** ⭐⭐ Crie `ARCO :RAIO :GRAUS` (como o círculo, mas com `:GRAUS`
  passos) e desenhe um **semicírculo** de raio 80.
- **3.4** ⭐⭐ Desenhe 10 círculos **concêntricos** (mesmo centro),
  raios 10, 20, ..., 100. Dica: antes de cada círculo, vá para o ponto
  de baixo `(0, -raio)` com a tartaruga olhando para a esquerda
  (`DEFINARUMO 270`).
- **3.5** ⭐⭐⭐ Crie `AREA_CIRCULO :R` (devolve `π × R × R`) e compare, para
  `R = 10`, com o quadrado de fora (área `4 × R × R`) e o quadrado de
  dentro (área `2 × R × R`). A área do círculo fica entre eles?

### 🚀 Desafio extra

Desenhe uma **flor de 8 pétalas**, em que cada pétala é feita de dois
arcos de 60° (com giro de 120° entre eles).

<details>
<summary>Ver respostas</summary>

**3.1**

```logo
PARA CIRCULO :RAIO
  REPITA 360 [ PF 2 * PI * :RAIO / 360 PD 1 ]
FIM
CIRCULO 80
```

**3.2** 62,83... e 3,14159... (= π).

```logo
MOSTRE 2 * PI * 10
MOSTRE 2 * PI * 0.5
```

**3.3**

```logo
PARA ARCO :RAIO :GRAUS
  REPITA :GRAUS [ PF 2 * PI * :RAIO / 360 PD 1 ]
FIM
ARCO 80 180
```

**3.4**

```logo
PARA CIRCULO :RAIO
  REPITA 360 [ PF 2 * PI * :RAIO / 360 PD 1 ]
FIM
PARACADA :r DE 10 ATE 100 PASSO 10 [
  LP
  VAIPARA 0 (0 - :r)
  DEFINARUMO 270
  AP
  CIRCULO :r
]
```

**3.5** A área é 314,159... (entre 200 e 400).

```logo
PARA AREA_CIRCULO :R
  DEVOLVA PI * :R * :R
FIM
MOSTRE 2 * 10 * 10
MOSTRE AREA_CIRCULO 10
MOSTRE 4 * 10 * 10
```

**Desafio:**

```logo
PARA ARCO :RAIO :GRAUS
  REPITA :GRAUS [ PF 2 * PI * :RAIO / 360 PD 1 ]
FIM
COR "rosa
REPITA 8 [
  ARCO 50 60
  PD 120
  ARCO 50 60
  PD 120
  PD 45
]
```

</details>

---

## Aula 4 - ENQUANTO: repetir até que algo mude

### 🔥 Aquecimento (3 min)

Quantas vezes você precisa dobrar 1 para passar de 1000? Você sabe
responder sem contar as dobras uma a uma? (Descubra agora, e observe que
você não sabia o número de repetições de antemão.)

### 💡 Ideia nova (5 min)

`REPITA` e `PARACADA` sabem, antes de começar, quantas vezes vão rodar.
O `ENQUANTO` repete **enquanto uma condição for verdadeira**:

```
FACA "x 1
ENQUANTO :x < 1000 [
  MOSTRE :x
  FACA "x :x * 2
]
```

**Cuidado:** se a condição nunca ficar falsa, o laço roda "para sempre".
Por segurança, este Logo interrompe o `ENQUANTO` depois de 200.000 voltas
e avisa. Mas o ideal é sempre ter, dentro do bloco, algo (como o
`FACA "x :x * 2`) que caminhe para tornar a condição falsa.

### 🛠️ Mão na massa (7 min)

Hexágonos cada vez maiores, até o lado passar de 150 (veja também
[`exemplos/avancado/07_enquanto_crescente.logo`](exemplos/avancado/07_enquanto_crescente.logo)):

```logo
FACA "lado 10
ENQUANTO :lado < 150 [
  REPITA 6 [ PF :lado PD 60 ]
  FACA "lado :lado + 12
]
```

Troque o `12` por `6`. Quantos hexágonos aparecem agora? Por quê?

### 🎯 Exercícios (5 min)

- **4.1** ⭐ Escreva os números de 1 a 10 com `ENQUANTO`.
- **4.2** ⭐ Dobre `1` até passar de 1000, escrevendo cada valor. Quantos
  valores foram escritos?
- **4.3** ⭐⭐ Desenhe uma espiral quadrada em que o lado começa em 5 e
  cresce de 5 em 5, **até passar de 200**.
- **4.4** ⭐⭐ **Juros compostos:** R$ 1000 crescendo 10% ao mês. Quantos
  meses até o dinheiro dobrar (chegar a 2000 ou mais)? (Multiplique
  por `1.1` a cada mês.)
- **4.5** ⭐⭐⭐ A **sequência de Collatz**: comece com um número `n`. Se
  `n` é par, divida por 2; se é ímpar, calcule `3 × n + 1`. Repita até
  chegar a 1. Escreva todos os valores para `n = 6` e para `n = 27`
  (conte quantos passos).

### 🚀 Desafio extra

Descubra qual número `n` menor que 30 gera a sequência de Collatz mais
longa. (Dica: use um segundo laço.)

<details>
<summary>Ver respostas</summary>

**4.1**

```logo
FACA "i 1
ENQUANTO :i <= 10 [
  MOSTRE :i
  FACA "i :i + 1
]
```

**4.2** São 11 valores (1, 2, 4, ..., 1024).

```logo
FACA "x 1
ENQUANTO :x < 1000 [
  MOSTRE :x
  FACA "x :x * 2
]
MOSTRE :x
```

**4.3**

```logo
FACA "lado 5
ENQUANTO :lado <= 200 [
  PF :lado
  PD 90
  FACA "lado :lado + 5
]
```

**4.4** 8 meses (1000 × 1,1⁸ ≈ 2143,59).

```logo
FACA "dinheiro 1000
FACA "meses 0
ENQUANTO :dinheiro < 2000 [
  FACA "dinheiro :dinheiro * 1.1
  FACA "meses :meses + 1
]
MOSTRE :meses
```

**4.5** Para `n = 6`: 6, 3, 10, 5, 16, 8, 4, 2, 1 (8 passos). Para
`n = 27`: 111 passos!

```logo
FACA "n 27
FACA "passos 0
ENQUANTO :n <> 1 [
  SE (:n % 2) = 0 [ FACA "n :n / 2 ] [ FACA "n :n * 3 + 1 ]
  FACA "passos :passos + 1
]
MOSTRE :passos
```

**Desafio:** (resposta: `n = 27`, com 111 passos)

```logo
FACA "melhor 1
FACA "recorde 0
PARACADA :inicio DE 1 ATE 29 [
  FACA "n :inicio
  FACA "passos 0
  ENQUANTO :n <> 1 [
    SE (:n % 2) = 0 [ FACA "n :n / 2 ] [ FACA "n :n * 3 + 1 ]
    FACA "passos :passos + 1
  ]
  SE :passos > :recorde [
    FACA "recorde :passos
    FACA "melhor :inicio
  ]
]
MOSTRE :melhor
MOSTRE :recorde
```

</details>

---

## Aula 5 - QUEBRA e CONTINUA: controlando um laço por dentro

### 🔥 Aquecimento (3 min)

Você procura as chaves numa gaveta com 10 compartimentos. Você continua
abrindo os compartimentos que sobram depois de achar as chaves? (Claro
que não!) Em programação, sair do laço mais cedo é `QUEBRA`.

### 💡 Ideia nova (5 min)

Dentro de qualquer laço (`REPITA`, `ENQUANTO` ou `PARACADA`):

- `QUEBRA` **sai do laço** imediatamente, mesmo que ele não tenha
  terminado.
- `CONTINUA` **pula** para a próxima volta, sem rodar o resto do bloco
  naquela volta.

```
REPITA 10 [
  SE REPCOUNT > 6 [ QUEBRA ]      ; para depois do sexto lado
  PF 30
  PD 36
]
```

Veja [`exemplos/avancado/06_quebra_continua.logo`](exemplos/avancado/06_quebra_continua.logo).

### 🛠️ Mão na massa (7 min)

Uma linha tracejada, com `CONTINUA` para pular as partes pares:

```logo
REPITA 20 [
  SE (REPCOUNT % 2) = 0 [ LP PF 15 AP CONTINUA ]
  PF 15
]
```

Em cada volta par, a tartaruga anda sem desenhar e **pula** o `PF 15`
final. Nas ímpares, desenha.

### 🎯 Exercícios (5 min)

- **5.1** ⭐ Desenhe um polígono de 10 lados (lado 30, giro de 36°), mas
  pare depois do sexto lado, com `QUEBRA`.
- **5.2** ⭐ Desenhe uma linha tracejada de 30 pedaços, com `CONTINUA`.
- **5.3** ⭐⭐ Desenhe um polígono de 20 lados (lado 20, giro de 18°) sem
  desenhar os lados cujo número é múltiplo de 3 (use `LP`/`AP` e
  `CONTINUA`).
- **5.4** ⭐⭐ Encontre o **menor número maior que zero que é múltiplo de
  7 e de 11 ao mesmo tempo**, usando `PARACADA` até 100 e `QUEBRA` quando
  achar. (Qual é a resposta?)
- **5.5** ⭐⭐⭐ Escreva a função `E_PRIMO :N` (devolve 1 se `:N` é primo e
  0 se não é), testando divisores com `PARACADA` e `DEVOLVA` de dentro do
  laço. Use-a para escrever **todos os primos até 50**.

### 🚀 Desafio extra

Melhore `E_PRIMO` testando só os divisores até a raiz quadrada de `:N`.
Por que isso basta?

<details>
<summary>Ver respostas</summary>

**5.1**

```logo
REPITA 10 [
  SE REPCOUNT > 6 [ QUEBRA ]
  PF 30
  PD 36
]
```

**5.2**

```logo
REPITA 30 [
  SE (REPCOUNT % 2) = 0 [ LP PF 10 AP CONTINUA ]
  PF 10
]
```

**5.3**

```logo
REPITA 20 [
  SE (REPCOUNT % 3) = 0 [
    LP
    PF 20
    PD 18
    AP
    CONTINUA
  ]
  PF 20
  PD 18
]
```

**5.4** Resposta: 77 (os múltiplos comuns de 7 e 11 são os múltiplos de
77).

```logo
PARACADA :i DE 1 ATE 100 [
  SE (:i % 7) = 0 [
    SE (:i % 11) = 0 [
      MOSTRE :i
      QUEBRA
    ]
  ]
]
```

**5.5** Primos até 50: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
43, 47.

```logo
PARA E_PRIMO :N
  SE :N < 2 [ DEVOLVA 0 ]
  PARACADA :d DE 2 ATE :N - 1 [
    SE (:N % :d) = 0 [ DEVOLVA 0 ]
  ]
  DEVOLVA 1
FIM
PARACADA :n DE 2 ATE 50 [
  SE (E_PRIMO :n) = 1 [ MOSTRE :n ]
]
```

**Desafio:** se `n` tem um divisor maior que sua raiz quadrada, ele
também tem o "par" menor que a raiz. Então basta testar até `RAIZ n`.

```logo
PARA E_PRIMO :N
  SE :N < 2 [ DEVOLVA 0 ]
  PARACADA :d DE 2 ATE RAIZ :N [
    SE (:N % :d) = 0 [ DEVOLVA 0 ]
  ]
  DEVOLVA 1
FIM
PARACADA :n DE 2 ATE 50 [
  SE (E_PRIMO :n) = 1 [ MOSTRE :n ]
]
```

(Confira: para `n = 4` o teste vai até `RAIZ 4 = 2` e `4 % 2 = 0`, então
devolve 0, correto. Para `n = 2` e `3` o laço nem chega a rodar e
devolve 1, também correto.)

</details>

---

## Aula 6 - Recursão: um procedimento que chama a si mesmo

### 🔥 Aquecimento (3 min)

Você já viu uma foto dentro de uma foto, dentro de uma foto...? Ou dois
espelhos frente a frente? Esse "dentro de si mesmo" é a ideia da aula de
hoje.

### 💡 Ideia nova (5 min)

Um procedimento pode **chamar a si mesmo**: é a **recursão**.

```
PARA CONTAGEM :N
  SE :N < 0 [ SAIA ]        ; condicao de parada
  MOSTRE :N
  CONTAGEM :N - 1           ; chama a si mesmo, com um numero menor
FIM

CONTAGEM 5                  ; escreve 5 4 3 2 1 0
```

Toda recursão precisa de duas partes:

1. **Condição de parada** (`SAIA` quando o problema ficou simples), senão
   ela chama a si mesma para sempre;
2. **Passo recursivo**: uma chamada a si mesma com um problema
   **menor** ou mais perto da parada.

`SAIA` sai do procedimento atual (sem devolver valor).

### 🛠️ Mão na massa (7 min)

Uma espiral recursiva: cada chamada anda um pouco mais que a anterior:

<!-- exemplo: avancado/13_espiral_recursiva.logo -->
```logo
PARA ESPIRAL :LADO
  SE :LADO > 150 [ SAIA ]
  PF :LADO
  PD 90
  ESPIRAL :LADO + 5
FIM

COR "azul
ESPIRAL 5
```

*(Este programa está pronto em [`exemplos/avancado/13_espiral_recursiva.logo`](exemplos/avancado/13_espiral_recursiva.logo).)*

Troque o `PD 90` por `PD 91`, e o `150` por `100`.

E o que acontece se **esquecermos** a condição de parada?

```logo-erro
PARA SEM_PARADA :N
  MOSTRE :N
  SEM_PARADA :N + 1
FIM

SEM_PARADA 1
```

O Logo conta quantas chamadas estão "abertas" e, passando de umas
centenas, interrompe com um aviso. (No terminal, isso não trava o
programa.)

### 🎯 Exercícios (5 min)

- **6.1** ⭐ Escreva `CONTAGEM :N` e teste com 5 e com 0.
- **6.2** ⭐ Troque a espiral para um **triângulo** (giro de 120°) que
  para quando o lado passa de 200 e cresce de 4 em 4.
- **6.3** ⭐⭐ Faça `ROSACEA :N`: se `:N` é 0, `SAIA`; senão desenha um
  quadrado de lado 50, gira 10° e chama `ROSACEA :N - 1`. Teste com 36.
- **6.4** ⭐⭐ Escreva `SOMA_ATE :N`, que **mostra** os números de `:N`
  até 1 e depois o total (use uma variável global `soma`).
- **6.5** ⭐⭐⭐ Faça uma espiral de quadrados que **encolhe**: cada
  chamada desenha um quadrado, gira 10° e chama a si mesma com lado
  multiplicado por `0.95`, parando quando o lado for menor que 5.

### 🚀 Desafio extra

Quantos quadrados a espiral encolhendo do 6.5 desenha (lado inicial 100)?
Resolva com uma variável contadora.

<details>
<summary>Ver respostas</summary>

**6.1**

```logo
PARA CONTAGEM :N
  SE :N < 0 [ SAIA ]
  MOSTRE :N
  CONTAGEM :N - 1
FIM
CONTAGEM 5
CONTAGEM 0
```

**6.2**

```logo
PARA ESPIRAL_TRI :LADO
  SE :LADO > 200 [ SAIA ]
  PF :LADO
  PD 120
  ESPIRAL_TRI :LADO + 4
FIM
ESPIRAL_TRI 5
```

**6.3**

```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARA ROSACEA :N
  SE :N = 0 [ SAIA ]
  QUADRADO 50
  PD 10
  ROSACEA :N - 1
FIM
ROSACEA 36
```

**6.4**

```logo
FACA "soma 0
PARA SOMA_ATE :N
  SE :N = 0 [ MOSTRE :soma SAIA ]
  MOSTRE :N
  FACA "soma :soma + :N
  SOMA_ATE :N - 1
FIM
SOMA_ATE 5
```

(Escreve 5, 4, 3, 2, 1 e, por fim, 15.)

**6.5**

```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARA ESPIRAL_Q :LADO
  SE :LADO < 5 [ SAIA ]
  QUADRADO :LADO
  PD 10
  ESPIRAL_Q :LADO * 0.95
FIM
ESPIRAL_Q 100
```

**Desafio:** são 59 quadrados (100 × 0,95⁵⁹ ≈ 4,9 < 5).

```logo
FACA "conta 0
PARA CONTA_QUADRADOS :LADO
  SE :LADO < 5 [ SAIA ]
  FACA "conta :conta + 1
  CONTA_QUADRADOS :LADO * 0.95
FIM
CONTA_QUADRADOS 100
MOSTRE :conta
```

</details>

---

## Aula 7 - Recursão com dois ramos: a árvore

### 🔥 Aquecimento (3 min)

Quando a recursão da aula passada parou? (Quando o lado ficou pequeno ou
o contador zerou.) Em uma árvore, cada galho se divide em outros galhos
menores até ficar pequeno demais. Dá para escrever isso?

### 💡 Ideia nova (5 min)

A árvore recursiva é um procedimento que desenha um galho e **chama a si
mesmo duas vezes**: uma para o galho da direita e outra para o da
esquerda, cada um menor:

```
PARA ARVORE :TAMANHO :ANGULO
  SE :TAMANHO < 10 [ SAIA ]
  PF :TAMANHO
  PD :ANGULO
  ARVORE :TAMANHO * 0.7 :ANGULO
  PE :ANGULO * 2
  ARVORE :TAMANHO * 0.7 :ANGULO
  PD :ANGULO
  PT :TAMANHO
FIM
```

Repare como a tartaruga **desfaz** tudo no fim (`PD`, `PT`): ela volta
ao ponto de partida, olhando para o mesmo lado, para a chamada de cima
continuar de onde parou. Veja também
[`exemplos/avancado/01_arvore_recursiva.logo`](exemplos/avancado/01_arvore_recursiva.logo).

**Ideia de matemática:** os tamanhos 100, 70, 49, 34,3... formam uma
**progressão geométrica** de razão 0,7. É a mesma ideia dos juros
compostos que você viu na Aula 4.

### 🛠️ Mão na massa (7 min)

<!-- exemplo: avancado/14_arvore_com_angulo.logo -->
```logo
PARA ARVORE :TAMANHO :ANGULO
  SE :TAMANHO < 10 [ SAIA ]
  PF :TAMANHO
  PD :ANGULO
  ARVORE :TAMANHO * 0.7 :ANGULO
  PE :ANGULO * 2
  ARVORE :TAMANHO * 0.7 :ANGULO
  PD :ANGULO
  PT :TAMANHO
FIM

COR "marrom
ARVORE 100 25
```

*(Este programa está pronto em [`exemplos/avancado/14_arvore_com_angulo.logo`](exemplos/avancado/14_arvore_com_angulo.logo).)*

Teste `ARVORE 100 40` e `ARVORE 100 10`. Qual parece um coqueiro, qual
parece um arbusto?

### 🎯 Exercícios (5 min)

- **7.1** ⭐ Troque o `0.7` por `0.5` e por `0.8`. O que muda na árvore?
- **7.2** ⭐ Troque o limite `10` por `5`. O desenho fica mais ou menos
  cheio? Por quê?
- **7.3** ⭐⭐ Faça os galhos pequenos (menores que 25) ficarem **verdes**
  e os grandes **marrons**, usando um procedimento `COR_DO_GALHO :T`.
- **7.4** ⭐⭐ Crie `ARVORE3`, com **três** ramos por galho (esquerda,
  centro e direita), com fator 0,6.
- **7.5** ⭐⭐⭐ Escreva a função `GALHOS :N` que devolve o **número de
  galhos** de uma árvore com `:N` níveis (cada nível dobra: 1, 3, 7,
  15...). Escreva a regra: `GALHOS :N = 1 + 2 × GALHOS(:N − 1)`.
  Quantos galhos tem uma árvore de 10 níveis?

### 🚀 Desafio extra

Escreva `GALHOS` de outra forma, sem recursão, usando o resultado
`2^N − 1` (use um laço que multiplica por 2).

<details>
<summary>Ver respostas</summary>

**7.1** Com 0,5 os galhos ficam muito curtos (árvore pequena, ralinha);
com 0,8, a árvore é grande e densa.

```logo
PARA ARVORE :TAMANHO :ANGULO
  SE :TAMANHO < 10 [ SAIA ]
  PF :TAMANHO
  PD :ANGULO
  ARVORE :TAMANHO * 0.8 :ANGULO
  PE :ANGULO * 2
  ARVORE :TAMANHO * 0.8 :ANGULO
  PD :ANGULO
  PT :TAMANHO
FIM
ARVORE 100 25
```

**7.2** Fica mais cheia: mais níveis de galhos antes de parar (cada
nível a mais **dobra** o número de galhos).

```logo
PARA ARVORE :TAMANHO :ANGULO
  SE :TAMANHO < 5 [ SAIA ]
  PF :TAMANHO
  PD :ANGULO
  ARVORE :TAMANHO * 0.7 :ANGULO
  PE :ANGULO * 2
  ARVORE :TAMANHO * 0.7 :ANGULO
  PD :ANGULO
  PT :TAMANHO
FIM
ARVORE 100 25
```

**7.3**

```logo
PARA COR_DO_GALHO :T
  SE :T < 25 [ COR "verde ] [ COR "marrom ]
FIM
PARA ARVORE :T
  SE :T < 10 [ SAIA ]
  COR_DO_GALHO :T
  PF :T
  PD 25
  ARVORE :T * 0.7
  PE 50
  ARVORE :T * 0.7
  PD 25
  COR_DO_GALHO :T
  PT :T
FIM
ARVORE 100
```

**7.4**

```logo
PARA ARVORE3 :T
  SE :T < 12 [ SAIA ]
  PF :T
  PE 40
  ARVORE3 :T * 0.6
  PD 40
  ARVORE3 :T * 0.6
  PD 40
  ARVORE3 :T * 0.6
  PE 40
  PT :T
FIM
ARVORE3 80
```

**7.5** 1023 galhos.

```logo
PARA GALHOS :N
  SE :N = 0 [ DEVOLVA 0 ]
  DEVOLVA 1 + 2 * GALHOS :N - 1
FIM
MOSTRE GALHOS 1
MOSTRE GALHOS 2
MOSTRE GALHOS 3
MOSTRE GALHOS 10
```

**Desafio:**

```logo
PARA GALHOS_SEM_RECURSAO :N
  FACA "p 1
  REPITA :N [ FACA "p :p * 2 ]
  DEVOLVA :p - 1
FIM
MOSTRE GALHOS_SEM_RECURSAO 10
```

</details>

---

## Aula 8 - Recursão que devolve valor: fatorial, Fibonacci e MDC

### 🔥 Aquecimento (3 min)

Quanto é `5!` (cinco fatorial, `5 × 4 × 3 × 2 × 1`)? E `6!`? Perceba que
`6! = 6 × 5!`. Esse "resolva usando uma versão menor do mesmo
problema" é o coração da recursão.

### 💡 Ideia nova (5 min)

Juntando `DEVOLVA` com recursão, funções matemáticas clássicas ficam
curtíssimas:

```
PARA FATORIAL :N
  SE :N <= 1 [ DEVOLVA 1 ]               ; caso mais simples
  DEVOLVA :N * FATORIAL :N - 1           ; N x (versao menor)
FIM

PARA FIBONACCI :N
  SE :N <= 1 [ DEVOLVA :N ]
  DEVOLVA (FIBONACCI :N - 1) + (FIBONACCI :N - 2)
FIM
```

Repare nos parênteses de `FIBONACCI`: como há **duas** chamadas
somadas, cada uma vai entre parênteses para o Logo saber onde cada
chamada termina. Na dúvida, use parênteses: nunca atrapalham. Veja
[`exemplos/avancado/05_fatorial_fibonacci.logo`](exemplos/avancado/05_fatorial_fibonacci.logo).

### 🛠️ Mão na massa (7 min)

A espiral áurea! Os números de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21...)
viram os raios de quartos de círculo encaixados:

<!-- exemplo: avancado/15_espiral_aurea.logo -->
```logo
PARA FIBONACCI :N
  SE :N <= 1 [ DEVOLVA :N ]
  DEVOLVA (FIBONACCI :N - 1) + (FIBONACCI :N - 2)
FIM

PARA ARCO :RAIO :GRAUS
  REPITA :GRAUS [ PF 2 * PI * :RAIO / 360 PD 1 ]
FIM

COR "dourado
ESPESSURA 2
PARACADA :i DE 1 ATE 10 [
  ARCO (FIBONACCI :i) * 3 90
]
```

*(Este programa está pronto em [`exemplos/avancado/15_espiral_aurea.logo`](exemplos/avancado/15_espiral_aurea.logo).)*

Escreva também a razão entre dois termos vizinhos:
`MOSTRE (FIBONACCI 20) / (FIBONACCI 19)`: dá 1,618..., a **razão áurea**.

### 🎯 Exercícios (5 min)

- **8.1** ⭐ Calcule `FATORIAL 6` e `FATORIAL 10`.
- **8.2** ⭐ Escreva `SOMA :N` recursivo: `SOMA 0 = 0` e
  `SOMA :N = :N + SOMA (:N − 1)`. Teste `SOMA 100` (deve dar 5050).
- **8.3** ⭐⭐ Escreva `POTENCIA :BASE :EXP` recursivo (`BASE^0 = 1`,
  `BASE^EXP = BASE × BASE^(EXP−1)`). Teste `POTENCIA 2 10` (1024).
- **8.4** ⭐⭐ O que acontece com `FATORIAL -3`? Conserte para escrever
  `[numero invalido]` e devolver 0 quando `:N < 0`.
- **8.5** ⭐⭐⭐ **MDC** (máximo divisor comum) pelo algoritmo de
  **Euclides**: `MDC :A :B` devolve `:A` se `:B = 0`; senão devolve
  `MDC :B (:A % :B)`. Teste `MDC 48 18` (6) e use-o para simplificar a
  fração `48/18`.

### 🚀 Desafio extra

Escreva uma versão **sem recursão** de `FIBONACCI` (com `ENQUANTO` e três
variáveis) e compare: qual calcula `FIBONACCI 25` mais depressa? Por quê?

<details>
<summary>Ver respostas</summary>

**8.1** 720 e 3628800.

```logo
PARA FATORIAL :N
  SE :N <= 1 [ DEVOLVA 1 ]
  DEVOLVA :N * FATORIAL :N - 1
FIM
MOSTRE FATORIAL 6
MOSTRE FATORIAL 10
```

**8.2**

```logo
PARA SOMA :N
  SE :N = 0 [ DEVOLVA 0 ]
  DEVOLVA :N + SOMA :N - 1
FIM
MOSTRE SOMA 100
```

**8.3**

```logo
PARA POTENCIA :BASE :EXP
  SE :EXP = 0 [ DEVOLVA 1 ]
  DEVOLVA :BASE * POTENCIA :BASE :EXP - 1
FIM
MOSTRE POTENCIA 2 10
MOSTRE POTENCIA 5 3
```

**8.4** Sem proteção, `FATORIAL -3` devolve 1 (porque `-3 <= 1`), o que
está errado: fatorial de negativo não existe.

```logo
PARA FATORIAL :N
  SE :N < 0 [ MOSTRE [numero invalido] DEVOLVA 0 ]
  SE :N <= 1 [ DEVOLVA 1 ]
  DEVOLVA :N * FATORIAL :N - 1
FIM
MOSTRE FATORIAL -3
MOSTRE FATORIAL 5
```

**8.5** `MDC 48 18 = 6`, então `48/18 = 8/3`.

```logo
PARA MDC :A :B
  SE :B = 0 [ DEVOLVA :A ]
  DEVOLVA MDC :B (:A % :B)
FIM
MOSTRE MDC 48 18
MOSTRE 48 / MDC 48 18
MOSTRE 18 / MDC 48 18
```

**Desafio:** a versão com laço faz 25 passos; a recursiva refaz os mesmos
cálculos muitas vezes (mais de 240 mil chamadas para o 25).

```logo
PARA FIB_LACO :N
  FACA "a 0
  FACA "b 1
  REPITA :N [
    FACA "c :a + :b
    FACA "a :b
    FACA "b :c
  ]
  DEVOLVA :a
FIM
MOSTRE FIB_LACO 25
```

</details>

---

## Aula 9 - Fractais: Koch, Sierpinski e a curva C

### 🔥 Aquecimento (3 min)

Olhe um brócolis, uma samambaia ou o contorno de uma costa marítima.
Cada pedacinho parece uma cópia menor do todo. Isso é um **fractal**: uma
forma feita de partes que se parecem com ela mesma.

### 💡 Ideia nova (5 min)

Um fractal é um desenho **recursivo**: o desenho de nível `N` é feito
de cópias menores do desenho de nível `N-1`. No nível 0, é uma forma
simples.

A **curva de Koch**: um segmento de nível `N` vira **4** segmentos de
nível `N-1` (cada um com 1/3 do tamanho), com viradas esquerda,
direita-direita, esquerda entre eles; no nível 0 é uma linha reta:

```
PARA KOCH :TAMANHO :NIVEL
  SE :NIVEL = 0 [ PF :TAMANHO SAIA ]
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PD 120
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
FIM
```

Cada nível multiplica o número de segmentos por 4: nível 3 tem
`4 × 4 × 4 = 64` segmentos; nível 5, mais de mil. Veja
[`exemplos/avancado/08_floco_de_neve.logo`](exemplos/avancado/08_floco_de_neve.logo).

### 🛠️ Mão na massa (7 min)

O **triângulo de Sierpinski**: um triângulo feito de 3 triângulos
menores, cada um feito de 3 menores, e assim por diante.

<!-- exemplo: avancado/16_sierpinski.logo -->
```logo
PARA SIERPINSKI :TAM :NIVEL
  SE :NIVEL = 0 [
    REPITA 3 [ PF :TAM PE 120 ]
    SAIA
  ]
  REPITA 3 [
    SIERPINSKI (:TAM / 2) (:NIVEL - 1)
    PF :TAM
    PE 120
  ]
FIM

COR "roxo
LP
VAIPARA -150 -120
DEFINARUMO 90
AP
SIERPINSKI 300 4
```

*(Este programa está pronto em [`exemplos/avancado/16_sierpinski.logo`](exemplos/avancado/16_sierpinski.logo).)*

Troque o nível 4 por 0, 1, 2, 3 e 5, e observe o que cada nível
acrescenta.

### 🎯 Exercícios (5 min)

- **9.1** ⭐ Desenhe, uma sobre a outra, as curvas de Koch de nível 0, 1,
  2 e 3 (tamanho 300).
- **9.2** ⭐ Desenhe o **floco de neve** completo (3 curvas de Koch, com
  giro de 120° entre elas) de nível 3.
- **9.3** ⭐⭐ Troque o sentido das viradas na Koch (`PD 60`, `PE 120`,
  `PD 60`). Que figura aparece no floco ("anti-floco")?
- **9.4** ⭐⭐ Quantos triângulos pequenos tem o Sierpinski de nível 4?
  (Cada nível multiplica por 3.) Calcule com `POTENCIA` ou um laço e
  confira contando no desenho.
- **9.5** ⭐⭐⭐ **Curva C de Lévy**: `CURVA_C :N :T` — se `:N` é 0, `PF :T`;
  senão: gira 45° para a direita, `CURVA_C` com `:N - 1` e `:T / RAIZ 2`,
  gira 90° para a esquerda, repete a chamada, gira 45° para a direita.
  Teste com `CURVA_C 10 200`.

### 🚀 Desafio extra

Calcule o **comprimento** da curva de Koch de nível `N` (tamanho 300):
cada nível multiplica o comprimento por `4/3`. Qual o comprimento do
nível 5? E o que acontece quando o nível fica muito grande?

<details>
<summary>Ver respostas</summary>

**9.1**

```logo
PARA KOCH :TAMANHO :NIVEL
  SE :NIVEL = 0 [ PF :TAMANHO SAIA ]
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PD 120
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
FIM
PARACADA :n DE 0 ATE 3 [
  LP
  VAIPARA -150 (:n * 100 - 150)
  DEFINARUMO 90
  AP
  KOCH 300 :n
]
```

**9.2**

```logo
PARA KOCH :TAMANHO :NIVEL
  SE :NIVEL = 0 [ PF :TAMANHO SAIA ]
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PD 120
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 60
  KOCH (:TAMANHO / 3) (:NIVEL - 1)
FIM
LP
VAIPARA -150 90
DEFINARUMO 90
AP
COR "azul
REPITA 3 [ KOCH 300 3 PD 120 ]
```

**9.3**

```logo
PARA ANTIKOCH :TAMANHO :NIVEL
  SE :NIVEL = 0 [ PF :TAMANHO SAIA ]
  ANTIKOCH (:TAMANHO / 3) (:NIVEL - 1)
  PD 60
  ANTIKOCH (:TAMANHO / 3) (:NIVEL - 1)
  PE 120
  ANTIKOCH (:TAMANHO / 3) (:NIVEL - 1)
  PD 60
  ANTIKOCH (:TAMANHO / 3) (:NIVEL - 1)
FIM
LP
VAIPARA -150 90
DEFINARUMO 90
AP
COR "vermelho
REPITA 3 [ ANTIKOCH 300 3 PD 120 ]
```

As "pontas" do floco passam a apontar **para dentro**.

**9.4** 81 triângulos (3⁴).

```logo
PARA POTENCIA :BASE :EXP
  SE :EXP = 0 [ DEVOLVA 1 ]
  DEVOLVA :BASE * POTENCIA :BASE :EXP - 1
FIM
MOSTRE POTENCIA 3 4
```

**9.5**

```logo
PARA CURVA_C :N :T
  SE :N = 0 [ PF :T SAIA ]
  PD 45
  CURVA_C (:N - 1) (:T / RAIZ 2)
  PE 90
  CURVA_C (:N - 1) (:T / RAIZ 2)
  PD 45
FIM
COR "verde
LP
VAIPARA -80 -100
DEFINARUMO 90
AP
CURVA_C 10 200
```

**Desafio:** nível 5: `300 × (4/3)⁵ ≈ 1264` (a curva é mais de 4 vezes
mais longa que o segmento de 300!). Quando o nível cresce, o
comprimento **cresce sem limite**, apesar de o desenho ocupar sempre o
mesmo espaço: uma curva infinitamente longa num espaço finito.

```logo
FACA "c 300
REPITA 5 [ FACA "c :c * 4 / 3 ]
MOSTRE :c
```

</details>

---

## Aula 10 - Projeto final: gráficos e tabuleiros

### 🔥 Aquecimento (3 min)

Revisão-relâmpago, sem computador:

1. Qual a diferença entre um procedimento e uma função? (a função
   **devolve** um valor)
2. Para que serve a condição de parada de uma recursão?
3. Quanto vale `RAIZ (9 + 16)`? (5)
4. Qual laço você usaria para "repetir até o dinheiro dobrar"?
   (`ENQUANTO`)

### 💡 Ideia nova (5 min)

Uma função matemática, como `f(x) = x² / 100`, pode ser **desenhada**:
para cada valor de `x`, calcule `f(x)` e ligue os pontos `(x, f(x))` com
`VAIPARA`. É assim que se fazem os gráficos de funções, e é a base de
qualquer **visualização de dados**.

### 🛠️ Mão na massa (7 min)

<!-- exemplo: avancado/17_grafico_de_funcao.logo -->
```logo
PARA F :X
  DEVOLVA :X * :X / 100
FIM

PARA EIXOS
  COR "cinza
  LP
  VAIPARA -200 0
  AP
  VAIPARA 200 0
  LP
  VAIPARA 0 -50
  AP
  VAIPARA 0 250
FIM

PARA PLOTA
  COR "azul
  ESPESSURA 2
  LP
  VAIPARA -150 (F -150)
  AP
  PARACADA :x DE -150 ATE 150 PASSO 5 [ VAIPARA :x (F :x) ]
FIM

EIXOS
PLOTA
```

*(Este programa está pronto em [`exemplos/avancado/17_grafico_de_funcao.logo`](exemplos/avancado/17_grafico_de_funcao.logo).)*

Aqui `F` é uma **parábola**. Mude a regra de `F` para `:X / 2 + 20`
(uma **reta**) e plote de novo.

### 🎯 Exercícios (5 min)

**Projeto:** escolha **um** e faça (planeje antes, no papel!):

- **10.1** ⭐ Plote **duas** funções no mesmo gráfico, com cores
  diferentes: `f(x) = x² / 100` e `g(x) = x / 2 + 20`. Onde elas se
  cruzam?
- **10.2** ⭐⭐ Um **tabuleiro de xadrez** completo (8 × 8), com `SE`
  para alternar as cores (veja
  [`exemplos/avancado/09_tabuleiro.logo`](exemplos/avancado/09_tabuleiro.logo)),
  e marque com um círculo (`CIRCULO`) uma casa que você escolher.
- **10.3** ⭐⭐⭐ Uma **paisagem fractal**: uma `ARVORE` grande, outra
  menor ao lado, montanhas com a curva C ou Koch, e um sol feito de
  `CIRCULO`.

**Checklist de autoavaliação:** ✅ usei pelo menos uma função com
`DEVOLVA`, ✅ usei recursão (com condição de parada) ou `ENQUANTO`,
✅ usei `PARACADA`, ✅ meu desenho cabe na tela, ✅ expliquei a um adulto
como o programa funciona.

### 🚀 Desafio extra

Plote `h(x) = x * x * x / 10000` (uma **cúbica**: negativa quando `x` é
negativo) junto com a parábola `x² / 100`, para `x` de −100 a 120. Em
quais valores de `x` o gráfico da cúbica cruza o da parábola? (Dica:
resolva `x³ / 10000 = x² / 100` em papel.)

<details>
<summary>Ver uma resposta para 10.1</summary>

As curvas se cruzam quando `x² / 100 = x / 2 + 20`, isto é,
`x² − 50x − 2000 = 0`, o que dá `x ≈ 76` e `x ≈ −26`. Confira no
gráfico: é onde a linha vermelha encontra a azul.

```logo
PARA F :X
  DEVOLVA :X * :X / 100
FIM
PARA G :X
  DEVOLVA :X / 2 + 20
FIM
PARA EIXOS
  COR "cinza
  LP
  VAIPARA -200 0
  AP
  VAIPARA 200 0
  LP
  VAIPARA 0 -50
  AP
  VAIPARA 0 250
FIM
EIXOS
COR "azul
LP
VAIPARA -150 (F -150)
AP
PARACADA :x DE -150 ATE 150 PASSO 5 [ VAIPARA :x (F :x) ]
COR "vermelho
LP
VAIPARA -150 (G -150)
AP
PARACADA :x DE -150 ATE 150 PASSO 5 [ VAIPARA :x (G :x) ]
```

**Desafio:** `x³/10000 = x²/100` dá `x² (x − 100) = 0`: elas se cruzam em
`x = 0` e `x = 100`.

```logo
PARA F :X
  DEVOLVA :X * :X / 100
FIM
PARA H :X
  DEVOLVA :X * :X * :X / 10000
FIM
COR "azul
LP
VAIPARA -100 (F -100)
AP
PARACADA :x DE -100 ATE 120 PASSO 5 [ VAIPARA :x (F :x) ]
COR "verde
LP
VAIPARA -100 (H -100)
AP
PARACADA :x DE -100 ATE 120 PASSO 5 [ VAIPARA :x (H :x) ]
```

</details>

---

## O que você aprendeu

- **Funções** com `DEVOLVA`: procedimentos que devolvem respostas
  (`DOBRO`, `MEDIA`, `HIPOTENUSA`, `DISTANCIA`).
- O **Teorema de Pitágoras**, trios pitagóricos e números irracionais.
- **Círculos** e o número π: circunferência (`2πr`) e área (`πr²`).
- `ENQUANTO` para repetir sem saber de antemão quantas vezes, e
  `QUEBRA`/`CONTINUA` para controlar um laço por dentro.
- **Recursão**: condição de parada, passo recursivo, árvores,
  fatorial, Fibonacci e MDC.
- **Fractais** (Koch, Sierpinski, curva C) e como cada nível
  multiplica o trabalho.
- **Gráficos de funções**, a base da visualização de dados.

## Para onde ir depois

Você já tem as ferramentas de um "Logo completo". Algumas ideias para
continuar por conta própria:

- Desenhe a **curva do dragão** e a **árvore de Pitágoras**.
- Use `FATORIAL` para escrever o **triângulo de Pascal** (um número por
  linha): `n! / (k! × (n−k)!)`.
- Escreva `MMC :A :B` usando o `MDC` (`A × B / MDC A B`).
- Faça um **gráfico de barras** de dados reais (as notas da turma, as
  vendas de uma loja) com `PARACADA`, `DEVOLVA` e `MEDIA`.
- Compare quanto tempo `FIBONACCI 25` (recursivo) e `FIB_LACO 25`
  (com laço) levam. Essa pergunta — **qual algoritmo é mais eficiente?**
  — é uma das grandes perguntas da ciência da computação.
