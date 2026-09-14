
import streamlit as st
import cloudinary
import cloudinary.uploader
from urllib.parse import quote

# =========================
# CONFIGURAÇÕES
# =========================

st.set_page_config(
    page_title="Vulcan Ant cheaters",
    page_icon="🛡️",
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
# ESTILO
# =========================

st.markdown("""
<style>

.stApp {
    background: #080808;
    color: white;
}

[data-testid="stHeader"] {
    background: #080808;
}

[data-testid="stToolbar"] {
    background: transparent;
}

h1, h2, h3 {
    color: #ef233c !important;
}

h1 {
    font-weight: 900 !important;
    letter-spacing: 3px;
}

p, label {
    color: #eeeeee;
}

.vulcan-header {
    background: linear-gradient(
        135deg,
        #190000,
        #080808 60%,
        #220000
    );

    border: 1px solid #700000;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    margin-bottom: 25px;
}

.vulcan-logo {
    color: #ef233c;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 5px;
}

.vulcan-subtitle {
    color: #999999;
    font-size: 13px;
    letter-spacing: 2px;
}

.vulcan-card {
    background: #111111;
    border: 1px solid #3d1111;
    border-radius: 14px;
    padding: 22px;
    margin: 15px 0;
}

.vulcan-section {
    color: #ef233c;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 12px;
}

.vulcan-description {
    color: #aaaaaa;
    font-size: 14px;
}

.vulcan-badge {
    display: inline-block;
    background: #350707;
    color: #ff334d;
    border: 1px solid #8b0000;
    border-radius: 6px;
    padding: 5px 10px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1px;
}

.vulcan-footer {
    text-align: center;
    color: #555555;
    font-size: 12px;
    padding: 30px 0 10px;
}

.stButton > button {
    background: #b30000;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    min-height: 42px;
}

.stButton > button:hover {
    background: #ef233c;
    color: white;
}

.stDownloadButton > button {
    background: #b30000;
    color: white;
}

[data-testid="stFileUploader"] {
    background: #111111;
    border: 1px solid #700000;
    border-radius: 12px;
    padding: 15px;
}

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    background: #111111;
    color: white;
    border: 1px solid #4d1111;
}

hr {
    border-color: #4d1111;
}

</style>
""", unsafe_allow_html=True)

# =========================
# CABEÇALHO
# =========================

st.markdown("""
<div class="vulcan-header">
    <div class="vulcan-logo">VULCAN</div>
    <div class="vulcan-subtitle">
        ANT CHEATERS • EVIDÊNCIAS
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# PÁGINA DE VÍDEO
# =========================

video_url = st.query_params.get("video")

if video_url:

    st.markdown(
        '<div class="vulcan-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="vulcan-badge">EVIDÊNCIA DE VÍDEO</div>',
        unsafe_allow_html=True
    )

    st.markdown("## 🎥 Vídeo compartilhado")

    st.video(video_url)

    st.success("Vídeo carregado com sucesso!")

    st.code(video_url, language="text")

    st.link_button(
        "▶ Abrir vídeo diretamente",
        video_url
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅ Voltar para a central"):
        st.query_params.clear()
        st.rerun()

    st.markdown(
        '<div class="vulcan-footer">'
        'VULCAN ANT CHEATERS © 2026'
        '</div>',
        unsafe_allow_html=True
    )

    st.stop()

# =========================
# CENTRAL DE DENÚNCIAS
# =========================

st.markdown("""
<div class="vulcan-card">
    <div class="vulcan-section">
        🛡️ Central de denúncias
    </div>

    <div class="vulcan-description">
        Envie evidências em vídeo de possíveis cheaters.
        Os vídeos serão hospedados na nuvem e poderão
        ser compartilhados por links públicos.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# CONFIGURAÇÃO
# =========================

if not CLOUDINARY_CONFIGURADO:

    st.error("Cloudinary não configurado.")

    st.info(
        "Configure os Secrets do Cloudinary no Streamlit Cloud "
        "para ativar o envio de vídeos."
    )

    st.stop()

# =========================
# DADOS DA EVIDÊNCIA
# =========================

st.markdown("## 📋 Informações da evidência")

titulo = st.text_input(
    "Título do vídeo",
    placeholder="Ex: Suspeita de aimbot no Prison Life"
)

descricao = st.text_area(
    "Descrição da denúncia",
    placeholder="Explique o que aconteceu no vídeo...",
    height=100
)

# =========================
# UPLOAD
# =========================

st.markdown("## 📤 Enviar evidência")

video = st.file_uploader(
    "Selecione seu vídeo MP4",
    type=["mp4"],
    accept_multiple_files=False
)

if video is not None:

    tamanho_mb = video.size / (1024 * 1024)

    st.write(f"**Arquivo:** {video.name}")
    st.write(f"**Tamanho:** {tamanho_mb:.2f} MB")

    st.markdown("### ▶️ Visualização")

    st.video(video)

    if st.button("🔴 Enviar evidência e gerar link"):

        if not titulo.strip():

            st.warning(
                "Digite um título para a evidência."
            )

        else:

            try:

                with st.spinner(
                    "Enviando evidência para a nuvem..."
                ):

                    resultado = cloudinary.uploader.upload(
                        video.getvalue(),
                        resource_type="video",
                        folder="vulcan_ant_cheaters",
                        use_filename=True,
                        unique_filename=True
                    )

                    link_video = resultado["secure_url"]

                st.success(
                    "Evidência enviada com sucesso!"
                )

                st.markdown("## 🔗 Link público")

                st.write(
                    "Compartilhe este link com seus amigos."
                )

                st.code(link_video, language="text")

                st.link_button(
                    "🎥 Abrir vídeo",
                    link_video
                )

                st.info(
                    "O link acima aponta diretamente para o vídeo "
                    "hospedado no Cloudinary."
                )

                st.markdown("### 📝 Dados da evidência")

                st.write(f"**Título:** {titulo}")

                if descricao.strip():

                    st.write(
                        f"**Descrição:** {descricao}"
                    )

            except Exception as erro:

                st.error(
                    "Não foi possível enviar o vídeo."
                )

                st.caption(
                    f"Detalhes técnicos: {erro}"
                )

# =========================
# RODAPÉ
# =========================

st.markdown(
    '<div class="vulcan-footer">'
    'VULCAN ANT CHEATERS © 2026<br>'
    'Central de evidências'
    '</div>',
    unsafe_allow_html=True
)
