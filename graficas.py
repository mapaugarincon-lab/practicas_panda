import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class Graficas:
    @staticmethod
    def grafica_completa(ingresos_plataforma, ingresos_genero, plataformas_mas_usada, genero_ventas):
        plt.figure(figsize=(16, 8))


        plt.subplot(2, 2, 1)
        plt.bar(ingresos_plataforma.index, ingresos_plataforma.values, color='violet')
        plt.title("Ingresos por Plataforma")
        plt.xticks(rotation=90)

        plt.subplot(2, 2, 2)
        plt.bar(ingresos_genero.index, ingresos_genero.values, color='lightcoral')
        plt.title("Ingresos por Género")
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 3)
        plt.bar(genero_ventas.index, genero_ventas.values, color='pink')
        plt.title("Ventas por Género")
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 4)
        counts = plataformas_mas_usada.value_counts()
        plt.bar(counts.index, counts.values, color='purple')
        plt.title("Cantidad de Ventas por Plataforma")
        plt.xticks(rotation=90)

        plt.tight_layout()
        plt.show()

def grafica_barras(ingresos_plataforma):
        Q1 = np.percentile(ingresos_plataforma.values , 25)
        Q2 = np.percentile(ingresos_plataforma.values , 50)
        Q3 = np.percentile(ingresos_plataforma.values , 75)

        plt.figure(figsize=(7, 5))
        sns.kdeplot(ingresos_plataforma.values, fill=True, color='skyblue')
        plt.axvline(Q1, color='green', linestyle='--', label=f'Q1 = {Q1:.0f}')
        plt.axvline(Q2, color='blue', linestyle='--', label=f'Q2 = {Q2:.0f}')
        plt.axvline(Q3, color='red', linestyle='--', label=f'Q3 = {Q3:.0f}')
        plt.title("Distribución de Ingresos por Plataforma con Cuartiles")
        plt.xlabel("Ingreso Total COP")
        plt.ylabel("Densidad")
        plt.legend()
        plt.show()
def grafica_cuartiles(genero_ventas):
        Q1 = np.percentile(genero_ventas.values , 25)
        Q2 = np.percentile(genero_ventas.values , 50) 
        Q3 = np.percentile(genero_ventas.values , 75)

        plt.figure(figsize=(7 , 4))
        sns.kdeplot(genero_ventas.values , fill=True , color='green')
        plt.axvline(Q1, color='black', linestyle='--', label=f'Q1 = {Q1:.0f}')
        plt.axvline(Q2, color='darkblue', linestyle='--', label=f'Q2 = {Q2:.0f}')
        plt.axvline(Q3, color='yellow', linestyle='--', label=f'Q3 = {Q3:.0f}')
        plt.title("Ingresos por genero")
        plt.xlabel("Ingresos Total COP")
        plt.ylabel("Densidad")
        plt.legend()
        plt.show()


