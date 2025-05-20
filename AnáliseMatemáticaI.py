import streamlit as st

st.set_page_config(page_title="Análise Matemática I", page_icon="📘")

st.title("📘 Análise Matemática I")
st.write("""
Este curso aborda os conceitos fundamentais de cálculo diferencial em uma variável real,
incluindo limites, continuidade e derivadas.
""")

st.latex(r"\lim_{x \to a} f(x) = L")
