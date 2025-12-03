import pandas as pd
import matplotlib.pyplot as plt

class Dashboard:
    def __init__(self, dataframe):
        self.df = dataframe

    def grafica_completa(self):
        ingresos_plataforma = self.df.groupby("Plataforma")["Ingreso_Total_COP"].sum()
        ingresos_genero = self.df.groupby("Genero")["Ingreso_Total_COP"].sum()

        print("===== INGRESOS POR PLATAFORMA =====")
        print(ingresos_plataforma)

        print("===== INGRESOS POR GÉNERO =====")
        print(ingresos_genero)

        genero_top = ingresos_genero.idxmax()
        valor_top = ingresos_genero.max()

        print(f" El género más vendido fue: {genero_top} con {valor_top} COP\n")


        plt.figure(figsize=(14, 6))

        plt.subplot(1, 2, 1)
        plt.bar(ingresos_plataforma.index, ingresos_plataforma.values, color='skyblue')
        plt.title("Ingresos por Plataforma")
        plt.xticks(rotation=90)

        plt.subplot(1, 2, 2)
        plt.bar(ingresos_genero.index, ingresos_genero.values, color='orange')
        plt.title("Ingresos por Género")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


df = pd.read_csv("practicas_panda/ventas_musica_cop (1).csv")

dashboard = Dashboard(df)
dashboard.grafica_completa()




