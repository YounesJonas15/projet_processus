import os
import sqlite3

parent_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(parent_dir, "..", "db_fournisseur.db")

# Se connecter à la base de données
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Obtenir la liste des tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Afficher les tables existantes
if tables:
    print("Les tables existantes dans la base de données sont :")
    for table in tables:
        print(table[0])
else:
    print("Aucune table n'existe dans la base de données.")

cursor.execute("SELECT * FROM demandes;")
rows = cursor.fetchall()

# Afficher les résultats
if rows:
    print("Les tuples existants dans la table demandes sont :")
    for row in rows:
        print(row)
else:
    print("Aucun tuple n'existe dans la table demandes.")


# Fermer la connexion
conn.close()
