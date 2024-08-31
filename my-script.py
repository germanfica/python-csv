import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('settlement-171391315-2024-08-05-163304.csv', delimiter=';')

# Mostrar el DataFrame
print(df)

# Guardar el DataFrame en un nuevo archivo CSV (opcional)
df.to_csv('ruta_al_nuevo_archivo.csv', index=False)
