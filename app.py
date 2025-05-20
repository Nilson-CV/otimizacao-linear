
import streamlit as st

main_page = st.Page("app.py", title="Cursos", icon="📚")
page_2 = st.Page("AnáliseMatemáticaI.py", title="Análise Matemática I", icon="❄️📘 ")

pg = st.navigation([main_page, page_2])

