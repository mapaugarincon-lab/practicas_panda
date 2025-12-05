import pandas as pd
from dashboard import Dashboard
from graficas import Graficas
from estadistica import Estadistica

df = pd.read_csv("practicas_panda/ventas_musica_cop.csv")
df.columns = df.columns.str.strip()

dashboard = Dashboard(df)

while True:
    print(" MENÚ PRINCIPAL ")
    print("1. Ver Dashboard")
    print("2. Estadísticas de una columna")
    print("3. Salir")
    
    
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        ingresos_plataforma = dashboard.ingresos_por_plataforma()
        ingresos_genero = dashboard.ingresos_por_genero()
        plataformas_mas_usada = dashboard.plataformas_mas_usadas()
        genero_ventas = dashboard.ventas_por_genero()
        genero_top, valor_top = dashboard.genero_top()

        print("--- Ingresos por Plataforma ---")
        print(ingresos_plataforma)

        print("--- Ingresos por Género ---")
        print(ingresos_genero)

        print("--- Plataformas más usadas ---")
        print(plataformas_mas_usada.to_list())

        print("--- Ventas por Género ---")
        print(genero_ventas)

        print(f"Género más vendido: {genero_top} ({valor_top} COP)")

        Graficas.grafica_completa(
            ingresos_plataforma,
            ingresos_genero,
            plataformas_mas_usada,
            genero_ventas
        )

    elif opcion == "2":
        
        columnas_numericas = df.select_dtypes(include='number').columns.tolist()
        if not columnas_numericas:
            print(" No hay columnas numéricas en el CSV.")
            continue

        print("Columnas numéricas disponibles:")
        for i, col in enumerate(columnas_numericas):
            print(f"{i+1}. {col}")

        columna_input = input("Elige el número de la columna: ").strip()
        if not columna_input.isdigit():
            print("Opción inválida.")
            continue

        num = int(columna_input) - 1
        if num < 0 or num >= len(columnas_numericas):
            print("Opción inválida.")
            continue

        columna = columnas_numericas[num]
        datos = df[columna]
        est = Estadistica(datos)
        est.mostrar()

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
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
