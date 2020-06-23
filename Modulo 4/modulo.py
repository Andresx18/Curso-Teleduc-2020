import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df = pd.read_csv("ejemplo.csv", encoding="latin-1", sep=";")

"""print(df.loc[(df["Monto"] > 5000000) & (df["Monto"] < 7000000)])
print(df.loc[(df["Monto"] < 1000000) | (df["Monto"] > 9000000)])

print(df.loc[df["Nombre"].str.split(" ", expand=True)[0] == "Daniela"])

print(df.loc[(df["Nombre"].str.split(" ", expand=True)[0] == "Daniela") & (df["Monto"] < 1000000) & (df["RUT"].str[-1:] == "8")])

df = df.sort_values(by=["Sexo", "Monto"], ascending=False)
print(df)

df2 = pd.read_csv("ejemplo2.csv", encoding="latin-1", sep=";")
df2 = df2.pivot(index="RUT", columns="BANCO", values="MONTO")
print(df2)"""

import numpy as np

df2 = pd.read_csv("ejemplo2.csv", encoding="latin-1", sep=";")
df2 = df2.pivot_table(index="BANCO", values="MONTO", columns="SEXO", aggfunc={np.mean, np.min, np.max})
print(df2)
