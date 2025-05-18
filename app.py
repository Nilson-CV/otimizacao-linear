# app.py
import streamlit as st
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np

st.title("🔧 Otimização Linear: Produção com Recursos Limitados")

# Entradas do usuário (interativas)
lucro_A = st.slider("Lucro por produto A (€)", 10, 100, 40)
lucro_B = st.slider("Lucro por produto B (€)", 10, 100, 30)

máquina_disp = st.slider("Horas de máquina disponíveis", 50, 200, 100)
mão_obra_disp = st.slider("Horas de mão de obra disponíveis", 50, 200, 80)

# Coeficientes do problema
c = [-lucro_A, -lucro_B]  # Negativo porque linprog faz minimização

A = [
    [2, 1],  # máquina
    [1, 2]   # mão de obra
]

b = [máquina_disp, mão_obra_disp]

# Restrições: x >= 0, y >= 0
x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if res.success:
    x, y = res.x
    st.success(f"📈 Produzir {x:.2f} unidades de A e {y:.2f} de B")
    st.info(f"💰 Lucro total: {-(res.fun):.2f} €")
else:
    st.error("❌ Problema sem solução")

# Visualização do espaço de soluções
st.subheader("📉 Espaço de Soluções Factíveis")

x_vals = np.linspace(0, 100, 500)
y1 = (máquina_disp - 2 * x_vals) / 1
y2 = (mão_obra_disp - 1 * x_vals) / 2

plt.figure(figsize=(6, 5))
plt.plot(x_vals, y1, label="Máquina")
plt.plot(x_vals, y2, label="Mão de obra")
plt.fill_between(x_vals, 0, np.minimum(y1, y2), where=(np.minimum(y1, y2) >= 0), alpha=0.3)
plt.xlim(0, max(x_vals))
plt.ylim(0, max(np.nanmax(y1), np.nanmax(y2)))
plt.xlabel("Produto A")
plt.ylabel("Produto B")
plt.legend()
plt.grid(True)
st.pyplot(plt)
