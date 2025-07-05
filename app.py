import streamlit as st

st.set_page_config(page_title="📘 Manual LaTeX", page_icon="📘", layout="wide")

# 🌈 Estilos personalizados
st.markdown(""
<style>
  body { background-color: #f0f4f8; }
  .title { color: #3366cc; text-align: center; }
  .footer { text-align: center; font-size: 12px; margin-top: 2em; }
</style>
""", unsafe_allow_html=True)

# 🧭 Navegación por secciones
secciones = [
    "1️⃣ ¿Qué es LaTeX?",
    "2️⃣ Estructura del documento",
    "3️⃣ Formato básico y listas",
    "4️⃣ Tablas y figuras",
    "5️⃣ Fórmulas matemáticas",
    "6️⃣ Diseño de página"
]
if "page" not in st.session_state:
    st.session_state.page = 0

with st.sidebar:
    st.title("📚 Secciones")
    st.session_state.page = st.radio("", secciones, index=st.session_state.page)

# 🎨 Título principal
st.markdown(f"<h1 class='title'>{secciones[st.session_state.page]}</h1>", unsafe_allow_html=True)

# 📄 Contenido de cada sección
page = st.session_state.page
if page == 0:
    st.write("""
**LaTeX** es un sistema de composición de textos de alta calidad, ideal para documentos científicos con fórmulas matemáticas. Fue creado por Donald Knuth en 1978 y popularizado por Leslie Lamport en 1984. :contentReference[oaicite:1]{index=1}
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/92/LaTeX_logo.svg", width=200)

elif page == 1:
    st.write("""
### Esqueleto básico de un documento (.tex)

```latex
\documentclass[a4paper,10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage[T1]{fontenc}

\title{Título}
\author{Autor}
\date{Fecha}

\begin{document}
\maketitle
\tableofcontents
Contenido...
\end{document}
``` :contentReference[oaicite:2]{index=2}
    """)

elif page == 2:
    st.write("""
### Formato básico y listas

- **Secciones**: `\section{}`, `\subsection{}`
- **Texto enfatizado**: `\textbf{}`, `\textit{}`, `\underline{}`
- **Listas**:
  - `itemize`: listas con viñetas
  - `enumerate`: listas numeradas
- Párrafos y saltos de línea: deja líneas en blanco o usa `\\`, `\newline` :contentReference[oaicite:3]{index=3}
    """)

elif page == 3:
    st.write("""
### Tablas: entorno `tabular`

```latex
\begin{tabular}{|l|c|r|}
\hline
Nombre & Ciudad & Edad \\
\hline
María & Valencia & 22 \\
Juan & Madrid & 50 \\
\hline
\end{tabular}
``` :contentReference[oaicite:4]{index=4}

También puedes usar `\multicolumn` y `\hline` para celdas combinadas y líneas divisorias.
    """)

elif page == 4:
    st.write("""
### Fórmulas matemáticas

- `$ ... $`: modo en línea  
- `$$ ... $$` o `equation`: display

Ejemplos:
```latex
\alpha, \beta, \sum_{i=1}^{n} i^2, \frac{a}{b}, \sqrt{x}, \int_0^1 x^2\,dx
``` :contentReference[oaicite:5]{index=5}

**Prueba por ti misma:**

""")
    formula = st.text_area("✏️ Tu fórmula LaTeX:", value=r"\int_0^1 x^2 dx")
    st.markdown("#### 👁️ Vista previa:")
    st.latex(formula)

elif page == 5:
    st.write("""
### Diseño de página y márgenes

```latex
\usepackage[a4paper, left=2.5cm, right=3.5cm, top=45mm, bottom=20mm]{geometry}
``` :contentReference[oaicite:6]{index=6}

Para encabezados y pies:
```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[L]{Izquierda}
\fancyhead[C]{Centro}
\fancyhead[R]{Derecha}
``` :contentReference[oaicite:7]{index=7}
    """)

# ⏮️⏭️ Botones de navegación
cols = st.columns([1,2,1])
with cols[0]:
    if st.button("⬅️ Anterior") and page>0:
        st.session_state.page -= 1
with cols[2]:
    if st.button("Siguiente ➡️") and page<len(secciones)-1:
        st.session_state.page += 1

# 🧡 Pie de página
st.markdown("<div class='footer'>Creado con ❤ por </div>", unsafe_allow_html=True)
CHUPA PENES.
