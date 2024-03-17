import pika
import requests
import json
# Se connecter à RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Déclarer une file d'attente nommée 'hello'
channel.queue_declare(queue='VerificationResult')

# Fonction de rappel pour traiter les messages reçus
def callback(ch, method, properties, body):
    print(f" [x] Message reçu: {body}")
    json_string = body.decode('utf-8')
    result = json.loads(json_string)
    print(result)

    response = requests.post("http://127.0.0.1:8000/verification_commande/", json={"id": result["id"], "response" : result["response"], "devis" : result["devis"]})
    print(response.json())

    #response = requests.post("http://127.0.0.1:8001/verification_commande_fournisseur/", json={"response" : result['response']})
    #print(response.json())
        

# Indiquer à RabbitMQ d'appeler la fonction de rappel lorsque des messages sont reçus
channel.basic_consume(queue='VerificationResult',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] En attente de messages. Pour sortir, appuyez sur CTRL+C')
channel.start_consuming()
