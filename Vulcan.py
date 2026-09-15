import streamlit as st
import cloudinary
import cloudinary.uploader
from datetime import datetime
import uuid
import html

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.title("🛡️ VULCAN")
st.caption("ANT CHEATERS • EVIDENCE CENTER")
st.success("● SISTEMA ONLINE")

# ============================================================
# CLOUDINARY
# ============================================================

try:
    cloud_name = st.secrets["cloudinary"]["cloud_name"]
    api_key = st.secrets["cloudinary"]["api_key"]
    api_secret = st.secrets["cloudinary"]["api_secret"]

    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret,
        secure=True
    )

    CLOUDINARY_CONFIGURADO = True

except Exception:
    CLOUDINARY_CONFIGURADO = False

# ============================================================
# SESSION STATE
# ============================================================

if "historico" not in st.session_state:
    st.session_state.historico = []

if "ultima_denuncia" not in st.session_state:
    st.session_state.ultima_denuncia = None


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at top,
            rgba(130, 0, 0, 0.13),
            transparent 35%
        ),
        #080808;
}

/* Remove alguns espaços padrões */
.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* =========================================================
   HEADER
========================================================= */

.vulcan-header {
    text-align: center;
    padding: 30px 20px 25px 20px;
    margin-bottom: 25px;

    background: linear-gradient(
        180deg,
        rgba(22,22,22,0.95),
        rgba(12,12,12,0.95)
    );

    border: 1px solid rgba(255, 40, 40, 0.16);
    border-radius: 20px;

    box-shadow:
        0 15px 45px rgba(0,0,0,0.35);
}

