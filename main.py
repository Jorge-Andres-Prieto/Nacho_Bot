import streamlit as st
from openai import OpenAI
import json

# Configuración inicial de Streamlit y OpenAI
st.set_page_config(page_title="NachoBot", layout="wide")
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

def get_openai_response(user_input):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": user_input}
        ]
    )
    response = completion.choices[0].message
    return response

# Interfaz del chat
st.title("NachoBot")
user_input = st.text_input("Ask NachoBot a question about Universidad Nacional de Colombia sede Medellín:", "")

if user_input:
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    st.session_state["chat_history"].append({"role": "user", "content": user_input})

    response = get_openai_response(user_input)
    st.session_state["chat_history"].append({"role": "assistant", "content": response})

    for message in st.session_state["chat_history"]:
        # Aseguramos que cada mensaje se maneje adecuadamente
        if message["role"] == "user":
            st.chat_message(message["content"], is_user=True)
        else:
            st.chat_message(message["content"], is_user=False)

# Guardando la historia de chat en la sesión para mantener el estado del chat
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
