import streamlit as st
from openai import OpenAI

# Configuración inicial de Streamlit y OpenAI
st.set_page_config(page_title="NachoBot", layout="wide")
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# Inicializa el estado de la sesión para almacenar mensajes si aún no está hecho
if "messages" not in st.session_state:
    st.session_state.messages = []

# Muestra los mensajes guardados en el estado de la sesión
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("¿Cómo puedo ayudarte?")
if prompt:
    # Agrega y muestra el mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Obtener respuesta de OpenAI
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant skilled in university related queries."},
            {"role": "user", "content": prompt}
        ]
    )
    response = completion.choices[0].message

    # Envía y muestra la respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
