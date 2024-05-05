import streamlit as st
from openai import OpenAI
import openai

# Configurar las claves de API de OpenAI usando el módulo secrets de Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]


# Inicializar el chatbot
def get_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response['choices'][0]['message']['content']


# Configurar la página
st.title('NachoBot - Chatbot de la Universidad Nacional')
st.write('Bienvenido al chatbot de la Universidad Nacional de Colombia sede Medellín. ¿En qué puedo ayudarte hoy?')

# Caja de entrada de mensajes
user_input = st.text_input("Escribe tu pregunta aquí:")

# Mostrar y manejar la conversación
if user_input:
    # Obtener la respuesta del modelo
    bot_response = get_response(user_input)

    # Simular el chat
    st.chat_message(user="Tú", message=user_input)
    st.chat_message(user="NachoBot", message=bot_response)
