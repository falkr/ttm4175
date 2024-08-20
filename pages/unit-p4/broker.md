# MQTT Broker (For Teaching Staff)



:warning:
This is only for teaching staff and maintenance of the MQTT broker, as a student you don't need to access the
server directly. 


We run a Mosquitto MQTT Broker on the server `mqtt20.iik.ntnu.no` on standard port 1883.
To log into the server, you need access that is provided by Pål Sæther.


## Mosquitto Configuration


Mosquitto needs to be configured using the file `/etc/mosquitto/mosquitto.conf`:


```
# Place your local configuration in /etc/mosquitto/conf.d/
#
# A full description of the configuration file is at
# /usr/share/doc/mosquitto/examples/mosquitto.conf.example

persistence true
persistence_location /var/lib/mosquitto/

log_dest file /var/log/mosquitto/mosquitto.log

include_dir /etc/mosquitto/conf.d

listener 1883
allow_anonymous true
```

## Mosquitto Service


Starting the service:

```bash
sudo systemctl start mosquitto
```

Restarting the service:

```bash
sudo systemctl restart mosquitto
```

Checking the log file for diagnosis:

```bash
sudo tail /var/log/mosquitto/mosquitto.log
```

