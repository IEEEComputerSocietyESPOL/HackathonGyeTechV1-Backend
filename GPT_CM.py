import openai

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

continuar = "s"
while continuar != "n":
    tema = input("Tema: ")
    tipo_contenido = input("Tipo de contenido: ")
    nIdeas = input("Cantidad de ideas: ")
    default_promp = """Como community manager, tu tarea es brindar n ideas de contenido (videos)
    a realizar a partir de un tema dado y el tipo de contenido que se desea realizar, donde n es el
    número de ideas que se desean generar.
    Ejemplo:
    Tema: El día de la madre
    Tipo de contenido: Burlesco
    Cantidad de ideas: 1
    Idea: Puedes hacer un video sobre el tipo de mamá que no te gustaría tener.
    Tema: """ + tema + "\nTipo de contenido: " + tipo_contenido + "\nCantidad de ideas: " + nIdeas + "\nIdea:"
    
    chatbot_response = generar_respuesta(default_promp)
    print("Ideas de Contenido:\n", chatbot_response)

    continuar = input("¿Continuar? s/n: ")
    if continuar.lower() == "n":
        print("Chatbot: Hasta luego. ¡Gracias por la conversación!")