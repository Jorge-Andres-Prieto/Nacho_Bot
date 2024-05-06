import streamlit as st
import openai

# Configurar el título de la aplicación de Streamlit
st.title('🤖 NachoBot')

# Inicializa el estado de la sesión para almacenar mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

# Configurar las claves de API de OpenAI usando el módulo secrets de Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Función para obtener respuestas del modelo de OpenAI usando la nueva API
def get_response(message):
    client = openai.OpenAI()
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return completion['choices'][0]['message']['content']  # Corregido para acceder correctamente al contenido
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Envía el primer mensaje del asistente si es la primera interacción
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿cómo puedo ayudarte?")
    st.session_state.messages.append({
        "role": "assistant", "content": "Hola, ¿cómo puedo ayudarte?"
    })
    st.session_state.first_message = False

# Captura y maneja la entrada del usuario
prompt = st.chat_input("¿Cómo puedo ayudarte?")
if prompt:
    # Agrega y muestra el mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Obtener respuesta del modelo OpenAI
    response = get_response(prompt)

    # Envía y muestra la respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
