
import streamlit as st
from pathlib import Path
import uuid

# =========================
# CONFIGURAÇÕES
# =========================

st.set_page_config(
    page_title="Vulcan Ant cheaters",
    page_icon="🎥",
    layout="centered"
)

PASTA_VIDEOS = Path("videos")
PASTA_VIDEOS.mkdir(exist_ok=True)

# =========================
# TEMA PRETO E VERMELHO
# =========================

st.markdown("""
<style>
    .stApp {
        background-color: #080808;
        color: white;
    }

    [data-testid="stHeader"] {
        background-color: #080808;
    }

    h1 {
        color: #e50914 !important;
        text-align: center;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    h2, h3 {
        color: #ff1a1a !important;
    }

    p, label {
        color: #eeeeee;
    }

    [data-testid="stFileUploader"] {
        background-color: #111111;
        border: 1px solid #b30000;
        border-radius: 12px;
        padding: 15px;
    }

    .stButton > button {
        background-color: #b30000;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #e50914;
        color: white;
    }

    .subtitulo {
        text-align: center;
        color: #aaaaaa;
        font-size: 16px;
    }

    .linha-vermelha {
        height: 3px;
        background-color: #e50914;
        border: none;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# CABEÇALHO
# =========================

st.markdown(
    '<h1>Vulcan Ant cheaters</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitulo">Central de vídeos • Compartilhe seus arquivos MP4</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<hr class="linha-vermelha">',
    unsafe_allow_html=True
)

# =========================
# PÁGINA DE VÍDEO
# =========================

video_id = st.query_params.get("video", "")

if video_id:

    # Segurança: aceitar apenas nomes de MP4
    if (
        not video_id.endswith(".mp4")
        or Path(video_id).name != video_id
    ):
        st.error("Vídeo inválido.")
        st.stop()

    caminho = PASTA_VIDEOS / video_id

    if caminho.exists():

        st.markdown("## 🎥 Vídeo compartilhado")

        with open(caminho, "rb") as arquivo:
            video_bytes = arquivo.read()

        st.video(video_bytes)

        st.success("Vídeo carregado com sucesso!")

        if st.button("⬅ Voltar para enviar vídeo"):
            st.query_params.clear()
            st.rerun()

    else:
        st.error("Vídeo não encontrado.")

    st.stop()

# =========================
# UPLOAD
# =========================

st.markdown("## 📤 Enviar vídeo")

st.write(
    "Escolha um arquivo MP4 para gerar um link de compartilhamento."
)

video = st.file_uploader(
    "Selecione seu vídeo",
    type=["mp4"],
    accept_multiple_files=False
)

if video is not None:

    tamanho_mb = video.size / (1024 * 1024)

    st.write(f"**Arquivo:** {video.name}")
    st.write(f"**Tamanho:** {tamanho_mb:.2f} MB")

    if tamanho_mb > 200:
        st.warning(
            "O vídeo é grande. Para testes locais, "
            "considere usar um arquivo menor."
        )

    if st.button("🔴 Gerar link do vídeo"):

        nome_unico = f"{uuid.uuid4().hex}.mp4"
        caminho = PASTA_VIDEOS / nome_unico

        with open(caminho, "wb") as arquivo:
            arquivo.write(video.getbuffer())

        # Link local de teste
        link = (
            "http://localhost:8501"
            f"?video={nome_unico}"
        )

        st.success("Vídeo salvo com sucesso!")

        st.markdown("### 🔗 Seu link")

        st.code(link, language="text")

        st.info(
            "Este é um link local de teste. "
            "Ele não funciona como link público para seus amigos."
        )

        st.markdown("### ▶️ Visualização")

        with open(caminho, "rb") as arquivo:
            st.video(arquivo.read())

# =========================
# RODAPÉ
# =========================

st.markdown(
    '<hr class="linha-vermelha">',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitulo">Vulcan Ant cheaters © 2026</p>',
    unsafe_allow_html=True
)
