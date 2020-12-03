import sqlalchemy # banco de dados
import pandas as pd # analise de dados
import matplotlib.pyplot as plt # criação de gráficos
import numpy as np # manipulação de array e matrizes multidimensionais


# driver utilizado tem que ser instalado nesse caso eu usei: pip install PyMySQL

#dialect+driver://username:password@host:port/database

db_type = 'mysql'
driver = 'pymysql'
user = 'root'
password = ''
host = 'localhost'
port = '3306'
dbname = 'python'

#conn = create_engine(f'{db_type}+{driver}://{user}:{password}@{host}:{port}/{dbname}')

conn = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/python')

sql = 'SELECT * FROM Vendas'
result = conn.execute(sql)
row = result.fetchall()

data = pd.DataFrame(row, columns=['produto', 'valor'])

names = data['produto']
values = data['valor']


fig, axs = plt.subplots(1, 3, figsize=(5, 5), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categoria')
plt.show()






    
    








#print(data)

# criando o gráfico


# encerra a conexão

result.close()












