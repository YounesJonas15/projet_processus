import os
import random
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import json
import asyncio
import requests
import pika 
import json
import uvicorn
from sqlalchemy.orm import Session
from db_fournisseur import engine, SessionLocal
from schema import  DemandeBase, DemandeCreate , Verification
from models import Demande, Base

#Concernant la Base de donnée 
def create_demande(db: Session, demande: DemandeCreate):
    
    random_id = random.randint(1, 1000)
    db_demande = Demande(
        id=random_id,
        email=demande.email,
        nom=demande.nom,
        prenom=demande.prenom,
        description=demande.description,
        statut="recus",
        devis = "notGenerated"  
    )
    db.add(db_demande)
    db.commit()
    db.refresh(db_demande)
    return db_demande



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)


##8001
app = FastAPI()

   
@app.post("/reception_commande/")
async def recevoir_commande(demande: DemandeBase, background_tasks: BackgroundTasks):
    print(demande)
    # Lancer la tâche en arrière-plan
    background_tasks.add_task(verificationDemande, demande.model_dump_json())
    background_tasks.add_task(create_demande, next(get_db()), demande)
    return {"message": "commande reçu et en cours de traitement"}




async def verificationDemande(demande):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.basic_publish(exchange='',
                      routing_key='commandList',
                      body=demande)

    print(" [x] Message envoyé à la file d'attente 'commandList'")

    # Fermer la connexion
    connection.close()

async def verificationCommande(verification):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.basic_publish(exchange='',
                      routing_key='VerificationResult',
                      body=verification)

    print(" [x] Message envoyé à la file d'attente 'VerificationResult'")

    # Fermer la connexion
    connection.close()

async def verificationDevis(db: Session, verification):
    if(verification.response == True):
        db.query(Demande).filter_by(id=verification.id).update({Demande.statut: "payé"})
    else:
        db.query(Demande).filter_by(id=verification.id).update({Demande.statut: "non payé"})

    db.commit()
    
        
        


     


@app.post("/verification_commande_fournisseur/")
async def verification_commande_fournisseur(verification: Verification, background_tasks: BackgroundTasks):
    background_tasks.add_task(verificationCommande, verification.model_dump_json())
    #response = requests.post("http://127.0.0.1:8000/verification_commande/", json={"response" : verification.response})
    #print(response.json())
    return("réponse reçu avec succès")



@app.post("/verification_devis/")
async def verification_devis(verification: Verification, background_tasks: BackgroundTasks):
    
    
    background_tasks.add_task(verificationDevis, next(get_db()), verification)
    #response = requests.post("http://127.0.0.1:8000/verification_commande/", json={"response" : verification.response})
    #print(response.json())
    return("OK")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)