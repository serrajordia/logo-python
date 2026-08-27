"""
Backend de desenho para a versao web do Logo em Python.

Em vez de abrir uma janela do Tkinter (como o modulo `turtle` padrao),
CanvasTurtle/CanvasScreen desenham num <canvas> HTML, usando a ponte
JS do Pyodide. Implementam exatamente os mesmos metodos que logo.py
chama em self.t / self.screen (a mesma lista que fake_turtle.py, usado
nos testes automatizados, ja cobre) - por isso o interpretador
(logo.py) roda sem nenhuma mudanca, tanto no desktop quanto aqui.

Diferencas conhecidas em relacao ao desktop:
- o desenho aparece instantaneo (sem animacao passo a passo); por isso
  VELOCIDADE nao tem efeito visivel aqui.
- ZOOM usa uma transformacao CSS no proprio <canvas> (mais simples e
  ainda reescala tudo que ja foi desenhado, como o turtle real faz).
"""

import math

from js import document


class CanvasScreen:
    def __init__(self, canvas_id="logo-canvas"):
        self.canvas = document.getElementById(canvas_id)
        self.ctx = self.canvas.getContext("2d")
        self._probe_ctx = document.createElement("canvas").getContext("2d")
        self._tracing = True

    # -- chamados por logo.py -----------------------------------------------

    def title(self, texto):
        pass  # nao ha janela de verdade na web

    def setup(self, width=850, height=650, **kw):
        pass  # o tamanho do canvas e definido pelo HTML/CSS da pagina

    def colormode(self, n):
        pass  # o canvas ja aceita 0-255 diretamente em rgb(...)

    def tracer(self, n):
        self._tracing = bool(n)

    def update(self):
        pass  # cada traco ja e desenhado na hora; nada para atualizar em lote

    def setworldcoordinates(self, llx, lly, urx, ury):
        largura_mundo = urx - llx
        zoom = (self.canvas.width / largura_mundo) if largura_mundo else 1.0
        self.canvas.style.transform = f"scale({zoom})"

    def exitonclick(self):
        pass

    def bye(self):
        pass

    # -- uso interno --------------------------------------------------------

    def clear_canvas(self):
        self.ctx.setTransform(1, 0, 0, 1, 0, 0)
        self.ctx.clearRect(0, 0, self.canvas.width, self.canvas.height)

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
        self.heading_ = (self.heading_ - n) % 360

    def left(self, n):
        self.heading_ = (self.heading_ + n) % 360

    def goto(self, x, y):
        self._move_to(x, y)

    def setheading(self, n):
        self.heading_ = n

    def home(self):
        self._move_to(0.0, 0.0)
        self.heading_ = 0.0  # mesmo comportamento do modulo turtle real

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
        pass  # sem animacao passo a passo na web (ver docstring do modulo)

    def showturtle(self):
        pass

    def hideturtle(self):
        pass

    def clear(self):
        self.screen.clear_canvas()

    # -- uso interno --------------------------------------------------------

    def _to_canvas(self, x, y):
        cw, ch = self.screen.canvas.width, self.screen.canvas.height
        return (cw / 2 + x, ch / 2 - y)

    def _move_to(self, nx, ny):
        if self.pen_down:
            x1, y1 = self._to_canvas(self.x, self.y)
            x2, y2 = self._to_canvas(nx, ny)
            ctx = self.screen.ctx
            ctx.strokeStyle = self.color
            ctx.lineWidth = self.width
            ctx.lineCap = "round"
            ctx.beginPath()
            ctx.moveTo(x1, y1)
            ctx.lineTo(x2, y2)
            ctx.stroke()
        self.x, self.y = nx, ny


def novo_interpretador(canvas_id="logo-canvas"):
    """Cria um logo.Interpreter pronto para desenhar no <canvas> indicado."""
    import logo
    screen = CanvasScreen(canvas_id)
    t = CanvasTurtle(screen)
    return logo.Interpreter(screen=screen, t=t)
