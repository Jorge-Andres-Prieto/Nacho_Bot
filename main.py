import streamlit as st
import openai

# Configurar el título de la aplicación de Streamlit y la clave de API de OpenAI
st.title('🤖 NachoBot')
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Inicializar el estado de la sesión para almacenar los mensajes de la conversación
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": "Hola, ¿cómo puedo ayudarte?"}
    ]

# Función para obtener respuestas del modelo de OpenAI
def get_response(message):
    st.session_state.conversation_history.append({"role": "user", "content": message})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.conversation_history
        )
        reply = response.choices[0].message['content']
        st.session_state.conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Interfaz de usuario para entrada de chat
prompt = st.chat_input("¿Cómo puedo ayudarte?")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
