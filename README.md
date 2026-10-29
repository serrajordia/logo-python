# Logo em Python

Um pequeno interpretador da linguagem Logo (comandos em português) para
ensinar geometria e programação desenhando com uma tartaruga. Sem
dependências além do Python padrão (usa o módulo `turtle`).

Além dos comandos clássicos do Logo (`PF`, `PD`, `REPITA`, `PARA`/`FIM`...),
tem elementos de linguagens de programação "de verdade": laços `PARACADA`
(for) e `ENQUANTO` (while), `QUEBRA`/`CONTINUA` (break/continue), e funções
que devolvem valor (`DEVOLVA`).

## Início rápido

Sem instalar nada: abra a **[versão web](https://serrajordia.github.io/logo-python/web/)**
(roda no navegador). A tartaruga aparece desenhando em tempo real, e o
controle 🐢—🐇 ajusta a velocidade (**∞** desenha tudo de uma vez).

No computador:

```
python logo.py                                        # modo interativo
python logo.py exemplos\basico\01_quadrado.logo        # roda um exemplo pronto
```

## Como aprender

São três trilhas, cada uma com **10 aulas de 20 minutos** (aquecimento,
ideia nova, mão na massa e exercícios ⭐ → ⭐⭐⭐ com respostas):

1. **[Trilha 1 - Básico](trilha-1-basico.md)** — sequência de comandos,
   ângulos, polígonos, o laço `REPITA`, cores, tabuada com `MOSTRE`,
   coordenadas.
2. **[Trilha 2 - Intermediário](trilha-2-intermediario.md)** — procedimentos
   com parâmetros, variáveis, `SE`, o laço `PARACADA` (inclusive aninhado),
   planejamento (decompor um desenho complicado em partes menores) e
   gráficos de barras.
3. **[Trilha 3 - Avançado](trilha-3-avancado.md)** — funções com `DEVOLVA`,
   Pitágoras, círculos e π, `ENQUANTO`, `QUEBRA`/`CONTINUA`, recursão,
   fractais e gráficos de funções.

Veja o **[TUTORIAL.md](TUTORIAL.md)** para as instruções de instalação e
uma tabela de referência com todos os comandos.

## Arquivos

- [`logo.py`](logo.py) — o interpretador.
- [`exemplos/`](exemplos) — 47 programas prontos, organizados em
  [`basico/`](exemplos/basico), [`intermediario/`](exemplos/intermediario)
  e [`avancado/`](exemplos/avancado), na mesma ordem das trilhas.
- [`web/`](web) — a versão que roda no navegador (Pyodide).
- [`TUTORIAL.md`](TUTORIAL.md) — instalação e referência rápida de comandos.
- `trilha-1-basico.md`, `trilha-2-intermediario.md`, `trilha-3-avancado.md`
  — as três trilhas de aprendizado.
