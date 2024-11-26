from typing import Optional
from models.usuario_model import Usuario
from sql.usuario_sql import *
from util.db import obter_conexao


class UsuarioRepo:
    @staticmethod
    def criar_tabela():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @staticmethod
    def inserir(usuario: Usuario) -> Optional[Usuario]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(
                SQL_INSERIR,
                (
                    usuario.nome,
                    usuario.data_nascimento,
                    usuario.email,
                    usuario.telefone,
                    usuario.senha,
                    usuario.perfil,
                ),
            )
            if cursor.rowcount == 0:
                return None
            usuario.id = cursor.lastrowid
            return usuario

    @staticmethod
    def obter_senha_por_email(email: str) -> Optional[str]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_SENHA_POR_EMAIL, (email,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return dados["senha"]

    @staticmethod
    def obter_dados_por_email(email: str) -> Optional[Usuario]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_DADOS_POR_EMAIL, (email,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return Usuario(**dados)
        
    @staticmethod
    def obter_por_id(id: int) -> Optional[Usuario]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_POR_ID, (id,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return Usuario(**dados)

    @staticmethod
    def atualizar_dados(usuario: Usuario) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(
                SQL_ATUALIZAR_DADOS,
                (
                    usuario.nome,
                    usuario.data_nascimento,
                    usuario.email,
                    usuario.telefone,
                    usuario.id,
                ),
            )
            if cursor.rowcount == 0:
                return False
            return True

    @staticmethod
    def atualizar_senha(id: int, senha: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ATUALIZAR_SENHA, (senha, id))
            return cursor.rowcount > 0    

    @staticmethod
    def excluir(id: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_EXCLUIR, (id,))
            return cursor.rowcount > 0