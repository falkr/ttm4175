#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import time


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mqttc, obj, mid):
    #print("mid: " + str(mid))
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    mqttc.publish('a/b/c/d')
    


def on_log(mqttc, obj, level, string):
    print(string)
    
    

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect('localhost', 1883)
mqttc.loop_start()


def test(topic):
    print('------ Subscribe to: {}'.format(topic))
    mqttc.subscribe(topic, 0)
    time.sleep(2)
    mqttc.unsubscribe(topic)

topics = ['#',
          '+/+/+',
'+/+/+/+',
'+/b/c/#',
'+/b/c/d',
'a/#',
'a/+/+/d',
'a/+/c/d',
'a/b/#',
'a/b/c',
'a/b/c/#',
'a/b/c/d/#',
'a/b/c/d',
'b/+/c/d',
'a/b/c/d/+']

for topic in topics:
    test(topic)
    
mqttc.loop_stop()