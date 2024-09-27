import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Ler os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Criar o gráfico de dispersão (scatter plot)
    fig, ax = plt.subplots()
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

    # 3. Criar a primeira linha de ajuste linear (usando todos os dados)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    # Gerar os anos de 1880 até 2050 para o gráfico
    years = pd.Series(range(1880, 2051))
    
    # Plotar a primeira linha de ajuste
    ax.plot(years, intercept + slope * years, 'r', label='First line of best fit')

    # 4. Criar a segunda linha de ajuste linear (usando dados a partir do ano 2000)
    df2 = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    
    # Gerar os anos de 2000 até 2050 para o gráfico
    years2 = pd.Series(range(2000, 2051))
    
    # Plotar a segunda linha de ajuste
    ax.plot(years2, intercept2 + slope2 * years2, 'b', label='Second line of best fit (2000 onwards)')

    # 5. Adicionar rótulos nos eixos e título ao gráfico em inglês
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")

    # 6. Salvar o gráfico e retornar os dados para testes (não modificar esta parte)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
