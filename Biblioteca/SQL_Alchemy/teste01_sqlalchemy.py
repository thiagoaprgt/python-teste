import sqlalchemy


# driver utilizado tem que ser instalado nesse caso eu usei: pip install PyMySQL

#dialect+driver://username:password@host:port/database

db_type = 'mysql'
driver = 'pymysql'
user = 'root'
password = ''
host = 'localhost'
port = '3306'
dbname = 'python'

conn = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/python')

#conn = create_engine(f'{db_type}+{driver}://{user}:{password}@{host}:{port}/{dbname}')

sql = 'SELECT * FROM Vendas'
result = conn.execute(sql)


for row in result:
    print(row)



# encerra a conexão

result.close()





