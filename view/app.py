from flask import Flask, render_template, request, redirect, url_for, flash
from controller.crud import AlunoController
import sys, os

# permite importar model/controller de qualquer diretório
sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "senai-mvc-2026"

ctrl = AlunoController()

# ── LISTAR ──────────────────────────────────────────────────
@app.route("/")
def index():
    alunos = ctrl.listar()
    return render_template("index.html", alunos=alunos)

# ── INSERIR ─────────────────────────────────────────────────
@app.route("/inserir", methods=["POST"])
def inserir():
    nome  = request.form.get("nome", "")
    email = request.form.get("email", "")
    curso = request.form.get("curso", "")
    resultado = ctrl.inserir(nome, email, curso)
    flash(resultado["mensagem"], "success" if resultado["ok"] else "danger")
    return redirect(url_for("index"))

# ── EDITAR (formulário) ──────────────────────────────────────
@app.route("/editar/<int:aluno_id>")
def editar(aluno_id):
    aluno = ctrl.buscar_por_id(aluno_id)
    if not aluno:
        flash("Aluno não encontrado.", "danger")
        return redirect(url_for("index"))
    return render_template("editar.html", aluno=aluno)

# ── ALTERAR (salvar) ─────────────────────────────────────────
@app.route("/alterar/<int:aluno_id>", methods=["POST"])
def alterar(aluno_id):
    nome  = request.form.get("nome", "")
    email = request.form.get("email", "")
    curso = request.form.get("curso", "")
    resultado = ctrl.alterar(aluno_id, nome, email, curso)
    flash(resultado["mensagem"], "success" if resultado["ok"] else "danger")
    return redirect(url_for("index"))

# ── EXCLUIR ──────────────────────────────────────────────────
@app.route("/excluir/<int:aluno_id>", methods=["POST"])
def excluir(aluno_id):
    resultado = ctrl.excluir(aluno_id)
    flash(resultado["mensagem"], "success" if resultado["ok"] else "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
