import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import base64
from scipy.integrate import quad


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
    st.info("### Simulador de Integral de Riemann")
    col1, col2 = st.columns([1.0, 1.5])
    
    with col1:
        cols = st.columns(2)
        # Entrada da função
        func_input = cols[0].text_input(":blue[**Digite a função f(x):**]", value="x**2")
        n = cols[1].slider(":blue[**Número de subdivisões (n):**]", min_value=1, max_value=100, value=10)

        # Intervalo e número de subdivisões
        cols1 = st.columns(2)
        a = cols1[0].number_input(":blue[**Limite inferior (a):**]", value=0.0)
        b = cols1[1].number_input(":blue[**Limite superior (b):**]", value=1.0)

        
        # Tipo de soma
        tipo = st.radio(" :blue[**Tipo de soma de Riemann:**]", ["Esquerda", "Direita", "Ponto médio"])

        # Define a função a partir da string usando eval (com segurança)
        try:
            f = lambda x: eval(func_input, {"x": x, "np": np, "__builtins__": {} })
        except Exception as e:
            st.error(f"Erro ao interpretar a função: {e}")
            st.stop()

        # Cálculo dos pontos e soma de Riemann
        x = np.linspace(a, b, 1000)
        dx = (b - a) / n

        if tipo == "Esquerda":
            xi = np.linspace(a, b - dx, n)
            riemann_sum = np.sum(f(xi)) * dx
        elif tipo == "Direita":
            xi = np.linspace(a + dx, b, n)
            riemann_sum = np.sum(f(xi)) * dx
        elif tipo == "Ponto médio":
            xi = np.linspace(a + dx/2, b - dx/2, n)
            riemann_sum = np.sum(f(xi)) * dx
        # Mostrar resultado
        st.latex(f"\\int_{{{a}}}^{{{b}}} f(x)\\,dx \\approx {riemann_sum:.5f}")

    with col2:
        # Plot
        fig, ax = plt.subplots()
        x_plot = np.linspace(a, b, 1000)
        ax.plot(x_plot, f(x_plot), label="f(x)", color="blue")

        # Desenhar retângulos
        for x0 in xi:
            ax.add_patch(plt.Rectangle((x0, 0), dx, f(x0), edgecolor='black', facecolor='orange', alpha=0.5))

        ax.set_xlim([a, b])
        ax.set_ylim([0, max(f(xi)) * 1.1])
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Aproximação pela soma de Riemann")
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)

with tab4:
    st.markdown("### :blue[...]")


    # Configuração inicial
    st.set_page_config(page_title="📐 Cálculo de Integral", layout="centered")
    st.title("🧮 Visualizador de Integrais com LaTeX")

    # 📌 Seção de entrada
    st.markdown("### 📝 Digite a função \( f(x) \), intervalo e pressione **Calcular**")

    func_input = st.text_input("Função f(x):", value="x**2")
    a = st.number_input("Limite inferior \( a \):", value=0.0, format="%.2f")
    b = st.number_input("Limite superior \( b \):", value=1.0, format="%.2f")

    # Botão de cálculo
    if st.button("📊 Calcular Integral"):
        try:
            # Criar função segura a partir da entrada do usuário
            f = lambda x: eval(func_input, {"x": x, "np": np, "__builtins__": {}})
            
            # Cálculo da integral
            result, _ = quad(f, a, b)

            # Exibir resultado em LaTeX grande
            st.markdown(f"""
            <div style='font-size: 32px; text-align: center; color: darkblue;'>
                \( \int_{{{a}}}^{{{b}}} {func_input.replace('**', '^')} \, dx = {result:.5f} \)
            </div>
            """, unsafe_allow_html=True)

            # Gráfico da função
            x = np.linspace(a, b, 400)
            y = f(x)

            fig, ax = plt.subplots()
            ax.plot(x, y, label=f"$f(x) = {func_input.replace('**', '^')}$", color='blue')
            ax.fill_between(x, y, alpha=0.3, color='orange', label="Área sob a curva")
            ax.axhline(0, color='black', linewidth=0.5)
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Erro ao interpretar a função: {e}")

