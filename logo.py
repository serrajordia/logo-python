"""
Logo em Python - um pequeno interpretador da linguagem Logo, com comandos
em portugues, feito para ensinar matematica (angulos, geometria, multiplicacao,
sequencias e recursao) desenhando com a tartaruga (turtle).

Como usar:
    python logo.py                 -> abre o modo interativo (REPL)
    python logo.py exemplos\01_quadrado.logo -> executa um arquivo .logo

Veja o TUTORIAL.md para uma introducao passo a passo.
"""

import math
import re
import sys
import turtle


# ---------------------------------------------------------------------------
# Erros e sinais de controle
# ---------------------------------------------------------------------------

class LogoError(Exception):
    """Erro de programa Logo (comando desconhecido, argumento invalido, etc.)."""


class StopProc(Exception):
    """Levantado por SAIA/STOP para sair de um procedimento antes do fim."""


class ProcOutput(Exception):
    """Levantado por DEVOLVA/OUTPUT para sair de um procedimento com um valor."""

    def __init__(self, valor):
        super().__init__()
        self.valor = valor


class BreakLoop(Exception):
    """Levantado por QUEBRA/BREAK para sair do laco mais interno."""


class ContinueLoop(Exception):
    """Levantado por CONTINUA/CONTINUE para pular para a proxima volta do laco."""


class StopProgram(Exception):
    """Levantado por PARE para interromper todo o programa."""


# ---------------------------------------------------------------------------
# Tokenizador
# ---------------------------------------------------------------------------

TOKEN_RE = re.compile(r'''
      \[ | \]
    | \( | \)
    | <= | >= | <>
    | [+\-*/%<>=]
    | :[A-Za-z_][A-Za-z0-9_]*
    | "[^\s\[\]()]*
    | [A-Za-z_][A-Za-z0-9_]*
    | \d+\.\d+
    | \d+
    | [,.!?:;]
''', re.VERBOSE)


def tokenize(text):
    # "-" e ambiguo: pode ser subtracao (10 - 5) ou um numero negativo (-5).
    # Regra (a mesma usada pelo Logo classico): se o "-" tem espaco (ou inicio
    # de linha) antes dele e NENHUM espaco depois, e um sinal de negativo;
    # nesse caso ele vira o token especial NEG, que _unary() trata como "-"
    # mas que o resto do parser nao confunde com o operador de subtracao.
    # Isso permite escrever "VAIPARA -180 -120" (dois numeros) sem ambiguidade.
    tokens = []
    for raw_line in text.splitlines():
        line = raw_line.split(';', 1)[0]  # ; inicia um comentario ate o fim da linha
        for m in TOKEN_RE.finditer(line):
            tok = m.group()
            if tok == '-':
                before_ok = m.start() == 0 or line[m.start() - 1].isspace()
                after_ok = m.end() < len(line) and not line[m.end()].isspace()
                if before_ok and after_ok:
                    tok = 'NEG'
            tokens.append(tok)
    return tokens


class TokenStream:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def has_next(self):
        return self.pos < len(self.tokens)

    def peek(self):
        return self.tokens[self.pos] if self.has_next() else None

    def next(self):
        if not self.has_next():
            raise LogoError("o programa terminou no meio de um comando")
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def expect(self, value):
        tok = self.next()
        if tok != value:
            raise LogoError(f"esperava '{value}' mas encontrei '{tok}'")

    def expect_word(self, palavra):
        tok = self.next()
        if tok.upper() != palavra:
            raise LogoError(f"esperava '{palavra}' mas encontrei '{tok}'")

    def read_bracket_block(self):
        self.expect('[')
        depth = 1
        block = []
        while depth > 0:
            tok = self.next()
            if tok == '[':
                depth += 1
            elif tok == ']':
                depth -= 1
                if depth == 0:
                    break
            block.append(tok)
        return block


# ---------------------------------------------------------------------------
# Nomes de cores em portugues -> nomes que o turtle entende
# ---------------------------------------------------------------------------

