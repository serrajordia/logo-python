# Trilha 2 - Intermediário

**O que você vai aprender:** criar seus próprios comandos
(procedimentos), guardar valores em variáveis, tomar decisões com `SE`,
repetir com `PARACADA` (um laço com variável de verdade) e planejar
desenhos grandes quebrando-os em partes menores.

**Formato:** 10 aulas de **20 minutos** cada, com dificuldade crescente.
Pré-requisito: a [Trilha 1 - Básico](trilha-1-basico.md).

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

> **Dica para digitar programas de várias linhas:** na versão web, cole o
> programa inteiro na caixa de comandos e aperte Enter (ou use Shift+Enter
> para pular linha). No terminal, digite as linhas e termine com `FIM`.
> Dentro dos exemplos, tudo que vem depois de `;` é comentário: o Logo
> ignora, é só para você ler.

---

## Aula 1 - Procedimentos: crie os seus próprios comandos

### 🔥 Aquecimento (3 min)

Na trilha passada, quantas vezes você digitou
`REPITA 4 [ PF 50 PD 90 ]`? Imagine desenhar 10 casas, cada uma com
vários quadrados. Haveria um jeito de ensinar a tartaruga a palavra
**QUADRADO**?

### 💡 Ideia nova (5 min)

Há! Com `PARA` e `FIM` você **ensina um comando novo** à tartaruga. É uma
"receita" com nome:

```
PARA QUADRADO
  REPITA 4 [ PF 50 PD 90 ]
FIM
```

Isso **não desenha nada ainda**: só ensina a receita. Para usar, basta
escrever o nome:

```
QUADRADO
```

**Ideia de programação:** dar nome a um conjunto de instruções chama-se
**abstração**. A receita é escrita **uma vez** e usada **quantas vezes
você quiser** — e se você mudar a receita, todos os usos mudam juntos.

### 🛠️ Mão na massa (7 min)

Vamos criar *dois* comandos e combiná-los num trenzinho de quadrados:

<!-- exemplo: intermediario/07_trenzinho.logo -->
```logo
PARA QUADRADO
  REPITA 4 [ PF 50 PD 90 ]
FIM

PARA PULA
  LP
  PD 90
  PF 70
  PE 90
  AP
FIM

REPITA 4 [ QUADRADO PULA ]
```

*(Este programa está pronto em [`exemplos/intermediario/07_trenzinho.logo`](exemplos/intermediario/07_trenzinho.logo).)*

Troque o 4 por 6. Troque o `70` do `PULA` por `50`. O que acontece com os
quadrados?

### 🎯 Exercícios (5 min)

- **1.1** ⭐ Crie o comando `TRIANGULO` (lado 60) e use-o.
- **1.2** ⭐ Crie o comando `PENTAGONO` (lado 40) e use-o.
- **1.3** ⭐⭐ Com `QUADRADO` criado, faça uma rosácea:
  `REPITA 36 [ QUADRADO PD 10 ]`. Ficou igual à da trilha passada?
- **1.4** ⭐⭐ Crie `FILEIRA`, que desenha 5 quadrados em linha, usando
  `QUADRADO` e `PULA`.
- **1.5** ⭐⭐⭐ Crie `DEGRAU` (sobe 20, vira à direita, anda 20, vira à
  esquerda) e depois `ESCADA`, que usa `DEGRAU` 6 vezes. Repare: um
  procedimento usando outro!

### 🚀 Desafio extra

Crie `MURO`, uma fila de 8 quadrados, usando `FILEIRA` duas vezes mais
uma de 3 quadrados. (Pense em como a tartaruga precisa voltar ao ponto
certo entre as filas.)

<details>
<summary>Ver respostas</summary>

**1.1**

```logo
PARA TRIANGULO
  REPITA 3 [ PF 60 PD 120 ]
FIM
TRIANGULO
```

**1.2**

```logo
PARA PENTAGONO
  REPITA 5 [ PF 40 PD 72 ]
FIM
PENTAGONO
```

**1.3** Sim: é a mesma rosácea, mas agora você a escreveu com uma
palavra sua.

```logo
PARA QUADRADO
  REPITA 4 [ PF 50 PD 90 ]
FIM
REPITA 36 [ QUADRADO PD 10 ]
```

**1.4**

```logo
PARA QUADRADO
  REPITA 4 [ PF 50 PD 90 ]
FIM
PARA PULA
  LP
  PD 90
  PF 70
  PE 90
  AP
FIM
PARA FILEIRA
  REPITA 5 [ QUADRADO PULA ]
FIM
FILEIRA
```

**1.5**

```logo
PARA DEGRAU
  PF 20
  PD 90
  PF 20
  PE 90
FIM
PARA ESCADA
  REPITA 6 [ DEGRAU ]
FIM
ESCADA
```

**Desafio:** depois de cada `FILEIRA`, a tartaruga fica à direita. Um
jeito é voltar com `LP PT 350 AP` (5 × 70) e subir com `PF 70`.

```logo
PARA QUADRADO
  REPITA 4 [ PF 50 PD 90 ]
FIM
PARA PULA
  LP
  PD 90
  PF 70
  PE 90
  AP
FIM
PARA FILEIRA :N
  REPITA :N [ QUADRADO PULA ]
FIM
PARA VOLTA :N
  LP
  PE 90
  PF :N * 70
  PD 90
  PF 70
  AP
FIM
FILEIRA 4
VOLTA 4
FILEIRA 4
```

(Este último já usa um parâmetro `:N` — assunto da próxima aula!)

</details>

---

## Aula 2 - Parâmetros: um comando para qualquer tamanho

### 🔥 Aquecimento (3 min)

O seu `QUADRADO` sempre desenha o mesmo tamanho. Se você quisesse
quadrados de tamanhos diferentes, precisaria de um procedimento para cada
tamanho?

### 💡 Ideia nova (5 min)

Não! Um **parâmetro** é um "espaço em branco" na receita, que você
preenche cada vez que a usa:

```
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

QUADRADO 30    ; o :LADO vira 30
QUADRADO 90    ; agora o :LADO vira 90
```

`:LADO` funciona como o `x` de uma equação: um nome para um número que
ainda não sabemos. Você pode ter **vários** parâmetros, separados por
espaços, e preenchê-los na mesma ordem:

