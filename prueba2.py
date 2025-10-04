import requests

# URL de tu servidor Flask/Gunicorn
url = "http://127.0.0.1:5000/get-response"


while 1:
    quest = input("Pregunta: ")

    response = requests.post(url, json={"message": quest})

    data = response.json()

    print("Bot response:", data["response"])