CORES = {
    'preto': 'black', 'branco': 'white', 'vermelho': 'red', 'verde': 'green',
    'azul': 'blue', 'amarelo': 'yellow', 'laranja': 'orange', 'roxo': 'purple',
    'rosa': 'pink', 'cinza': 'gray', 'marrom': 'brown', 'ciano': 'cyan',
    'magenta': 'magenta', 'dourado': 'gold', 'prata': 'silver',
}

# comandos aceitos como sinonimos entre si (portugues abreviado + ingles)
_SYNONYMS = {
    'PF': ('PF', 'FORWARD', 'FD'),
    'PT': ('PT', 'BACK', 'BK'),
    'PD': ('PD', 'RIGHT', 'RT'),
    'PE': ('PE', 'LEFT'),
    'LP': ('LP', 'PENUP', 'SUBACANETA'),
    'AP': ('AP', 'PENDOWN', 'ABAIXACANETA', 'ABAIXAPENA'),
    'LT': ('LT', 'CLEARSCREEN', 'LIMPATELA', 'LIMPA', 'CS'),
    'MT': ('MT', 'SHOWTURTLE'),
    'ET': ('ET', 'HIDETURTLE'),
    'OP': ('OP', 'HOME', 'PARAORIGEM'),
}
SYNONYMS = {alias: key for key, aliases in _SYNONYMS.items() for alias in aliases}


# ---------------------------------------------------------------------------
# Interpretador
# ---------------------------------------------------------------------------

