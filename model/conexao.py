import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'banco.db')

class Conexao:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row  # retorna dicionários
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome  TEXT    NOT NULL,
                email TEXT    NOT NULL,
                curso TEXT    NOT NULL
            )
        """)
        self.conn.commit()

    def fechar(self):
        self.conn.close()
