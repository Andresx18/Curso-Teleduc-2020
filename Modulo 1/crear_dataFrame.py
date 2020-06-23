import pandas as pd
data = [["Felipe", 24, "Masculino", 4.5], ["Andres", 21, "Femenino", 7.0],
         ["Tomas", 21, "Masculino", 6.1], ["Roberto", 20, "Masculino", 5.5]]

df = pd.DataFrame(data, columns=["Nombre", "Edad", "Genero", "Calificacion"])

df = df.rename(columns={"Age":"Edad"})

print(df.dtypes)


