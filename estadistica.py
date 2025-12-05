import pandas as pd

class Estadistica:
    def __init__(self, datos):
  
        self.datos = pd.to_numeric(datos.astype(str).str.replace(',', '').str.strip(), errors='coerce')
        self.datos = self.datos.dropna()

        if len(self.datos) > 0:
            self.promedio = self.datos.mean()
            self.minimo = self.datos.min()
            self.maximo = self.datos.max()
            self.mediana = self.datos.median()
            moda_vals = self.datos.mode()
            self.moda = moda_vals.iloc[0] if not moda_vals.empty else None
            self.desviacion = self.datos.std()
        else:
            self.promedio = self.minimo = self.maximo = None
            self.mediana = self.moda = self.desviacion = None

    def mostrar(self):
        print("--- ESTADÍSTICAS COMPLETAS ---")
        if self.promedio is None:
            print("No hay datos numéricos para mostrar.")
        else:
            print(f"Promedio:        {self.promedio}")
            print(f"Mínimo:          {self.minimo}")
            print(f"Máximo:          {self.maximo}")
            print(f"Mediana:         {self.mediana}")
            print(f"Moda:            {self.moda}")
            print(f"Desviación Std.: {self.desviacion}")
        
