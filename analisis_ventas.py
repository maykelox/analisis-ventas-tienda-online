# Paso 1: Importar la librería pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paso 2: Cargar el archivo CSV
df = pd.read_csv('ventas_tienda_online.csv')

# Paso 3: Mostrar las primeras filas
print(df.head())

# Paso 4: Mostrar información general de la tabla
print(df.info())

#---------------------------------------------------------------------------------------------------------------------

# Ver la cantidad de ventas por producto
ventas_por_producto = df.groupby('Producto').agg({
    'Cantidad': 'sum',
    'Precio': 'mean'
}).reset_index()

# Agregar una columna con el total de ventas (Cantidad * Precio)
ventas_por_producto['Total Ventas'] = ventas_por_producto['Cantidad'] * ventas_por_producto['Precio']

# Mostrar las primeras filas
print("Ventas por Producto:")
print(ventas_por_producto.sort_values(by='Total Ventas', ascending=False).head())

#---------------------------------------------------------------------------------------------------------------------

# Ventas totales por región
ventas_por_region = df.groupby('Región').agg({
    'Cantidad': 'sum',
    'Precio': 'mean'
}).reset_index()

# Agregar columna Total Ventas por región
ventas_por_region['Total Ventas'] = ventas_por_region['Cantidad'] * ventas_por_region['Precio']

# Mostrar resultados
print("\nVentas por Región:")
print(ventas_por_region)

#---------------------------------------------------------------------------------------------------------------------

# Convertir la columna 'Fecha' a formato de fecha
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Crear una nueva columna con el mes y el año de la venta
df['Mes_Año'] = df['Fecha'].dt.to_period('M')

# Ventas totales por mes
ventas_por_mes = df.groupby('Mes_Año').agg({
    'Cantidad': 'sum',
    'Precio': 'mean'
}).reset_index()

# Agregar columna de Total Ventas por mes
ventas_por_mes['Total Ventas'] = ventas_por_mes['Cantidad'] * ventas_por_mes['Precio']

# Mostrar resultados
print("\nVentas por Mes:")
print(ventas_por_mes.sort_values(by='Total Ventas', ascending=False))

#---------------------------------------------------------------------------------------------------------------------


# Configurar estilo de gráficos
sns.set(style="whitegrid")

# **Gráfico 1: Ventas por Producto**
plt.figure(figsize=(10, 6))
sns.barplot(x='Total Ventas', y='Producto', data=ventas_por_producto.sort_values(by='Total Ventas', ascending=True))
plt.title('Ventas Totales por Producto')
plt.xlabel('Total Ventas')
plt.ylabel('Producto')
plt.show()

# **Gráfico 2: Ventas por Región**
plt.figure(figsize=(10, 6))
sns.barplot(x='Total Ventas', y='Región', data=ventas_por_region.sort_values(by='Total Ventas', ascending=True))
plt.title('Ventas Totales por Región')
plt.xlabel('Total Ventas')
plt.ylabel('Región')
plt.show()

# **Gráfico 3: Ventas por Mes**
plt.figure(figsize=(10, 6))
sns.lineplot(x='Mes_Año', y='Total Ventas', data=ventas_por_mes, marker='o')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes-Año')
plt.ylabel('Total Ventas')
plt.xticks(rotation=45)
plt.show()
