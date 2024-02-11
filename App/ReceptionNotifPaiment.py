from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Notification(BaseModel):
    notification: str

@app.post("/reception_paiement/")
async def reception_paiement(notification_data: Notification):
    print(notification_data.notification)

if __name__ == "__main__":
    uvicorn.run("ReceptionNotifPaiment:app", host="127.0.0.1", port=8003, reload=True)
