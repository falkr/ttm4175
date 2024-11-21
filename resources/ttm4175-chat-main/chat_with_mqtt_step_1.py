from chat_gui import ChatGui
import paho.mqtt.client as mqtt
import json

# TODO change to fit your team
my_id = "team1a"


# Called by MQTT client when we are connected
def on_connect(mqttc, obj, flags, rc):
    print("Connected: " + str(rc))


# Called by the MQTT client for every message we receive
def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    try:
        data = json.loads(msg.payload)
    except json.JSONDecodeError as e:
        print("The payload is not valid json!")
        print(e)
        return
    if msg.topic.endswith("message"):
        gui.receive(data["sender"], data["message"], data["uuid"])
    else:
        print("Unknown topic: {}".format(msg.topic))


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect("mqtt.item.ntnu.no", 1883)
mqttc.loop_start()
mqttc.subscribe("ttm4175/chat/{}/message".format("team1a"))


# Called by the Chat UI when we want to send a message
def on_send(sender, receiver, message, uuid):
    print("Sending {} --> {} {}".format(sender, receiver, message[:5] + "..."))
    payload_dict = {
        "sender": sender,
        "receiver": receiver,
        "message": message,
        "uuid": uuid,
    }
    payload_json = json.dumps(payload_dict)
    mqttc.publish("ttm4175/chat/{}/message".format(receiver), payload=payload_json)


# Called by the Chat UI when we start typing to somebody
def on_type(sender, receiver):
    print("Typing: {} --> {}".format(sender, receiver))


# Called by the Chat UI when we have read a message
def on_read(sender, receiver, uuid):
    print("Read: {} --> {} {}".format(sender, receiver, uuid[:5] + "..."))


gui = ChatGui(my_id, on_send=on_send, on_type=on_type, on_read=on_read)
gui.show()