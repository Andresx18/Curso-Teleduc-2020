import pandas as pd

desired_width=320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df_consultas = pd.read_csv("consultas.csv", encoding="latin-1", sep=";")
print(df_consultas)

"""cambio de tipo object a datetime de columna Fecha"""
df_consultas["Fecha_Hora_Consulta"] = df_consultas["Fecha_Hora_Consulta"].astype("datetime64")

print(df_consultas.dtypes)

"""consultas size y shape"""
print(df_consultas.size)
print(df_consultas.shape)

"""cambio de index"""
df_consultas = df_consultas.set_index("RUT")
print(df_consultas)

"""consultas head y tail"""
print(df_consultas.head())
print(df_consultas.tail())
print(df_consultas)

"""busqueda de información"""
print(df_consultas.loc["6.079.686-2"])
print(df_consultas.loc["4.367.282-7":"19.500.328-3"])

"""resetea index para localizar por index original"""
df_consultas.reset_index()

"""buscar por indice"""
print(df_consultas.iloc[23])
print(df_consultas.iloc[76:89])

"""cambio nombre de columna"""
df_consultas = df_consultas.rename(columns={"Fecha_Hora_Consulta" : "Fecha_Consulta"})
df_consultas = df_consultas.rename(columns={"RUT2" : "RUT_Medico"})
print(df_consultas)

"""cambio de datos NaN a 10000"""
df_consultas = df_consultas.fillna(10000)
print(df_consultas)

df_consultas2 = pd.read_csv("consultas2.csv", encoding="latin-1", sep=";")
print(df_consultas2)

df_consultas.reset_index()
df_consultas2.reset_index()
print(df_consultas)
print(df_consultas2)