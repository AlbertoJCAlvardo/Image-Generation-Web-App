from flask import Flask, render_template, request, redirect
from openai import OpenAI
import base64
from utils.config import settings
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Configura tu clave API de OpenAI
client = OpenAI(api_key = settings.api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_imagen', methods=['POST'])
def generar_imagen():

    prompt = request.form['prompt']
    ancho = int(request.form['ancho'])
    alto = int(request.form['alto'])

    dimensiones = [ '1024x1024', '1024x1792', '1792x1024'] 

    if ancho>0 and alto>0 and f"{ancho}x{alto}" in dimensiones:
        response = client.images.generate(
        model="dall-e-3",
        prompt= prompt,
        size=f"{ancho}x{alto}",
        quality="standard",
        n=1,
        response_format = 'b64_json'
        )

        b64_string = response.data[0].b64_json

        decoded = base64.b64decode(b64_string)

        image = Image.open(BytesIO(decoded)).convert("RGB")    
        fpath = 'static/imagenes/result.jpg'
        image.save(fpath, "jpeg")
    
        return render_template('resultado.html' )
    else:
        return "Error!"

if __name__ == '__main__':
    app.run(debug=True)

