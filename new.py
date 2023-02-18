import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect("""
password=postgres dbname=postgres user=postgres port=38746 host=localhost
""", cursor_factory=RealDictCursor)
connection.autocommit = True
cursor = connection.cursor()



title = input('Введите название экипровки: ')
color = input('Введите цвет экипровки: ')

cursor.execute(f"update equipment set title = '{title}', color = '{color}' where id = '{id}' returning id")
res = cursor.fetchall()
print(res)

