# MartianCore Assistant

Este proyecto implementa **el backend** de un asistente para la vida en Marte.  
Recibe preguntas del usuario (por ejemplo: *"¿Está lloviendo afuera?"* o *"Qué temperatura hay?"*), selecciona la función más adecuada y genera una respuesta clara y útil usando **modelos de lenguaje de Hugging Face (FLAN-T5)**.

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