```
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [ PF :TAMANHO PD 360 / :LADOS ]
FIM

POLIGONO 6 50
```

Veja [`exemplos/intermediario/01_poligono_funcao.logo`](exemplos/intermediario/01_poligono_funcao.logo).

### 🛠️ Mão na massa (7 min)

Quadrados concentrados num mesmo canto, cada um maior que o anterior:

<!-- exemplo: intermediario/08_quadrados_crescentes.logo -->
```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

REPITA 8 [ QUADRADO REPCOUNT * 10 ]
```

*(Este programa está pronto em [`exemplos/intermediario/08_quadrados_crescentes.logo`](exemplos/intermediario/08_quadrados_crescentes.logo).)*

Aqui o `REPCOUNT` entra como o parâmetro: 10, 20, 30... 80.

### 🎯 Exercícios (5 min)

- **2.1** ⭐ Crie `TRIANGULO :LADO` e desenhe três triângulos de lados
  30, 60 e 90.
- **2.2** ⭐ Use `POLIGONO` para desenhar um octógono de lado 40.
- **2.3** ⭐⭐ Crie `RETANGULO :BASE :ALTURA` (não dá para usar um só
  número, os lados são diferentes).
- **2.4** ⭐⭐ Desenhe os polígonos de 3, 4, 5, 6, 7 e 8 lados, todos com
  lado 40, chamando `POLIGONO` seis vezes. Eles ficam "um dentro do
  outro"?
- **2.5** ⭐⭐⭐ Faça uma rosácea de quadrados **crescentes**: 36
  quadrados, o lado de cada um é `20 + REPCOUNT * 3`, girando 10° entre
  eles.

### 🚀 Desafio extra

Crie `CASINHA :LADO` de forma que um único número controle o tamanho de
um quadrado com um triângulo no telhado de **mesmo** lado. (Veja a Aula 4.)

<details>
<summary>Ver respostas</summary>

**2.1**

```logo
PARA TRIANGULO :LADO
  REPITA 3 [ PF :LADO PD 120 ]
FIM
TRIANGULO 30
TRIANGULO 60
TRIANGULO 90
```

**2.2**

```logo
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [ PF :TAMANHO PD 360 / :LADOS ]
FIM
POLIGONO 8 40
```

**2.3**

```logo
PARA RETANGULO :BASE :ALTURA
  REPITA 2 [ PF :ALTURA PD 90 PF :BASE PD 90 ]
FIM
RETANGULO 120 50
```

**2.4** Sim: todos compartilham o ponto de partida e crescem juntos.

```logo
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [ PF :TAMANHO PD 360 / :LADOS ]
FIM
POLIGONO 3 40
POLIGONO 4 40
POLIGONO 5 40
POLIGONO 6 40
POLIGONO 7 40
POLIGONO 8 40
```

**2.5**

```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
REPITA 36 [ QUADRADO 20 + REPCOUNT * 3 PD 10 ]
```

</details>

---

## Aula 3 - Variáveis: guardando valores com FACA

### 🔥 Aquecimento (3 min)

O que é uma variável em matemática? (Uma letra, como `x`, que guarda um
valor.) Em que ela se parece com um parâmetro?

### 💡 Ideia nova (5 min)

Um parâmetro só existe dentro do procedimento. Para guardar um valor
"solto", use `FACA` — que **cria ou muda** uma variável:

```
FACA "idade 10        ; guarda 10 na variavel idade
MOSTRE :idade         ; escreve 10
FACA "idade :idade + 1
MOSTRE :idade         ; escreve 11
```

- `"idade` (com aspas) é o **nome** da variável.
- `:idade` (com dois-pontos) é o **valor** guardado nela.

`FACA "idade :idade + 1` é uma ideia importantíssima de programação:
"pegue o valor antigo, some 1 e guarde o resultado no mesmo lugar".

**Ideia de matemática:** com variáveis dá para calcular. Para um quadrado
de lado `L`: perímetro = `L * 4`, área = `L * L`.

### 🛠️ Mão na massa (7 min)

Quadrados que crescem, usando uma variável que aumenta de 10 em 10:

<!-- exemplo: intermediario/09_quadrados_variavel.logo -->
```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

FACA "lado 10
REPITA 8 [
  QUADRADO :lado
  FACA "lado :lado + 10
]
MOSTRE :lado
```

*(Este programa está pronto em [`exemplos/intermediario/09_quadrados_variavel.logo`](exemplos/intermediario/09_quadrados_variavel.logo).)*

O `MOSTRE` final escreve 90. Por que não 80? (Dica: o `FACA` roda depois de
cada quadrado, inclusive o último.)

### 🎯 Exercícios (5 min)

- **3.1** ⭐ Guarde sua idade numa variável, escreva-a, aumente em 1 e
  escreva de novo.
- **3.2** ⭐ Guarde a base (12) e a altura (5) de um retângulo e escreva o
  **perímetro** e a **área**.
- **3.3** ⭐⭐ Desenhe uma espiral usando uma variável: `lado` começa em 5,
  e a cada volta (50 voltas) a tartaruga anda `:lado`, gira 91° e `lado`
  aumenta 3.
- **3.4** ⭐⭐ Escreva a tabuada do 6 usando uma variável `n` que começa em
  1 e aumenta de 1 em 1 (dez linhas).
- **3.5** ⭐⭐⭐ Comece com `FACA "x 1` e, dez vezes, escreva `:x` e dobre-o
  (`:x * 2`). Quando o valor passa de 1000? Que sequência é essa?

### 🚀 Desafio extra

Escreva os 12 primeiros termos da sequência que começa em 1, 1 e em que
cada termo é a soma dos dois anteriores (1, 1, 2, 3, 5, 8, 13...), usando
três variáveis (`a`, `b`, `c`).

<details>
<summary>Ver respostas</summary>

**3.1**

```logo
FACA "idade 10
MOSTRE :idade
FACA "idade :idade + 1
MOSTRE :idade
```

**3.2** Perímetro: `2 × (12 + 5) = 34`; área: `12 × 5 = 60`.

