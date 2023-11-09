import pyodbc

DRIVER = 'ODBC Driver 18 for SQL Server'
SERVER = 'localhost'
DATABASE = 'ApresentacaoSQLServer'
USERNAME = 'sa'
PASSWORD = 'adm123'

connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};Trusted_Connection=yes;Encrypt=no'

conn = pyodbc.connect(connectionString)

cursor = conn.cursor()


# Inserindo valores no banco de dados

# string_sql = """
#    INSERT INTO usuarios VALUES('Gabriel dos Santos Avelino',
#    '2004-04-26',
#    'Rei do Truco')
# """

# cursor.execute(string_sql)
# conn.commit()


# Atualizar informações do banco de dados

# string_sql = """
#    UPDATE usuarios SET data_nascimento = '2004-09-20' WHERE usuario_id = 2 ;
# """
# cursor.execute(string_sql)
# conn.commit()


# Remover informações do banco de dados

string_sql = """
    DELETE usuarios WHERE nome_usuario = 'Gabriel dos Santos Avelino';
"""
cursor.execute(string_sql)
conn.commit()


# Lendo valores do banco de dados e trazendo como uma lista de tuplas

string_sql = """
    SELECT * FROM usuarios;
"""

cursor.execute(string_sql)
# print(cursor.fetchall())  # Escrever tudo na mesma linha

for p in cursor.fetchall():
    print(f'''Código: {p[0]:<10}
Nome: {p[1]:<10}
Data:{p[2]:<10}
Apelido: {p[3]:<10}''')  # Um usuário por linha
    print()
