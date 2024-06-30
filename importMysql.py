import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os

db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE')
}

# Conect to DB
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()
query = "SELECT * FROM vendas"
df = pd.read_sql(query, cnx)

# Query
query = "SELECT * FROM vendas"
cursor.execute(query)

# Show Results
for (id, produto_id, cliente_id, data_venda, quantidade, receita) in cursor:
    print(f"{id}, {produto_id}, {cliente_id}, {
          data_venda}, {quantidade}, {receita}")

# End Conection
cursor.close()
cnx.close()
print(df.head())

# Create a sales chart by product
df.groupby('produto_id')['receita'].sum().plot(kind='bar')
plt.xlabel('Produto ID')
plt.ylabel('Receita Total')
plt.title('Receita por Produto')
plt.show()
