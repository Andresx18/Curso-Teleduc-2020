import pandas as pd
import numpy as np

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_column", 12)

print("Actividad 1")
detalle_boletas = pd.read_csv("detalle_boletas.csv", encoding="latin-1", sep=",")
print(detalle_boletas)
print("\n")

print("Actividad 2")
del detalle_boletas["Precio_prod"]
print(detalle_boletas)

detalle_boletas["Pais_Venta"] = "CHILE"
print(detalle_boletas)

detalle_boletas = detalle_boletas.rename(columns={"NXXX" : "Num Boleta"})
print(detalle_boletas)

print(detalle_boletas["Fecha"].str.contains("!"))
print(detalle_boletas["Fecha"].str.contains("{"))
print(detalle_boletas["Fecha"].str.contains("-"))
print(detalle_boletas["Fecha"].str.contains("."))
print(detalle_boletas["Fecha"].str.contains("_"))

detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("!", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("{", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("-", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace(".", "")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("_", "")
print(detalle_boletas)
print("\n")

print("Actividad 3")
detalle_boletas = detalle_boletas.set_index("Num Boleta")
detalle_boletas = detalle_boletas.drop("55417XXXXXXX", axis=0)
print(detalle_boletas)

detalle_boletas = detalle_boletas.set_index("ID")
detalle_boletas = detalle_boletas.drop("4XXXXX", axis=0)
detalle_boletas.reset_index(inplace=True)
print(detalle_boletas)
print("\n")


print("Actividad 4")
print(detalle_boletas.pivot_table(index="ID", values="Cantidad", aggfunc={np.mean, np.std, np. min, np.max}))
print("\n")

print("Actividad 5")
df_aux = detalle_boletas["Fecha"].str.split("/", expand=True)
df_aux.columns = ["ANHO", "MES", "DIA"]
detalle_boletas = detalle_boletas.join(df_aux)
del detalle_boletas["Fecha"]

print(detalle_boletas)
print(detalle_boletas.dtypes)
print("\n")

print("Actividad 6")
lista_productos = pd.read_csv("Lista productos.csv", encoding="utf-8", sep=",")
print(lista_productos)
print("\n")

print("Actividad 7")
print(detalle_boletas.dtypes)
detalle_boletas["ID"] = detalle_boletas["ID"].astype("int64")
print(detalle_boletas.dtypes)
print(lista_productos.dtypes)
detalle_boletas2 = detalle_boletas.merge(lista_productos, on="ID")
print(detalle_boletas2)
print("\n")

print("Actividad 8")
detalle_boletas2["Ingreso Total"] = detalle_boletas2["Precio Unitario"] * detalle_boletas2["Cantidad"]
print(detalle_boletas2)
print("\n")

print("Actividad 9")
print(detalle_boletas2.pivot_table(index="ID", values="Ingreso Total", aggfunc={np.mean, np.std, np. min, np.max, np.sum}))