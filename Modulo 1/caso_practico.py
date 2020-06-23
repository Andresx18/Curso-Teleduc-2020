import pandas as pd

df_pacientes = pd.read_csv("datos_pacientes.csv", encoding="latin-1", sep=";")

df_pacientes["Reajuste"] = df_pacientes["Monto_Deuda"] * 1.03

print(df_pacientes.describe())

df_pacientes.to_csv("datos_pacientes_reajustados.csv", sep=";", index=False)