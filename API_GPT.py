# Importar librerias
from flask import Flask, jsonify, request
import openai

# API KEY
api_key = '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'
openai.api_key = api_key

# APP FLASK
app = Flask(__name__)

# BODY
@app.route('/generar-respuesta', methods=['POST'])
def generar_respuesta():
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
        max_tokens=2000
    )
    generated_text = response.choices[0].text.strip()
    return generated_text




# Ejecucion Flask
if __name__ == '__main__':
    app.run(debug=True, port=4000)