import matplotlib.pyplot as plt

class DashboardGraficas:
    """Clase para graficar datos de un DashboardVentas."""

    def __init__(self, dashboard):
        self.dashboard = dashboard

    def graficar_dashboard(self):
        """Genera un dashboard con 2 gráficas: barras por mes y pastel por medio de venta."""
        ventas_mes = self.dashboard.total_por_mes()
        ventas_medio = self.dashboard.total_por_medio()

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

    #Genera un boxplot de los ingresos mostrando cuartiles y outliers con etiquetas.
    def graficar_cuartiles(self):
        ingresos = self.dashboard.obtener_ingresos()
        if ingresos is None:
            print("No hay datos para graficar.")
            return

        # Calcular estadísticos con pandas
        q1 = ingresos.quantile(0.25)
        mediana = ingresos.median()
        q3 = ingresos.quantile(0.75)

        fig, ax = plt.subplots(figsize=(8, 6))

        box = ax.boxplot(ingresos, vert=True, patch_artist=True, labels=["Ingreso_Total_COP"])

        ax.set_title("Boxplot de Ventas - Cuartiles")
        ax.set_ylabel("Ingreso Total (COP)")
        ax.grid(axis="y")

         # Agregar etiquetas con valores calculados
        ax.text(1.05, q1, f"Q1: {q1:,.0f}", va='center', fontsize=10, color='blue')
        ax.text(1.05, mediana, f"Mediana: {mediana:,.0f}", va='center', fontsize=10, color='green')
        ax.text(1.05, q3, f"Q3: {q3:,.0f}", va='center', fontsize=10, color='red')

        plt.show()

