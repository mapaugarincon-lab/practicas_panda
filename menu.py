from funcion import DashboardVentas
from graficas import graficar_dashboard

if __name__ == "__main__":
    dashboard = DashboardVentas(r"C:\Users\Aprendiz\Videos\pandas\practicas_panda\ventas_musica_cop.csv")
    dashboard.cargar_datos()

    if dashboard.df is not None:
        mes, total = dashboard.mes_mayor_venta()
        print(f"➡ El mes con más ventas fue: {mes} con un total de {total}")

        graficar_dashboard(dashboard)