class Interpreter:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Logo em Python")
        self.screen.setup(width=850, height=650)
        self.screen.colormode(255)
        self._half_w, self._half_h = 425.0, 325.0  # usado por ZOOM

        self.t = turtle.Turtle()
        self.t.speed(6)
        self.t.setheading(90)  # 0 graus aponta para cima, como no Logo classico

        self.procs = {}          # nome -> (params, corpo_de_tokens)
        self.scopes = [{}]       # pilha de escopos de variaveis; scopes[0] = global
        self.repcount_stack = []
        self.loop_depth = 0      # > 0 enquanto executamos dentro de REPITA/ENQUANTO/PARACADA
        self.proc_depth = 0      # > 0 enquanto executamos dentro de um procedimento (PARA/FIM)

    # -- variaveis ----------------------------------------------------------

    def get_var(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise LogoError(f"a variavel :{name} nao existe")

    def set_var(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return
        self.scopes[0][name] = value

    # -- avaliacao de expressoes numericas -----------------------------------

    def eval_expr(self, stream):
        return self._add(stream)

    def _add(self, stream):
        val = self._mul(stream)
        while stream.peek() in ('+', '-'):
            op = stream.next()
            rhs = self._mul(stream)
            val = val + rhs if op == '+' else val - rhs
        return val

    def _mul(self, stream):
        val = self._unary(stream)
        while stream.peek() in ('*', '/', '%'):
            op = stream.next()
            rhs = self._unary(stream)
            if op == '*':
                val *= rhs
            elif op == '/':
                if rhs == 0:
                    raise LogoError("divisao por zero")
                val /= rhs
            else:
                val %= rhs
        return val

    def _unary(self, stream):
        if stream.peek() in ('-', 'NEG'):
            stream.next()
            return -self._unary(stream)
        if stream.peek() == '+':
            stream.next()
            return self._unary(stream)
        return self._primary(stream)

    def _primary(self, stream):
        if not stream.has_next():
            raise LogoError("esperava um numero, mas o programa terminou")
        tok = stream.next()
        if tok == '(':
            val = self.eval_expr(stream)
            stream.expect(')')
            return val
        if tok.startswith(':'):
            return self.get_var(tok[1:].upper())
        if tok.upper() == 'REPCOUNT':
            if not self.repcount_stack:
                raise LogoError("REPCOUNT so pode ser usado dentro de um REPITA")
            return self.repcount_stack[-1]
        if tok.upper() == 'PI':
            return math.pi
        if tok.upper() in ('RAIZ', 'SQRT'):
            valor = self._unary(stream)
            if valor < 0:
                raise LogoError("RAIZ nao aceita numero negativo")
            return math.sqrt(valor)
        if re.match(r'^\d+\.\d+$', tok):
            return float(tok)
        if re.match(r'^\d+$', tok):
            return int(tok)
        if tok.upper() in self.procs:
            valor = self.run_proc(tok.upper(), stream)
            if valor is None:
                raise LogoError(
                    f"o procedimento {tok} nao devolveu um valor "
                    f"(use DEVOLVA dentro dele para ele funcionar como funcao)"
                )
            return valor
        raise LogoError(f"esperava um numero, encontrei '{tok}'")

    def eval_condition(self, stream):
        left = self.eval_expr(stream)
        op = stream.next()
        right = self.eval_expr(stream)
        if op == '=':
            return left == right
        if op == '<':
            return left < right
        if op == '>':
            return left > right
        if op == '<=':
            return left <= right
        if op == '>=':
            return left >= right
        if op == '<>':
            return left != right
        raise LogoError(f"operador de comparacao invalido: '{op}'")

    # -- execucao -------------------------------------------------------------

    def exec_sequence(self, stream):
        while stream.has_next():
            self.exec_one(stream)

    def exec_one(self, stream):
        tok = stream.next()
        up = SYNONYMS.get(tok.upper(), tok.upper())

        if up == 'PF':
            self.t.forward(self.eval_expr(stream))
        elif up == 'PT':
            self.t.backward(self.eval_expr(stream))
        elif up == 'PD':
            self.t.right(self.eval_expr(stream))
        elif up == 'PE':
            self.t.left(self.eval_expr(stream))
        elif up == 'LP':
            self.t.penup()
        elif up == 'AP':
            self.t.pendown()
        elif up == 'LT':
            self.t.clear()
        elif up == 'MT':
            self.t.showturtle()
        elif up == 'ET':
            self.t.hideturtle()
        elif up == 'OP':
            self.t.home()
        elif up in ('VELOCIDADE', 'SPEED'):
            self.t.speed(self.eval_expr(stream))
        elif up in ('RAPIDO', 'TURBO'):
            self.screen.tracer(0)
        elif up == 'NORMAL':
            self.screen.tracer(1)
            self.screen.update()
        elif up == 'ZOOM':
            self.cmd_zoom(self.eval_expr(stream))
        elif up in ('ESPESSURA', 'SETPENSIZE', 'PENSIZE'):
            self.t.pensize(self.eval_expr(stream))
        elif up in ('VAIPARA', 'SETPOS', 'SETXY'):
            x = self.eval_expr(stream)
            y = self.eval_expr(stream)
            self.t.goto(x, y)
        elif up in ('DEFINARUMO', 'SETHEADING', 'SETH'):
            graus = self.eval_expr(stream)
            self.t.setheading((90 - graus) % 360)
        elif up in ('COR', 'SETCOLOR', 'COLOR'):
            self.cmd_cor(stream)
        elif up in ('MOSTRE', 'PRINT', 'SHOW'):
            self.cmd_mostre(stream)
        elif up in ('REPITA', 'REPEAT'):
            self.cmd_repita(stream)
        elif up in ('ENQUANTO', 'WHILE'):
            self.cmd_enquanto(stream)
        elif up in ('PARACADA', 'FOR'):
            self.cmd_paracada(stream)
        elif up in ('PARA', 'TO'):
            self.cmd_para(stream)
        elif up in ('SE', 'IF'):
            self.cmd_se(stream)
        elif up in ('FACA', 'MAKE'):
            self.cmd_faca(stream)
        elif up in ('SAIA', 'STOP'):
            if self.proc_depth == 0:
                raise LogoError("SAIA so pode ser usado dentro de um procedimento (PARA ... FIM)")
            raise StopProc()
        elif up in ('DEVOLVA', 'RETORNE', 'OUTPUT'):
            if self.proc_depth == 0:
                raise LogoError("DEVOLVA so pode ser usado dentro de um procedimento (PARA ... FIM)")
            raise ProcOutput(self.eval_expr(stream))
        elif up in ('QUEBRA', 'BREAK'):
            if self.loop_depth == 0:
                raise LogoError("QUEBRA so pode ser usado dentro de um REPITA/ENQUANTO/PARACADA")
            raise BreakLoop()
        elif up in ('CONTINUA', 'CONTINUE'):
            if self.loop_depth == 0:
                raise LogoError("CONTINUA so pode ser usado dentro de um REPITA/ENQUANTO/PARACADA")
            raise ContinueLoop()
        elif up == 'PARE':
            raise StopProgram()
        elif up in ('FIM', 'END'):
            raise LogoError("'FIM' sem um 'PARA' correspondente")
        elif up in self.procs:
            self.run_proc(up, stream)
        else:
            raise LogoError(f"nao conheco o comando '{tok}'")

    def cmd_mostre(self, stream):
        tok = stream.peek()
        if tok == '[':
            palavras = stream.read_bracket_block()
            partes = []
            for p in palavras:
                pedaco = p[1:] if p.startswith('"') else p
                if pedaco in (',', '.', '!', '?', ':', ';') and partes:
                    partes[-1] += pedaco
                else:
                    partes.append(pedaco)
            print(' '.join(partes))
            return
        if tok is not None and tok.startswith('"'):
            stream.next()
            print(tok[1:])
            return
        print(self.fmt(self.eval_expr(stream)))

    def cmd_zoom(self, fator):
        if fator <= 0:
            raise LogoError("ZOOM precisa de um numero maior que zero")
        hw = self._half_w / fator
        hh = self._half_h / fator
        self.screen.setworldcoordinates(-hw, -hh, hw, hh)

    def cmd_cor(self, stream):
        tok = stream.peek()
        if tok is not None and (tok[0].isdigit() or tok in ('(', '-')):
            r = self.eval_expr(stream)
            g = self.eval_expr(stream)
            b = self.eval_expr(stream)
            self.t.pencolor(int(r), int(g), int(b))
            return
        nome = stream.next()
        if nome.startswith('"'):
            nome = nome[1:]
        cor = CORES.get(nome.lower(), nome.lower())
        try:
            self.t.pencolor(cor)
        except turtle.TurtleGraphicsError:
            raise LogoError(f"nao conheco a cor '{nome}'")

    def cmd_repita(self, stream):
        count = self.eval_expr(stream)
        block = stream.read_bracket_block()
        self.repcount_stack.append(0)
        self.loop_depth += 1
        try:
            for i in range(1, int(count) + 1):
                self.repcount_stack[-1] = i
                try:
                    self.exec_sequence(TokenStream(block))
                except BreakLoop:
                    break
                except ContinueLoop:
                    continue
        finally:
            self.loop_depth -= 1
            self.repcount_stack.pop()

    MAX_ENQUANTO = 200000  # protege contra ENQUANTO cuja condicao nunca muda

    def cmd_enquanto(self, stream):
        cond_tokens = []
        while stream.peek() != '[':
            if not stream.has_next():
                raise LogoError("ENQUANTO precisa de um bloco [ ... ]")
            cond_tokens.append(stream.next())
        bloco = stream.read_bracket_block()
        self.loop_depth += 1
        try:
            voltas = 0
            while self.eval_condition(TokenStream(cond_tokens)):
                voltas += 1
                if voltas > self.MAX_ENQUANTO:
                    raise LogoError(
                        "ENQUANTO rodou muitas vezes sem parar - a condicao nunca "
                        "fica falsa? (programa interrompido para nao travar)"
                    )
                try:
                    self.exec_sequence(TokenStream(bloco))
                except BreakLoop:
                    break
                except ContinueLoop:
                    continue
        finally:
            self.loop_depth -= 1

    def cmd_paracada(self, stream):
        var_tok = stream.next()
        if not var_tok.startswith(':'):
            raise LogoError("PARACADA espera uma variavel, como :i")
        nome = var_tok[1:].upper()
        stream.expect_word('DE')
        inicio = self.eval_expr(stream)
        stream.expect_word('ATE')
        fim = self.eval_expr(stream)
        passo = 1
        if stream.peek() is not None and stream.peek().upper() == 'PASSO':
            stream.next()
            passo = self.eval_expr(stream)
        if passo == 0:
            raise LogoError("PASSO nao pode ser zero")
        bloco = stream.read_bracket_block()
        self.scopes.append({nome: inicio})
        self.loop_depth += 1
        try:
            valor = inicio
            while (valor <= fim) if passo > 0 else (valor >= fim):
                self.scopes[-1][nome] = valor
                try:
                    self.exec_sequence(TokenStream(bloco))
                except BreakLoop:
                    break
                except ContinueLoop:
                    pass
                valor += passo
        finally:
            self.loop_depth -= 1
            self.scopes.pop()

    def cmd_para(self, stream):
        nome = stream.next()
        params = []
        while stream.peek() and stream.peek().startswith(':'):
            params.append(stream.next()[1:].upper())
        corpo = []
        while True:
            if not stream.has_next():
                raise LogoError(f"o procedimento {nome} nao tem um 'FIM'")
            tok = stream.next()
            if tok.upper() in ('FIM', 'END'):
                break
            corpo.append(tok)
        self.procs[nome.upper()] = (params, corpo)

    def run_proc(self, nome, stream):
        """Chama um procedimento como comando OU como funcao dentro de uma
        expressao; devolve o valor do DEVOLVA, ou None se ele nao devolveu nada."""
        params, corpo = self.procs[nome]
        args = [self.eval_expr(stream) for _ in params]
        self.scopes.append(dict(zip(params, args)))
        self.proc_depth += 1
        try:
            self.exec_sequence(TokenStream(corpo))
            return None
        except StopProc:
            return None
        except ProcOutput as saida:
            return saida.valor
        finally:
            self.proc_depth -= 1
            self.scopes.pop()

    def cmd_se(self, stream):
        cond = self.eval_condition(stream)
        bloco1 = stream.read_bracket_block()
        bloco2 = None
        if stream.peek() == '[':
            bloco2 = stream.read_bracket_block()
        if cond:
            self.exec_sequence(TokenStream(bloco1))
        elif bloco2 is not None:
            self.exec_sequence(TokenStream(bloco2))

    def cmd_faca(self, stream):
        tok = stream.next()
        if not tok.startswith('"'):
            raise LogoError('FACA espera um nome de variavel, como "lado')
        nome = tok[1:].upper()
        valor = self.eval_expr(stream)
        self.set_var(nome, valor)

    # -- utilidades -------------------------------------------------------------

    @staticmethod
    def fmt(v):
        if isinstance(v, float) and v.is_integer():
            return str(int(v))
        return str(v)

    def run_program(self, text):
        stream = TokenStream(tokenize(text))
        try:
            self.exec_sequence(stream)
        except StopProgram:
            pass
        except (StopProc, ProcOutput, BreakLoop, ContinueLoop):
            pass  # ja deveriam ter sido tratados antes; nunca deixa travar o programa
        except LogoError as e:
            print(f"Erro: {e}")
        finally:
            # garante que o desenho aparece mesmo se RAPIDO ficou ligado
            self.screen.update()


# ---------------------------------------------------------------------------
# Modo interativo (REPL) e execucao de arquivos
# ---------------------------------------------------------------------------

def run_repl(interp):
    print("=== Logo em Python - modo interativo ===")
    print("Digite comandos Logo e tecle Enter. Digite SAIR para encerrar.\n")
    buffer = ""
    while True:
        try:
            line = input("...   " if buffer else "logo> ")
        except (EOFError, KeyboardInterrupt):
            break
        if not buffer and line.strip().upper() in ('SAIR', 'EXIT', 'QUIT'):
            break
        buffer += line + "\n"
        toks = tokenize(buffer)
        ups = [t.upper() for t in toks]
        para_bal = ups.count('PARA') + ups.count('TO') - ups.count('FIM') - ups.count('END')
        colch_bal = toks.count('[') - toks.count(']')
        if buffer.strip() and para_bal <= 0 and colch_bal <= 0:
            interp.run_program(buffer)
            buffer = ""
    print("Ate logo!")


def main():
    interp = Interpreter()
    if len(sys.argv) > 1:
        caminho = sys.argv[1]
        with open(caminho, encoding='utf-8') as f:
            texto = f.read()
        interp.run_program(texto)
        print("Pronto! Clique na janela do desenho para fechar.")
        interp.screen.exitonclick()
    else:
        run_repl(interp)


if __name__ == '__main__':
    main()
