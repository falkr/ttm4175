# MQTT Broker (For Teaching Staff)


We run a Mosquitto MQTT Broker on the server `mqtt20.iik.ntnu.no` on standard port 1883.
To log into the server, you need a username, provided by [Pål Sæther](mailto:pal.sather@ntnu.no).


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

