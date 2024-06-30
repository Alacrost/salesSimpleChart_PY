import os

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_database = os.getenv('DB_DATABASE')

print(f"DB_USER: {db_user}")
print(f"DB_PASSWORD: {db_password}")
print(f"DB_HOST: {db_host}")
print(f"DB_PORT: {db_port}")
print(f"DB_DATABASE: {db_database}")
