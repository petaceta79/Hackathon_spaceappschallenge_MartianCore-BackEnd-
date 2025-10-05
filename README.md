# MartianCore Assistant

**MartianCore Assistant** is the backend of an intelligent chatbot designed to support daily life in a Martian colony.  
It receives user queries (for example: *“Is it raining outside?”* or *“What’s the current temperature?”*), selects the most suitable function, and generates clear, actionable responses using **Hugging Face language models (FLAN-T5)**.

> During the hackathon, we used **FLAN-T5** due to limited laptop performance.  
> This resulted in reduced language understanding and reasoning capabilities.  
> However, **the module responsible for selecting the most appropriate function works reliably**, even on modest hardware.  
> The component that interprets results and formulates the final response, on the other hand, requires a more powerful model.  
> Tests with larger models have shown **significantly better and more complete answers**, suggesting that with NASA-level resources, results could be far more accurate and comprehensive.

---

## Overview

The backend is developed in **Python** using **Flask** and leverages **Hugging Face** models for natural language processing.  
We used relatively lightweight models due to limited resources during the hackathon, but experiments with more powerful ones yielded much better results.  
Our long-term goal, with NASA’s resources, is to **train a specialized model** tailored specifically for Martian operational needs.

The system follows a **modular design**, composed of multiple functions that process different types of data.  
One ML model determines which functions are relevant to the user’s query, and another interprets the outputs together with the request to produce **clear, concise, and useful responses**.  
This modular structure allows new capabilities to be added easily as new data sources or operational challenges emerge.

In simpler terms, the system is built around **two core modules**:
1. **Selector Module** – Chooses the most optimal tools from a set of available ones.  
2. **Interpreter Module** – Executes those tools and generates accurate yet easily understandable responses for the user.

The idea is that the functions accessible to the model handle all the complex computations — for example:
- Measuring temperature from environmental sensors  
- Retrieving resource levels from the colony’s database  
- Analyzing local radiation  
- Predicting incoming sandstorms  

The possibilities are virtually limitless.

Since ML models are **probabilistic** and not ideal for precise calculations, they act only as **interpreters**.  
The functions in the system’s catalog perform the heavy computational tasks, while the ML model simply “translates” the outputs into human-readable responses.  
This approach means the model doesn’t require extensive or highly specialized training — it only needs strong language understanding and explanation skills, enabling it to **generalize to new functions without retraining**.

---

## Frontend

The **frontend** for this project can be found here:  
[hackaton_nasa (frontend)](https://github.com/sebasgit27/hackaton_nasa)

It features an interactive web interface built with **React**, allowing users to chat with the assistant, explore its capabilities, and receive responses in a friendly and intuitive way.

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
