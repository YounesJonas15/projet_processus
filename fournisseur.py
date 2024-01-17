import os
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import json
import asyncio
import requests
##8001
app = FastAPI()

async def verificationDemande():
    await asyncio.sleep(2)
    response = True 
    if(response):
        print("demande vérifié! ")
        response = requests.post("http://127.0.0.1:8000/verification_commande/", json={"response" : response})
        print(response.json())




class Demande(BaseModel):
    nom: str
    prenom: str
    ville: str
    email: str
    description: str


@app.post("/reception_commande/")
async def recevoir_commande(demande: Demande, background_tasks: BackgroundTasks):
    print(demande)
    # Lancer la tâche en arrière-plan
    background_tasks.add_task(verificationDemande)
    return {"message": "commande reçu et en cours de traitement"}



