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


from collections import Counter

texto = """
Python es un lenguaje de programación poderoso y fácil de aprender.
Tiene estructuras de datos eficientes y una sintaxis clara.
"""

# Preprocesar el texto
palabras = texto.lower().split()

# Contar las palabras
conteo = Counter(palabras)

# Mostrar las 5 palabras más comunes
for palabra, cantidad in conteo.most_common(5):
    print(f"{palabra}: {cantidad}")
