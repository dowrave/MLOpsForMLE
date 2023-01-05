import pandas as pd
import psycopg2

from sklearn.model_selection import train_test_split

db_connect = psycopg2.connect(host = 'localhost', 
        database = 'mydatabase',
        user = 'myuser', 
        password='mypassword')

df =pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 100", db_connect)
print(df.head())
