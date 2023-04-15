from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os 

load_dotenv()

API_KEY = os.getenv("FLASK_OPEN_AI_KEY")

openai.api_key = API_KEY

preamble = "Responde como chilango"

def magic(p):
    completion = openai.Completion.create(
        model = "text-davinci-003",
        prompt = f"{preamble} {p}",
        max_tokens = 500,
        temperature = 0.0
    )
    return completion.choices[0].text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/respuesta', methods=['POST'])
def respuesta():
    prompt = request.json['prompt']
    response = magic(prompt)
    return jsonify({'respuesta': response})

if __name__ == '__main__':
    app.run(debug=True)
