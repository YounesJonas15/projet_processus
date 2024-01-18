import requests
from fastapi import FastAPI, BackgroundTasks
from suds.client import Client
import tkinter as tk
import httpx

def envoi_devis():
    url_reception_devis = "http://127.0.0.1:8000/reception_devis/"

    devis = {"montant": 1000}  # Remplacez par les données réelles de votre devis

    response = httpx.post(url_reception_devis, json=devis)

    if response.status_code == 200:
        print("Devis envoyée avec succès à l'API de réception de devis")
    else:
        print(f"Échec de l'envoi du devis. Code d'erreur : {response.status_code}")

envoi_devis()
