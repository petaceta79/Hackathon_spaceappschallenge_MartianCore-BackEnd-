# librerias 
from transformers import pipeline
from flask import Flask, request, jsonify
from flask_cors import CORS







# prueba
def funcion0():
    return "raining"
def funcion1():
    return "10:00am"
def funcion2():
    return "35 grados"
def funcion3():
    return "05%"
def funcion4():
    return "80kg"







# Descarga y carga un modelo text-to-text 
generator_sel_func = pipeline("text2text-generation", model="google/flan-t5-large", device=-1)
generator_final_answer = pipeline("text2text-generation", model="google/flan-t5-large", device=-1)
# mejor modelo flan-t5-xl


# Declaracion de las funciones 
funciones_desc = {
    -1: "No relevant function for this query",
     0: "Check weather conditions like rain, temperature, or wind",
     1: "Get the current time on Mart",
     2: "Retrieve the temperature outside",
     3: "Retrieve the humidity level",
     4: "Returns the amount of food available"
}

funciones_dir = {
    0: funcion0,
    1: funcion1,
    2: funcion2,
    3: funcion3,
    4: funcion4
}


# Funcion que prepara el prompt para el seleccionador
def prompDesign_function_chooser(quest):
    prompt = "You are a system that selects the most relevant function based on the user's query.\n"
    prompt += "Functions:\n"

    for idx, desc in funciones_desc.items():
        prompt += f"{idx}: {desc}\n"
    prompt += 'Query: "' + quest + '"\nAnswer:'

    return prompt

# Dado la pregunta devuelve que funcion seria la mas indicada
def most_adecuated_function(quest):
    respuesta = generator_sel_func(prompDesign_function_chooser(quest))
    return respuesta[0]['generated_text']


# Dado un numero ejecuta una funcion y devuleve su resultado
def ejecutar_funcion(idx):
    if (idx == -1):
        return "No data available"
    return funciones_desc[idx] + ': ' + str(funciones_dir[idx]())


# Funcion para diseñar el prompt para la respuesta final
def prompDesign_final_answer(quest, func_to_use):
    prompt = """You are a personal assistant managing a Mars habitat.
        Answer the user's question with clear and elaborated sentences, 
        giving useful advice for survival and daily life. 
        Do not repeat the question, only give the answer.

        Examples:
        User: "How much radiation is outside?" 
        Info: "Radiation level: 70%"
        Answer: "Radiation levels are at 70%. That is quite high, it is safer to stay inside the habitat today."

        User: "Do we have enough water?" 
        Info: "Water tanks at 40%"
        Answer: "Water tanks are only 40% full. It would be wise to reduce consumption and plan for rationing."

        User: "How much oxygen is left in the tanks?"  
        Info: "No data available"  
        Answer: "I don’t have the latest oxygen tank data right now, but oxygen is a critical resource on Mars, so please check the life support system manually to be safe."  

        Now follow the same style.

        """

    prompt += "\nInformation:\n"
    prompt += f'User: "{quest}"\n'
    prompt += f'Info: "{ejecutar_funcion(int(func_to_use))}"\n'
    prompt += "Answer:"
    return prompt


def final_answer(quest, func_to_use):
    respuesta = generator_final_answer(
            prompDesign_final_answer(quest, func_to_use),
            max_new_tokens=80,   # límite razonable
            num_return_sequences=1
        )
    return respuesta[0]['generated_text']


# Para levantar el servidor 
# python3 Servidor_MartianCore.py
# venv -> source venv/bin/activate

app = Flask(__name__)
CORS(app)


@app.route("/get-response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "")

    func_to_use = most_adecuated_function(user_message)
    response_text = final_answer(user_message, func_to_use)

    return jsonify({"response": response_text})

if __name__ == "__main__":
    # host="0.0.0.0" permite recibir requests desde otros PCs en la misma red
    app.run(host="0.0.0.0", port=5000, debug=True)