```logo
FACA "base 12
FACA "altura 5
MOSTRE 2 * (:base + :altura)
MOSTRE :base * :altura
```

**3.3**

```logo
FACA "lado 5
REPITA 50 [
  PF :lado
  PD 91
  FACA "lado :lado + 3
]
```

**3.4**

```logo
FACA "n 1
REPITA 10 [
  MOSTRE :n * 6
  FACA "n :n + 1
]
```

**3.5** Passa de 1000 na décima dobra (1024). São as **potências de 2**.

```logo
FACA "x 1
REPITA 11 [
  MOSTRE :x
  FACA "x :x * 2
]
```

**Desafio:** (Fibonacci)

```logo
FACA "a 1
FACA "b 1
REPITA 12 [
  MOSTRE :a
  FACA "c :a + :b
  FACA "a :b
  FACA "b :c
]
```

</details>

---

## Aula 4 - Planejamento: quebrando um desenho complicado

### 🔥 Aquecimento (3 min)

Olhe para uma casa desenhada por uma criança. De quais **formas simples**
ela é feita? (Um quadrado e um triângulo, no mínimo.)

### 💡 Ideia nova (5 min)

**Planejar** um desenho é descobrir as formas simples que o compõem e
escrever **um procedimento por forma**. Depois, um procedimento maior
**usa** os pequenos. Programadores raramente escrevem tudo do zero: eles
reaproveitam peças que já funcionam.

Plano de uma casa:

```
CASA = QUADRADO (paredes) + TELHADO (triangulo em cima)
```

Veja também
[`exemplos/intermediario/03_casa.logo`](exemplos/intermediario/03_casa.logo).

### 🛠️ Mão na massa (7 min)

<!-- exemplo: intermediario/10_casa_planejada.logo -->
```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

PARA TELHADO :LADO
  PD 90                          ; vira para a direita (ao longo do teto)
  REPITA 3 [ PF :LADO PE 120 ]   ; triangulo para cima
  PE 90
FIM

PARA CASA :LADO
  QUADRADO :LADO
  LP
  PF :LADO                       ; sobe ate o canto de cima
  AP
  TELHADO :LADO
  LP
  PT :LADO                       ; volta ao ponto de partida
  AP
FIM

CASA 100
```

*(Este programa está pronto em [`exemplos/intermediario/10_casa_planejada.logo`](exemplos/intermediario/10_casa_planejada.logo).)*

Repare que `CASA` termina onde começou, olhando para o mesmo lado: isso
facilita usá-la várias vezes.

### 🎯 Exercícios (5 min)

- **4.1** ⭐ Desenhe três casas de tamanhos diferentes (30, 60 e 100)
  chamando `CASA` três vezes.
- **4.2** ⭐⭐ Crie `RUA`: três casas de lado 60 lado a lado (use um
  `PULA :D` que anda `:D` passos para a direita sem desenhar).
- **4.3** ⭐⭐ Crie `ARVORE`: um tronco (retângulo 20 × 60, marrom) e uma
  copa (polígono de 12 lados e lado 20, verde) em cima.
- **4.4** ⭐⭐ Acrescente à casa uma `JANELA :LADO` (um quadrado pequeno
  dentro da parede), criando `CASA_COM_JANELA :LADO`.
- **4.5** ⭐⭐⭐ **Projeto:** um **boneco de palitos**, com um procedimento
  para cada parte do corpo: `CABECA`, `CORPO`, `BRACOS` e `PERNAS`.

### 🚀 Desafio extra

Faça uma vila com uma `RUA`, uma `ARVORE` entre as casas e um sol.

<details>
<summary>Ver respostas</summary>

**4.1**

```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARA TELHADO :LADO
  PD 90
  REPITA 3 [ PF :LADO PE 120 ]
  PE 90
FIM
PARA CASA :LADO
  QUADRADO :LADO
  LP
  PF :LADO
  AP
  TELHADO :LADO
  LP
  PT :LADO
  AP
FIM
CASA 30
LP
PD 90
PF 50
PE 90
AP
CASA 60
LP
PD 90
PF 100
PE 90
AP
CASA 100
```

**4.2**

```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARA TELHADO :LADO
  PD 90
  REPITA 3 [ PF :LADO PE 120 ]
  PE 90
FIM
PARA CASA :LADO
  QUADRADO :LADO
  LP
  PF :LADO
  AP
  TELHADO :LADO
  LP
  PT :LADO
  AP
FIM
PARA PULA :D
  LP
  PD 90
  PF :D
  PE 90
  AP
FIM
PARA RUA
  REPITA 3 [ CASA 60 PULA 80 ]
FIM
RUA
```

**4.3**

```logo
PARA RETANGULO :BASE :ALTURA
  REPITA 2 [ PF :ALTURA PD 90 PF :BASE PD 90 ]
FIM
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [ PF :TAMANHO PD 360 / :LADOS ]
FIM
PARA ARVORE
  COR "marrom
  RETANGULO 20 60
  COR "verde
  LP
  PF 98
  PE 90
  PF 30
  PD 90
  AP
  POLIGONO 12 20
FIM
ARVORE
```

**4.4**

```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARA TELHADO :LADO
  PD 90
  REPITA 3 [ PF :LADO PE 120 ]
  PE 90
FIM
PARA CASA :LADO
  QUADRADO :LADO
  LP
  PF :LADO
  AP
  TELHADO :LADO
  LP
  PT :LADO
  AP
FIM
PARA JANELA :LADO
  QUADRADO :LADO
FIM
PARA CASA_COM_JANELA :LADO
  CASA :LADO
  LP
  PF :LADO / 3
  PD 90
  PF :LADO / 3
  PE 90
  AP
  JANELA :LADO / 3
FIM
CASA_COM_JANELA 120
```

**4.5** (usa coordenadas para cada parte ficar independente)

```logo
PARA CABECA
  LP
  VAIPARA 0 0
  DEFINARUMO 270
  AP
  REPITA 36 [ PF 3 PD 10 ]
FIM
PARA CORPO
  LP
  VAIPARA 0 0
  AP
  VAIPARA 0 -60
FIM
PARA BRACOS
  LP
  VAIPARA 0 -15
  AP
  VAIPARA -30 -40
  VAIPARA 0 -15
  VAIPARA 30 -40
FIM
PARA PERNAS
  LP
  VAIPARA 0 -60
  AP
  VAIPARA -25 -110
  LP
  VAIPARA 0 -60
  AP
  VAIPARA 25 -110
FIM
CABECA
CORPO
BRACOS
PERNAS
```

