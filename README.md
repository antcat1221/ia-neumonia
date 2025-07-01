# Detección de neumonía a través de imágenes de rayos X usando CNN
Este proyecto consiste en el desarrollo de un sistema automatizado capaz de detectar neumonía en imágenes de rayos X utilizando redes neuronales convolucionales (CNN). Incluye una interfaz web para que los usuarios puedan subir imágenes y recibir un diagnóstico instantáneo, todo desplegado en la nube.

La neumonía es una enfermedad pulmonar que puede diagnosticarse mediante radiografías de tórax. Sin embargo, en zonas con poco acceso a radiólogos, este diagnóstico se dificulta. Este sistema busca ofrecer una herramienta accesible que, mediante inteligencia artificial, permita clasificar automáticamente imágenes de rayos X como "Normal" o "Neumonía".

## Tecnologías Usadas

- Python 3.12
- TensorFlow / Keras
- NumPy / Matplotlib
- Flask
- HTML / CSS / JavaScript
- Render (para despliegue)
- Dataset: [Chest X-Ray Images (Pneumonia) – Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

---

## 🧱 Arquitectura del Sistema

```plaintext
[Aplicación Web] --> [Servidor Flask con el modelo entrenado] --> [Diagnóstico automático]
        ↑                                                                   ↓
    Imagen del usuario                                              Imagen clasificada
```
## Entrenamiento del Modelo
El modelo fue entrenado utilizando el conjunto train del dataset de Kaggle. Se empleó una arquitectura CNN sencilla con capas Conv2D, MaxPooling2D y Dense. El entrenamiento se realizó por 10 épocas, alcanzando:

Precisión en entrenamiento: 99%

Precisión en validación: 100% en algunas épocas

---

## Despliegue
El sistema está desplegado en Render.com. La API recibe imágenes, las preprocesa, ejecuta el modelo CNN y retorna el diagnóstico como JSON.

Frontend: HTML + JavaScript

Backend: Flask + modelo .keras

Endpoint principal: POST /predecir

La aplicación está desplegada en el siguiente enlace: https://ia-neumonia.netlify.app/

---

## Resultados
El sistema devuelve dos tipos de diagnósticos:

* NORMAL
* PNEUMONIA