.vulcan-logo {
    font-size: 46px;
    font-weight: 900;
    letter-spacing: 8px;

    background: linear-gradient(
        90deg,
        #ffffff,
        #ff5555
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.vulcan-subtitle {
    color: #888;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-top: 5px;
}

.vulcan-status {
    display: inline-block;

    margin-top: 16px;
    padding: 7px 14px;

    border-radius: 999px;

    color: #ff7777;
    background: rgba(255,40,40,0.07);

    border: 1px solid rgba(255,40,40,0.18);

    font-size: 11px;
    font-weight: 700;
}


/* =========================================================
   CARDS
========================================================= */

.vulcan-card {
    background: rgba(18,18,18,0.92);

    border: 1px solid #242424;
    border-radius: 18px;

    padding: 25px;
    margin-bottom: 20px;

    box-shadow: 0 10px 35px rgba(0,0,0,0.25);

    transition:
        transform 0.2s ease,
        border-color 0.2s ease;
}

.vulcan-card:hover {
    transform: translateY(-2px);
    border-color: rgba(255,60,60,0.28);
}

.vulcan-card-red {
    border-left: 3px solid #d72b2b;
}

.vulcan-title {
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 6px;
}

.vulcan-description {
    color: #929292;
    font-size: 14px;
    line-height: 1.6;
}


/* =========================================================
   BADGES
========================================================= */

.vulcan-badge {
    display: inline-block;

    padding: 5px 10px;
    margin: 3px;

    border-radius: 7px;

    background: #171717;
    border: 1px solid #292929;

    color: #aaa;

    font-size: 11px;
    font-weight: 600;
}


/* =========================================================
   STEPS
========================================================= */

.vulcan-step {
    padding: 13px 15px;
    margin: 9px 0;

    background: #111;
    border: 1px solid #222;
    border-radius: 10px;

    color: #bbb;
    font-size: 13px;
}

.vulcan-step-number {
    display: inline-flex;

    width: 25px;
    height: 25px;

    align-items: center;
    justify-content: center;

    margin-right: 8px;

    border-radius: 50%;

    background: rgba(190,20,20,0.15);
    border: 1px solid rgba(220,40,40,0.25);

    color: #f35b5b;

    font-weight: 800;
}


/* =========================================================
   HISTÓRICO
========================================================= */

.history-card {
    background: #101010;

    border: 1px solid #242424;
    border-radius: 13px;

    padding: 17px;
    margin-top: 12px;
}

.history-id {
    color: #ef5350;
    font-weight: 800;
    font-size: 13px;
}

.history-title {
    color: #eee;
    font-weight: 700;
    margin-top: 5px;
}

.history-date {
    color: #777;
    font-size: 11px;
    margin-top: 6px;
}

.status-success {
    color: #65d68b;
    font-size: 12px;
    font-weight: 700;
}

.status-error {
    color: #ff6464;
    font-size: 12px;
    font-weight: 700;
}


/* =========================================================
   FOOTER
========================================================= */

.vulcan-footer {
    text-align: center;

    margin-top: 45px;
    padding-top: 20px;

    border-top: 1px solid #202020;

    color: #555;
    font-size: 11px;
}


/* =========================================================
   RESPONSIVO
========================================================= */

@media (max-width: 600px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .vulcan-logo {
        font-size: 35px;
        letter-spacing: 5px;
    }

    .vulcan-card {
        padding: 18px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
<div class="vulcan-header">

    <div class="vulcan-logo">
        VULCAN
    </div>

    <div class="vulcan-subtitle">
        ANT CHEATERS • EVIDENCE CENTER
    </div>

    <div class="vulcan-status">
        ● SISTEMA ONLINE
    </div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# VÍDEO COMPARTILHADO
# ============================================================

video_url = st.query_params.get("video")

if video_url:

    st.markdown(
        """
<div class="vulcan-card vulcan-card-red">

<div class="vulcan-title">
🎥 Evidência compartilhada
</div>

<div class="vulcan-description">
Este vídeo foi disponibilizado através do VULCAN Ant Cheaters.
</div>

</div>
""",
        unsafe_allow_html=True
    )

    try:
        st.video(video_url)

        st.markdown("### 🔗 Link da evidência")

        st.code(video_url, language="text")

        st.link_button(
            "🎥 Abrir vídeo diretamente",
            video_url,
            use_container_width=True
        )

        if st.button(
            "← Voltar para a central",
            use_container_width=True
        ):
            st.query_params.clear()
            st.rerun()

    except Exception:
        st.error("Não foi possível carregar este vídeo.")

    st.stop()


# ============================================================
# INTRODUÇÃO
# ============================================================

st.markdown(
    """
<div class="vulcan-card">

<div class="vulcan-title">
🛡️ Central de evidências
</div>

<div class="vulcan-description">
Envie vídeos de possíveis infrações para gerar uma evidência
compartilhável através de um link público.
</div>

<br>

<span class="vulcan-badge">MP4</span>
<span class="vulcan-badge">Máx. 200 MB</span>
<span class="vulcan-badge">Link público</span>
<span class="vulcan-badge">Cloud Storage</span>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# COMO FUNCIONA
# ============================================================

with st.expander("🛡️ Como funciona"):

    st.markdown(
        """
<div class="vulcan-step">
<span class="vulcan-step-number">1</span>
Preencha as informações da denúncia.
</div>

<div class="vulcan-step">
<span class="vulcan-step-number">2</span>
Selecione o vídeo da evidência.
</div>

<div class="vulcan-step">
<span class="vulcan-step-number">3</span>
Confira o preview antes do envio.
</div>

<div class="vulcan-step">
<span class="vulcan-step-number">4</span>
Envie o vídeo para o sistema.
</div>

<div class="vulcan-step">
<span class="vulcan-step-number">5</span>
Receba um link público para compartilhar.
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# CENTRAL DE DENÚNCIAS
# ============================================================

st.markdown(
    """
<div class="vulcan-card vulcan-card-red">

<div class="vulcan-title">
📞 Central de denúncias
</div>

<div class="vulcan-description">
Forneça informações claras e objetivas sobre a possível infração.
</div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# FORMULÁRIO
# ============================================================

titulo = st.text_input(
    "🏷️ Nome da denúncia",
    placeholder="Ex.: Suspeita de aimbot"
)

descricao = st.text_area(
    "📝 Descrição",
    placeholder="Descreva o que acontece no vídeo..."
)


# ============================================================
# UPLOAD
# ============================================================

st.markdown("### 📤 Evidência em vídeo")

video = st.file_uploader(
    "Arraste o vídeo para esta área ou clique para selecionar",
    type=["mp4"],
    accept_multiple_files=False,
    help="Somente MP4. Tamanho máximo: 200 MB."
)


# ============================================================
# PREVIEW
# ============================================================

if video is not None:

    tamanho_bytes = video.size
    tamanho_mb = tamanho_bytes / (1024 * 1024)

    st.markdown(
        f"""
<div class="vulcan-card">

<div class="vulcan-title">
📹 Preview da evidência
</div>

<div class="vulcan-description">
Arquivo: <b>{html.escape(video.name)}</b><br>
Tamanho: <b>{tamanho_mb:.2f} MB</b>
</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.video(video)


# ============================================================
# SEGURANÇA
# ============================================================

st.markdown(
    """
<div class="vulcan-card">

<div class="vulcan-title">
🔒 Segurança
</div>

<div class="vulcan-description">

• Aceitamos somente arquivos MP4.<br>
• O tamanho máximo permitido é 200 MB.<br>
• Não envie informações pessoais desnecessárias.<br>
• Envie apenas evidências relacionadas à denúncia.<br>
• Links gerados podem ser compartilhados com terceiros.

</div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# ENVIO
# ============================================================

if st.button(
    "🚀 ENVIAR EVIDÊNCIA",
    use_container_width=True,
    type="primary"
):

    # -----------------------------
    # Validações
    # -----------------------------

    if not CLOUDINARY_CONFIGURADO:
        st.error(
            "❌ O Cloudinary não está configurado corretamente."
        )
        st.stop()

    if not titulo.strip():
        st.warning(
            "⚠️ Informe o nome da denúncia."
        )
        st.stop()

    if video is None:
        st.warning(
            "⚠️ Selecione um vídeo MP4."
        )
        st.stop()

    if video.size > MAX_FILE_SIZE_BYTES:
        st.error(
            f"❌ O vídeo ultrapassa o limite de "
            f"{MAX_FILE_SIZE_MB} MB."
        )
        st.stop()

    if not video.name.lower().endswith(".mp4"):
        st.error(
            "❌ O arquivo precisa estar no formato MP4."
        )
        st.stop()


    # -----------------------------
    # ID da denúncia
    # -----------------------------

    denuncia_id = (
        "VUL-"
        + datetime.now().strftime("%Y%m%d")
        + "-"
        + uuid.uuid4().hex[:6].upper()
    )

    data_envio = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )


    # -----------------------------
    # Status enviando
    # -----------------------------

    status_area = st.empty()
    progress_bar = st.progress(0)

    status_area.info(
        f"☁️ Enviando {denuncia_id} para o Cloudinary..."
    )

    progress_bar.progress(25)


    try:

        # -----------------------------
        # Upload
        # -----------------------------

        resultado = cloudinary.uploader.upload(
            video.getvalue(),
            resource_type="video",
            folder="vulcan_ant_cheaters",
            use_filename=True,
            unique_filename=True
        )

        progress_bar.progress(100)

        link_video = resultado["secure_url"]


        # -----------------------------
        # Registro
        # -----------------------------

        registro = {
            "id": denuncia_id,
            "titulo": titulo,
            "descricao": descricao,
            "data": data_envio,
            "link": link_video,
            "status": "Concluído"
        }

        st.session_state.historico.insert(
            0,
            registro
        )

        st.session_state.ultima_denuncia = registro


        # -----------------------------
        # Status concluído
        # -----------------------------

        status_area.success(
            f"✅ {denuncia_id} enviado com sucesso!"
        )


        # -----------------------------
        # Resultado
        # -----------------------------

        st.markdown(
            """
<div class="vulcan-card vulcan-card-red">

<div class="vulcan-title">
✅ Evidência enviada
</div>

</div>
""",
            unsafe_allow_html=True
        )

        st.success(
            f"Denúncia {denuncia_id} concluída."
        )

        st.markdown("### 🔗 Link público")

        st.code(
            link_video,
            language="text"
        )

        st.link_button(
            "🎥 Abrir vídeo",
            link_video,
            use_container_width=True
        )

        # Botão copiar usando HTML/JS
        st.components.v1.html(
            f"""
            <button
                onclick="navigator.clipboard.writeText({link_video!r})"
                style="
                    width:100%;
                    padding:12px;
                    border-radius:8px;
                    border:1px solid #333;
                    background:#151515;
                    color:#eee;
                    cursor:pointer;
                    font-weight:700;
                "
            >
                📋 COPIAR LINK
            </button>
            """,
            height=55
        )

    except Exception as erro:

        progress_bar.progress(0)

        status_area.error(
            "❌ Erro durante o envio."
        )

        st.error(
            f"Não foi possível enviar o vídeo: {erro}"
        )


# ============================================================
# HISTÓRICO
# ============================================================

if st.session_state.historico:

    st.markdown("---")

    st.markdown(
        """
<div class="vulcan-card">

<div class="vulcan-title">
📋 Histórico desta sessão
</div>

<div class="vulcan-description">
As evidências abaixo foram enviadas durante esta sessão.
</div>

</div>
""",
        unsafe_allow_html=True
    )

    for item in st.session_state.historico:

        titulo_html = html.escape(
            item["titulo"]
        )

        st.markdown(
            f"""
<div class="history-card">

<div class="history-id">
🛡️ {html.escape(item["id"])}
</div>

<div class="history-title">
{titulo_html}
</div>

<div class="history-date">
🕐 {html.escape(item["data"])}
</div>

<div class="status-success">
● {html.escape(item["status"])}
</div>

</div>
""",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            st.link_button(
                "🎥 Ver vídeo",
                item["link"],
                use_container_width=True
            )

        with col2:

            st.components.v1.html(
                f"""
                <button
                    onclick="navigator.clipboard.writeText({item['link']!r})"
                    style="
                        width:100%;
                        height:38px;
                        border-radius:7px;
                        border:1px solid #333;
                        background:#151515;
                        color:#eee;
                        cursor:pointer;
                        font-weight:600;
                    "
                >
                    📋 Copiar
                </button>
                """,
                height=45
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="vulcan-footer">

VULCAN ANT CHEATERS<br>

Evidence Center • Sistema de gerenciamento de evidências

</div>
""",
    unsafe_allow_html=True
)
