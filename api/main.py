from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

# Initialize FastAPI app
app = FastAPI()

# FIXED: Absolute-safe model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "saved_models", "1")

print("Model path:", MODEL_PATH)
print("Model exists:", os.path.exists(MODEL_PATH))

# Load model
MODEL = tf.keras.models.load_model(MODEL_PATH)

# Class names
class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']


#  Image preprocessing function
def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).convert("RGB")   # ensure 3 channels
    image = image.resize((256, 256))                   # match model input
    image = np.array(image).astype("float32")  
    return image


# Health check API
@app.get("/ping")
async def ping():
    return {"message": "alive"}


#  Prediction API
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read file
        data = await file.read()
        print("File size:", len(data))

        if len(data) == 0:
            return {"error": "Empty file received"}

        # Convert to image
        image = read_file_as_image(data)
        image = np.expand_dims(image, axis=0)

        print("Image shape:", image.shape)

        # Predict
        predictions = MODEL.predict(image)
        print("Predictions:", predictions)

        # Extract result
        predicted_index = int(np.argmax(predictions[0]))
        predicted_class = class_names[predicted_index]
        confidence = float(np.max(predictions[0]))

        result = {
            "class": predicted_class,
            "confidence": confidence
        }

        print("RESULT:", result)

        return result

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}

#  Run server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)