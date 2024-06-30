import mysql.connector

# Configuração da conexão
config = {
    'user': 'baumer91',
    'password': '123123',
    'host': '127.0.0.1',
}

# Conectar ao servidor MySQL
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Executar o comando para listar os bancos de dados
cursor.execute("SHOW DATABASES")

# Exibir os resultados
for (database,) in cursor:
    print(database)

# Fechar a conexão
cursor.close()
cnx.close()
