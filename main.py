import pandas as pd
from dashboard import Dashboard
from graficas import Graficas

class Menu:
    def __init__(self):
        # Cargar CSV y crear Dashboard
        self.df = pd.read_csv("practicas_panda/ventas_musica_cop .csv")
        self.dashboard = Dashboard(self.df)

    def mostrar(self):
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Mostrar Dashboard Completo")
        print("2. Salir")
        print("====================================")

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = input(" Selecciona una opción: ").strip()

            if opcion == "1":
                print("Mostrando dashboard...")
            
                ingresos_plataforma = self.dashboard.ingresos_por_plataforma()
                ingresos_genero = self.dashboard.ingresos_por_genero()
                plataformas_mas_usada = self.dashboard.plataformas_mas_usadas()
                genero_ventas = self.dashboard.ventas_por_genero()
                genero_top, valor_top = self.dashboard.genero_top()

                # Mostrar tablas en terminal
                print("===== INGRESOS POR PLATAFORMA =====")
                print(ingresos_plataforma)
                print("===== INGRESOS POR GÉNERO =====")
                print(ingresos_genero)
                print("===== PLATAFORMAS MÁS USADAS =====")
                print(plataformas_mas_usada.to_list())
                print("===== VENTAS POR GÉNERO =====")
                print(genero_ventas)
                print(f"\nEl género más vendido según ingresos: {genero_top} con {valor_top} COP\n")

                # Mostrar gráficas
                Graficas.grafica_completa(ingresos_plataforma, ingresos_genero, plataformas_mas_usada, genero_ventas)

            elif opcion == "2":
                print("Saliendo del programa")
                break

            else:
                print(" Opción inválida. Por favor, ingresa 1 o 2.")


if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()