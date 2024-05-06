import streamlit as st
import openai

# Configuración de Streamlit
st.set_page_config(page_title="NachoBot", page_icon=":robot_face:")

# Cliente de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Inicialización del historial de chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def send_query():
    user_input = st.session_state.user_input
    if user_input:
        # Añadir mensaje del usuario al historial
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Llamar al modelo de OpenAI
        responses = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.chat_history,
            max_tokens=100,
            stop=None
        )

        # Añadir la respuesta al historial
        assistant_reply = responses["choices"][0]["message"]["content"]
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})

        # Mostrar la respuesta
        st.session_state.display_text += f"\n\nYou: {user_input}\nNachoBot: {assistant_reply}"

# Entrada de usuario
st.text_input("Enter a prompt:", key="user_input", on_change=send_query)

# Botón para enviar la consulta
st.button("Send", on_click=send_query)

# Mostrar el chat
if 'display_text' not in st.session_state:
    st.session_state.display_text = ""

st.markdown(st.session_state.display_text)
