from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = FastAPI()

# load your FINAL model
model = load_model("plant_disease_model.keras")

class_names = [
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato_healthy'
]

@app.get("/")
def home():
    return {"message": "Krushi Mitra ML API running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = Image.open(file.file).resize((224,224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)

    prediction = class_names[np.argmax(pred)]
    confidence = float(np.max(pred)) * 100

    response = {
        "prediction": prediction,
        "confidence": confidence
    }

    if confidence < 50:
        response["warning"] = "Low confidence prediction"

    return response
