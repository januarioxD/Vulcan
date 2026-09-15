
import streamlit as st
import cloudinary
import cloudinary.uploader
from datetime import datetime
import uuid



st.set_page_config(
    page_title="VULCAN • Ant Cheaters",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)




MAX_FILE_SIZE_MB = 200
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


# Formatos de vídeo aceitos
FORMATOS_VIDEO = [
    "mp4",
    "mov",
    "avi",
    "mkv",
    "webm",
    "m4v",
    "mpeg",
    "mpg",
    "wmv",
    "flv"
]


FORMATOS_VIDEO_TEXTO = (
    "MP4, MOV, AVI, MKV, WEBM, M4V, "
    "MPEG, MPG, WMV e FLV"
)




st.markdown(
    """
    <style>

    .stApp {
        background-color: #080808;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        color: #ff4444 !important;
    }

    .stButton > button {
        border-radius: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)




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



if "historico" not in st.session_state:
    st.session_state.historico = []

if "ultima_denuncia" not in st.session_state:
    st.session_state.ultima_denuncia = None



st.title("🛡️ VULCAN")

st.caption(
    "ANT CHEATERS • EVIDENCE CENTER"
)

st.success(
    "● SISTEMA ONLINE"
)

st.divider()




video_url = st.query_params.get("video")


if video_url:

    st.header("🎥 Evidência compartilhada")

    st.write(
        "Este vídeo foi disponibilizado através do "
        "VULCAN Ant Cheaters."
    )

    try:

        st.video(video_url)

        st.subheader("🔗 Link da evidência")

        st.code(
            video_url,
            language=None
        )

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

        st.error(
            "Não foi possível carregar este vídeo."
        )

    st.stop()



st.header("🛡️ Central de evidências")

st.write(
    "Envie vídeos de possíveis infrações para gerar "
    "uma evidência compartilhável através de um link público."
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Formatos",
        "10"
    )


with col2:

    st.metric(
        "Limite",
        "200 MB"
    )


with col3:

    st.metric(
        "Armazenamento",
        "Cloud"
    )


with col4:

    st.metric(
        "Status",
        "Online"
    )




with st.expander("🛡️ Como funciona"):

    st.write(
        "**1.** Preencha as informações da denúncia."
    )

    st.write(
        "**2.** Selecione o vídeo da evidência."
    )

    st.write(
        "**3.** Confira o preview antes do envio."
    )

    st.write(
        "**4.** Envie o vídeo para o sistema."
    )

    st.write(
        "**5.** Receba um link público para compartilhar."
    )
=

st.header("📞 Central de denúncias")

st.info(
    "Forneça informações claras e objetivas sobre "
    "a possível infração."
)



titulo = st.text_input(
    "🏷️ Nome da denúncia",
    placeholder="Ex.: Suspeita de aimbot"
)


descricao = st.text_area(
    "📝 Descrição",
    placeholder="Descreva o que acontece no vídeo..."
)



st.subheader("📤 Evidência em vídeo")

st.write(
    f"**Formatos aceitos:** {FORMATOS_VIDEO_TEXTO}"
)

st.write(
    f"**Tamanho máximo:** {MAX_FILE_SIZE_MB} MB"
)


video = st.file_uploader(
    "Arraste o vídeo para esta área ou clique para selecionar",
    type=FORMATOS_VIDEO,
    accept_multiple_files=False,
    help=(
        f"Formatos aceitos: {FORMATOS_VIDEO_TEXTO}. "
        f"Tamanho máximo: {MAX_FILE_SIZE_MB} MB."
    )
)




if video is not None:

    tamanho_mb = video.size / (1024 * 1024)

    extensao = video.name.lower().split(".")[-1]

    st.subheader("📹 Preview da evidência")

    st.write(
        f"**Arquivo:** {video.name}"
    )

    st.write(
        f"**Formato:** {extensao.upper()}"
    )

    st.write(
        f"**Tamanho:** {tamanho_mb:.2f} MB"
    )


    # --------------------------------------------------------
    # VERIFICAR TAMANHO
    # --------------------------------------------------------

    if tamanho_mb > MAX_FILE_SIZE_MB:

        st.error(
            f"❌ O arquivo ultrapassa o limite de "
            f"{MAX_FILE_SIZE_MB} MB."
        )

-

    elif extensao not in FORMATOS_VIDEO:

        st.error(
            "❌ Este formato de vídeo não é suportado."
        )



    else:

        st.success(
            "✅ Arquivo dentro do limite permitido."
        )

        st.info(
            f"🎬 Formato detectado: {extensao.upper()}"
        )

        # Preview
        try:

            st.video(video)

        except Exception:

            st.warning(
                "⚠️ O navegador não conseguiu reproduzir "
                "este formato diretamente. "
                "O arquivo ainda poderá ser enviado."
            )


# ============================================================
# SEGURANÇA
# ============================================================

st.subheader("🔒 Segurança")

st.warning(
    "Não envie informações pessoais desnecessárias. "
    "Envie somente evidências relacionadas à denúncia."
)


st.write(
    f"• Formatos aceitos: {FORMATOS_VIDEO_TEXTO}."
)

st.write(
    f"• Tamanho máximo: {MAX_FILE_SIZE_MB} MB."
)

st.write(
    "• Os links gerados podem ser compartilhados."
)



if st.button(
    "🚀 ENVIAR EVIDÊNCIA",
    use_container_width=True,
    type="primary"
):



    if not CLOUDINARY_CONFIGURADO:

        st.error(
            "❌ O Cloudinary não está configurado corretamente."
        )

        st.stop()


    # ========================================================
    # TÍTULO
    # ========================================================

    if not titulo.strip():

        st.warning(
            "⚠️ Informe o nome da denúncia."
        )

        st.stop()




    if video is None:

        st.warning(
            "⚠️ Selecione um vídeo."
        )

        st.stop()


   
    if video.size > MAX_FILE_SIZE_BYTES:

        st.error(
            f"❌ O vídeo ultrapassa o limite de "
            f"{MAX_FILE_SIZE_MB} MB."
        )

        st.stop()


  

    extensao = video.name.lower().split(".")[-1]


    if extensao not in FORMATOS_VIDEO:

        st.error(
            "❌ O formato deste vídeo não é suportado."
        )

        st.stop()


    
    denuncia_id = (
        "VUL-"
        + datetime.now().strftime("%Y%m%d")
        + "-"
        + uuid.uuid4().hex[:6].upper()
    )


    data_envio = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )


    status = st.empty()

    progresso = st.progress(0)


    status.info(
        f"☁️ Enviando {denuncia_id}..."
    )


    progresso.progress(10)


    try:

       
        resultado = cloudinary.uploader.upload(
            video.getvalue(),

            resource_type="video",

            folder="vulcan_ant_cheaters",

            use_filename=True,

            unique_filename=True
        )


        progresso.progress(100)


     

        link_video = resultado["secure_url"]




        registro = {

            "id": denuncia_id,

            "titulo": titulo,

            "descricao": descricao,

            "data": data_envio,

            "arquivo": video.name,

            "formato": extensao.upper(),

            "tamanho": f"{video.size / (1024 * 1024):.2f} MB",

            "link": link_video,

            "status": "Concluído"
        }


        st.session_state.historico.insert(
            0,
            registro
        )


        st.session_state.ultima_denuncia = registro


      
        status.success(
            f"✅ {denuncia_id} enviado com sucesso!"
        )


        st.header("✅ Evidência enviada")


        st.success(
            f"Denúncia {denuncia_id} concluída."
        )


        st.write(
            f"**Arquivo:** {video.name}"
        )


        st.write(
            f"**Formato:** {extensao.upper()}"
        )


        st.write(
            f"**Tamanho:** {video.size / (1024 * 1024):.2f} MB"
        )


        st.subheader("🔗 Link público")


        st.code(
            link_video,
            language=None
        )


        st.link_button(
            "🎥 Abrir vídeo",
            link_video,
            use_container_width=True
        )


        st.info(
            "💡 Para copiar o link, clique no botão de copiar "
            "do campo acima."
        )




    except Exception as erro:

        progresso.empty()

        status.error(
            "❌ Erro durante o envio."
        )

        st.error(
            f"Não foi possível enviar o vídeo: {erro}"
        )



if st.session_state.historico:

    st.divider()

    st.header("📋 Histórico desta sessão")

    st.write(
        "As evidências abaixo foram enviadas durante esta sessão."
    )


    for item in st.session_state.historico:

        with st.expander(
            f"🛡️ {item['id']} — {item['titulo']}"
        ):

            st.write(
                f"**Data:** {item['data']}"
            )

            st.write(
                f"**Status:** {item['status']}"
            )

            st.write(
                f"**Arquivo:** {item['arquivo']}"
            )

            st.write(
                f"**Formato:** {item['formato']}"
            )

            st.write(
                f"**Tamanho:** {item['tamanho']}"
            )


            if item["descricao"]:

                st.write(
                    f"**Descrição:** {item['descricao']}"
                )


            st.write(
                "**Link:**"
            )


            st.code(
                item["link"],
                language=None
            )


            st.link_button(
                "🎥 Abrir vídeo",
                item["link"],
                use_container_width=True
            )




st.divider()


st.caption(
    "VULCAN ANT CHEATERS • Evidence Center"
)


st.caption(
    "Sistema de gerenciamento de evidências"
)


