import os
import sqlite3

parent_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(parent_dir, "db_fournisseur.db")

def connection_bd():
    conn = sqlite3.connect(db_path)
    return conn

def close_connection(conn):
    conn.close()


def get_data(cursor):
    cursor.execute("SELECT * FROM demandes")
    data = cursor.fetchall()
    return data


def insert_tuples(conn,cursor,id, nom, prenom, email,description,statut,devis):
    try:
        sql_query = """INSERT INTO demandes (id, nom, prenom, email, description, statut, devis)
                        VALUES (?, ?, ?, ?, ?, ?, ?)"""
        
        values = (id, nom, prenom, email, description, statut, devis)
        
        cursor.execute(sql_query, values)
        

        conn.commit()
        
        print("Tuple inséré avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de l'insertion du tuple :", e)

conn= connection_bd()
cursor = conn.cursor()

def delete_all_rows(conn, cursor, table_name):
    try:
        sql_query = f"DELETE FROM {table_name};"
        cursor.execute(sql_query)
        conn.commit()
        
        print(f"Toutes les données de la table {table_name} ont été supprimées avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression des données :", e)

delete_all_rows(conn,cursor,"demandes")


data_to_insert = [
    (156, "Alice", "Dupont", "alice.dupont@example.com", "Réparation smartphone", "en cours", "notGenerated"),
    (157, "Bob", "Martin", "bob.martin@example.com", "Maintenance réseau", "validé", "300"),
    (158, "Laura", "Garcia", "laura.garcia@example.com", "Dépannage matériel", "en cours", "notGenerated"),
    (159, "David", "Lee", "david.lee@example.com", "Installation système d'exploitation", "payé", "600"),
    (160, "Sophie", "Lambert", "sophie.lambert@example.com", "Réparation imprimante", "validé", "400"),
    (161, "Thomas", "Nguyen", "thomas.nguyen@example.com", "Configuration logiciel", "en cours", "notGenerated"),
    (162, "Julie", "Fournier", "julie.fournier@example.com", "Réparation tablette", "payé", "450"),
    (163, "Antoine", "Girard", "antoine.girard@example.com", "Maintenance serveur", "validé", "700"),
    (164, "Marie", "Roy", "marie.roy@example.com", "Dépannage réseau", "en cours", "notGenerated"),
    (165, "Luc", "Lefebvre", "luc.lefebvre@example.com", "Installation antivirus", "en cours", "notGenerated"),
    (166, "Emma", "Moreau", "emma.moreau@example.com", "Réparation disque dur", "payé", "550"),
    (167, "Louis", "Dubois", "louis.dubois@example.com", "Configuration réseau sans fil", "validé", "800"),
    (168, "Chloé", "Gagnon", "chloe.gagnon@example.com", "Dépannage système", "en cours", "notGenerated"),
    (169, "Gabriel", "Bergeron", "gabriel.bergeron@example.com", "Installation périphérique", "payé", "500"),
    (170, "Léa", "Rousseau", "lea.rousseau@example.com", "Réparation voiture", "refusé", "notGenerated"),
    (171, "Nathan", "Lavoie", "nathan.lavoie@example.com", "Maintenance PC portable", "validé", "350"),
    (172, "Zoé", "Caron", "zoe.caron@example.com", "Configuration serveur", "en cours", "notGenerated"),
    (173, "Mia", "Martinez", "mia.martinez@example.com", "Dépannage logiciel", "en cours", "notGenerated"),
    (174, "Ethan", "Sanchez", "ethan.sanchez@example.com", "Installation système de sécurité", "payé", "700"),
    (175, "Manon", "Legrand", "manon.legrand@example.com", "installation meuble", "refusé", "notGenerated")
    
]


for data in data_to_insert:
    insert_tuples(conn, cursor, *data)

"""
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

# Requête pour vider la table "demandes"
'''sql_query = "DELETE FROM demandes;"

# Exécuter la requête
cursor.execute(sql_query)
conn.commit()'''

# Fermer la connexion
conn.close()
"""

# Requête pour vider la table "demandes"
'''sql_query = "DELETE FROM demandes;"

# Exécuter la requête
cursor.execute(sql_query)
conn.commit()'''


