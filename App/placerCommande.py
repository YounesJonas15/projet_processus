import os
from fastapi import FastAPI, BackgroundTasks
import pika
from pydantic import BaseModel
import json
import asyncio
import requests
import httpx
import uvicorn
from schema import DemandeBase

##8000
app = FastAPI()




class Verification(BaseModel):
    response: bool


@app.post("/effectue_commande/")
async def effectue_commande(demande: DemandeBase):
    print(demande)
    demande_json = {
        "nom" : demande.nom,
        "prenom": demande.prenom,
        "ville": demande.ville,
        "email": demande.email,
        "description": demande.description
    }
    response = requests.post("http://127.0.0.1:8001/reception_commande/", json=demande_json)
    print(demande)
    return {"message": "commande reçu et en cours de traitement"}

@app.post("/verification_commande/")
async def verification_commande(verification: Verification):
    if (verification.response):
        print("votre commande est valide.")
    else:
        print("votre commande est pas valide.")
    return("réponse reçu avec succès")



class devis (BaseModel):
      montant: int 

@app.post("/reception_devis/")
async def reception_devis(devis: devis, background_tasks: BackgroundTasks):
    print(devis)

    background_tasks.add_task(verificationDevis, devis.model_dump_json(), background_tasks)
    return {"message": "Devis  reçu et en cours de traitement"}
    

async def verificationDevis(devis: devis, background_tasks: BackgroundTasks):
    reponse = True
    if reponse:
        print("devis accepté")
        background_tasks.add_task(envoyer_notification,notification_text)

    return reponse



def envoyer_notification(notification_text):
    url_reception_paiement = "http://127.0.0.1:8003/reception_paiement/"

    data = {"notification": notification_text}

    response = httpx.post(url_reception_paiement, json=data)

    if response.status_code == 200:
        print("Notification envoyée avec succès à l'API de réception de paiement")
    else:
        print(f"Échec de l'envoi de la notification. Code d'erreur : {response.status_code}")


notification_text = "Paiement reçu avec succès"



if __name__ == "__main__":
    uvicorn.run("placerCommande:app", host="127.0.0.1", port=8000, reload=True)
