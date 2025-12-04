from funcion import DashboardVentas
from graficas import DashboardGraficas

def main():
    # Inicializamos el dashboard
    dashboard = DashboardVentas(r"C:\Users\Aprendiz\Videos\pandas\practicas_panda\ventas_musica_cop.csv")
    dashboard.cargar_datos()

    graficas = DashboardGraficas(dashboard)

    if dashboard.df is None:
        print("No se pudieron cargar los datos.")
        return

    while True:
        # Menú de opciones
        print("\n=== Menú de Dashboard de Ventas ===")
        print("1. Mostrar mes con más ventas")
        print("2. Graficar dashboard")
        print("3. Mostrar estadísticas y graficar cuartiles")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mes, total = dashboard.mes_mayor_venta()
            print(f"➡ El mes con más ventas fue: {mes} con un total de {total}")
        elif opcion == "2":
            graficas.graficar_dashboard()
        elif opcion == "3":
            # Mostrar estadísticas
            stats = dashboard.estadisticas_cuartiles()
            print("\n Estadísticas de ventas:")
            for k, v in stats.items():
                print(f"{k}: {v}")
            # Graficar cuartiles
            graficas.graficar_cuartiles()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
