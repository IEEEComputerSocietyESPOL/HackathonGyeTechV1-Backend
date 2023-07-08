from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

class IdeaRequest(BaseModel):
    tema: str
    tipo_contenido: str
    n_ideas: int

api_key = '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'
openai.api_key = api_key

def generar_respuesta(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000  # Ajusta este valor según tus necesidades
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

@app.post("/ideas")
def generar_ideas(request: IdeaRequest):
    tema = request.tema
    tipo_contenido = request.tipo_contenido
    n_ideas = request.n_ideas

    default_prompt = """Como community manager, tu tarea es brindar n ideas de contenido (videos)
    a realizar a partir de un tema dado y el tipo de contenido que se desea realizar, donde n es el
    número de ideas que se desean generar.
    Ejemplo:
    Tema: El día de la madre
    Tipo de contenido: Burlesco
    Cantidad de ideas: 1
    Idea: Puedes hacer un video sobre el tipo de mamá que no te gustaría tener.
    Tema: """ + tema + "\nTipo de contenido: " + tipo_contenido + "\nCantidad de ideas: " + str(n_ideas) + "\nIdea:"
    
    chatbot_response = generar_respuesta(default_prompt)
    ideas = chatbot_response.split("\n")[1:]  # Obtener las ideas de contenido sin la primera línea

    return {"ideas": ideas}
