import streamlit as st
import openai

# Configuración de la API de OpenAI utilizando los secrets
openai.api_key = st.secrets["openai"]["api_key"]

def get_openai_response(user_input):
    """
    Esta función toma la entrada del usuario y devuelve la respuesta del modelo de OpenAI.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Soy NachoBot, aquí para responder tus preguntas sobre la Universidad Nacional sede Medellín."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content']

def main():
    """
    Función principal que ejecuta la aplicación de Streamlit.
    """
    st.title('NachoBot - Universidad Nacional de Colombia sede Medellín')
    user_input = st.text_input("Hazme una pregunta sobre la universidad:")

    if st.button("Enviar"):
        if user_input:
            respuesta = get_openai_response(user_input)
            st.chat_message(message=respuesta, is_user=False)  # Muestra la respuesta del bot

if __name__ == "__main__":
    main()
