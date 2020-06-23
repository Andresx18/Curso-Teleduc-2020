import pandas as pd

df = pd.read_csv("clientes.csv", encoding="latin-1", sep=";")

df["NACIONALIDAD"] = "CHILE"
df.to_csv("clientes_modificado.csv", sep=";", index=False)

print(df)

df = df["PUNTAJE_CREDITICIO"] * 1.1

print(df)

"""print(df.describe())

df["NACIONALIDAD"] = "CHILE"

print(df)

del df["NACIONALIDAD"]

print(df)
df["BONO"] = df["MONTO"]/df["PUNTAJE_CREDITICIO"]

print(df)"""