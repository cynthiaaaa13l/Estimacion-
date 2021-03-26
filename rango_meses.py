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
max = fronteras.groupby(fronteras["Date"].dt.strftime("%m"))["Value"].max()
min = fronteras.groupby(fronteras["Date"].dt.strftime("%m"))["Value"].min()
rango = (max + min) / 2
rango_meses = rango.to_numpy()
nombre_meses = ["Mes 1","Mes 2","Mes 3","Mes 4","Mes 5","Mes 6","Mes 7","Mes 8","Mes 9","Mes 10","Mes 11","Mes 12","Total"]
max_total = fronteras["Value"].max()
min_total = fronteras["Value"].min()
rango_total = (max_total + min_total) / 2
total = np.append(rango_meses, rango_total)
plt.bar(nombre_meses, total)
plt.show()