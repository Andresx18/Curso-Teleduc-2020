import pandas as pd

df = pd.read_csv("clientes.csv", encoding="latin-1", sep=";")

df = df.rename(columns={"FECHA_NAC":"FECHA_NACIMIENTO"})

print(df.dtypes)

print(df.shape)

print(df.size)

print(df.head())

print((df.tail()))

print(df.loc[5])

print(df.loc[5:9])

df = df.set_index("RUT")

print(df.loc["11.170.160-6"])

print(df.loc["11.170.160-6":"15.910.648-9"])

print(df.loc[df["TIPO_CLIENTE"] == "C"])

print(df.iloc[5])

print(df.iloc[5:9])