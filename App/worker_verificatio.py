import pika
import json
import requests
# Se connecter à RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Déclarer une file d'attente nommée 'hello'
channel.queue_declare(queue='commandList')

# Fonction de rappel pour traiter les messages reçus
def callback(ch, method, properties, body):
    print(f" [x] Message reçu: {body}")
    json_string = body.decode('utf-8')
    result = json.loads(json_string)

    ##Verification par humain
    ##Stockage base de données 

    url = "http://localhost:3000/update-description2"
    '''data_web = {
        "description": result["description"]
    }
    response_from_web = requests.post(url, json=data_web)'''

    response_from_web = requests.post(url)
    print("Status Code", response_from_web.status_code)
    print("JSON Response ", response_from_web.json())
    ''' response = response_from_web.json()["message"]
    result["response"] = response
    result["devis"] = response_from_web.json()["prix"]
    print(result)
    
    
    print("demande vérifié! ")
    channel.basic_publish(exchange='',
                    routing_key='VerificationResult',
                    body=json.dumps(result))'''



# Indiquer à RabbitMQ d'appeler la fonction de rappel lorsque des messages sont reçus
channel.basic_consume(queue='commandList',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] En attente de messages. Pour sortir, appuyez sur CTRL+C')
channel.start_consuming()
