from azure.eventhub import eventhub_producer_client, EventData
import json

#Remember to give DB service principal access to key vault
EVENT_HUB_CONNECTION_STR = dbutils.secrets.get(scope="key-vault", key="Eventhubconnection")

#EVENT_HUB_CONNECTION_STR = "XXX"
#Conect using a connection string & send data to the event hub.
producer = eventhub_producer_client.EventHubProducerClient.from_connection_string(conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME)

#function to send events to event hub
def send_event(event_data):
    #create batches for sending events
    event_data_batch = producer.create_batch()
    #dumb files as json to event hub
    event_data_batch.add(EventData(json.dumps(event_data)))
    producer.send_batch(event_data_batch)

#Send and close the producer
#send_event(event_data)
#producer.close()

