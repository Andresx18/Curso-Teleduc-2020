import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df = pd.read_csv("ejemplo.csv", encoding="latin-1", sep=";")

for index, row in df.iterrows():
    print(index)
    print(row["Nombre"])

"""for index,row in df.iterrows():
    primer_nombre = row["Nombre"].split(" ")[0]
    print(primer_nombre)"""

print(df["Nombre"].str.len())

"""Extrae un caracter de un string, en este caso el primero"""
print(df["RUT"].str[0])

"""extraer un conjunto de caracteres de un string"""
print(df["RUT"].str[0:4])

"""mostrar columna nombre en minuscula"""
print(df["Nombre"].str.lower())

"""mostrar columna nombre en mayuscula"""
print(df["Nombre"].str.upper())

"""reemplazar datos en columna"""
print(df["Fecha_Nac"].str.replace("/", "-"))

"""revisa si dato contiene"""
print(df["RUT"].str.contains('-'))

"""determina en que posicion esta el string buscado"""
print(df["Nombre"].str.find(" "))

"""funcion split para separar un string"""
print(df["Nombre"].str.split(" "))

"""generar nuevo dataframe a partir de una columna"""
df2 = df["Nombre"].str.split(" ", expand=True)
df2.columns=["Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido"]
df = df.join(df2, rsuffix="_df2", lsuffix="_df")
print(df.dtypes)




