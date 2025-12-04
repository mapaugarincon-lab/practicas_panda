import matplotlib.pyplot as plt

class Graficas:
    @staticmethod
    def grafica_completa(ingresos_plataforma ,ingresos_genero, plataformas_mas_usada, genero_ventas):
        plt.figure(figsize=(16, 8))

        plt.subplot(2, 2, 1)
        plt.bar(ingresos_plataforma.index, ingresos_plataforma.values, color='violet')
        plt.title("Ingresos por Plataforma")
        plt.xticks(rotation=90)
        
        plt.subplot(2, 2, 2)
        plt.bar(ingresos_genero.index, ingresos_genero.values, color='lightcoral')
        plt.title("Ingresos por Género")
        plt.xticks(rotation=45)

        
        plt.subplot(2, 2, 3)
        plt.bar(genero_ventas.index, genero_ventas.values, color='pink')
        plt.title("Ventas por Género")
        plt.xticks(rotation=45)

        
        plt.subplot(2, 2, 4)
        counts = ingresos_plataforma.copy()  
        counts = counts.index.value_counts() 
        
        plt.bar(plataformas_mas_usada, [1]*len(plataformas_mas_usada), color='purple')  
        plt.title("Cantidad de Ventas por Plataforma")
        plt.xticks(rotation=90)

        plt.tight_layout()
        plt.show()
