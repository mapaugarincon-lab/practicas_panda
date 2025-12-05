from graficas import Graficas, grafica_barras, grafica_cuartiles
import pandas as pd

df = pd.read_csv("ventas_musica_cop.csv")
ingresos_plataforma = df.groupby('Plataforma')['Ingreso_Total_COP'].sum()
ingresos_genero = df.groupby('Genero')['Ingreso_Total_COP'].sum()
plataformas_mas_usada = df['Plataforma']
genero_ventas = df.groupby('Genero')['Cantidad_Ventas'].sum()

def menu():
    while True:
        print("Menú ")
        print("1. Gráficas de barras completas")
        print("2. Curva de cuartiles (Ingresos por Plataforma)")
        print("3. Curva de cuartiles (Ventas por Género)")
        print("4. Salir")

        opcion = input("Elige una opción : ")

        if opcion == "1":
            Graficas.grafica_completa(ingresos_plataforma, ingresos_genero, plataformas_mas_usada, genero_ventas)
        elif opcion == "2":
            grafica_barras(ingresos_plataforma)
        elif opcion == "3":
            grafica_cuartiles(genero_ventas)
        elif opcion == "4":
            print("¡Saliendo del programa!")
 
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
