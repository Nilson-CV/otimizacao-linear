
import streamlit as st

st.set_page_config(
    page_title="Portal de Cursos - Matemática Aplicada",
    page_icon="🧮",
    layout="centered",
)

st.title("🧮 Matemática + x = y ")
st.markdown("""
Olá, sou Nilson e seja bem-vindo à página de apoio às disciplinas que costumo lecionar.

Use o menu lateral para navegar entre os seguintes módulos:

- 📘 Análise Matemática I  
- 📗 Análise Matemática II  
- 🔗 Teoria dos Grafos  
- 💻  Programação Matemática  

---

Esta página visa consolidar conteúdos, exemplos, ferramentas de visualização e aplicações práticas relacionadas a cada disciplina.

🟢 Selecione uma disciplina no menu lateral para começar.
""")

# Opcional: rodapé
st.markdown("""<hr style="margin-top: 2em;"/>
<div style='text-align: center; font-size: 13px; color: gray;'>
    Página da autoria e desenvolvida por: **Nilson Moreira**
</div>
""", unsafe_allow_html=True)


# Inicializa estado
#if "pagina" not in st.session_state:
#    st.session_state.pagina = "Início"

# Barra lateral com botões
#st.sidebar.title("📚 Outros Cursos")
#if st.sidebar.button("🏠 Início"):
#    st.session_state.pagina = "Início"
#if st.sidebar.button("📘 Análise Matemática I"):
#    st.session_state.pagina = "AM1"
#if st.sidebar.button("📗 Análise Matemática II"):
#    st.session_state.pagina = "Análise Matemática II"
#if st.sidebar.button("💻 Programação Matemática"):
#    st.session_state.pagina = "Programação Matemática"
#if st.sidebar.button("🔗 Teoria dos Grafos"):
#    st.session_state.pagina = "Teoria dos Grafos"

# Conteúdo principal
#if st.session_state.pagina == "Início":
#    st.title("Bem-vindo")
#elif st.session_state.pagina == "AM1":
#    st.title("📘 Análise Matemática I")
#elif st.session_state.pagina == "Análise Matemática II":
#    st.title("📗 Análise Matemática II")
#elif st.session_state.pagina == "Programação Matemática":
#    st.title("💻 Programação Matemática")
#elif st.session_state.pagina == "🔗 Teoria dos Grafos":
#    st.title("🔗 Teoria dos Grafos")
