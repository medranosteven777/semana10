import pandas as pd 

# Este data set contiene informacion de ventas de videojuegos en todo el mundo
# Las tablas principales son, nombre del juego, plataforma, año de lanzamiento, genero, editor y ventas en diferentes regiones.
# https://www.kaggle.com/datasets/gregorut/videogamesales

df = pd.read_csv('vgsales.csv') 

print("Primeros 5 datos son:") 
print(df.head(5))

print("Informacion general:")
print( df.info()) 
 
print("Estadistica de los datos:")
print(df.describe()) 

print("el numero de filas y columnas es: ")
print(df.shape)

print(f"Total de valores nulos en cada columna: ")
print(df.isnull().sum())
print(f"Total de filas duplicadas: {df.duplicated().sum()}")

"""
Que puedo deducir de esta inspeccion?
La mayoria de datos estan completos, pero hay algunos valores nulos en la columna Year,
lo que puede afectar el analisis de ventas por año.

No hay filas duplicadas, lo que es bueno para la integridad de los datos.
"""

columnasSeleccionadas = df[['Name', 'Platform', 'Genre', 'Global_Sales']]
print(columnasSeleccionadas)

juegoPopulares = df[(df['Genre'] == 'Shooter') & (df['Global_Sales'] > 20)][['Name', 'Platform', 'Global_Sales']]
print("Shooters con más de 20 millones de ventas")
print(juegoPopulares)

"""
Que conclusiones obtienes al aplicar estos filtros?
En este caso vemos que solo un juego del genero Shooter ha vendido mas 
de 20 millones de copias 
"""

ventasPromedio = df.groupby('Genre')['Global_Sales'].mean()
print("Ventas promedio por genero:")
print(ventasPromedio)

correlacion = df['NA_Sales'].corr(df['Global_Sales'])
print(f"Correlación (Ventas Norteamérica vs Globales): {correlacion}")

"""
tinene una relación positiva fuerte, significa que si un juego tiene muchas ventas en Norteamérica
es probable que también tenga muchas ventas globales.
"""

