// index.js
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const Database = require('better-sqlite3');

// Permet de setup EJS
app.set('view engine', 'ejs');
app.use(bodyParser.json());


//utilisation de sqllite
const sqlite3 = require('sqlite3').verbose();
const dbPath = '../App/db_fournisseur.db';





// Récupérer tous les tuples de la table "demandes"buttons-container

let commandes = [];
let commandes_preparation = []
function fetchData(commandes) {  

    // Ouvrir une connexion à la base de données
    const db = new Database(dbPath);
    try {
        const rows = db.prepare('SELECT * FROM demandes').all();
       
        rows.forEach(demande => {
            if(demande.statut == 'recus') {
            d = {
                id: demande.id,
                description : demande.description,
                devis : ""
            }
            
            
            commandes.push(d)
        }
        })
    } catch (err) {
        console.error(err.message);
    } 
    
    db.close((err) => {
        if (err) {
            console.error(err.message);
        }
        console.log('Déconnexion de la base de données SQLite');
    });
}

function fetchDataPreparation(commandes) {  

    // Ouvrir une connexion à la base de données
    const db = new Database(dbPath);
    try {
        const rows = db.prepare('SELECT * FROM demandes').all();
       
        rows.forEach(demande => {
            if(demande.statut == 'payé') {
            d = {
                id: demande.id,
                description : demande.description,
                devis : ""
            }
            
            
            commandes.push(d)
        }
        })
    } catch (err) {
        console.error(err.message);
    } 
    
    db.close((err) => {
        if (err) {
            console.error(err.message);
        }
        console.log('Déconnexion de la base de données SQLite');
    });
}


function validateCommande(id, validate, prix) {
    const db = new Database(dbPath);


    try {
        
        let sqlQuery = ``
        if (validate == true) {
        sqlQuery = `
        UPDATE demandes
        SET statut = 'valide', devis = $prix
        WHERE id = $id
        `;}
        else {
        sqlQuery = `
        UPDATE demandes
        SET statut = 'non valide'
        WHERE id = $id
        `;
        }
        
        const result = db.prepare(sqlQuery).run({
            prix : prix,
            id : id
        });
    } catch (err) {
        console.error(err.message);
    }

    db.close((err) => {
        if (err) {
            console.error(err.message);
        }
        console.log('Déconnexion de la base de données SQLite');
    });

}





let description = 'Aucune Description'


let decision = null
let prix = 0

app.get('/home2', async (req, res) => {
    commandes = []
    fetchData(commandes)
    res.render('home2', { commandes });
});

app.get('/commande_preparation', async (req, res) => {
    commandes_preparation = []
    fetchDataPreparation(commandes_preparation)
    res.render('commande_preparation', { commandes_preparation });
});


app.post('/update-description2', async (req, res) => {
    commandes = []
    fetchData(commandes)
    res.send({message: "reçu"})

});
app.post('/update-decision2', async (req, res) => {
    if (!req.body) {
        return res.status(400).json({ error: 'Le corps de la requête est invalide.' });
    }
    commandes = commandes.filter(commande => commande.id !== req.body.id)
    console.log(req.body)
    validateCommande(parseInt(req.body.id), req.body.decision, req.body.devis)
    const url = "http://127.0.0.1:8001/verification_commande_fournisseur/";
    
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({"id" : req.body.id, "response" : req.body.decision,"devis" : req.body.devis}),
    });
    

    res.send("réussi")

})



const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}/home2`);
});
