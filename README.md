# MartianCore Assistant

Este proyecto implementa **el backend** de un asistente para la vida en Marte.  
Recibe preguntas del usuario (por ejemplo: *"¿Está lloviendo afuera?"* o *"Qué temperatura hay?"*), selecciona la función más adecuada y genera una respuesta clara y útil usando **modelos de lenguaje de Hugging Face (FLAN-T5)**.

> ⚠️ Durante la hackathon usamos **FLAN-T5** porque los portátiles eran poco potentes. Esto hace que los modelos tengan más dificultad interpretando correctamente el lenguaje y generando respuestas con razonamiento propio. Cabe destacar que **el modelo que selecciona la función más adecuada funciona correctamente** incluso en portátiles modestos; sin embargo, para la parte que interpreta los resultados y genera la respuesta final, se necesita un modelo más potente. Hemos probado con modelos más grandes y las respuestas son claramente mejores. Creemos que usando modelos más potentes, los resultados serían mucho más precisos y completos.

The backend is developed in Python using Flask and leverages Hugging Face models for natural language processing. We used relatively lightweight models due to limited resources during the hackathon, but tests run with more powerful models produced significantly better results. The goal, with NASA’s resources, would be to train a specialized model tailored for this specific task.
The system is based on a modular design with a set of functions that process different types of data. One ML model determines which functions are relevant according to the user’s query, and another interprets the results together with the user’s request to generate clear and actionable responses. This modular design allows new functions to be easily added as new challenges or data arise.
In other words, the system consists of two main modules: the first selects the most optimal tools from a set of available ones, and the second uses them to provide accurate yet simple responses to the user.
The idea is that the functions accessible to the model perform the complex calculations themselves—such as measuring temperature through sensors, retrieving current resource levels from the database, analyzing local radiation, or predicting upcoming sandstorms. The possibilities are virtually limitless.
The crucial part is that, since we know ML models are probabilistic and not well-suited for performing precise calculations, they act only as interpreters. The functions from the system’s catalog handle the complex computations, while the ML model simply “translates” them into a more understandable form for the user. Therefore, the model does not require extremely exhaustive or specialized training—it only needs to understand human language well and explain results clearly, allowing it to generalize to new functions without needing retraining.

El **frontend** del proyecto se encuentra aquí:  
[hackaton_nasa (frontend)](https://github.com/sebasgit27/hackaton_nasa)

---

## ⚙️ Tecnologías usadas
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/) – Servidor web
- [Flask-CORS](https://flask-cors.readthedocs.io/) – Soporte CORS
- [Transformers (Hugging Face)](https://huggingface.co/transformers/) – Modelos NLP (`flan-t5-large`)

---

## Levantar el servidor

``` bash
python3 Servidor_MartianCore.py
```
