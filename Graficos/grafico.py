import pandas as pd
import matplotlib.pyplot as plt


data =  pd.read_csv('Graficos/vendas.csv')
data['Mes'] = pd.to_datetime(data['Mes'])
vendas_por_mes = data.groupby(data['Mes'])
print(vendas_por_mes['Vendas'].sum())

# data['Mes'] = pd.to_datetime(data['Mes'])
# vendas_por_mes = data.groupby(data['Vendas'].dt.to_period('M')).sum()


plt.figure(figsize=(10, 5))
# plt.plot(vendas_por_mes.index.astype(str), vendas_por_mes['Vendas'], marker='o')
plt.title('Vendas Totais por Mês')
plt.xlabel('Mês')
plt.ylabel('Número de Vendas')
plt.grid(True)
plt.show()