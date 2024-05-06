import streamlit as st
import openai
from openai.error import APIError

# Configuración de Streamlit
st.set_page_config(page_title="NachoBot", page_icon=":robot_face:")

# Cliente de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Función para enviar y recibir respuestas del modelo de OpenAI
def ask_openai(question):
    try:
        response = openai.Completion.create(
            model="text-davinci-002",  # Asegúrate de que el modelo sea correcto
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except APIError as e:
        st.error(f"Error al conectar con OpenAI: {e}")
        return None

# Interfaz de usuario
st.title("Bienvenido a NachoBot")

# Inicializa el historial de chat si no existe
if 'history' not in st.session_state:
    st.session_state.history = []

# Entrada de chat del usuario
chat_input = st.text_input("Hazme una pregunta:", key="chat_input")

if chat_input:
    # Guarda la pregunta del usuario en el historial
    st.session_state.history.append({'role': 'user', 'message': chat_input})

    # Procesa la pregunta y obtiene una respuesta
    answer = ask_openai(chat_input)

    if answer:
        # Guarda la respuesta del bot en el historial
        st.session_state.history.append({'role': 'assistant', 'message': answer})

    # Limpia el input para la siguiente pregunta
    st.session_state.chat_input = ""

# Mostrar el historial de chat
for message in st.session_state.history:
    if message['role'] == 'user':
        with st.chat_message('You'):
            st.write(message['message'])
    elif message['role'] == 'assistant':
        with st.chat_message('NachoBot'):
            st.write(message['message'])

if __name__ == "__main__":
    st.main()
