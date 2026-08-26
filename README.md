# Logo em Python

Um pequeno interpretador da linguagem Logo (comandos em português) para
ensinar geometria e programação desenhando com uma tartaruga. Sem
dependências além do Python padrão (usa o módulo `turtle`).

Além dos comandos clássicos do Logo (`PF`, `PD`, `REPITA`, `PARA`/`FIM`...),
tem elementos de linguagens de programação "de verdade": laços `PARACADA`
(for) e `ENQUANTO` (while), `QUEBRA`/`CONTINUA` (break/continue), e funções
que devolvem valor (`DEVOLVA`).

## Início rápido

```
python logo.py                                        # modo interativo
python logo.py exemplos\basico\01_quadrado.logo        # roda um exemplo pronto
```

## Como aprender

1. **[Trilha 1 - Básico](trilha-1-basico.md)** — sequência de comandos,
   ângulos, polígonos, o laço `REPITA`.
2. **[Trilha 2 - Intermediário](trilha-2-intermediario.md)** — procedimentos
   com parâmetros, variáveis, `SE`, o laço `PARACADA`, planejamento
   (decompor um desenho complicado em partes menores).
3. **[Trilha 3 - Avançado](trilha-3-avancado.md)** — recursão, funções
   com `DEVOLVA`, `ENQUANTO`, `QUEBRA`/`CONTINUA`, círculos, o Teorema de
   Pitágoras, fractais.

Veja o **[TUTORIAL.md](TUTORIAL.md)** para as instruções de instalação e
uma tabela de referência com todos os comandos.

## Arquivos

- [`logo.py`](logo.py) — o interpretador.
- [`exemplos/`](exemplos) — programas prontos, organizados em
  [`basico/`](exemplos/basico), [`intermediario/`](exemplos/intermediario)
  e [`avancado/`](exemplos/avancado), na mesma ordem das trilhas.
- [`TUTORIAL.md`](TUTORIAL.md) — instalação e referência rápida de comandos.
- `trilha-1-basico.md`, `trilha-2-intermediario.md`, `trilha-3-avancado.md`
  — as três trilhas de aprendizado.