</details>

---

## Aula 5 - Estrelas e mais ângulos

### 🔥 Aquecimento (3 min)

Qual o giro de um pentágono? (72°.) E se a tartaruga girasse **o dobro**
em cada canto, 144°? Aposte no desenho antes de testar.

### 💡 Ideia nova (5 min)

Com o giro do polígono (`360 / pontas`), a tartaruga anda de ponta em
ponta. Com o **dobro** desse giro, ela **pula uma ponta** e cruza pelo
meio: aparece uma **estrela**!

```
PARA ESTRELA :PONTAS :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * 2 / :PONTAS ]
FIM
```

Veja [`exemplos/intermediario/02_estrela.logo`](exemplos/intermediario/02_estrela.logo).
Podemos "pular" mais de uma ponta, com um terceiro parâmetro, o
**salto** `:SALTO`: o giro passa a ser `360 * :SALTO / :PONTAS`.

### 🛠️ Mão na massa (7 min)

<!-- exemplo: intermediario/11_estrelas_com_salto.logo -->
```logo
PARA ESTRELAS :PONTAS :SALTO :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * :SALTO / :PONTAS ]
FIM

COR "roxo
ESTRELAS 7 2 120
COR "azul
ESTRELAS 7 3 120
```

*(Este programa está pronto em [`exemplos/intermediario/11_estrelas_com_salto.logo`](exemplos/intermediario/11_estrelas_com_salto.logo).)*

Duas estrelas de 7 pontas diferentes: a roxa pula 2 pontas, a azul pula 3.

### 🎯 Exercícios (5 min)

- **5.1** ⭐ Desenhe uma estrela de 5 pontas, lado 100 (`ESTRELAS 5 2 100`).
- **5.2** ⭐ Desenhe a estrela de 4 pontas (`ESTRELAS 4 2 100`). O que
  aparece? Por quê? (Quanto vale o giro?)
- **5.3** ⭐⭐ Faça uma "rosácea de estrelas": 12 estrelas de 5 pontas,
  lado 60, com giro de 30° entre elas.
- **5.4** ⭐⭐ Desenhe `ESTRELAS 8 3 80`. Compare com `ESTRELAS 8 2 80`.
- **5.5** ⭐⭐⭐ Teste `ESTRELAS 9 3 80` e `ESTRELAS 10 4 80`. Elas fecham
  numa figura só ou em várias? Descubra a regra para saber quando uma
  estrela "dá a volta toda" (dica: o que `9` e `3` têm em comum? E `10` e
  `4`?).

### 🚀 Desafio extra

Faça uma estrela de 9 pontas que desenhe tudo "numa linha só". Que salto
você usou?

<details>
<summary>Ver respostas</summary>

**5.1**

```logo
PARA ESTRELAS :PONTAS :SALTO :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * :SALTO / :PONTAS ]
FIM
ESTRELAS 5 2 100
```

**5.2** O giro é `360 * 2 / 4 = 180`: a tartaruga vai e **volta pelo
mesmo caminho**, desenhando só uma linha (ou duas sobrepostas).

```logo
PARA ESTRELAS :PONTAS :SALTO :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * :SALTO / :PONTAS ]
FIM
ESTRELAS 4 2 100
```

**5.3**

```logo
PARA ESTRELAS :PONTAS :SALTO :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * :SALTO / :PONTAS ]
FIM
REPITA 12 [ ESTRELAS 5 2 60 PD 30 ]
```

**5.4**

```logo
PARA ESTRELAS :PONTAS :SALTO :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * :SALTO / :PONTAS ]
FIM
ESTRELAS 8 3 80
COR "vermelho
ESTRELAS 8 2 80
```

A de salto 3 é uma estrela de 8 pontas; a de salto 2 vira **dois
quadrados** cruzados.

**5.5**

```logo
PARA ESTRELAS :PONTAS :SALTO :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * :SALTO / :PONTAS ]
FIM
ESTRELAS 9 3 80
COR "azul
ESTRELAS 10 4 80
```

`9` e `3` têm o divisor comum 3: a figura fecha antes e vira 3
triângulos. `10` e `4` têm o divisor 2: a figura fecha na metade do caminho
e vira **duas estrelas de 5 pontas** sobrepostas. **Regra:** quando `PONTAS` e `SALTO` **não têm
divisor comum** (a não ser 1), a estrela é de uma linha só.

**Desafio:** salto 2 (ou 4), porque 9 e 2 não têm divisor comum.

```logo
PARA ESTRELAS :PONTAS :SALTO :TAMANHO
  REPITA :PONTAS [ PF :TAMANHO PD 360 * :SALTO / :PONTAS ]
FIM
ESTRELAS 9 2 80
```

</details>

---

## Aula 6 - SE: o programa decide

### 🔥 Aquecimento (3 min)

"Se estiver chovendo, levo guarda-chuva; senão, levo óculos de sol." Isso
é uma **decisão**. Dê dois exemplos de decisões que você toma em um dia.

### 💡 Ideia nova (5 min)

`SE condição [ ... ]` executa o bloco **só se** a condição for verdadeira.
Um segundo bloco opcional é o "senão":

```
SE :idade >= 18 [ MOSTRE [pode dirigir] ] [ MOSTRE [ainda nao] ]
```

Comparações: `=` (igual), `<` (menor), `>` (maior), `<=`, `>=` e `<>`
(diferente). Para saber se um número é par, use o **resto** da divisão
por 2: `:N % 2` é 0 quando `:N` é par.

> O Logo daqui não tem "E" nem "OU" para juntar condições. Use um `SE`
> **dentro** de outro: é a mesma coisa.

### 🛠️ Mão na massa (7 min)

