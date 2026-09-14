
import streamlit as st
import cloudinary
import cloudinary.uploader
from io import BytesIO

# =========================
# CONFIGURAÇÕES
# =========================

st.set_page_config(
    page_title="Vulcan Ant cheaters",
    page_icon="🎥",
    layout="centered"
)

# =========================
# CLOUDINARY
# =========================

try:
    cloudinary.config(
        cloud_name=st.secrets["cloudinary"]["cloud_name"],
        api_key=st.secrets["cloudinary"]["api_key"],
        api_secret=st.secrets["cloudinary"]["api_secret"],
        secure=True
    )

    CLOUDINARY_CONFIGURADO = True

except Exception:
    CLOUDINARY_CONFIGURADO = False

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

    .vulcan-card {
        background-color: #111111;
        border: 1px solid #8b0000;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
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

    .aviso {
        background-color: #250000;
        border: 1px solid #b30000;
        border-radius: 10px;
        padding: 15px;
        color: white;
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
    '<p class="subtitulo">'
    'Central de vídeos • Compartilhe seus arquivos MP4'
    '</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<hr class="linha-vermelha">',
    unsafe_allow_html=True
)

# =========================
# VERIFICAR CONFIGURAÇÃO
# =========================

if not CLOUDINARY_CONFIGURADO:

    st.error("Cloudinary não configurado.")

    st.info(
        "Configure os Secrets do Cloudinary no Streamlit Cloud "
        "para ativar o upload de vídeos."
    )

    st.stop()

# =========================
# UPLOAD
# =========================

st.markdown("## 📤 Enviar vídeo")

st.write(
    "Envie um vídeo MP4 e gere um link público "
    "para compartilhar com seus amigos."
)

video = st.file_uploader(
    "Selecione seu vídeo MP4",
    type=["mp4"],
    accept_multiple_files=False
)

if video is not None:

    tamanho_mb = video.size / (1024 * 1024)

    st.write(f"**Arquivo:** {video.name}")
    st.write(f"**Tamanho:** {tamanho_mb:.2f} MB")

    if tamanho_mb > 200:

        st.warning(
            "O vídeo possui mais de 200 MB. "
            "Confira os limites do seu plano de armazenamento."
        )

    st.markdown("### ▶️ Visualização")

    st.video(video)

    if st.button("🔴 Enviar e gerar link público"):

        try:

            with st.spinner("Enviando vídeo para a nuvem..."):

                # Lê o vídeo enviado
                video_bytes = video.getvalue()

                # Envia para o Cloudinary
                resultado = cloudinary.uploader.upload(
                    BytesIO(video_bytes),
                    resource_type="video",
                    folder="vulcan_ant_cheaters",
                    use_filename=True,
                    unique_filename=True
                )

                # URL pública HTTPS
                link_publico = resultado["secure_url"]

            st.success("Vídeo enviado com sucesso!")

            st.markdown("## 🔗 Seu link público")

            st.write(
                "Qualquer pessoa que tiver este link "
                "poderá acessar o vídeo."
            )

            st.code(link_publico, language="text")

            st.link_button(
                "🎥 Abrir vídeo",
                link_publico
            )

            st.info(
                "Copie o link acima e envie para seus amigos "
                "no Discord, WhatsApp ou onde quiser."
            )

        except Exception as erro:

            st.error("Não foi possível enviar o vídeo.")

            st.write(
                "Verifique se os Secrets do Cloudinary "
                "estão configurados corretamente."
            )

            st.caption(f"Detalhes técnicos: {erro}")

# =========================
# RODAPÉ
# =========================

st.markdown(
    '<hr class="linha-vermelha">',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitulo">'
    'Vulcan Ant cheaters © 2026'
    '</p>',
    unsafe_allow_html=True
)
