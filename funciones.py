import pandas as pd
import matplotlib.pyplot as plt

class DashboardVentas:
    """Clase completa: carga datos, analiza y genera dashboard."""

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
    
    # GRÁFICOS DEL DASHBOARD
    def graficar_dashboard(self):
        """Genera un dashboard con 2 gráficas."""
        ventas_mes = self.total_por_mes()
        ventas_medio = self.total_por_medio()

        fig, axes = plt.subplots(2, 1, figsize=(10, 8))

        # Gráfico de barras por mes
        axes[0].bar(ventas_mes.index, ventas_mes.values)
        axes[0].set_title("Ventas por Mes")
        axes[0].set_xlabel("Mes")
        axes[0].set_ylabel("Ingreso Total (COP)")

        # Gráfico circular por medio de venta
        axes[1].pie(ventas_medio.values, labels=ventas_medio.index, autopct="%1.1f%%")
        axes[1].set_title("Ventas por Medio de Venta")

        plt.tight_layout()
        plt.show()

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    dashboard = DashboardVentas("C:/Users/FORMACION/Pictures/nikol/practicas_panda/ventas_musica_cop.csv")
    dashboard.cargar_datos()

    if dashboard.df is not None:
        # Mostrar resultados en consola
        mes, total = dashboard.mes_mayor_venta()
        print(f"➡ El mes con más ventas fue: {mes} con un total de {total}")

        # Dibujar dashboard
        dashboard.graficar_dashboard()
