from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

api_key = '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'
openai.api_key = api_key

class Idea(BaseModel):
    tema: str
    tipo_contenido: str
    n_ideas: str


def generar_respuesta(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000  # Ajusta este valor según tus necesidades
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

@app.post("/ideas")
#def generar_ideas(request: IdeaRequest):
def generar_ideas(idea: Idea):
    default_prompt = """Como community manager, tu tarea es brindar n ideas de contenido (videos)
    a realizar a partir de un tema dado y el tipo de contenido que se desea realizar, donde n es el
    número de ideas que se desean generar.
    Ejemplo:
    Tema: El día de la madre
    Tipo de contenido: Burlesco
    Cantidad de ideas: 1
    Idea: Puedes hacer un video sobre el tipo de mamá que no te gustaría tener.
    Tema: """ + idea.tema + "\nTipo de contenido: " + idea.tipo_contenido + "\nCantidad de ideas: " + idea.n_ideas + "\nIdea:"
    
    ideas = generar_respuesta(default_prompt).split("\n")
    return {"Ideas": ideas}
#http://127.0.0.1:8000/docs