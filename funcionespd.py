import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas_musica_cop.csv")
class Dashboard ():
    def __init__(self,Plataforma,Cantidad_Ventas,Genero):
        self.Plataforma = Plataforma
        self.Cantidad_Ventas = Cantidad_Ventas
        self.Genero = Genero

Plataformas_mas_usada = df['Plataforma'].mode()
print(Plataformas_mas_usada)

Genero_ventas = df.groupby('Genero')['Cantidad_Ventas'].sum()
print(Genero_ventas)

Genero_ventas.plot(kind='bar' , title=("Ventas por Genero "))
plt.xlabel('Genero')
plt.ylabel('Cantidad_Ventas')
plt.show()