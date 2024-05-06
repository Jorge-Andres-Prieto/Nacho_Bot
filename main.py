import streamlit as st
from openai import OpenAI

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
    except Exception as e:
        st.error("Error al conectar con OpenAI: " + str(e))
        return None

# Interfaz de usuario
st.title("Bienvenido a NachoBot")
user_input = st.text_input("Hazme una pregunta:")

if user_input:
    with st.spinner('Pensando...'):
        answer = ask_openai(user_input)
        st.text_area("Respuesta:", value=answer, height=200)

# Principal
if __name__ == "__main__":
    st.main()
