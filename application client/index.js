// index.js
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
// Permet de setup EJS
app.set('view engine', 'ejs');
app.use(bodyParser.json());
const fetch = require("node-fetch")


let commandes = {description: "Aucune commande.", devis: "hidden"}

app.get('/home', async (req, res) => {
    res.render('add_commande');
});

app.get('/add_commande', async (req, res) => {
    res.render ('add_commande')});

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

const port = 3001;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}/home`);
});

