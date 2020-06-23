import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

df_pacientes = pd.read_csv("datos_pacientes3.csv", encoding="utf-8", sep=";")
print(df_pacientes)

print(df_pacientes.loc[df_pacientes["RUT"].str.contains("-J")])