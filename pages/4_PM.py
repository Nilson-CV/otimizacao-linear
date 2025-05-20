import streamlit as st

st.title("📐 Programação Matemática")
st.write("""
Modelagem e resolução de problemas de otimização linear e não linear.
""")

st.latex(r"""
\text{Minimizar } \quad c^T x \quad 
\text{ sujeito a } \quad A x \leq b
""")


