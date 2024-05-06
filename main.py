import streamlit as st
import openai

# Configurar el título de la aplicación de Streamlit
st.title('🤖 NachoBot')

# Inicializar el estado de la sesión para almacenar mensajes y la historia de la conversación
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": "Hola, ¿cómo puedo ayudarte?"}
    ]

# Configurar las claves de API de OpenAI usando el módulo secrets de Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Función para obtener respuestas del modelo de OpenAI
def get_response(message):
    try:
        st.session_state.conversation_history.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.conversation_history
        )
        reply = response.choices[0].message['content']
        st.session_state.conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Captura y maneja la entrada del usuario
prompt = st.chat_input("¿Cómo puedo ayudarte?")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Obtener respuesta del modelo OpenAI
    response = get_response(prompt)

    # Envía y muestra la respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
