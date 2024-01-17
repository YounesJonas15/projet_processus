import requests
from fastapi import FastAPI, BackgroundTasks
from suds.client import Client
import tkinter as tk

url = "http://127.0.0.1:8000/effectue_commande/"

app = FastAPI()

def recup_info():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    ville = entry_ville.get()
    email = entry_email.get()
    description = entry_description.get()
    root.destroy()

    data = {
    "nom": nom,
    "prenom": prenom,
    "ville": ville,
    "email": email,
    "description": description

    }

    response = requests.post(url, json=data)

    
    try:
        if response.text:
            print(response.json())
        else:
            print("La réponse est vide.")
    except requests.exceptions.JSONDecodeError:
        print("La réponse n'est pas au format JSON.")
        print("Contenu brut de la réponse:", response.text)

# Création de l'interface utilisateur
root = tk.Tk()
root.title("Formulaire de demande de prêt")

label_nom = tk.Label(root, text="Nom : ")
label_nom.grid(row=0, column=0)
entry_nom = tk.Entry(root)
entry_nom.grid(row=0, column=1)

label_prenom = tk.Label(root, text="Prénom : ")
label_prenom.grid(row=1, column=0)
entry_prenom = tk.Entry(root)
entry_prenom.grid(row=1, column=1)

label_ville = tk.Label(root, text="Ville : ")
label_ville.grid(row=2, column=0)
entry_ville = tk.Entry(root)
entry_ville.grid(row=2, column=1)

label_email = tk.Label(root, text="Email : ")
label_email.grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

label_type = tk.Label(root, text="Description du service : ")
label_type.grid(row=4, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=4, column=1)


submit_button = tk.Button(root, text="Soumettre", command=recup_info)
submit_button.grid(row=9, column=1)

root.mainloop()




