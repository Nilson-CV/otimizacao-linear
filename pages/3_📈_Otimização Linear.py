import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import base64

st.set_page_config(page_title="Otimização Linear", page_icon="📈", layout="wide")


inicio = st.columns(2)

inicio[0] = st.title("📈 Otimização Linear")
st.success("Este curso aborda os conceitos fundamentais de ...", icon="✅")
inicio[1] = st.markdown("""
    <p style="font-size:16px;">
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

tab1, tab2, tab3, tab4 = st.tabs(["📘 Teoria", "🔢 Exercícios ", "📉 Solver", "🎥 Videos"])

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
    st.subheader("Formulação Matemática")
    # LaTeX..

with tab3:
    st.header("📈 Solver Interativo - 2D")

    st.caption("Este solver resolve, caso seja possível, o seguinte problema:")

    c1, c2 = 40, 30  # (usar as variáveis reais no app)
    st.latex(f"\\text{{Maximizar: }} Z = c_1x_1 + c_2x_2")

    st.latex(f"""
    \\text{{Sujeito a:}}\\quad
    \\begin{{cases}}
    a_{{11}}x_1 + a_{{12}}x_2 \\leq b_1 \\\\
    a_{{21}}x_1 + a_{{22}}x_2 \\leq b_2 \\\\
    x_1 \\geq 0,\\quad x_2 \\geq 0
    \\end{{cases}}
    """)
    # CRIA DUAS COLUNAS
    col1, col2 = st.columns([1.2, 1.0])  # Esquerda maior  sliders

    with col1:
        st.header("🧮 Dados do Problema")

        st.subheader("🎯 Função Objetivo")
        lucro = st.columns(2)
        c1 = lucro[0].number_input("Lucro por unidade de A (€)", value=40, step=1)
        c2 = lucro[1].number_input("Lucro por unidade de B (€)", value=30, step=1)
        st.latex(f"Z = f(x_1,x_2) = {c1}x_1 + {c2}x_2")

        st.subheader("📋 Matriz de Coeficientes (Recursos consumidos por produto)")
        st.caption("Cada célula indica quanto de cada recurso é necessário para cada produto.")

        default_A = pd.DataFrame(
            [[2, 1],  # Recurso 1
            [1, 2]], # Recurso 2
            columns=["Produto A", "Produto B"],
            index=["Recurso 1", "Recurso 2"]
        )

        A_df = st.data_editor(
            default_A,
            use_container_width=True,
            num_rows="fixed",
            key="matriz_A"
        )
        st.latex(f"A = \\left[\\begin{{array}}{{ll}} {A_df.values[0,0]} \\ \\ \\ {A_df.values[0,1]} \\\\  {A_df.values[1,0]} \\ \\ \\ {A_df.values[1,1]} \\end{{array}}\\right]")


        st.subheader("📊 Limite de Recursos")
        recurso = st.columns(2)
        b1 = recurso[0].number_input("Disponibilidade Recurso 1", value=100)
        b2 = recurso[1].number_input("Disponibilidade Recurso 2", value=80)
        st.latex(f"b = \\left[\\begin{{array}}{{l}} {b1} \\\\ {b2} \\end{{array}}\\right]")
    # -------- Cálculo e Gráfico na Coluna Direita --------
    with col2:
        st.header("📉 Gráfico da Região Factível")

        A = A_df.values
        b = [b1, b2]
        c = [-c1, -c2]  # Linprog faz minimização

        # Solver
        res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)], method="highs")

        # Gráfico
        x = np.linspace(0, 50, 500)
        y1 = (b[0] - A[0, 0] * x) / A[0, 1]
        y2 = (b[1] - A[1, 0] * x) / A[1, 1]

        plt.figure(figsize=(5, 5))
        plt.plot(x, y1, label="Restrição 1")
        plt.plot(x, y2, label="Restrição 2")
        plt.fill_between(x, 0, np.minimum(y1, y2), where=(np.minimum(y1, y2) >= 0), color='gray', alpha=0.3)
        plt.xlim(0, max(x))
        plt.ylim(0, max(np.nanmax(y1), np.nanmax(y2)))
        plt.xlabel("Produto A")
        plt.ylabel("Produto B")
        plt.title("Região Factível")
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    with col2:
        # RESULTADO FINAL (abaixo das colunas)
        if res.success:
            x_opt, y_opt = res.x
            lucro_max = -res.fun
            st.subheader("✅ Solução Ótima")
            st.success(f"x1 = {x_opt:.2f} e x2 = {y_opt:.2f}")
            st.subheader("✅ Valor Ótimo")
            st.info(f"💰 Z = {-res.fun:.2f}")

            # Exportar resultados
            resultado = pd.DataFrame({
            "Variável": ["Produto A (x₁)", "Produto B (x₂)", "Lucro Máximo"],
            "Valor": [x_opt, y_opt, lucro_max]
            })
            csv = resultado.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar resultado (.csv)", csv, file_name="resultado_otimizacao.csv", mime="text/csv")
        else:
            st.error("Não foi possível encontrar uma solução ótima com os dados fornecidos.")
with tab4:
    st.subheader("Solução Ótima")
    # Resultado e download...


# Inicializa estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "Início"

# Barra lateral com botões
st.sidebar.title("📚 Outros Cursos")
if st.sidebar.button("🏠 Início"):
    st.session_state.pagina = "Início"
if st.sidebar.button("📘 Análise Matemática I"):
    st.session_state.pagina = "Analise Matemática I"
if st.sidebar.button("📗 Análise Matemática II"):
    st.session_state.pagina = "Analise Matemática II"
if st.sidebar.button("💻 Programação Matemática"):
    st.session_state.pagina = "Programação Matemática"
if st.sidebar.button("🔗 Teoria dos Grafos"):
    st.session_state.pagina = "Teoria dos Grafos"

# Conteúdo principal
if st.session_state.pagina == "Início":
    st.title("Bem-vindo")
elif st.session_state.pagina == "Analise Matemática I":
    st.title("📘 Análise Matemática I")
elif st.session_state.pagina == "Análise Matemática II":
    st.title("📗 Análise Matemática II")
elif st.session_state.pagina == "Programação Matemática":
    st.title("💻 Programação Matemática")
elif st.session_state.pagina == "🔗 Teoria dos Grafos":
    st.title("🔗 Teoria dos Grafos")
