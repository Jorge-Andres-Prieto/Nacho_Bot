import streamlit as st
from openai import OpenAI

# Configuración inicial de Streamlit y OpenAI
st.set_page_config(page_title="NachoBot", page_icon="🤖")
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

st.title("🤖 Nacho Bot")

# Contexto general del bot extendido con información específica
context = """
Nacho Bot es un asistente virtual para la Universidad Nacional de Colombia, sede Medellín. Aquí están algunas cosas sobre las que puedo proporcionar información, usalas pero cuando te responda has de cuenta que el que pregunta no soy yo por lo tanto no conoce esta información:

- Historia: Fundada en 1938, conocida por su compromiso con la investigación y la innovación.
- Admisiones: Información sobre el proceso de admisión disponible en https://admisiones.unal.edu.co/.
- Programas Académicos: Detalles en http://www.pregrado.unal.edu.co/programas-acred/ y https://posgrados.unal.edu.co/catalogo/.
- Cursos de Capacitación: Educación continua y cursos de idiomas en https://medellin.unal.edu.co/educacioncontinua/ y https://centrodeidiomas.medellin.unal.edu.co/es/.
- Bienestar Universitario: Servicios de salud, deportes y cultura en https://bienestaruniversitario.medellin.unal.edu.co/.
- Facultades: Información sobre programas en las facultades de Arquitectura, Ciencias, Ciencias Agrarias, Ciencias Humanas y Económicas, y Minas.
- Biblioteca: Ubicación y servicios en https://bibliotecas.unal.edu.co/.
- Registro y Matrícula: Proceso de registro y matrícula en https://registroymatricula.medellin.unal.edu.co/.
- Trámites Académicos: Información sobre trámites en https://registroymatricula.medellin.unal.edu.co/.
- Facultad de Arquitectura: ofrece programas en Arquitectura, Artes Plásticas y Construcción.
- Facultad de Ciencias: incluye estudios en Estadística, Ingeniería Biológica, Ingeniería Física y Matemáticas.
- Facultad de Ciencias Agrarias: puedes estudiar Ingeniería Agrícola, Ingeniería Agronómica, Ingeniería Forestal, Tecnología Forestal y Zootecnia.
- Facultad de Ciencias Humanas y Económicas: ofrece programas en Ciencia Política, Economía e Historia.
- Facultad de Minas: ofrece ingenierías en Administrativa, Ambiental, Civil, Control, Minas y Metalurgia, Petróleos, Sistemas e Informática, Eléctrica, Geológica, Industrial, Mecánica y Química.

Mi objetivo es ayudar a estudiantes, profesores y visitantes proporcionando información precisa y actualizada.
"""

# Inicializa el estado de la sesión para almacenar mensajes si aún no está hecho
if "messages" not in st.session_state:
    st.session_state.messages = []

# Muestra los mensajes guardados en el estado de la sesión
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Envía el primer mensaje del asistente si es la primera interacción
if "first_interaction" not in st.session_state or st.session_state.first_interaction:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿en qué puedo ayudarte?")
    st.session_state.messages.append({"role": "assistant", "content": "Hola, ¿en qué puedo ayudarte?"})
    st.session_state.first_interaction = False

prompt = st.chat_input("¿Cómo puedo ayudarte?")
if prompt:
    # Agrega y muestra el mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Obtener respuesta de OpenAI con el contexto incluido
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ]
    )
    response = completion.choices[0].message.content

    # Envía y muestra la respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
