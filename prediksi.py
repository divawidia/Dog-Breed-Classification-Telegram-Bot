import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from bot import path_to_tensor, ResNet50_predict_labels, dog_detector, Resnet50_predict_breed
from glob import glob 

model = None

def load_model():
    model = MobileNetV2(weights="imagenet")
    return model

def prediksi(image: Image.Image):
    global model
    if model is None:
        model = load_model()

    image = np.asarray(image.resize((224,224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0

    result = decode_predictions(model.predict(image), 2)[0]

    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"
        response.append(resp)
    return response


def read_imageFile(file)-> Image.Image:
    image = Image.open(BytesIO(file))
    return image