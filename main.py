import streamlit as st
from openai import OpenAI, OpenAIError

# Configuración de Streamlit
st.set_page_config(page_title="NachoBot", page_icon=":robot_face:")

# Cliente de OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Función para enviar y recibir respuestas del modelo de OpenAI
def ask_openai(question):
    try:
        response = client.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except OpenAIError as e:
        st.error(f"Error al conectar con OpenAI: {e}")
        return None

# Interfaz de usuario
st.title("Bienvenido a NachoBot")
user_input = st.text_input("Hazme una pregunta:")

if user_input:
    with st.spinner('Pensando...'):
        answer = ask_openai(user_input)
        st.text_area("Respuesta:", value=answer, height=200)

if __name__ == "__main__":
    st.main()
