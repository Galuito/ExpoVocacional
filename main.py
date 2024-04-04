from flask import Flask, request, jsonify, render_template
import random
app = Flask(__name__)

greetings = [
    'Guten Tag!',
    'Bonjour!',
    '🤨🤨🤨🤨?',
    'Good morning!',
    'Also try Terraria',
    'Recuerden tomar fotos!',
    'No tengan miedo en hacer preguntas!',
    'Tú también puedes!',
    'Estos mensajes son al azar',
]

# Define una ruta básica para probar que el servidor está funcionando
@app.route('/')
def index():
    return '¡Servidor Flask funcionando correctamente!'

@app.route('/luis')
def luis():
    return render_template('card.html', recipient_name="Nathaniel", greeting_message="Bienvenido")

# Define un endpoint para recibir solicitudes GET
@app.route('/get_card', methods=['GET'])
def get_card():
    # Aquí puedes colocar la lógica para obtener datos
    return render_template('card.html')

@app.route('/generate_card', methods=['GET'])
def generate_card():
    return render_template('generate_card.html')

@app.route('/generate_card', methods=['POST'])
def send_card():
    name = request.form.get('name')
    random_greeting = random.choice(greetings)
    return render_template('card.html', recipient_name = name, greeting_message = random_greeting)

# Define un endpoint para recibir solicitudes POST
@app.route('/post_data', methods=['POST'])
def post_data():
    # Obtén los datos enviados en la solicitud POST
    data = request.json
    
    # Aquí puedes colocar la lógica para procesar los datos recibidos
    # Por ejemplo, puedes guardarlos en una base de datos, enviarlos al Arduino, etc.
    
    # Retorna una respuesta
    response = {'message': 'Datos recibidos correctamente', 'data': data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=42024)  # Ejecuta la aplicación en modo debug para facilitar la depuración
    print("App is running")
