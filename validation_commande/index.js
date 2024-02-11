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
const dbPath = '../projet_processus/App/db_fournisseur.db';





// Récupérer tous les tuples de la table "demandes"buttons-container

let commandes = [];
function fetchData(commandes) {
    

    // Ouvrir une connexion à la base de données
    const db = new Database(dbPath);


    try {
        const rows = db.prepare('SELECT * FROM demandes').all();
        console.log(rows); // Afficher les lignes récupérées
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
    console.log("commande validé")
    res.send("réussi")

})

app.post('/update-description', async (req, res) => {
    try {
        if (!req.body) {
            return res.status(400).json({ error: 'Le corps de la requête est invalide.' });
        }
        // Récupérer la description depuis le corps de la requête POST
        const newDescription = req.body.description;
        
        decision = null
        commandes.description = newDescription
        commandes.devis = ""
        while (decision === null) {
            // Attente courte pour éviter de bloquer le serveur
            await new Promise(resolve => setTimeout(resolve, 1000));
        }

        if (decision === true) {
            // Répondre avec un message de succès
        res.send({ message: true, prix: prix });
        commandes = {description: "Aucune commande.", devis: "hidden"}
        }
        else {
            res.send({message: false, prix: 0})
        }
    } catch (error) {
        console.error('Erreur lors de la mise à jour de la description:', error);
        res.status(500).send({ error: 'Erreur lors de la mise à jour de la description.' });
    }
});

app.post('/update-decision', async (req, res) => {
    decision = req.body.decision
    prix = req.body.devis
    commandes = {description: "Aucune commande.", devis: "hidden"}
    res.send("réussi")

});

const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}/home2`);
});
