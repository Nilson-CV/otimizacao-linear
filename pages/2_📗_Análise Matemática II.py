import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import base64

st.set_page_config(page_title="Análise Matemática II", page_icon="📘", layout="wide")

inicio = st.columns(2)

inicio[0] = st.title("📘 Análise Matemática II")
st.success("Este curso aborda os conceitos fundamentais de cálculo diferencial e integral em várias variáveis reais, incluindo limites, continuidade, derivadas e integrais.", icon="✅")
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
    st.markdown("### Fundamentos Teóricos")
    # Caminho para o arquivo PDF
    pdf_file = "teste.pdf"

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

