# Tutorial de Logo em Python

Este é um pequeno "Logo" (a linguagem clássica de ensino de programação, criada
nos anos 1960) escrito em Python. Você dá comandos para uma tartaruga que
desenha na tela, e no caminho aprende geometria, ângulos, algoritmos e
programação.

Este arquivo cobre só a **instalação** e serve de **referência rápida de
comandos**. Para aprender passo a passo, siga as trilhas:

1. **[Trilha 1 - Básico](trilha-1-basico.md)** - movimento, ângulos, `REPITA`.
2. **[Trilha 2 - Intermediário](trilha-2-intermediario.md)** - procedimentos,
   variáveis, `SE`, `PARACADA`, planejamento.
3. **[Trilha 3 - Avançado](trilha-3-avancado.md)** - recursão, funções
   (`DEVOLVA`), `ENQUANTO`, `QUEBRA`/`CONTINUA`, fractais.

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

**Rodando um arquivo pronto** (os exemplos ficam na pasta `exemplos`, em
subpastas `basico`, `intermediario` e `avancado`):

```
python logo.py exemplos\basico\01_quadrado.logo
```

No modo interativo, digite `SAIR` para encerrar.

## 3. Referência rápida de comandos

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
| `REPITA n [ ... ]` | `REPEAT` | repete o bloco n vezes (trilha 1) |
| `REPCOUNT` | | número da repetição atual dentro do REPITA (trilha 1) |
| `PARA nome :a :b ... / FIM` | `TO` / `END` | define um procedimento (trilha 2) |
| `FACA "nome valor` | `MAKE` | guarda um valor numa variável (trilha 2) |
| `SE condição [ ... ] [ ... ]` | `IF` | executa um bloco se for verdade (segundo bloco = senão) (trilha 2) |
| `PARACADA :v DE a ATE b [PASSO p] [ ... ]` | `FOR` | laço com uma variável `:v` indo de `a` até `b` (trilha 2) |
| `ENQUANTO condição [ ... ]` | `WHILE` | repete enquanto a condição for verdadeira (trilha 3) |
| `QUEBRA` | `BREAK` | sai imediatamente do laço mais interno (trilha 3) |
| `CONTINUA` | `CONTINUE` | pula para a próxima volta do laço (trilha 3) |
| `DEVOLVA valor` | `RETORNE`, `OUTPUT` | sai de um procedimento devolvendo um valor, transformando-o numa função (trilha 3) |
| `SAIA` | `STOP` | sai do procedimento atual sem devolver valor |
| `PARE` | | para o programa inteiro |
| `MOSTRE valor` | `PRINT`, `SHOW` | imprime um número, uma palavra (`MOSTRE "ola`) ou uma frase (`MOSTRE [ola mundo]`) |

Operadores matemáticos nas expressões: `+ - * / %` (`%` é o resto da
divisão) e parênteses `( )` para agrupar contas, por exemplo
`PF (10 + 5) * 2`. Comparações (usadas em `SE`/`ENQUANTO`): `= < > <= >= <>`
(`<>` é "diferente"). Use `RAIZ n` (ou `SQRT n`) para raiz quadrada, por
exemplo `PF 100 * RAIZ 2` anda a diagonal de um quadrado de lado 100.
`PI` vale o número π (3.14159...) — útil para desenhar circunferências,
por exemplo `REPITA 360 [ PF 2 * PI * 100 / 360   PD 1 ]` desenha um
círculo de raio 100.

> **Dica sobre parênteses em chamadas de função:** quando você combina o
> resultado de duas chamadas numa mesma conta (por exemplo,
> `(FIBONACCI :N - 1) + (FIBONACCI :N - 2)`), sempre use parênteses ao
> redor de cada chamada — veja a Trilha 3, Lição 3, para o motivo.

Divirta-se explorando junto com seu filho ou filha!
