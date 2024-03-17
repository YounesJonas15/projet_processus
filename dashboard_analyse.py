import streamlit as st
import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt


parent_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(parent_dir, "App/db_fournisseur.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

st.title('Liste des commandes et clients')
for table in tables:
    table_name = table[0]
    st.write(table_name)

    cursor.execute(f"SELECT * FROM {table_name};")
    table_data = cursor.fetchall()

## Mettre les données dans un DataFrame
    df = pd.DataFrame(table_data)

## Afficher le DataFrame
    st.write(df)


cursor.execute("SELECT statut, count(*) AS number_c from demandes GROUP BY statut;")
status_data = cursor.fetchall()
print(status_data)
status_df = pd.DataFrame(status_data, columns=['Statut', 'Nombre de commandes'])


## Affichage du graphique
st.title('Nombre de commandes par statut')
fig, ax = plt.subplots()
ax.bar(status_df['Statut'], status_df['Nombre de commandes'])
ax.set_xlabel('Statut')
ax.set_ylabel('Nombre de commandes')
st.pyplot(fig)
