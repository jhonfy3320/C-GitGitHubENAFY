import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(
    dbname="mi_base",
    user="mi_usuario",
    password="mi_contraseña",
    host="localhost",
    port="5432"
)

# Crear un cursor
cur = conn.cursor()

# Ejecutar una consulta
cur.execute("SELECT * FROM mi_tabla LIMIT 5;")

# Obtener resultados
rows = cur.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión
cur.close()
conn.close()
