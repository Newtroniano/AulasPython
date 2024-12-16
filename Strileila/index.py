import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Meu Primeiro App com Streamlit')

valor = st.slider('Escolha um valor', 0, 100, 50)

x = np.linspace(0, 10, 100)
y = np.sin(x) * valor

plt.plot(x, y)
plt.title(f'Seno com valor {valor}')
plt.xlabel('X')
plt.ylabel('Y')

st.pyplot(plt)
