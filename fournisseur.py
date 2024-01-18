import os
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import json
import asyncio
import requests
import pika 
import json
import uvicorn
##8001
app = FastAPI()

class Demande(BaseModel):
    nom: str
    prenom: str
    ville: str
    email: str
    description: str

class Verification(BaseModel):
    response: bool

async def verificationDemande(demande):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.basic_publish(exchange='',
                      routing_key='commandList',
                      body=demande)

    print(" [x] Message envoyé à la file d'attente 'commandList'")

    # Fermer la connexion
    connection.close()

   








@app.post("/reception_commande/")
async def recevoir_commande(demande: Demande, background_tasks: BackgroundTasks):
    print(demande)
    # Lancer la tâche en arrière-plan
    background_tasks.add_task(verificationDemande, demande.model_dump_json())
    return {"message": "commande reçu et en cours de traitement"}



@app.post("/verification_commande_fournisseur/")
async def verification_commande_fournisseur(verification: Verification):
    
    response = requests.post("http://127.0.0.1:8000/verification_commande/", json={"response" : verification.response})
    print(response.json())
    return("réponse reçu avec succès")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)