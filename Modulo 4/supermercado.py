import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df = pd.read_csv("ventas.csv", encoding="latin-1", sep=";")
print(df.head())
df["FECHA"] = df["FECHA"].str.replace("=", "/")
print(df.head())

df["NUM"] = df["NUM"].str.replace(" ", "")
df["NUM"] = df["NUM"].str.replace(".", "")
df["NUM"] = df["NUM"].str.replace(",", "")
print(df.head())

df2 = pd.read_csv("lista_productos.csv", encoding="utf-8")
print("DF: (ventas.csv)")
print(df.dtypes)
print("DF: (lista_productos.csv)")
print(df2.dtypes)

df2["NUM"] = df2["NUM"].astype(str)

print("DF: (ventas.csv)")
print(df.dtypes)
print("DF: (lista_productos.csv)")
print(df2.dtypes)

df = df.merge(df2, on="NUM")
print(df.head())

print(df.loc[(df["PRECIO"] < 1000) & (df["CANT"] < 5)])

df_aux = df["FECHA"].str.split("/", expand=True)
df_aux.columns = ["ANHO", "MES", "DIA"]
df = df.join(df_aux)
print(df.head())
print(df.loc[(df["PRECIO"] < 1000) & (df["CANT"] < 5) & ((df["MES"] == "4") | (df["MES"] == "5"))])

df["TOTAL"] = df["PRECIO"] * df["CANT"]
print(df.head())

import numpy as np

df3 = df.pivot_table(index="MES", values="TOTAL", columns="CAT", aggfunc={np.mean, np.std, np.min, np.max})
print(df3)

df3.to_csv("reporte_ventas.csv")
df.to_csv("dataframe_reporte_ventas.csv")

print(df3)