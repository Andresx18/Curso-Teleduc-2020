import pandas as pd

desired_width=320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df = pd.read_csv("clientes.csv", encoding="latin-1", sep=";")
print(df.dtypes)

df = df.set_index("RUT")
print(df.iloc[0:3])


df = df.drop(df.iloc[100:103].index)
print(df)
