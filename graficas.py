import matplotlib.pyplot as plt

def graficar_dashboard(dashboard):
    """Genera un dashboard con 2 gráficas usando datos de DashboardVentas."""

    ventas_mes = dashboard.total_por_mes()
    ventas_medio = dashboard.total_por_medio()

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

