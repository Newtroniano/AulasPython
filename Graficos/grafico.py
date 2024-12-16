import pandas as pd
import matplotlib.pyplot as plt
import math

# numeros = list(range(1, 37))
# print(len(numeros))

data =  pd.read_csv('Graficos/vendas.csv')
data['Mes'] = pd.to_datetime(data['Mes'])
vendas_por_mes = data.groupby(data['Mes'].dt.to_period('M'))
totalMes= vendas_por_mes['Vendas'].sum()
vendas_por_mes_list = totalMes.to_dict()
df = pd.DataFrame(list(vendas_por_mes_list.items()), columns=['Mes', 'Vendas'])

print(df['Mes'])





# rows = math.ceil(df['Mes']/2)
# for i in range(20):
#     plt.subplot(rows, 2, i+1)
#     plt.plot(df['Mes'].astype(str)[i], df['Vendas'][i])
#     plt.title(f'Gráfico {i + 1}')
#     plt.xlabel('Eixo X')
#     plt.ylabel('Eixo Y')

# plt.figure(1)
# plt.subplot(2,1,1)
# plt.plot(df['Mes'].astype(str), df['Vendas'], marker='o')
# plt.show()


# plt.figure(figsize=(10, 5))
# plt.bar(df['Mes'].astype(str), df['Vendas'])
# plt.show()


# plt.title('Vendas Totais por Mês')
# plt.xlabel('Mes')
# plt.ylabel('Número de Vendas')



# plt.title('Vendas Totais por Mês')
# plt.xlabel('Mês')
# plt.ylabel('Número de Vendas')
# plt.show()

# vendas_por_mes = data.groupby(data['Mes'])


# vendas_por_mes = data.groupby(data['Vendas'].dt.to_period('M')).sum()



# data['Mes'] = pd.to_datetime(data['Mes'])
# vendas_por_mes = data.groupby(data['Vendas'].dt.to_period('M')).sum()
# print(data['Mes'])

# plt.figure(figsize=(10, 5))
# plt.plot(data['Mes'], vendas_por_mes['Vendas'].sum())
# plt.title('Vendas Totais por Mês')
# plt.xlabel('Mês')
# plt.ylabel('Número de Vendas')
# plt.grid(True)
# plt.show()