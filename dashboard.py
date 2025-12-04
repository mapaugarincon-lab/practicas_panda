import matplotlib.pyplot as plt 
class Dashboard:
    def __init__(self, dataframe):
        self.df = dataframe

    # Métodos para obtener datos
    def ingresos_por_plataforma(self):
        return self.df.groupby("Plataforma")["Ingreso_Total_COP"].sum()

    def ingresos_por_genero(self):
        return self.df.groupby("Genero")["Ingreso_Total_COP"].sum()

    def plataformas_mas_usadas(self):
        return self.df['Plataforma'].mode()

    def ventas_por_genero(self):
        return self.df.groupby('Genero')['Cantidad_Ventas'].sum()

    def genero_top(self):
        ingresos_genero = self.ingresos_por_genero()
        genero_top = ingresos_genero.idxmax()
        valor_top = ingresos_genero.max()
        return genero_top, valor_top

      
      