<!-- exemplo: intermediario/12_par_ou_impar.logo -->
```logo
PARA PAR_OU_IMPAR :N
  SE (:N % 2) = 0 [ MOSTRE [par] ] [ MOSTRE [impar] ]
FIM

PAR_OU_IMPAR 7
PAR_OU_IMPAR 10
PAR_OU_IMPAR 0
```

*(Este programa está pronto em [`exemplos/intermediario/12_par_ou_impar.logo`](exemplos/intermediario/12_par_ou_impar.logo).)*

Teste mais cinco números seus. Algum resultado te surpreendeu?

### 🎯 Exercícios (5 min)

- **6.1** ⭐ Escreva `MAIOR :A :B`, que escreve o maior dos dois números.
- **6.2** ⭐ Escreva `SINAL :N`, que escreve `[positivo]`, `[negativo]` ou
  `[zero]` (use dois `SE`).
- **6.3** ⭐⭐ Escreva `FIGURA :N`: se `:N` for menor que 3, escreva
  `[isso nao e um poligono]`; senão, desenhe o polígono regular de `:N`
  lados (lado 40).
- **6.4** ⭐⭐ Desenhe 10 quadrados crescentes, alternando as cores:
  azul quando `REPCOUNT` é par, vermelho quando é ímpar.
- **6.5** ⭐⭐⭐ Escreva `CLASSIFICA :A :B :C`, que diz se um triângulo
  com esses lados é `[equilatero]` (3 lados iguais), `[isosceles]` (2
  iguais) ou `[escaleno]` (todos diferentes). Veja
  [`exemplos/intermediario/06_condicionais.logo`](exemplos/intermediario/06_condicionais.logo).

### 🚀 Desafio extra

Melhore `CLASSIFICA` para avisar `[nao forma triangulo]` quando o maior
lado for maior ou igual à soma dos outros dois (a **desigualdade
triangular**).

<details>
<summary>Ver respostas</summary>

**6.1**

```logo
PARA MAIOR :A :B
  SE :A > :B [ MOSTRE :A ] [ MOSTRE :B ]
FIM
MAIOR 4 9
MAIOR 12 7
```

**6.2**

```logo
PARA SINAL :N
  SE :N > 0 [ MOSTRE [positivo] ] [
    SE :N < 0 [ MOSTRE [negativo] ] [ MOSTRE [zero] ]
  ]
FIM
SINAL 5
SINAL -3
SINAL 0
```

**6.3**

```logo
PARA FIGURA :N
  SE :N < 3 [ MOSTRE [isso nao e um poligono] ] [
    REPITA :N [ PF 40 PD 360 / :N ]
  ]
FIM
FIGURA 2
FIGURA 7
```

**6.4**

```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
REPITA 10 [
  SE (REPCOUNT % 2) = 0 [ COR "azul ] [ COR "vermelho ]
  QUADRADO REPCOUNT * 8 + 10
]
```

**6.5**

```logo
PARA CLASSIFICA :A :B :C
  SE :A = :B [
    SE :B = :C [ MOSTRE [equilatero] ] [ MOSTRE [isosceles] ]
  ] [
    SE :A = :C [ MOSTRE [isosceles] ] [
      SE :B = :C [ MOSTRE [isosceles] ] [ MOSTRE [escaleno] ]
    ]
  ]
FIM
CLASSIFICA 3 3 3
CLASSIFICA 3 3 5
CLASSIFICA 3 4 5
```

**Desafio:** acrescente antes de tudo um teste da desigualdade (qualquer
lado maior ou igual à soma dos outros dois). Como não há "OU", encadeie
três `SE`:

```logo
PARA CLASSIFICA :A :B :C
  SE :A >= :B + :C [ MOSTRE [nao forma triangulo] SAIA ]
  SE :B >= :A + :C [ MOSTRE [nao forma triangulo] SAIA ]
  SE :C >= :A + :B [ MOSTRE [nao forma triangulo] SAIA ]
  SE :A = :B [
    SE :B = :C [ MOSTRE [equilatero] ] [ MOSTRE [isosceles] ]
  ] [
    SE :A = :C [ MOSTRE [isosceles] ] [
      SE :B = :C [ MOSTRE [isosceles] ] [ MOSTRE [escaleno] ]
    ]
  ]
FIM
CLASSIFICA 1 2 5
CLASSIFICA 3 4 5
```

</details>

---

## Aula 7 - PARACADA: contando com uma variável

### 🔥 Aquecimento (3 min)

Conte de 1 a 10, depois de 10 a 1, e depois só os números pares até 20.
Qual regra muda em cada contagem? (Onde começa, onde termina e de quanto
em quanto pula.)

### 💡 Ideia nova (5 min)

`REPCOUNT` só conta de 1 em 1. O `PARACADA` deixa **você** escolher o nome
da variável, de onde ela começa, onde termina e (se quiser) o passo:

```
PARACADA :i DE 1 ATE 10 [ MOSTRE :i ]

PARACADA :i DE 10 ATE 1 PASSO -1 [ MOSTRE :i ]    ; contagem regressiva

PARACADA :i DE 2 ATE 20 PASSO 2 [ MOSTRE :i ]     ; so os pares
```

### 🛠️ Mão na massa (7 min)

Dá para **acumular** uma conta num laço. A soma de 1 a 10:

<!-- exemplo: intermediario/13_soma_acumulada.logo -->
```logo
FACA "soma 0
PARACADA :i DE 1 ATE 10 [
  FACA "soma :soma + :i
  MOSTRE :soma
]
```

*(Este programa está pronto em [`exemplos/intermediario/13_soma_acumulada.logo`](exemplos/intermediario/13_soma_acumulada.logo).)*

Escreve 1, 3, 6, 10, 15... até 55: são as **somas parciais**. Cada linha
pega o valor antigo da `soma` e acrescenta o `:i` da volta.

### 🎯 Exercícios (5 min)

- **7.1** ⭐ Escreva a contagem de 1 a 10 e depois a contagem regressiva
  de 10 a 0.
- **7.2** ⭐ Escreva os números pares de 2 a 20 e os múltiplos de 5 até 50.
- **7.3** ⭐⭐ Calcule a soma de 1 a 100 (o jovem Gauss fez isso em
  segundos!). Compare com a fórmula `100 * 101 / 2`.
