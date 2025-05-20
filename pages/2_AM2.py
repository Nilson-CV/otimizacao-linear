import streamlit as st

st.set_page_config(page_title="Análise Matemática II", page_icon="📗")


st.title("📗 Análise Matemática II")
st.write("""
Extensão do cálculo para integrais, séries infinitas e funções de várias variáveis.
""")

st.latex(r"\int_a^b f(x)\,dx \quad \text{ e } \quad \sum_{n=1}^\infty a_n")
