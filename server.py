from msilib.schema import File

from fastapi import FastAPI, UploadFile, File
import uvicorn
from starlette.responses import RedirectResponse
import prediksi

app = FastAPI()

# @app.get('/index')
# def hello_world():
#     return "hello world!"

@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")

@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Foto harus dengan format jpg, jpeg, atau png"
    image = prediksi.read_imageFile(await file.read())
    prediction = prediksi.prediksi(image)
    return prediction

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='localhost')
