# Descripción de la Propuesta:
Social Mentor es una API que emplea inteligencia artificial para generar ideas de contenido, sugerencias de
edición de contenido y emular un planificador de horarios de publicación.

## Generador de ideas
Utiliza un prompt que se completa con el tema del que se desea crear la idea, el tipo de contenido que se quiere
desarrollar y la cantidad de ideas que se desea.
```
Ejemplo de entrada:
Tema: Película Elementos
Tipo: Informativo
Cantidad de ideas: 1
Ejemplo de salida:
Sugerencias: Video con curiosidades de la película Elementos y un breve análisis de la película
```

## Consejero de contenidos
Utiliza un prompt que se completa con la idea propuesta, el tipo de contenido que se quiere desarrollar y
el formato del contenido (Imágenes o video) y detalla aspectos principales que debería tener dicha idea al
momento de llevarla a cabo.
```
Ejemplo de entrada: Tomaremos la idea de la primera salida
Idea: Curiosidades de la película Elementos y un breve análisis de la película
Tipo de contenido: Informativo
Formato: Video
Ejemplo de salida:
Música: El tema principal de la película Elementos
Efectos de sonido: Noticiero al inicio y al final del video
Duración estimada: 15 minutos
Transiciones: puedes utilizar una transición de entrada para cada sección y una de salida al final del video
Flujo de video: Cortos de las partes más importantes según lo que se está tratando
```

## Planificador
Se aspira a que se obtengan los datos de las API's de las redes sociales para analizar los días y horarios en los que se obtuvo
un mayor alcance en cada publicación y en base a eso se recomiendan los días y horas en las que es más recomendable publicar contenido.
Por lo pronto, esto emula el accedo a datos ficticios mediante un diccionario de posts y ejecuta un prompt para decidir los días y horas.
```
Ejemplo de salida:
Días: lunes, miércoles y domingo
Horas: 12h50, 17h40, 21h10, 22h00
```
