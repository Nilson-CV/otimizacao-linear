
import streamlit as st

st.set_page_config(
    page_title="Portal de Cursos - Matemática Aplicada",
    page_icon="🧮",
    layout="centered",
)

st.title("🧮 Portal de Matemática Aplicada")
st.markdown("""
Bem-vindo ao aplicativo de apoio aos cursos da área de **Matemática Aplicada**.

Use o menu lateral para navegar entre os seguintes módulos:

- 📘 Análise Matemática I  
- 📗 Análise Matemática II  
- 🔗 Teoria dos Grafos  
- 📐 Programação Matemática  

---

Este portal visa consolidar conteúdos, exemplos, ferramentas de visualização e aplicações práticas relacionadas a cada disciplina.

🟢 Selecione uma disciplina no menu lateral para começar.
""")

# Opcional: rodapé
st.markdown("""<hr style="margin-top: 2em;"/>
<div style='text-align: center; font-size: 13px; color: gray;'>
    Desenvolvido com ❤️ usando Streamlit · <a href="mailto:teu@email.com">Contato</a>
</div>
""", unsafe_allow_html=True)





