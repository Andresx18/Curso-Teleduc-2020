import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df_pacientes = pd.read_csv("datos_pacientes.csv", encoding="latin-1", sep=";")
print(df_pacientes.head(10))

#1
lista_montos = []
for index, row in df_pacientes.iterrows():
    Monto_Dolar = row["Monto_Deuda"]/700
    lista_montos.append(Monto_Dolar)

print(lista_montos[0:10])

#2
print(df_pacientes["Nombre"].str[0:10])

#3
df_pacientes["Nombre"] = df_pacientes["Nombre"].str.upper()
print(df_pacientes.head())

#4
print(df_pacientes.loc[df_pacientes["Nombre"].str.contains("Ñ")])

#5
df_pacientes2 = pd.read_csv("datos_pacientes2.csv", encoding="latin-1", sep=";")
print(df_pacientes2)

#6
print(df_pacientes2)
df_pacientes2 = df_pacientes2.loc[~(df_pacientes2["RUT"].str.contains("XXXX")) & ~(df_pacientes2["Nombre"].str.contains("XXXX"))]
print(df_pacientes2)