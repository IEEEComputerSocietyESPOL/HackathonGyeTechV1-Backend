from fastapi import FastAPI
from pydantic import BaseModel
import openai

# API KEY
api_key = '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'
openai.api_key = api_key

class Idea(BaseModel):
    tema: str
    tipo_contenido: str
    n_ideas: str

@app.route('/',methods=["GET"])
def index():
    return "Hello World"

# BODY
@app.route('/generar-ideas', methods=['POST'])
def ideas():
    data = request.json
    tema = data.get('tema')
    tipo_contenido = data.get('tipo_contenido')
    n_ideas = data.get('n_ideas')

    default_prompt = """
    Como community manager, tu tarea es brindar n ideas de contenido (videos)
    a realizar a partir de un tema dado y el tipo de contenido que se desea realizar, donde n es el
    número de ideas que se desean generar.
    Ejemplo:
    Tema: {}
    Tipo de contenido: {}
    Cantidad de ideas: {}
    Idea:
    """.format(tema, tipo_contenido, n_ideas)
    
    chatbot_response = generar_respuesta(default_prompt)
    return jsonify({'ideas_de_contenido': chatbot_response.split("\n")})

def generar_respuesta(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000  # Ajusta este valor según tus necesidades
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

@app.route('/consejero-contenido', methods=['POST'])
def consejero():
    data = request.json
    idea = data.get('Idea')
    tipo = data.get('Tipo_Contenido')
    formato = data.get('Formato')
    default_prompt = """Como Community Manager, experto en redes sociales, edición de videos e imágenes y publicación de contenido, necesito que me brindes sugerencias según el formato (imagen o video) y tipo de contenido que te indique, y las directrices que tengo q usar para hacer la idea de un contenido dada, bajo el formato "Tipo de sugerencia": "descripción de 5 palabras máximo", recuerda limitar la descripcion de la sugerencia a 5 palabras. Ejemplo:
Idea: Mis gatitos bailando Cha cha chá
Formato: video
Tipo de contenido: gracioso
Sugerencias:
Música: Los pollitos dicen
Efectos de sonido: claxson, niños gritando
Duración estimada: 40 segundos
Transiciones: No
Flujo de video (limítate a 5 secuencias máximo): cortos que muestren a los gatos moviéndose, acercamientos y alejamientos
En el caso de las imágenes:
Idea: Taller de Docker
Formato: Imágenes
Tipo de contenido: informativo
Sugerencias:
Cantidad máxima: 4 a 6
Gama de colores:  Azul, negro
Color de tipografía: Blanco
Tipografía: Arial Black
Sé breve, no digas que estas son solo sugerencias y demás, solo lo que te he pedido
Idea: {}
Tipo: {}
Formato: {}
Sugerencias:""".format(idea, tipo, formato)
    chatbot_response = generar_respuesta(default_prompt)
    return jsonify({'Sugerencias': chatbot_response.split("\n")})

# Ejecucion Flask
if __name__ == '__main__':
    app.run(debug=True, port=4000)
