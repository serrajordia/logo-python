// Logo em Python - animacao da tartaruga na versao web.
//
// O interpretador (logo.py) roda de uma vez so; turtle_canvas.py nao desenha
// nada, apenas grava uma "fita" de operacoes (andar, girar, trocar de cor...)
// e entrega aqui via Tartaruga.enfileirar(). Este modulo toca a fita na
// velocidade escolhida no controle da pagina (1 a 10, ou 11 = infinita, que
// desenha a fita inteira de imediato). Na web, VELOCIDADE/RAPIDO/NORMAL
// escritos no codigo Logo sao ignorados: so o controle da pagina manda.
//
// Formato das operacoes (arrays):
//   ["m", x1, y1, x2, y2, caneta(0/1), cor, espessura]  anda de (x1,y1) a (x2,y2)
//   ["t", graus]                gira (positivo = esquerda)
//   ["c"]                       limpa o desenho
//   ["s", 0/1]                  esconde/mostra a tartaruga
//   ["z", fator]                ZOOM (escala CSS do canvas)

(() => {
  const canvas = document.getElementById("logo-canvas");
  const ctx = canvas.getContext("2d");
  const desenho = document.createElement("canvas");
  desenho.width = canvas.width;
  desenho.height = canvas.height;
  const dctx = desenho.getContext("2d");

  const NIVEL_INFINITO = 11;
  // pixels por segundo para cada nivel de velocidade (1..10)
  const PX_POR_SEG = [0, 40, 80, 140, 220, 340, 500, 800, 1300, 2200, 4000];
  const CUSTO_GRAU = 0.8; // girar 1 grau "custa" 0.8 px de tempo de animacao
  const LIMITE_MS_INSTANTANEO = 40; // fatia de trabalho por quadro no modo infinito

  let fila = [];
  let indice = 0;
  let emAndamento = null; // progresso da operacao atual: {total, feito}
  let nivel = 6;
  let forcar = false; // usado por pular(): desenha de imediato so desta vez
  let estado = { x: 0, y: 0, h: 90, visivel: true };
  let quadroId = null;
  let ultimoTempo = 0;

  const instantaneo = () => forcar || nivel >= NIVEL_INFINITO;
  const temOperacoes = () => indice < fila.length;

  function paraCanvas(x, y) {
    return [canvas.width / 2 + x, canvas.height / 2 - y];
  }

  function riscar(x1, y1, x2, y2, cor, espessura) {
    const [a, b] = paraCanvas(x1, y1);
    const [c, d] = paraCanvas(x2, y2);
    dctx.strokeStyle = cor;
    dctx.lineWidth = espessura;
    dctx.lineCap = "round";
    dctx.beginPath();
    dctx.moveTo(a, b);
    dctx.lineTo(c, d);
    dctx.stroke();
  }

  // Executa operacoes da fita gastando no maximo `orcamento` (em px de
  // animacao) e, se `limiteMs` for dado, parando ao estourar esse tempo.
  function avancar(orcamento, limiteMs) {
    const inicio = performance.now();
    let contador = 0;
    while (temOperacoes()) {
      if (instantaneo()) orcamento = Infinity;
      if (limiteMs && (++contador & 255) === 0 && performance.now() - inicio > limiteMs) return;
      const op = fila[indice];
      switch (op[0]) {
        case "m": {
          const [, x1, y1, x2, y2, caneta, cor, espessura] = op;
          if (!emAndamento) emAndamento = { total: Math.hypot(x2 - x1, y2 - y1), feito: 0 };
          const resta = emAndamento.total - emAndamento.feito;
          const passo = Math.min(resta, orcamento);
          emAndamento.feito += passo;
          const f = emAndamento.total > 0 ? emAndamento.feito / emAndamento.total : 1;
          const nx = emAndamento.feito >= emAndamento.total ? x2 : x1 + (x2 - x1) * f;
          const ny = emAndamento.feito >= emAndamento.total ? y2 : y1 + (y2 - y1) * f;
          if (caneta) riscar(estado.x, estado.y, nx, ny, cor, espessura);
          estado.x = nx;
          estado.y = ny;
          orcamento -= passo;
          if (emAndamento.feito < emAndamento.total) return; // acabou o orcamento
          emAndamento = null;
          indice++;
          break;
        }
        case "t": {
          const graus = op[1];
          if (!emAndamento) emAndamento = { total: Math.abs(graus) * CUSTO_GRAU, feito: 0, aplicado: 0 };
          const resta = emAndamento.total - emAndamento.feito;
          const passo = Math.min(resta, orcamento);
          emAndamento.feito += passo;
          const alvo = emAndamento.total > 0 ? graus * (emAndamento.feito / emAndamento.total) : graus;
          estado.h += alvo - emAndamento.aplicado;
          emAndamento.aplicado = alvo;
          orcamento -= passo;
          if (emAndamento.feito < emAndamento.total) return;
          emAndamento = null;
          indice++;
          break;
        }
        case "c":
          dctx.clearRect(0, 0, desenho.width, desenho.height);
          indice++;
          break;
        case "s":
          estado.visivel = !!op[1];
          indice++;
          break;
        case "z":
          canvas.style.transform = `scale(${op[1]})`;
          indice++;
          break;
        default:
          indice++;
      }
    }
    fila = [];
    indice = 0;
  }

  function desenharTartaruga() {
    const [cx, cy] = paraCanvas(estado.x, estado.y);
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate((-estado.h * Math.PI) / 180); // 0 rad aponta para a direita
    ctx.fillStyle = "#16a34a";
    ctx.strokeStyle = "#14532d";
    ctx.lineWidth = 1.5;
    // patas
    for (const [px, py] of [[-6, -9], [6, -9], [-6, 9], [6, 9]]) {
      ctx.beginPath();
      ctx.ellipse(px, py, 4, 2.5, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    }
    // cabeca (aponta para a frente)
    ctx.beginPath();
    ctx.arc(12, 0, 4.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    // casco
    ctx.beginPath();
    ctx.ellipse(0, 0, 11, 8, 0, 0, Math.PI * 2);
    ctx.fillStyle = "#22c55e";
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }

  function renderizar() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(desenho, 0, 0);
    if (estado.visivel) desenharTartaruga();
  }

  function quadro(agora) {
    quadroId = null;
    const dt = Math.min((agora - ultimoTempo) / 1000, 0.1);
    ultimoTempo = agora;
    if (instantaneo()) avancar(Infinity, LIMITE_MS_INSTANTANEO);
    else avancar(PX_POR_SEG[nivel] * dt, 0);
    renderizar();
    if (temOperacoes()) agendar();
  }

  function agendar() {
    if (quadroId === null) {
      ultimoTempo = performance.now();
      quadroId = requestAnimationFrame(quadro);
    }
  }

  window.Tartaruga = {
    enfileirar(ops) {
      for (const op of ops) fila.push(op);
      agendar();
    },
    // termina de desenhar tudo o que falta, sem animar
    pular() {
      forcar = true;
      avancar(Infinity, 0);
      forcar = false;
      emAndamento = null;
      renderizar();
    },
    // volta tudo ao estado inicial (usado pelo botao Reiniciar)
    reiniciar() {
      fila = [];
      indice = 0;
      emAndamento = null;
      estado = { x: 0, y: 0, h: 90, visivel: true };
      dctx.clearRect(0, 0, desenho.width, desenho.height);
      canvas.style.transform = "";
      renderizar();
    },
    definirNivel(n) {
      nivel = n;
      if (instantaneo() && temOperacoes()) agendar();
    },
    nivel: () => nivel,
    NIVEL_INFINITO,
  };

  renderizar();
})();
