from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

class Modelo:
    def __init__(self):
        self.model = {}
        self.cargado = False
    
    def cargar_modelo(self):
        self.model = load_model('modelo_entrenado.h5')
        self.cargado = True
        return "Modelo cargado correctamente"
    
    def modeloCargado(self):
        return self.cargado
    
    def predecir(self, imagen):
        img = image.load_img(imagen, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = self.model.predict(img_array)
        score = float(prediction[0][0])

        umbral = 0.8
        if score > umbral:
            mensaje = f"Resultado: Neumonía ({score*100:.2f}%)"
        else:
            mensaje = f"Resultado: Normal ({(1-score)*100:.2f}%)"

        return { "msg": mensaje }

modelo = Modelo()

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    cargado = modelo.modeloCargado()

    if cargado == True:
        return { "msg": "Servicio funcionando." }
    else:
        modelo.cargar_modelo()
        return Response("", 500)

@app.route("/predecir", methods=['POST'])
@cross_origin()
def predecir():
    if request.method == 'POST':
        archivo = request.files['imagen']
        print(archivo)
        if archivo:
            ruta = os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename)
            archivo.save(ruta)
            resultado = modelo.predecir(ruta)
            os.remove(ruta)
            return resultado

if __name__ == '__main__':
    print(modelo.cargar_modelo())
    app.run(debug=True)