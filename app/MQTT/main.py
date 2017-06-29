import paho.mqtt.client as mqtt
import json


from model.model_devices import create_reading


def parsedata(data):
    """This funcion parses the data for inserting to the database"""
    try:
        # First we get device id
        j = json.loads(data)
        for v in j:
            print v
        # Next we get the values
        dev_id = j["id"]
        val = j["v"]
        # And we parse the data into a dictionary
        datadict = {"dev_id": dev_id, "value": val}
        # We return a dictionary of the data
        return datadict
    except Exception as e:
        print e
        return False


def on_connect(client, userdata, flags, rc):
    # The callback for when the client receives a CONNACK response from the server.
    print "Connected with result code "+str(rc)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Topic1")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print msg.topic+" "+str(msg.payload)
    # Check valid json - add SQL insert here
    data = parsedata(msg.payload)
    if data:
        create_reading(data["dev_id"], data["value"])
    else:
        print "invalid data"
        # Implement mqtt response Here
        return


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Client connects to host on port, with timeout
client.connect("localhost")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()