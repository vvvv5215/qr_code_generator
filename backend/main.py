import segno
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/api/ping')
def ping():
    return {"ping": "pong"}

@app.post("/api/generate")
async def form(item: Request):
    try:
        data = await item.json()
        url = data["url"]
        qrcode = segno.make(url, micro=False)
        qr = qrcode.svg_data_uri(scale=10)
        return {"qr": qr}
    except Exception as err:
        print(err)
        return {
            "error": str(err),
        }


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/ping')
def ping():
    return {"ping": "pong"}

@app.post("/api/generate")
async def form(item: Request):
    try:
        data = await item.json()
        url = data["url"]
        qrcode = segno.make(url, micro=False)
        qr = qrcode.svg_data_uri(scale=10)
        return {"qr": qr}
    except Exception as err:
        print(err)
        return {
            "error": str(err),
        }