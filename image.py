from flask import Flask, render_template, request, redirect
from openai import OpenAI
import base64
from utils.config import settings

app = Flask(__name__)

# Configura tu clave API de OpenAI
client = OpenAI(api_key = settings.api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_imagen', methods=['POST'])
def generar_imagen():

    prompt = request.form['prompt']

    response = client.images.generate(
    model="dall-e-3",
    prompt= prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    response_format = 'b64_json'
    )

    b64_string = response.data[0].b64_json
    decoded = base64.b64decode(b64_string)
    
    fpath = 'static/imagenes/result.jpg'
    f = open(fpath,'wb')

    f.write(decoded)
    f.close()
 
    return render_template('resultado.html' )

if __name__ == '__main__':
    app.run(debug=True)

