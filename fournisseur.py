import os
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import json
import asyncio
import requests
import pika 
import json
##8001
app = FastAPI()

class Demande(BaseModel):
    nom: str
    prenom: str
    ville: str
    email: str
    description: str

async def verificationDemande(demande):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='commandList')
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=demande)

    print(" [x] Message envoyé à la file d'attente 'hello'")

    # Fermer la connexion
    connection.close()

    await asyncio.sleep(2)
    response = True 
    if(response):
        print("demande vérifié! ")
        response = requests.post("http://127.0.0.1:8000/verification_commande/", json={"response" : response})
        print(response.json())








@app.post("/reception_commande/")
async def recevoir_commande(demande: Demande, background_tasks: BackgroundTasks):
    print(demande)
    # Lancer la tâche en arrière-plan
    background_tasks.add_task(verificationDemande, demande.model_dump_json())
    return {"message": "commande reçu et en cours de traitement"}



