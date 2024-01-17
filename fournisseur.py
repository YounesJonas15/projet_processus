import os
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import json
import asyncio

app = FastAPI()

async def verificationDemande():
    await asyncio.sleep(2)
    print("demande vérifié! ")

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