- **7.4** ⭐⭐ Desenhe todos os polígonos de 3 a 10 lados (lado 40), usando
  `PARACADA :n DE 3 ATE 10 [ POLIGONO :n 40 ]`.
- **7.5** ⭐⭐⭐ Calcule `10!` (fatorial de 10: `1 × 2 × 3 × ... × 10`)
  acumulando um **produto** em vez de uma soma.

### 🚀 Desafio extra

Escreva a soma dos **ímpares** de 1 a 99 e compare com `50 * 50`. Que
propriedade matemática é essa?

<details>
<summary>Ver respostas</summary>

**7.1**

```logo
PARACADA :i DE 1 ATE 10 [ MOSTRE :i ]
PARACADA :i DE 10 ATE 0 PASSO -1 [ MOSTRE :i ]
```

**7.2**

```logo
PARACADA :i DE 2 ATE 20 PASSO 2 [ MOSTRE :i ]
PARACADA :i DE 5 ATE 50 PASSO 5 [ MOSTRE :i ]
```

**7.3** 5050 nos dois casos.

```logo
FACA "soma 0
PARACADA :i DE 1 ATE 100 [ FACA "soma :soma + :i ]
MOSTRE :soma
MOSTRE 100 * 101 / 2
```

**7.4**

```logo
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [ PF :TAMANHO PD 360 / :LADOS ]
FIM
PARACADA :n DE 3 ATE 10 [ POLIGONO :n 40 ]
```

**7.5** 3628800.

```logo
FACA "f 1
PARACADA :i DE 1 ATE 10 [ FACA "f :f * :i ]
MOSTRE :f
```

**Desafio:** a soma dos primeiros `n` ímpares é `n × n` (aqui 50 ímpares:
2500).

```logo
FACA "soma 0
PARACADA :i DE 1 ATE 99 PASSO 2 [ FACA "soma :soma + :i ]
MOSTRE :soma
MOSTRE 50 * 50
```

</details>

---

## Aula 8 - Laços dentro de laços: grades e tabelas

### 🔥 Aquecimento (3 min)

Quantos quadradinhos tem uma grade de 3 linhas por 4 colunas? (12.) E uma
de 5 por 5? (25.) Qual é a conta?

### 💡 Ideia nova (5 min)

Um `PARACADA` **dentro** de outro repete em **duas dimensões**: a variável
de fora é a linha, a de dentro é a coluna. Cada volta da linha faz o
laço da coluna rodar inteiro:

```
PARACADA :linha DE 1 ATE 3 [
  PARACADA :coluna DE 1 ATE 4 [
    ...   ; roda 3 x 4 = 12 vezes
  ]
]
```

É a base de tudo que tem linhas e colunas: tabelas, planilhas,
tabuleiros e imagens. Veja
[`exemplos/intermediario/05_paracada_grade.logo`](exemplos/intermediario/05_paracada_grade.logo).

### 🛠️ Mão na massa (7 min)

Uma grade 3 × 3 de quadradinhos, posicionando cada um com `VAIPARA`:

<!-- exemplo: intermediario/14_grade_3x3.logo -->
```logo
PARA QUADRADINHO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

PARACADA :linha DE 0 ATE 2 [
  PARACADA :coluna DE 0 ATE 2 [
    LP
    VAIPARA (:coluna * 40 - 60) (:linha * 40 - 60)
    AP
    QUADRADINHO 30
  ]
]
```

*(Este programa está pronto em [`exemplos/intermediario/14_grade_3x3.logo`](exemplos/intermediario/14_grade_3x3.logo).)*

O `40` é o espaçamento entre os quadradinhos (30 de lado + 10 de folga).

### 🎯 Exercícios (5 min)

- **8.1** ⭐ Faça uma grade de 4 linhas por 6 colunas.
- **8.2** ⭐ Escreva as combinações da tabuada de multiplicar de 1 a 5
  (25 linhas), com `MOSTRE :linha * :coluna`.
- **8.3** ⭐⭐ Faça uma **pirâmide**: linha 1 com 1 quadradinho, linha 2
  com 2, ... linha 5 com 5. Dica: o laço da coluna vai `ATE :linha`.
- **8.4** ⭐⭐ Faça uma grade de **hexágonos** (lado 15), 3 por 4.
- **8.5** ⭐⭐⭐ Faça um **tabuleiro** 6 × 6 em que as cores dos quadradinhos
  alternam (azul e vermelho), como num tabuleiro de damas. Dica: a cor
  depende de `(:linha + :coluna) % 2`.

### 🚀 Desafio extra

Desenhe a **tabuada em tabela**: um tabuleiro 9 × 9 (sem desenhar
números) cujas células ficam azuis quando `:linha * :coluna` é par e
vermelhas quando é ímpar. Que padrão aparece?

<details>
<summary>Ver respostas</summary>

**8.1**

```logo
PARA QUADRADINHO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARACADA :linha DE 0 ATE 3 [
  PARACADA :coluna DE 0 ATE 5 [
    LP
    VAIPARA (:coluna * 40 - 100) (:linha * 40 - 70)
    AP
    QUADRADINHO 30
  ]
]
```

**8.2**

```logo
PARACADA :linha DE 1 ATE 5 [
  PARACADA :coluna DE 1 ATE 5 [
    MOSTRE :linha * :coluna
  ]
]
```

**8.3**

```logo
PARA QUADRADINHO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARACADA :linha DE 1 ATE 5 [
  PARACADA :coluna DE 1 ATE :linha [
    LP
    VAIPARA (:coluna * 35 - 100) (100 - :linha * 35)
    AP
    QUADRADINHO 30
  ]
]
```

**8.4**

```logo
PARA HEXAGONO :LADO
  REPITA 6 [ PF :LADO PD 60 ]
FIM
PARACADA :linha DE 0 ATE 2 [
  PARACADA :coluna DE 0 ATE 3 [
    LP
    VAIPARA (:coluna * 40 - 60) (:linha * 40 - 40)
    AP
    HEXAGONO 15
  ]
]
```

**8.5**

