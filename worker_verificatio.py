import pika

# Se connecter à RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Déclarer une file d'attente nommée 'hello'
channel.queue_declare(queue='hello')

# Fonction de rappel pour traiter les messages reçus
def callback(ch, method, properties, body):
    print(f" [x] Message reçu: {body}")

# Indiquer à RabbitMQ d'appeler la fonction de rappel lorsque des messages sont reçus
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] En attente de messages. Pour sortir, appuyez sur CTRL+C')
channel.start_consuming()
