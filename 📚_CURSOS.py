
import streamlit as st



st.set_page_config(
    page_title="Portal de Cursos de Matemática",
    page_icon="∑",
    layout="centered",
)


st.title("✅ Matemática + x = y ")

st.success(""" 
##### Olá, sou Nilson e seja bem-vindo à página de apoio às disciplinas que costumo lecionar.""")

st.info("""            
##### Use o menu lateral para navegar entre os seguintes módulos:

- 📘 Análise Matemática I  
- 📗 Análise Matemática II 
- 📈 Otimização Linear              
- 💻 Otimização não Linear            
- 🔗 Teoria dos Grafos  
 
""")
st.markdown("---")

st.warning("""  
Esta página visa consolidar conteúdos, exemplos, ferramentas de visualização e aplicações práticas relacionadas a cada disciplina.

🟢 Selecione uma disciplina no menu lateral para começar.
""")

# Opcional: rodapé
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.8em;'>"
    "© 2025 Nilson Moreira. Todos os direitos reservados."
    "</div>",
    unsafe_allow_html=True
)


# EXTRAS
if "pagina" not in st.session_state:
    st.session_state.pagina = "Início"

# Barra lateral com botões
st.sidebar.title("📚 EXTRAS")
if st.sidebar.button("🔺 Matlab"):
    st.session_state.pagina = "Matlab"
if st.sidebar.button("🐍 Python"):
    st.session_state.pagina = "Python"
if st.sidebar.button("📊 R"):
    st.session_state.pagina = "R"
if st.sidebar.button("🌐 Streamlit"):
    st.session_state.pagina = "Streamlit"

# Conteúdo principal
if st.session_state.pagina == "Matlab":
    st.title("🔺 Matlab")
elif st.session_state.pagina == "Python":
    st.title("🐍 Python")
elif st.session_state.pagina == "R":
    st.title("📊 R")
elif st.session_state.pagina == "Streamlit":
    st.title("🌐 Streamlit")

