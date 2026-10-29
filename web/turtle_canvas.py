"""
Backend de desenho para a versao web do Logo em Python.

Em vez de abrir uma janela do Tkinter (como o modulo `turtle` padrao),
CanvasTurtle/CanvasScreen implementam exatamente os mesmos metodos que
logo.py chama em self.t / self.screen (a mesma lista que fake_turtle.py,
usado nos testes automatizados, ja cobre) - por isso o interpretador
(logo.py) roda sem nenhuma mudanca, tanto no desktop quanto aqui.

Eles nao desenham nada diretamente: cada movimento vira uma operacao numa
"fita" (lista), entregue ao JavaScript (web/tartaruga.js) quando o programa
termina de rodar (screen.update()). La, a fita e tocada na velocidade
escolhida no controle da pagina, com a tartaruga se movendo; na velocidade
infinita tudo aparece de imediato. O formato das operacoes esta documentado
no cabecalho de tartaruga.js.

Diferencas conhecidas em relacao ao desktop:
- VELOCIDADE, RAPIDO e NORMAL escritos no codigo Logo sao ignorados aqui:
  so o controle de velocidade da pagina manda (senao exemplos que comecam
  com "VELOCIDADE 0" nunca mostrariam a animacao).
- ZOOM usa uma transformacao CSS no proprio <canvas> (mais simples e
  ainda reescala tudo que ja foi desenhado, como o turtle real faz).
"""

import math

import js
from js import document
from pyodide.ffi import to_js


class CanvasScreen:
    def __init__(self, canvas_id="logo-canvas"):
        self.canvas = document.getElementById(canvas_id)
        self._probe_ctx = document.createElement("canvas").getContext("2d")
        self.fila = []  # operacoes ainda nao entregues ao JavaScript

    def emitir(self, *op):
        self.fila.append(op)

    # -- chamados por logo.py -----------------------------------------------

    def title(self, texto):
        pass  # nao ha janela de verdade na web

    def setup(self, width=850, height=650, **kw):
        pass  # o tamanho do canvas e definido pelo HTML/CSS da pagina

    def colormode(self, n):
        pass  # o canvas ja aceita 0-255 diretamente em rgb(...)

    def tracer(self, n):
        pass  # RAPIDO/NORMAL: ignorado na web (ver docstring do modulo)

    def update(self):
        # entrega ao JavaScript tudo o que foi gravado desde a ultima vez
        if self.fila:
            fila, self.fila = self.fila, []
            js.Tartaruga.enfileirar(to_js(fila))

    def setworldcoordinates(self, llx, lly, urx, ury):
        largura_mundo = urx - llx
        zoom = (self.canvas.width / largura_mundo) if largura_mundo else 1.0
        self.emitir("z", zoom)

    def exitonclick(self):
        pass

    def bye(self):
        pass

    # -- uso interno --------------------------------------------------------

    def clear_canvas(self):
        self.emitir("c")

    def cor_valida(self, cor):
        sentinela = "#010203"
        self._probe_ctx.fillStyle = sentinela
        antes = self._probe_ctx.fillStyle
        self._probe_ctx.fillStyle = cor
        depois = self._probe_ctx.fillStyle
        return depois != antes or cor.lower() in ("black", "#000", "#000000")


class CanvasTurtle:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = 0.0, 0.0
        self.heading_ = 90.0  # 0 graus aponta pra cima, como no Logo classico
        self.pen_down = True
        self.color = "black"
        self.width = 1

    # -- movimento ------------------------------------------------------------

    def forward(self, n):
        rad = math.radians(self.heading_)
        self._move_to(self.x + n * math.cos(rad), self.y + n * math.sin(rad))

    def backward(self, n):
        self.forward(-n)

    def right(self, n):
        self.left(-n)

    def left(self, n):
        self.heading_ = (self.heading_ + n) % 360
        if n:
            self.screen.emitir("t", n)

    def goto(self, x, y):
        self._move_to(x, y)

    def setheading(self, n):
        self._girar_para(n)

    def home(self):
        self._move_to(0.0, 0.0)
        self._girar_para(0.0)  # mesmo comportamento do modulo turtle real

    def position(self):
        return (self.x, self.y)

    # -- caneta -----------------------------------------------------------------

    def penup(self):
        self.pen_down = False

    def pendown(self):
        self.pen_down = True

    def pensize(self, n=None):
        if n is not None:
            self.width = n

    def pencolor(self, *args):
        if len(args) == 1:
            cor = args[0]
            if not self.screen.cor_valida(cor):
                raise ValueError(f"cor invalida: {cor}")
            self.color = cor
        elif len(args) == 3:
            r, g, b = args
            self.color = f"rgb({int(r)},{int(g)},{int(b)})"

    def speed(self, n=None):
        pass  # VELOCIDADE: ignorado na web (ver docstring do modulo)

    def showturtle(self):
        self.screen.emitir("s", 1)

    def hideturtle(self):
        self.screen.emitir("s", 0)

    def clear(self):
        self.screen.clear_canvas()

    # -- uso interno --------------------------------------------------------

    def _girar_para(self, n):
        # gira pelo caminho mais curto ate a direcao n (graus, 0 = leste)
        delta = (n - self.heading_ + 180) % 360 - 180
        self.heading_ = n
        if delta:
            self.screen.emitir("t", delta)

    def _move_to(self, nx, ny):
        self.screen.emitir(
            "m", self.x, self.y, nx, ny, 1 if self.pen_down else 0, self.color, self.width
        )
        self.x, self.y = nx, ny


def novo_interpretador(canvas_id="logo-canvas"):
    """Cria um logo.Interpreter pronto para desenhar no <canvas> indicado."""
    import logo
    screen = CanvasScreen(canvas_id)
    t = CanvasTurtle(screen)
    return logo.Interpreter(screen=screen, t=t)
