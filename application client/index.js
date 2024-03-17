// index.js
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
// Permet de setup EJS
app.set('view engine', 'ejs');
app.use(bodyParser.json());
const fetch = require("node-fetch")


let commande = {id: "Aucune commande.", etat: "#####",devis: "#####"}

app.get('/home', async (req, res) => {
    res.render('add_commande');
});

app.get('/validate_commande', async (req, res) => {
    res.render ('validate_commande', {commande});
});

app.post('/send_commande', async (req, res) => {
    console.log(req.body.nom)
    const url = "http://127.0.0.1:8000/effectue_commande/";

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(req.body),
    });

    if (response.ok) {
        const resultat = await response.json();
        console.log("Commande effectuée avec succès!", resultat);
        res.send('Réussi');
    } else {
        console.error("Erreur lors de l'effectuation de la commande:", response.status);
        
        res.status(response.status).send('ERROR:')
    }



})

app.post('/commande_to_validate', async (req, res) => {
    console.log(req.body)
    commande.id = req.body.id
    commande.etat = req.body.response
    commande.devis = req.body.devis
    console.log(commande)

    res.send("reçu avec succès, en attente de validation par le client")

})

app.post('/validate_devis', async (req, res) => {
    console.log(req.body)
    commande.etat = req.body.decision
    console.log(commande)
    const url = "http://127.0.0.1:8000/validate_devis/";

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({id : commande.id, response: commande.etat, devis: commande.devis}),
    });

    if (response.ok) {
        const resultat = await response.json();
        console.log("validation effectuée avec succès!", resultat);
        res.send('Réussi');
    } else {
        console.error("Erreur lors de l'effectuation de la commande:", response.status);
        
        res.status(response.status).send('ERROR:')
    }

    commande = {id: "Aucune commande.", etat: "#####",devis: "#####"}
    
    

})

const port = 3001;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}/home`);
});

