import streamlit as st
import requests
import base64
from io import BytesIO

# Adiciona CSS personalizado apenas para centralizar o título
st.markdown("""
    <style>
    .title {
        text-align: center;
        padding: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Título centralizado
st.markdown("<h1 class='title'>Chat - Stihl</h1>", unsafe_allow_html=True)

#API_URL = "http://localhost:8000/query"  # ajuste se seu backend estiver em outro endereço
API_URL = "https://6f75-2804-4458-fc00-5700-d47f-887a-887d-8e70.ngrok-free.app/query"

query = st.text_input("Digite sua pergunta:")

if st.button("Perguntar") and query:
    with st.spinner("Consultando..."):
        try:
            response = requests.post(API_URL, json={"query": query})
            res = response.json()
            resposta = res.get("document", "Sem resposta")
            image_base64 = res.get("image_base64", None)
            st.text_area("Resposta do Assistente", resposta, height=200)
            if image_base64:
                img_bytes = base64.b64decode(image_base64)
                st.image(BytesIO(img_bytes), caption=f"PDF: {res.get('pdf', '')}, Página: {res.get('page_number', '')}")
            else:
                st.info("Nenhuma imagem retornada.")
        except Exception as e:
            st.error(f"Erro: {e}")

# Rodapé
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 0.8em;'>Desenvolvido pela equipe Vent</p>",
    unsafe_allow_html=True
)