import pika
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
    response = False 
    result["response"] = response
    print(result)
    
    
    print("demande vérifié! ")
    channel.basic_publish(exchange='',
                    routing_key='VerificationResult',
                    body=json.dumps(result))



# Indiquer à RabbitMQ d'appeler la fonction de rappel lorsque des messages sont reçus
channel.basic_consume(queue='commandList',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] En attente de messages. Pour sortir, appuyez sur CTRL+C')
channel.start_consuming()