```logo
PARA QUADRADINHO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARACADA :linha DE 0 ATE 5 [
  PARACADA :coluna DE 0 ATE 5 [
    LP
    VAIPARA (:coluna * 30 - 90) (:linha * 30 - 90)
    AP
    SE ((:linha + :coluna) % 2) = 0 [ COR "azul ] [ COR "vermelho ]
    QUADRADINHO 30
  ]
]
```

**Desafio:** o produto é ímpar só quando **os dois** fatores são ímpares
(ímpar × ímpar = ímpar); o resto é par. Aparece um padrão de "xadrez" de
vermelhos nas posições ímpar-ímpar.

```logo
PARA QUADRADINHO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM
PARACADA :linha DE 1 ATE 9 [
  PARACADA :coluna DE 1 ATE 9 [
    LP
    VAIPARA (:coluna * 25 - 150) (:linha * 25 - 150)
    AP
    SE ((:linha * :coluna) % 2) = 0 [ COR "azul ] [ COR "vermelho ]
    QUADRADINHO 25
  ]
]
```

</details>

---

## Aula 9 - Gráficos de barras: desenhando números

### 🔥 Aquecimento (3 min)

Um gráfico de barras serve para quê? (Comparar números com o olho.) Em
que ele é melhor do que uma lista de números?

### 💡 Ideia nova (5 min)

Com procedimentos, parâmetros e laços, você escreve seu próprio
"programa de gráficos". A peça-chave é uma `BARRA` cuja altura depende de
um número:

```
PARA BARRA :ALTURA
  PF :ALTURA     ; sobe
  PT :ALTURA     ; desce de volta
  PD 90
  PF 20          ; anda para a proxima barra
  PE 90
FIM
```

Com `ESPESSURA 8` a linha vira uma barra grossa. Agora a tabuada em
gráfico: a barra `i` tem altura `i × fator`, e crescem sempre do mesmo
tanto (uma sequência em "escada"). Veja também
[`exemplos/intermediario/04_tabuada_grafico.logo`](exemplos/intermediario/04_tabuada_grafico.logo).

### 🛠️ Mão na massa (7 min)

<!-- exemplo: intermediario/15_tabuada_comparada.logo -->
```logo
PARA BARRA :ALTURA
  PF :ALTURA
  PT :ALTURA
  PD 90
  PF 20
  PE 90
FIM

PARA TABUADA :FATOR :X
  LP
  VAIPARA :X -120
  DEFINARUMO 0
  AP
  ESPESSURA 8
  REPITA 10 [
    MOSTRE REPCOUNT * :FATOR
    BARRA REPCOUNT * :FATOR * 3
  ]
  ESPESSURA 1
FIM

COR "azul
TABUADA 3 -200
COR "vermelho
TABUADA 6 20
```

*(Este programa está pronto em [`exemplos/intermediario/15_tabuada_comparada.logo`](exemplos/intermediario/15_tabuada_comparada.logo).)*

Dois gráficos lado a lado: qual cresce mais rápido? Quanto a barra
vermelha da última coluna é maior que a azul? (Exatamente o dobro: o
fator é o dobro.)

### 🎯 Exercícios (5 min)

- **9.1** ⭐ Rode `TABUADA 7 -100` sozinho, em verde.
- **9.2** ⭐ Troque o `* 3` por `* 2`. O que muda na altura (e no gráfico)?
- **9.3** ⭐⭐ Desenhe o gráfico dos **quadrados perfeitos** de 1 a 10
  (altura `REPCOUNT * REPCOUNT * 2`).
- **9.4** ⭐⭐ Desenhe um **eixo** (uma linha horizontal fina) por baixo dos
  gráficos da Mão na massa.
- **9.5** ⭐⭐⭐ **Dados reais:** as vendas de 5 meses foram 30, 55, 40, 80 e
  65. Desenhe as 5 barras (altura = vendas × 2), calcule a **média** (soma
  ÷ 5) com `MOSTRE`, e desenhe uma **linha vermelha** na altura da média.

### 🚀 Desafio extra

Acrescente ao gráfico das vendas uma **linha de tendência** ligando o
topo da primeira barra ao topo da última. Ela sobe ou desce?

<details>
<summary>Ver respostas</summary>

**9.1**

```logo
PARA BARRA :ALTURA
  PF :ALTURA
  PT :ALTURA
  PD 90
  PF 20
  PE 90
FIM
PARA TABUADA :FATOR :X
  LP
  VAIPARA :X -120
  DEFINARUMO 0
  AP
  ESPESSURA 8
  REPITA 10 [
    MOSTRE REPCOUNT * :FATOR
    BARRA REPCOUNT * :FATOR * 3
  ]
  ESPESSURA 1
FIM
COR "verde
TABUADA 7 -100
```

**9.2** As barras ficam 2/3 do tamanho (a "escala" muda; a forma do
gráfico, não).

**9.3**

```logo
PARA BARRA :ALTURA
  PF :ALTURA
  PT :ALTURA
  PD 90
  PF 20
  PE 90
FIM
LP
VAIPARA -100 -120
DEFINARUMO 0
AP
ESPESSURA 8
COR "roxo
REPITA 10 [ BARRA REPCOUNT * REPCOUNT * 2 ]
```

**9.4**

```logo
LP
VAIPARA -210 -120
DEFINARUMO 90
AP
COR "preto
PF 480
```

**9.5** Soma = 270, média = 54.

```logo
PARA BARRA :VALOR
  PF :VALOR * 2
  PT :VALOR * 2
  PD 90
  PF 20
  PE 90
FIM
LP
VAIPARA -100 -100
DEFINARUMO 0
AP
ESPESSURA 8
COR "azul
BARRA 30
BARRA 55
BARRA 40
BARRA 80
BARRA 65
ESPESSURA 1
FACA "soma 30 + 55 + 40 + 80 + 65
FACA "media :soma / 5
MOSTRE :soma
MOSTRE :media
COR "vermelho
LP
VAIPARA -110 (-100 + :media * 2)
AP
VAIPARA 10 (-100 + :media * 2)
```

**Desafio:** a linha sobe (de 30 para 65), mesmo que a série oscile.

