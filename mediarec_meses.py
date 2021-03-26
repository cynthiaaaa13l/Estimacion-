import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
fronteras = pd.read_csv("fronteras.csv")
measure = fronteras["Measure"] == "Pedestrians"
fronteras = fronteras[measure]
lugar = fronteras["Port Name"] == "Brownsville"
fronteras = fronteras[lugar]
fronteras["Date"] = pd.to_datetime(fronteras["Date"])
años = (fronteras["Date"] >= '01/01/2015 00:00:00') & (fronteras["Date"] <= '12/01/2019 00:00:00')
fronteras = fronteras[años]
suma_meses = fronteras.groupby(fronteras["Date"].dt.strftime("%m"))["Value"].sum()
max = fronteras.groupby(fronteras["Date"].dt.strftime("%m"))["Value"].max()
min = fronteras.groupby(fronteras["Date"].dt.strftime("%m"))["Value"].min()
media_rec = (suma_meses - (max + min)) / 3
media = media_rec.to_numpy()
valores = fronteras["Value"].to_numpy()
ordenados = sorted(valores)
restar_valores = list()
i = 0
while i in range(6):
    restar_valores.append(ordenados[i])
    restar_valores.append(ordenados[(len(ordenados)-1) - i])
    i = i + 1
suma1 = sum(ordenados)
suma2 = sum(restar_valores)
nombre_meses = ["Mes 1","Mes 2","Mes 3","Mes 4","Mes 5","Mes 6","Mes 7","Mes 8","Mes 9","Mes 10","Mes 11","Mes 12","Total"]
total = np.append(media, (suma1 - suma2) / 48)
plt.bar(nombre_meses, total)
plt.show()