from flask import Flask, jsonify, request
import openai
import csv

# API KEY
api_key = 'api_key'
openai.api_key = api_key
# APP FLASK
app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return """Bienvenido al Social Mentor
    Accesos:
    Ideas de contenido: /generar-ideas
    Consejos de contenido: /consejero-contenido
    PLanificador: /planificador
    """

@app.route('/planificador', methods=['GET'])
def planificador():
    registros = [
    {"idPost": 1, "nLikes": 100, "nComments": 234, "publishDate": "12-02-21", "publishTime": "12h50m23"},
    {"idPost": 2, "nLikes": 50, "nComments": 54, "publishDate": "14-02-21", "publishTime": "16h23m04"},
    {"idPost": 3, "nLikes": 23, "nComments": 87, "publishDate": "17-02-21", "publishTime": "19h12m45"},
    {"idPost": 4, "nLikes": 78, "nComments": 12, "publishDate": "20-02-21", "publishTime": "09h34m51"},
    {"idPost": 5, "nLikes": 209, "nComments": 76, "publishDate": "22-02-21", "publishTime": "14h17m32"},
    {"idPost": 6, "nLikes": 65, "nComments": 43, "publishDate": "25-02-21", "publishTime": "17h06m19"},
    {"idPost": 7, "nLikes": 172, "nComments": 98, "publishDate": "28-02-21", "publishTime": "20h55m07"},
    {"idPost": 8, "nLikes": 93, "nComments": 21, "publishDate": "03-03-21", "publishTime": "08h43m54"},
    {"idPost": 9, "nLikes": 45, "nComments": 67, "publishDate": "07-03-21", "publishTime": "12h32m41"},
    {"idPost": 10, "nLikes": 87, "nComments": 32, "publishDate": "10-03-21", "publishTime": "15h21m28"},
    {"idPost": 11, "nLikes": 33, "nComments": 76, "publishDate": "15-03-21", "publishTime": "22h09m15"},
    {"idPost": 12, "nLikes": 150, "nComments": 44, "publishDate": "19-03-21", "publishTime": "03h58m02"},
    {"idPost": 13, "nLikes": 76, "nComments": 54, "publishDate": "23-03-21", "publishTime": "07h46m49"},
    {"idPost": 14, "nLikes": 98, "nComments": 27, "publishDate": "28-03-21", "publishTime": "14h34m36"},
    {"idPost": 15, "nLikes": 63, "nComments": 88, "publishDate": "01-04-21", "publishTime": "18h23m23"},
    {"idPost": 16, "nLikes": 112, "nComments": 39, "publishDate": "05-04-21", "publishTime": "21h12m10"},
    {"idPost": 17, "nLikes": 41, "nComments": 63, "publishDate": "09-04-21", "publishTime": "00h00m57"},
    {"idPost": 18, "nLikes": 87, "nComments": 19, "publishDate": "14-04-21", "publishTime": "06h48m44"},
    {"idPost": 19, "nLikes": 56, "nComments": 73, "publishDate": "18-04-21", "publishTime": "10h37m31"},
    {"idPost": 20, "nLikes": 120, "nComments": 37, "publishDate": "22-04-21", "publishTime": "13h26m18"}
    ]
    diccionario = {}
    times = []
    days = []
    for registro in registros:
         id_post = registro["idPost"]
         diccionario[id_post] = registro
    for clave, valor in diccionario.items():
         id_post = valor["idPost"]
         n_likes = valor["nLikes"]
         n_comments = valor["nComments"]
         publish_date = valor["publishDate"]
         publish_time = valor["publishTime"]
         # Calcula el alcance ponderado combinando los likes y comentarios
         weighted_score = n_likes + n_comments
         # Aquí puedes ajustar los criterios para determinar las horas y días con mayor alcance
         if weighted_score >= 150:
              times.append(publish_date)
              days.append(publish_time)
    default_prompt = f"""Las horas y días con mayor alcance en mis publicaciones de Instagram son:
{times} {days}. ¿Cuándo debo publicar para obtener un alcance máximo? Solo responde con una lista de días (quiero solo el día de la semana) y una lista de horas
Completa la salida:
Días: 
Horas Factibles: """
    chatbot_response = generar_respuesta(default_prompt)
    return jsonify({'Planificación recomendada': chatbot_response.split("\n")})

@app.route('/generar-ideas', methods=['POST'])
def ideas():
    data = request.json
    tema = data.get('tema')
    tipo_contenido = data.get('tipo_contenido')
    n_ideas = data.get('n_ideas')

    default_prompt = """
    Como community manager, tu tarea es brindar n ideas de contenido (videos o imágenes)
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