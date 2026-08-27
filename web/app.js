// Logo em Python - versao web
// Roda o mesmo logo.py do desktop dentro do navegador via Pyodide, desenhando
// num <canvas> atraves de web/turtle_canvas.py.

const EXEMPLOS = {
  "basico": [
    "01_quadrado", "02_poligonos_diretos", "03_espiral", "04_cores",
  ],
  "intermediario": [
    "01_poligono_funcao", "02_estrela", "03_casa", "04_tabuada_grafico",
    "05_paracada_grade", "06_condicionais",
  ],
  "avancado": [
    "01_arvore_recursiva", "02_circulo_pi", "03_circulos_concentricos",
    "04_pitagoras", "05_fatorial_fibonacci", "06_quebra_continua",
    "07_enquanto_crescente", "08_floco_de_neve", "09_tabuleiro",
  ],
};

const consoleEl = document.getElementById("console");
const entradaEl = document.getElementById("entrada");
const loadingOverlay = document.getElementById("loading-overlay");
const loadingText = document.getElementById("loading-text");

let pyodide = null;
let logoModulo = null;
let interp = null;
let buffer = "";

function logLinha(texto, classe) {
  const div = document.createElement("div");
  if (classe) div.className = classe;
  div.textContent = texto;
  consoleEl.appendChild(div);
  consoleEl.scrollTop = consoleEl.scrollHeight;
}

function nomeBonito(slug) {
  return slug.replace(/^\d+_/, "").replaceAll("_", " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

function montarListaExemplos() {
  const container = document.getElementById("lista-exemplos");
  container.innerHTML = "";
  for (const trilha of Object.keys(EXEMPLOS)) {
    const titulo = document.createElement("div");
    titulo.className = "grupo-titulo";
    titulo.textContent = trilha;
    container.appendChild(titulo);
    for (const slug of EXEMPLOS[trilha]) {
      const btn = document.createElement("button");
      btn.textContent = nomeBonito(slug);
      btn.addEventListener("click", () => carregarExemplo(trilha, slug));
      container.appendChild(btn);
    }
  }
}

async function carregarExemplo(trilha, slug) {
  try {
    const resp = await fetch(`../exemplos/${trilha}/${slug}.logo`);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const texto = await resp.text();
    entradaEl.value = texto;
    entradaEl.focus();
  } catch (e) {
    logLinha(`Nao consegui carregar o exemplo: ${e}`, "linha-erro");
  }
}

function ativarTab(nome) {
  document.querySelectorAll(".tab-btn").forEach((b) => {
    b.classList.toggle("active", b.dataset.tab === nome);
  });
  document.querySelectorAll(".tab-content").forEach((c) => {
    c.classList.toggle("active", c.id === `tab-${nome}`);
  });
}

function executarBuffer(texto) {
  if (!texto.trim()) return;
  logLinha(texto.split("\n").map((l, i) => (i === 0 ? "logo> " : "...   ") + l).join("\n"), "linha-entrada");
  try {
    interp.run_program(texto);
  } catch (e) {
    logLinha(`Erro interno: ${e}`, "linha-erro");
  }
}

function rodarEntradaAtual() {
  const linha = entradaEl.value;
  entradaEl.value = "";
  buffer += (buffer ? "\n" : "") + linha;
  if (logoModulo.is_buffer_complete(buffer)) {
    executarBuffer(buffer);
    buffer = "";
  }
}

function limparDesenho() {
  interp.run_program("LP OP LT AP");
}

function reiniciarTudo() {
  pyodide.runPython("interp = turtle_canvas.novo_interpretador('logo-canvas')");
  interp = pyodide.globals.get("interp");
  buffer = "";
  entradaEl.value = "";
  consoleEl.innerHTML = "";
  logLinha("(reiniciado)", "linha-saida");
}

async function iniciar() {
  montarListaExemplos();

  document.getElementById("btn-executar").addEventListener("click", rodarEntradaAtual);
  document.getElementById("btn-limpar").addEventListener("click", limparDesenho);
  document.getElementById("btn-reiniciar").addEventListener("click", reiniciarTudo);
  document.getElementById("btn-ajuda").addEventListener("click", () => {
    document.getElementById("help-panel").classList.toggle("escondido");
  });
  document.querySelectorAll(".tab-btn").forEach((b) => {
    b.addEventListener("click", () => ativarTab(b.dataset.tab));
  });

  entradaEl.addEventListener("keydown", (ev) => {
    if (ev.key === "Enter" && !ev.shiftKey) {
      ev.preventDefault();
      rodarEntradaAtual();
    }
  });

  try {
    pyodide = await loadPyodide({
      stdout: (msg) => logLinha(msg, "linha-saida"),
      stderr: (msg) => logLinha(msg, "linha-erro"),
    });

    const [logoSrc, canvasSrc] = await Promise.all([
      fetch("../logo.py").then((r) => r.text()),
      fetch("turtle_canvas.py").then((r) => r.text()),
    ]);
    pyodide.FS.writeFile("logo.py", logoSrc);
    pyodide.FS.writeFile("turtle_canvas.py", canvasSrc);

    pyodide.runPython(
      "import logo\nimport turtle_canvas\ninterp = turtle_canvas.novo_interpretador('logo-canvas')"
    );
    logoModulo = pyodide.globals.get("logo");
    interp = pyodide.globals.get("interp");

    loadingOverlay.remove();
    logLinha("Pronto! Digite um comando Logo ali embaixo e aperte Enter.", "linha-saida");
    entradaEl.focus();
  } catch (e) {
    loadingText.textContent = "Ops, algo deu errado ao carregar o Python no navegador: " + e;
  }
}

iniciar();
