# university_info.py

info_data = {
    "saludo": ["¡Hola! ¿En qué puedo ayudarte hoy?", "Saludos, bienvenido a la Universidad Nacional de Colombia, sede Medellín. ¿Cómo puedo asistirte?"],
    "informacion general": ["La Universidad Nacional de Colombia, Sede Medellín, es reconocida por su excelencia académica y su compromiso con la investigación y la innovación. Fundada en 1938, esta institución ha jugado un papel crucial en el desarrollo de la región de Antioquia, ofreciendo una amplia gama de programas en ingeniería, ciencias, arquitectura y humanidades. Su campus, conocido por su extensa vegetación y arquitectura moderna, crea un ambiente propicio para el estudio y la investigación, atrayendo a estudiantes de todo el país y del extranjero."],
    "admisiones": ["Puedes encontrar toda la información sobre el proceso de admisión en nuestra página web: https://admisiones.unal.edu.co/"],
    "programas academicos": ["Consulta los programas de pregrado en http://www.pregrado.unal.edu.co/programas-acred/ y los programas de postgrado en https://posgrados.unal.edu.co/catalogo/"],
    "programas disponibles": ["La universidad nacional ofrece distintos programas académicos que se encuentran en las siguientes facultades: facultad de arquitectura, facultad de ciencias, facultad de ciencias agrarias, facultad de ciencias humanas y económicas y por último está la facultad de minas. ¿Deseas conocer los programas ofrecidos en alguna facultad específica?"],
    "cursos capacitaciones": ["La oferta de cursos de educación continua la encuentras en https://medellin.unal.edu.co/educacioncontinua/ y los cursos de idiomas en https://centrodeidiomas.medellin.unal.edu.co/es/"],
    "bienestar universitario": ["Bienestar Universitario ofrece una variedad de servicios, incluyendo salud, deportes y cultura. Más detalles en https://bienestaruniversitario.medellin.unal.edu.co/"],
    "facultad arquitectura": ["La facultad de arquitectura ofrece programas en arquitectura, artes plásticas y construcción. Puedes encontrar más información en http://www.pregrado.unal.edu.co/programas-acred/"],
    "facultad ciencias": ["La facultad de ciencias ofrece estudios en estadística, ingeniería biológica, ingeniería física y matemáticas. Puedes encontrar más información en nuestro sitio web: http://www.pregrado.unal.edu.co/programas-acred/"],
    "facultad ciencias agrarias": ["En la facultad de ciencias agrarias puedes estudiar ingeniería agrícola, ingeniería agronómica, ingeniería forestal, tecnología forestal y zootecnia. Más detalles en http://www.pregrado.unal.edu.co/programas-acred/"],
    "facultad ciencias humanas economicas": ["La facultad de ciencias humanas y económicas ofrece programas en ciencia política, economía e historia. Consulta más información en nuestro sitio web: http://www.pregrado.unal.edu.co/programas-acred/"],
    "facultad minas": ["La facultad de minas ofrece ingenierías en administrativa, ambiental, civil, control, minas y metalurgia, petróleos, sistemas e informática, eléctrica, geológica, industrial, mecánica y química. Más detalles en http://www.pregrado.unal.edu.co/programas-acred/"],
    "biblioteca": ["Puedes encontrar la biblioteca en el edificio principal. Para pedir libros y conocer más sobre los servicios y el sistema de préstamo, visita nuestro sitio web: https://bibliotecas.unal.edu.co/"],
    "registro matricula": ["Toda la información sobre registro y matrícula la puedes encontrar en nuestro sitio web: https://registroymatricula.medellin.unal.edu.co/"],
    "tramites academicos": ["Toda la información sobre trámites para estudiantes y profesores, incluyendo información para cambiarte de carrera, la puedes encontrar en nuestro sitio web: https://registroymatricula.medellin.unal.edu.co/"],
    "ayuda general": ["Puedes preguntarme sobre: \n- Información general de la Universidad Nacional sede Medellín\n- Aplicar a un pregrado\n- Programas académicos y cursos disponibles\n- Servicios de bienestar universitario\n- Información sobre las facultades y la biblioteca\n- Trámites académicos\n ¿En qué más puedo ayudarte?"],
    "despedida": ["¡Adiós! Espero haberte sido de ayuda. ¡Vuelve pronto!", "Hasta luego, ¡espero que tengas un gran día!", "De nada, ¡estoy aquí para ayudarte cuando lo necesites!"]
}

def get_information(topic):
    # Devuelve la información relacionada con el tema solicitado
    return info_data.get(topic.lower(), "Lo siento, no tengo información sobre ese tema.")
