from flask import Flask, render_template, request, redirect
from openai import OpenAI
import base64

app = Flask(__name__)

# Configura tu clave API de OpenAI
client = OpenAI(api_key = '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')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_imagen', methods=['POST'])
def generar_imagen():
    """
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
    
    fpath = 'templates/result.jpg'
    print(fpath) 

    f = open(fpath,'wb')

    f.write(decoded)
    f.close()
    """
    return render_template('resultado.html' )

if __name__ == '__main__':
    app.run(debug=True)

