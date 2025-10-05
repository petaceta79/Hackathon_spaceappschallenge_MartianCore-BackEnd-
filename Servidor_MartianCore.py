# libraries 
from transformers import pipeline
from flask import Flask, request, jsonify
from flask_cors import CORS


# Test functions for the MVP (Here would be calculations with data from sensors, NASA information...)
def weatherFunc():
    return "sunny"
def timeFunc():
    return "10:00am"
def tempFunc():
    return "35 grados"
def humidityFunc():
    return "05%"
def foodFunc():
    return "Meat: 20 kg, Vegetables: 10 kg, Water: 35 L"
def radiationFunc():
    return "70%"
def oxygenFunc():
    return "40%"



# Download and upload a text-to-text template
# It is better to connect CUDA to use the GPU, because of our resources we must use the CPU
generator_sel_func = pipeline("text2text-generation", model="google/flan-t5-large", device=-1) 
generator_final_answer = pipeline("text2text-generation", model="google/flan-t5-large", device=-1)
# Due to our limitations we used very low-power models, but we have found that with better models the responses are much better.


# Declaration of functions
funciones_desc = {
    -1: "No relevant function for this query",
     0: "Check weather conditions like rain, temperature, or wind",
     1: "Get the current time on Mart",
     2: "Retrieve the temperature outside",
     3: "Retrieve the humidity level",
     4: "Returns the amount of food available",
     5: "Returns the quantity of radiation",
     6: "Return de percentage of oxygen"
}
funciones_dir = {
    0: weatherFunc,
    1: timeFunc,
    2: tempFunc,
    3: humidityFunc,
    4: foodFunc,
    5: radiationFunc,
    6: oxygenFunc
}


# Function that prepares the prompt for the selector
def prompDesign_function_chooser(quest):
    prompt = "You are a system that selects the most relevant function based on the user's query.\n"
    prompt += "Functions:\n"

    for idx, desc in funciones_desc.items():
        prompt += f"{idx}: {desc}\n"

    prompt += f'Query: "{quest}"\n'
    prompt += "Answer with only the number corresponding to the most relevant function. Do not include any text or explanation.\n"
    prompt += "Answer:"

    return prompt

# Given the question, it returns which function would be the most appropriate.
def most_adecuated_function(quest):
    respuesta = generator_sel_func(prompDesign_function_chooser(quest))
    return respuesta[0]['generated_text']


# Given a number, execute a function and return its result.
def ejecutar_funcion(idx):
    if (idx == -1):
        return "No data available"
    return funciones_desc[idx] + ': ' + str(funciones_dir[idx]())


# Function to design the prompt for the final response
def prompDesign_final_answer(quest, func_to_use):
    prompt = """You are a personal assistant managing a Mars habitat.
        Answer the user's question with clear and elaborated sentences, 
        giving useful advice for survival and daily life. 
        Do not repeat the question, only give the answer.

        Examples:
        User: "Is it raining outside?"  
        Info: "Rain 60%"  
        Answer: "There is a 60% chance of rain. You should carry protective gear or stay inside if possible."

        User: "What's the current temperature?"  
        Info: "-20°C"  
        Answer: "The temperature is currently -20°C. Make sure to wear appropriate clothing to stay warm."

        User: "How are our food supplies?"  
        Info: "Meat: 15 kg, Vegetables: 12 kg, Water: 40 L"  
        Answer: "The food reserves are: Meat: 15 kg, Vegetables: 12 kg, Water: 40 L. Everything is mostly sufficient for now."

        User: "How much oxygen is in the cabin?"  
        Info: "55%"  
        Answer: "The cabin oxygen level is at 55%. It's functional but should be monitored and replenished soon."

        User: "How much fuel is left for the rover?"  
        Info: "No data available"  
        Answer: "I don’t have the latest fuel data for the rover right now, so please check the system manually before planning any trips."
 

        Now follow the same style.

        """

    prompt += "\nInformation:\n"
    prompt += f'User: "{quest}"\n'
    prompt += f'Info: "{ejecutar_funcion(int(func_to_use))}"\n'
    prompt += "Answer:"
    return prompt

# Function that returns the final answer
def final_answer(quest, func_to_use):
    respuesta = generator_final_answer(
            prompDesign_final_answer(quest, func_to_use),
            max_new_tokens=80,   # límite razonable
            num_return_sequences=1
        )
    return respuesta[0]['generated_text']


# Flask server declaration
app = Flask(__name__)
CORS(app)

# Method configuration
@app.route("/get-response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "")

    func_to_use = most_adecuated_function(user_message)
    response_text = final_answer(user_message, func_to_use)

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
