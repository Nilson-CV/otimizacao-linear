import streamlit as st

st.set_page_config(page_title=" Otimização não Linear", page_icon="💻")


st.title("💻 Otimização não Linear")
st.write("""
Modelagem e resolução de problemas de otimização linear e não linear.
""")

st.latex(r"""
\text{Minimizar } \quad c^T x \quad 
\text{ sujeito a } \quad A x \leq b
""")


