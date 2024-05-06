import streamlit as st
import openai

# Configura el título de la aplicación de Streamlit
st.title('🤖 NachoBot')

# Configura la API key de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Inicializa el estado de la sesión para almacenar mensajes si aún no está hecho
if "messages" not in st.session_state:
    st.session_state.messages = []

if "first_message" not in st.session_state:
    st.session_state.first_message = True

# Muestra los mensajes guardados en el estado de la sesión
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Envía el primer mensaje del asistente si es la primera interacción
if st.session_state.first_message:
    welcome_message = "¡Hola! Soy NachoBot, aquí para responder tus preguntas sobre la Universidad Nacional de Colombia sede Medellín."
    with st.chat_message("assistant"):
        st.markdown(welcome_message)
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})
    st.session_state.first_message = False

# Captura y maneja la entrada del usuario
prompt = st.chat_input("¿Cómo puedo ayudarte?")
if prompt:
    # Agrega y muestra el mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Procesa la entrada del usuario usando OpenAI GPT-3.5 Turbo
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Estás hablando con NachoBot, un asistente virtual."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        # Acceso correcto a 'content'
        chat_response = response['choices'][0]['message']['content']
        with st.chat_message("assistant"):
            st.markdown(chat_response)
        st.session_state.messages.append({"role": "assistant", "content": chat_response})
    except Exception as e:
        print("Error al procesar la respuesta: ", e)

    # Envía y muestra la respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(response['choices'][0]['message']['content'])
    st.session_state.messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
