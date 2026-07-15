import sqlite3
class Banco:
    def __init__(self, banco = 'mercado.db'):
        self.__banco = banco
        self.criar_tabela()

    def conectar(self):
        return sqlite3.connect(self.__banco)
    
    def criar_tabela(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS produtos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE,
                    preco REAL NOT NULL,
                    estoque INTEGER NOT NULL)
                       """)
        conn.commit()
        conn.close()

    def cadastrar(self, nome, preco, estoque):
        conn = None
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO produtos(nome, preco, estoque) VALUES(?,?,?)",
                (nome, preco, estoque)
                 )
            conn.commit()
            return True
        
        except sqlite3.IntegrityError:
            return False
        
        finally:
            if conn:
                conn.close()



    def listar(self):
        conn = None
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, preco, estoque  FROM produtos")
            return cursor.fetchall()
        finally:
            if conn:
                conn.close()
        

    def buscar(self, id_produto):
        conn = None
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, preco, estoque FROM produtos WHERE id = ?",
                (id_produto,))
            return cursor.fetchone()
        finally:
            if conn:
                conn.close()
        

    def editar(self, id_produto, nome_novo , preco_novo, estoque_novo):
        conn = None
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("""
                        UPDATE produtos
                        SET nome = ?, preco = ?, estoque = ?
                        WHERE id = ?
                        """,
                        (nome_novo, preco_novo, estoque_novo, id_produto))
            if cursor.rowcount == 0:
                return 'o produto não foi encontrado'
            else:
                conn.commit()
                return 'produto editado com sucesso'
        except sqlite3.IntegrityError:
                return 'ja existe um produto com esse nome'
        
        finally:
            if conn:
                conn.close()

    def deletar(self, id_produto):
        conn = None
        try:    
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?",
                    (id_produto,))   
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        finally:
            if conn:
                conn.close()
    
    def buscar_por_nome(self, nome):
        conn = None
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, preco, estoque FROM produtos WHERE nome = ?",
                           (nome,))
            return cursor.fetchall()
        finally:
            if conn:
                conn.close()

    
    def entrada_estoque(self, id_produto, qtd_produto):
        conn = None
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("""
                        UPDATE produtos
                        SET estoque = estoque + ?
                        WHERE id = ?
                           """,
                           (qtd_produto, id_produto))
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        
        finally:
            if conn:
                conn.close()

    
    def vender(self, id_produto, qtd_produto):
        conn = None
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("""
                        UPDATE produtos
                        SET estoque = estoque - ?
                        WHERE id = ? AND estoque >= ?
                           """,
                           (qtd_produto, id_produto, qtd_produto))
            if cursor.rowcount == 0:
                return False
            
            else:
                conn.commit()
                return True
        finally:
            if conn:
                conn.close()

            

        