```logo
PARA BARRA :VALOR
  PF :VALOR * 2
  PT :VALOR * 2
  PD 90
  PF 20
  PE 90
FIM
LP
VAIPARA -100 -100
DEFINARUMO 0
AP
ESPESSURA 8
COR "azul
BARRA 30
BARRA 55
BARRA 40
BARRA 80
BARRA 65
ESPESSURA 2
COR "verde
LP
VAIPARA -100 -40
AP
VAIPARA 0 30
```

</details>

---

## Aula 10 - Projeto final: a minha cidade

### 🔥 Aquecimento (3 min)

Revisão-relâmpago:

1. Para que serve `PARA ... FIM`? (criar um comando novo)
2. Qual a diferença entre `:LADO` num `PARA` e `:lado` criado com `FACA`?
   (o primeiro é parâmetro, só existe naquele comando; o segundo é uma
   variável guardada)
3. Quantas voltas dá um `PARACADA :i DE 2 ATE 20 PASSO 2`? (10)
4. Como o Logo decide entre dois caminhos? (`SE`)

### 💡 Ideia nova (5 min)

Hoje você junta **tudo**: procedimentos com parâmetros, laços aninhados
(para as janelas), `SE` e cores. A regra de ouro é a mesma da Aula 4:
**planeje primeiro**.

```
CIDADE = CHAO + PREDIO (varios, de tamanhos diferentes) + SOL
PREDIO = RETANGULO + JANELAS (grade de quadradinhos, com PARACADA aninhado)
```

### 🛠️ Mão na massa (7 min)

<!-- exemplo: intermediario/16_cidade.logo -->
```logo
PARA QUADRADO :LADO
  REPITA 4 [ PF :LADO PD 90 ]
FIM

PARA PREDIO :X :LARGURA :ANDARES
  LP
  VAIPARA :X -100
  DEFINARUMO 0
  AP
  REPITA 2 [ PF :ANDARES * 30 PD 90 PF :LARGURA PD 90 ]
  PARACADA :andar DE 1 ATE :ANDARES [
    PARACADA :j DE 1 ATE :LARGURA / 30 [
      LP
      VAIPARA (:X + :j * 30 - 20) (-100 + :andar * 30 - 22)
      DEFINARUMO 0
      AP
      QUADRADO 10
    ]
  ]
FIM

PARA SOL
  LP
  VAIPARA 150 120
  DEFINARUMO 270
  AP
  REPITA 36 [ PF 4 PD 10 ]
FIM

PARA CHAO
  LP
  VAIPARA -250 -100
  DEFINARUMO 90
  AP
  PF 500
FIM

COR "preto
CHAO
COR "azul
PREDIO -200 60 3
COR "vermelho
PREDIO -120 90 5
COR "verde
PREDIO -10 60 4
COR "roxo
PREDIO 70 60 2
COR "dourado
SOL
```

*(Este programa está pronto em [`exemplos/intermediario/16_cidade.logo`](exemplos/intermediario/16_cidade.logo).)*

Experimente trocar o número de andares e a largura dos prédios (a
largura deve ser múltipla de 30 para as janelas encaixarem).

### 🎯 Exercícios (5 min)

**Projeto:** escolha **um** e faça (planeje antes, no papel!):

- **10.1** ⭐ Acrescente `NUVEM` (dois círculos juntinhos) e `ARVORE` à cidade.
- **10.2** ⭐⭐ Uma **vila**: 5 casas (Aula 4), cada uma com uma cor
  diferente escolhida por `SE`/`REPCOUNT`, e uma rua.
- **10.3** ⭐⭐⭐ Um **parque**: um gramado (grade de quadradinhos
  verdes), um lago (polígono de muitos lados), caminhos (linhas) e
  árvores espalhadas (`ARVORE` chamada em várias posições).

**Checklist de autoavaliação:** ✅ usei pelo menos 3 procedimentos,
✅ pelo menos um tem parâmetro, ✅ usei um laço aninhado ou um `SE`,
✅ usei `COR`, ✅ expliquei a um adulto como o programa está dividido.

### 🚀 Desafio extra

Faça os prédios com alturas e cores escolhidas **por regra** (por
exemplo, o andar mais alto fica no centro e as cores alternam com `SE`).

<details>
<summary>Ver uma resposta para 10.1</summary>

```logo
PARA NUVEM :X :Y
  LP
  VAIPARA :X :Y
  DEFINARUMO 270
  AP
  REPITA 36 [ PF 2 PD 10 ]
  LP
  PD 90
  PF 12
  PE 90
  AP
  REPITA 36 [ PF 3 PD 10 ]
FIM
PARA RETANGULO :BASE :ALTURA
  REPITA 2 [ PF :ALTURA PD 90 PF :BASE PD 90 ]
FIM
PARA POLIGONO :LADOS :TAMANHO
  REPITA :LADOS [ PF :TAMANHO PD 360 / :LADOS ]
FIM
PARA ARVORE :X
  LP
  VAIPARA :X -100
  DEFINARUMO 0
  AP
  COR "marrom
  RETANGULO 10 30
  COR "verde
  LP
  PF 49
  PE 90
  PF 14
  PD 90
  AP
  POLIGONO 12 10
FIM
COR "cinza
NUVEM -150 100
NUVEM 40 130
ARVORE 190
ARVORE 230
```

</details>

---

## O que você aprendeu

- Criar **procedimentos** (`PARA`/`FIM`) com e sem **parâmetros**:
  abstração e reaproveitamento.
- Guardar e atualizar valores com **variáveis** (`FACA`) e calcular
  (perímetro, área, somas, produtos).
- **Planejar** um desenho decompondo-o em partes.
- Estrelas e o papel do **salto** (e do divisor comum).
- Decidir com `SE`/senão, par ou ímpar, `=`, `<`, `>`, `<>`.
- Repetir com `PARACADA` (passo, contagem regressiva, acumuladores) e
  com laços **aninhados** (grades, tabelas, tabuleiros).
- Desenhar **gráficos de barras** a partir de números e calcular uma
  média.

## Pronto para a próxima trilha?

Na [Trilha 3 - Avançado](trilha-3-avancado.md) você vai aprender funções
que **devolvem** valores (`DEVOLVA`), o Teorema de Pitágoras, círculos
e o número π, o laço `ENQUANTO`, `QUEBRA`/`CONTINUA`, **recursão** e
fractais de verdade.
