from model.conexao import Conexao

class AlunoController:
    # ── CREATE ──────────────────────────────────────────────
    def inserir(self, nome: str, email: str, curso: str) -> dict:
        db = Conexao()
        try:
            db.cursor.execute(
                "INSERT INTO alunos (nome, email, curso) VALUES (?, ?, ?)",
                (nome.strip(), email.strip(), curso.strip())
            )
            db.conn.commit()
            return {"ok": True, "mensagem": f"Aluno '{nome}' cadastrado com sucesso!"}
        except Exception as e:
            return {"ok": False, "mensagem": str(e)}
        finally:
            db.fechar()

    # ── READ ────────────────────────────────────────────────
    def listar(self) -> list:
        db = Conexao()
        try:
            db.cursor.execute("SELECT * FROM alunos ORDER BY nome")
            return [dict(row) for row in db.cursor.fetchall()]
        finally:
            db.fechar()

    def buscar_por_id(self, aluno_id: int) -> dict | None:
        db = Conexao()
        try:
            db.cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
            row = db.cursor.fetchone()
            return dict(row) if row else None
        finally:
            db.fechar()

    # ── UPDATE ──────────────────────────────────────────────
    def alterar(self, aluno_id: int, nome: str, email: str, curso: str) -> dict:
        db = Conexao()
        try:
            db.cursor.execute(
                "UPDATE alunos SET nome=?, email=?, curso=? WHERE id=?",
                (nome.strip(), email.strip(), curso.strip(), aluno_id)
            )
            db.conn.commit()
            if db.cursor.rowcount == 0:
                return {"ok": False, "mensagem": "Aluno não encontrado."}
            return {"ok": True, "mensagem": f"Aluno atualizado com sucesso!"}
        except Exception as e:
            return {"ok": False, "mensagem": str(e)}
        finally:
            db.fechar()

    # ── DELETE ──────────────────────────────────────────────
    def excluir(self, aluno_id: int) -> dict:
        db = Conexao()
        try:
            db.cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
            db.conn.commit()
            if db.cursor.rowcount == 0:
                return {"ok": False, "mensagem": "Aluno não encontrado."}
            return {"ok": True, "mensagem": "Aluno excluído com sucesso!"}
        except Exception as e:
            return {"ok": False, "mensagem": str(e)}
        finally:
            db.fechar()
