import os
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import json
import asyncio
import requests

##8000
app = FastAPI()


class Demande(BaseModel):
    nom: str
    prenom: str
    ville: str
    email: str
    description: str

class Verification(BaseModel):
    response: bool


@app.post("/effectue_commande/")
async def effectue_commande(demande: Demande):
    print(demande)
    demande_json = {
        "nom" : demande.nom,
        "prenom": demande.prenom,
        "ville": demande.ville,
        "email": demande.ville,
        "description": demande.description
    }
    # Lancer la tâche en arrière-plan
    response = requests.post("http://127.0.0.1:8001/reception_commande/", json=demande_json)
    print(demande)
    return {"message": "commande reçu et en cours de traitement"}

@app.post("/verification_commande/")
async def verification_commande(verification: Verification):
    if (verification):
        print("votre commande est valide.")
    else:
        print("votre commande est pas valide.")
    return("réponse reçu avec succès")

