import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df_clientes = pd.read_csv("clientes.csv", encoding="latin-1", sep=";")
print(df_clientes.head(10))

for index, row in df_clientes.iterrows():
    print(row["RUT"])

print(df_clientes["RUT"].str.len())