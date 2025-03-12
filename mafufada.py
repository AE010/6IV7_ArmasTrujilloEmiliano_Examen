import pandas as pandas
import matplotlib.pyplot as plotter

data = pandas.read_csv('./housing.csv')

columnas = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 
            'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

def calcular_estadisticas(columna):
    columna = pandas.Series(columna)
    return pandas.DataFrame([columna.mean(), columna.median(), columna.mode().iloc[0], columna.std(), columna.max()-columna.min(), columna.var()], 
                            index=['Media', 'Moda', 'Mediana', 'Desviación Estándar', 'Rango', 'Varianza'])

for i in range(0, len(columnas)):
    print("Medidas estadísticas de la columna:", columnas[i], "\n", calcular_estadisticas(data[columnas[i]]))

plotter.bar(data['population'][:10000], data['median_house_value'][:10000], width=500)

plotter.xlabel('Population')
plotter.ylabel('House Value')
plotter.title('Population and House Value')

plotter.show()

