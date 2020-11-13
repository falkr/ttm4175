
# Temperature Sensor System


In this (a little bit artificial) example, we want to create a temperature sensor that delivers its measurements tp a web server, so we can check the temperature from a web browser.
In addition, the web site should also show the air temperature forecast for the location from Yr.
This is what our system looks like:

---
type: figure
source: figures/http/smart-home.png
---

It should work in the following steps:

1. The temperature sensor sends its measured temperature with a HTTP `POST` request to the server. In our example, we do this only once, but in a real system the sensor would measure the temperature from a real sensor and then periodically send the temperature.

2. A web browser makes an HTTP `GET` request to the server, because we want to read the temperature.

3. To answer the request from the browser, the web server makes itself a request to Yr.no to figure out the air temperature. 

4. The web server then combines the temperature sent before from the sensor (via the `POST` request), combines it with the result of the request to Yr.no, and answer the browser with a HTML page that shows both temperatures.




# Code for the Sensor

As said, our program for the sensor just imitates how a real sensor would work. Here we just write the temperature fixed, and only send a single update instead of doing it periodically.

Store the following file in a file `sensor.py`.


```python
import requests
import json
from urllib.parse import quote, unquote


def dictionary_to_string(dictionary):
    return json.dumps(dictionary)


def encode_string_into_url(string):
    return quote(string)


def print_response(response):
    print("-------- Response --------")
    print("Status code: {}".format(response.status_code))
    print("-------- Content--------")
    print(response.text)
    print("------------------------")


# example data
dictionary = {}
dictionary["temperature"] = 20.0

data = dictionary_to_string(dictionary)
print(data)

data = encode_string_into_url(data)
print(data)

response = requests.post("http://localhost:8023/?data={}".format(data))
print_response(response)
```




# Code for the Server

The code for the server is longer, because it handles the `POST` request from the sensor, makes a `GET` request to Yr.no, and answers a `GET` request from a browser. 

Stor it in a file called `webserver.py`.


```python
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import quote, unquote
import json
import socket
import requests


def extract_json_string(string):
    start = string.find("{")
    stop = string.rfind("}")
    return string[start : stop + 1]


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


def dictionary_to_string(dictionary):
    return json.dumps(dictionary)


def json_string_to_dictionary(json_string):
    return json.loads(json_string)


def encode_string_into_url(string):
    return quote(string)


def decode_url_back_to_string(url_encoded_string):
    return unquote(url_encoded_string)


def string_to_unicode_bytes(string):
    return string.encode("utf-8")


places = {
    "Trondheim": {"lat": 63.43, "lon": 10.39},
    "Oslo": {"lat": 59.91, "lon": 10.75},
    "Bergen": {"lat": 60.39, "lon": 5.32},
    "Avaldsnes": {"lat": 59.35, "lon": 5.27},
    "Tromsø": {"lat": 69.64, "lon": 18.95},
}


def get_air_temp_2(place):
    coordinates = places[place]
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}".format(
        coordinates["lat"], coordinates["lon"]
    )
    response = requests.get(url)
    return response.json()["properties"]["timeseries"][-1]["data"]["instant"][
        "details"
    ]["air_temperature"]


def generate_html_page(title, local_temperature, air_temperature, place):
    lines = []
    lines.append("<html>")
    lines.append("    <head><title>{}</title></head>".format(title))
    lines.append("    <body>")
    lines.append(
        "        <p>Local temperature {}: <b>{} C</b></p>".format(
            place, local_temperature
        )
    )
    lines.append("        <p>Temperature: <b>{} C</b></p>".format(air_temperature))
    lines.append("    </body>")
    lines.append("</html>")
    return "\n".join(lines)


class RequestHandler(BaseHTTPRequestHandler):
    def store_data(self, name, data):
        if not hasattr(self.server, "data"):
            self.server.data = {}
        self.server.data[name] = data

    def load_data(self, name):
        if hasattr(self.server, "data"):
            if name in self.server.data:
                return self.server.data[name]
        return None

    def do_POST(self):
        """HTTP POST request as it comes from the sensor device application,
        for instance to send the current temerature."""

        print("-------- Incoming POST request --------")
        print("  Request data: {}".format(self.requestline))

        decoded_request = decode_url_back_to_string(self.requestline)
        print("  Decoded data: {}".format(decoded_request))

        json_string = extract_json_string(decoded_request)
        print("  Extracted JSON string: {}".format(json_string))

        dictionary = json_string_to_dictionary(json_string)
        print(dictionary)

        # We extract the temperature...
        temperature = dictionary["temperature"]
        # ...and store it
        self.store_data("temperature", temperature)

        # Phase 2: Which data do we want to send back?
        response = "ok"

        # Phase 3: Let's send back the data!
        response_in_bytes = string_to_unicode_bytes(response)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response_in_bytes)

    def do_GET(self):
        # Phase 1: What has been requested?
        print("-------- Incoming GET request --------")
        print("  Request data: {}".format(self.requestline))

        decoded_request = decode_url_back_to_string(self.requestline)
        print("  Decoded data: {}".format(decoded_request))

        json_string = extract_json_string(decoded_request)
        print("  Extracted JSON string: {}".format(json_string))

        dictionary = json_string_to_dictionary(json_string)
        print(dictionary)

        place = dictionary["place"]

        air_temperature = get_air_temp_2(place)
        local_temperature = self.load_data("temperature")

        # Phase 2: Which data do we want to send back?
        response = generate_html_page(
            "Temperature", local_temperature, air_temperature, place
        )

        # Phase 3: Let's send back the data!
        response_in_bytes = string_to_unicode_bytes(response)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response_in_bytes)


# This just starts the server
port = 8023
httpd = HTTPServer(
    ("", port),
    RequestHandler,
)
print("")
print(" ******** TTM4175 Web Server  ******** ")
print(
    "    The server will be reachable via  http://{}:{}/".format(get_ip_address(), port)
)
print("    Terminate the server via Ctrl-C.")
print(" ************************************* ")
print("")
httpd.serve_forever()
```

:task: Go through the code of the server, and try to understand what each function achieves. It is maybe not necessary to understand all details, but the coarse task of each line and function.


# Running it


**Step 1: Start the Server**

In a terminal window, start the server:

```bash
python3 webserver.py
```


**Step 2: Start the Sensor**

In another terminal window, start the sensor:

```bash
python3 sensor.py
```


Observe what happens in the terminal of the server.


**Step 3: Request from the Browser**

In a web browser, make the following request in the address field:

```
http://localhost:8023/?data={"place": "Trondheim"}
```



# Tasks


:task: Run the system as explained above, and document what happens in the terminal and the browser. Show screenshots. Does all work as expected?


(The code above should be complete, no changes are necessary.)


:task: Can you get the air temperature for any of the other cities? How?


:task: Observe how the address line in the browser changes after you press Enter and request the page. What happens here probably? How does the server take care of this?


:task: Look at the functions `do_POST()` and `do_GET()` in the server. What do they have in common, and what is different?
