import pandas as pd

class DashboardVentas:
    """Clase que carga datos, analiza y genera métricas."""

    def __init__(self, ruta_csv):
        self.ruta = ruta_csv
        self.df = None

    # CARGA DEL ARCHIVO
    def cargar_datos(self):
        """Carga el archivo CSV y crea columnas necesarias."""
        try:
            self.df = pd.read_csv(self.ruta)
            print("Archivo CSV cargado correctamente.")

            # Convertir Fecha_Venta a datetime y sacar el mes
            self.df["Fecha_Venta"] = pd.to_datetime(self.df["Fecha_Venta"])
            self.df["Mes"] = self.df["Fecha_Venta"].dt.month

        except Exception as e:
            print("Error al cargar el archivo:", e)

    # ANÁLISIS DE DATOS
    def total_por_mes(self):
        """Retorna ventas totales agrupadas por mes."""
        return self.df.groupby("Mes")["Ingreso_Total_COP"].sum()

    def total_por_medio(self):
        """Retorna ventas totales agrupadas por medio de venta."""
        return self.df.groupby("Medio_Venta")["Ingreso_Total_COP"].sum()

    def mes_mayor_venta(self):
        """Retorna el mes donde más se vendió."""
        totales = self.total_por_mes()
        return totales.idxmax(), totales.max()
