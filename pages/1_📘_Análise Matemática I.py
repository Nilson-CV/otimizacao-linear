import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import base64

st.set_page_config(page_title="Análise Matemática I", page_icon="📘", layout="wide")

inicio = st.columns(2)

inicio[0] = st.title("📘 Análise Matemática I")
st.success("Este curso aborda os conceitos fundamentais de cálculo diferencial e integral em uma variável real, incluindo limites, continuidade, derivadas, primitivas e integrais. Além disso serão abordos assuntos relacionados com noções topológicas em R, séries e sucessões numéricas e método da indução matemática.", icon="✅")
inicio[1] = st.markdown("""
    <p style="font-size:26px;">
        📬 Para dúvidas ou sugestões, envie e-mail para 
        <a href="mailto:contato@minhaempresa.com">nilsonmat27@gmail.com</a>
    </p>
""", unsafe_allow_html=True)

# Estilo para nomes das abas
st.markdown("""
    <style>
    /* Aumentar tamanho do texto dos títulos das abas */
    button[role="tab"] {
        font-size: 38px !important;
        font-weight: 600 !important;
        color: #2c3e50 !important;
    }
    </style>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📘 Teoria",  "🔢 Exercícios ", "📉 Solver", "🎥 Videos"])

with tab1:
    pdf_file = "teste.pdf"
    st.sidebar.info("### 📘 Análise Matemática I")
    if st.sidebar.button("### 📖 Capítulo 1: Nocões Topológicas em $\mathbb{R} \hspace{0.75cm}$"):
        st.info("### Nocões Topológicas em $\mathbb{R}$")
        pdf_file = "AM1/Cap1-NT.pdf"
    if st.sidebar.button("### 📖 Capítulo 2: Sucessões e Séries Numéricas  $\hspace{0.25cm}$"):
        st.info("### Sucessões e Séries Numéricas")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 3: Generalidades sobre Funções   $\hspace{0.25cm}$    "):
        st.info("### Generalidades sobre Funções")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 4: Limites e Continuidade  $\hspace{1cm}$ "):
        st.info("### Limites e Continuidade")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 5: Derivadas               $\hspace{2.6cm}$          "):
        st.info("### Derivadas")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 6: Aplicação das Derivadas $\hspace{0.9cm}$          "):
        st.info("### Aplicação das Derivadas")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 7: Primitivas/Integrais Indefinidas  "):
        st.info("### Primitivas/Integrais Indefinidas")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 8: Integrais Definidas       $\hspace{1.5cm}$        "):
        st.info("### Integrais Definidas")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 9: Aplicação de Integrais Definidas  "):
        st.info("### Aplicação de Integrais Definidas")
        pdf_file = "teste.pdf"
    if st.sidebar.button("### 📖 Capítulo 10: Intgrais Impróprias          $\hspace{1.35cm}$    "):
        st.info("### Intgrais Impróprias")
        pdf_file = "teste.pdf"

        

    # Caminho para o arquivo PDF
    # Ler e codificar o PDF como base64
    # Tenta carregar o arquivo
    try:
        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        # HTML para mostrar PDF
        pdf_display = f"""
        <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" height="700px" type="application/pdf">
        </iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("❌ Arquivo PDF não encontrado. Verifique o caminho ou nome do arquivo.")
with tab2:
    st.markdown("### :blue[...]")

with tab3:
    st.markdown("### :blue[...]")

with tab4:
    st.markdown("### :blue[...]")
