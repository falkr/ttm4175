Today you should realize the system we have already studied in the preparation. A Raspberry Pi with a Sense HAT acts as a temperature sensor in a smart home, which constantly reads the temperature and sends it to a web server with a HTTP **POST** request. The web server makes the temperature readable by offering a website to any clients. 


---
type: figure
source: figures/iot/smart-home.png
caption: "Sketch of the smart home system."
---


## Task: Sequence Diagram


Create again the sequence diagram from the lecture that shows three lifelines, one for the Raspberry Pi that is the sensor, one for the web server, and one for the browser. Add as many details to the diagram as you already know about, and make sure everyone in the team has the same understanding of the details. **Today, you will implement this sequence diagram!**

**For the report:** Include the sequence diagram and describe what is happening.


## Some Hints for Today:

You have several options how to work today, that means, on which machines.

* Ideally, work on a Raspberry Pi. You can run both the sensor client and the web server on the same Raspberry Pi. 
* You can also run the web server on a separate Raspberry Pi (this is more like the real system) but then you need to switch between Pis. 
* You can also work on the lab PCs or a private PC and implement most of the lab on it, as long as Python 3 is running on them.
* In the end, you should use a Pi for the sensor since you should read the real temperature from the Sense HAT.

## Task 1: Basic Webserver

Copy the following code into a file `webserver_1.py`. 

* Read carefully through the code, starting with line 52, and then the class of line 31. 
* Explain the code lines (especially 32 to ca. 45 to each other). This will be the core of what we do today.

<script src="https://gist.github.com/falkr/6c3025ec5f4278e5847bc469b9ad8b29.js"></script>


* Run the code.


**A detail:** You may see that the `do_GET()` function only has `self` as parameter (from the class), and does not have a return value. 
This may be surprising, since it should get the request as input and then compute an answer. However, see how the code above gets access to the request, namely via the attribute `self.requestline`. Similarly, the response is created by calling some functions on the parent class, for instance `self.wfile.write(response_in_bytes)`. So therefore the `do_GET()` does not have any input or return parameters. It's more a question of how the API is designed, the authors have made a decision here.


### Task 2.2: Request via Web Browser

* Either on the same machine, or (even better) on a different machine, access the website address that the server prints out in a browser.
* If you access the browser on the same machine, you can type `http://localhost:8000/` as address. Otherwise, use the IP address.
* What happens in the browser, and what happens in the command where the server program runs?
* Create a sequence diagram of what you have just observed, and annotate it with details that you find relevant.
* Answer the following questions:
    * In which format is the answer sent from the webserver to the client? Which steps are involved to convert the data for the response?
    * What happens if you send the request to the wrong port, for instance port `8001`?


### Task 1.2: Request from Python

A browser is not the only way to send a HTTP request. Another one is to create a HTTP request directly in Python. The following code creates an HTTP request in Python:

<script src="https://gist.github.com/falkr/a91d1a52173297e2c7a15a4df67320a7.js"></script>

* You need to adjust the address in the request. 
* Run the code while the server is active. Describe what happens.



## Task 2: Nicer HTML Output

Now that we can send a simple string as a response, let's make the answer more advanced and send a proper website in HTML. HTML is in principle also only a string, but the browser reads the formatting tags and created a nicely rendered page out of it. The following code contains a simple Python method that creates some HTML:

<script src="https://gist.github.com/falkr/d3140ef3386a7606a38ee83b9a7ba4ac.js"></script>

* Obviously, copy the code above into the web server file from above. Place the function just below the import statements, so that it is at the top level of the file. (Not within the class declaration.)
* Exchange the simple string in the web server so that it instead returns the HTML page created by this function.
* To make all correct and tidy, update the line where we set the content type so that it uses `self.send_header("Content-type", "text/html")`.

* Now go back to the browser, and access the website again. What changed?
* Can you set the title of the website?


## Task 3: Storing Data in the Server

Later the web server should store the temperature and other values that the sensors send in. So we need some way to store data in the web server. In a real system, this is done with data bases or more powerful storage solutions optimized to serve many requests. For our little server, just storing the data in a Python dictionary is enough. 

There are several ways of doing this, but we try to add the code only in the method that processes the GET requests.   Since the method is called for each request, we need to store the data in a central place. For that, we use the context of the server, and declare a variable there. Luckily, we can access the server object using the variable `self.server`. Have a look at the following code:

<script src="https://gist.github.com/falkr/de6d6534bbaebd3d6a4b98ac149c3863.js"></script>

* Add this code at a proper place in the method `do_GET()` 
* Add some code so that the counter is increased with each request.
* Add code to the HTML so that it prints the counter's value, and tells the reader in the browser that "this is the i-th request". 
* Answer the following questions: 
    * Why is it not working to just use a local variable declared within the `do_GET()` method? Why do we need to access the variable via `self.server.data`?


## Task 4: Sending Data to the Server

We can send additional data with our request, by appending it into the URL as follows:

    http://localhost:8000/?data={"time": "12:05", "temperature": 20.0, "humidity": 54.3}


### Task 4.1: Sending Data via the Browser

* Copy the URL from above, but adjust it to your IP address (if necessary). 
* Paste the entire URL with the data part into your browser. 
* Observe what happens in the address line after the response returns. Did the browser change the data?
* Check which information was received by the server. 
* Has the data been transformed somehow?


### Task 4.2: GET and POST on the Server

When we use HTTP to both request data and store data, we should use different HTTP commands for these tasks. To read a website, we alread use the **GET** command. To set data, we should use instead the **POST** command. In Task 4.1 above we have "misused" the browser, and let it make a GET request with the data. For making all neat and tidy, we should use a **POST** instead.

* Create a new file `webserver_2.py` with a copy of the original webserver.
* Add a function `do_POST():` **in addition** to the already existing `do_GET()` function.

We use from now on the `do_GET()` function to serve the web site that reports the stored values, and the function `do_POST()` to receive data from the temperature sensor. The web server can hence process two different requests: one for storing data, one for serving a website that presents the data.

### Task 4.3: Sending Data via Python Requests

We now want to send data from Python. Later, a sensor should do this automated and at constant intervals, for which we cannot use a browser.

<script src="https://gist.github.com/falkr/7959a3380f6835e900c43d374595bb6a.js"></script>

* Create a new client program with the code above. 
* Add the necessary lines to convert the code, use the included functions. 
* With the server from before running, execute the client code.
* Document what happens.



### Task 4.4: Storing Data in the Server

* Pay now attention to the method `do_POST()` in the server, and work on the incoming data to decode it. There are helper functions in the server code you can use. Among others, the function `extract_json_string(string)` is useful to extract a JSON string (within curly brackets) from a string.
* Re-create the incoming dictionary that originates at the client.
* Store it in the data dictionary. 


## Task 5: Periodic POSTS from the Raspberry Pi and Sense HAT

Create a client on the Raspberry Pi with the Sense HAT that periodically reads the temperature and humidity from the Sense HAT and sends a **POST** request to the web server. (Running on the same Pi or another one.)

### Task 5.1

* Start with a little program that reads the temperature from the Sense HAT and just prints it to the console. (Make that work, first.)
* Find out how to create a task in Python that is repeated (probably a loop?) every 10 seconds (some wait?), and create a program that reads the temperature very 10 seconds. Document the result.
* In addition to printing out, add the code to send the HTTP POST. Figure out how to include the data using JSON and all necessary serialization. You know all the building blocks for this task, you "just" have to set them together!



## Task 6: Temperature in the Browser

Prepare the `do_GET()` method in the web server so that it sends back an HTML page that displays the temperature (and humidity) that was stored.

* First, send some plain text data with just the value. 
* Try to send some nicer HTML that displays the values in a better readable form.
* Document the entire system for the report.

## Task 7: Optional Tasks

Now that the very basic stuff is running, you can play with it and extend the system further, so it gets more realistic. The following are examples of stuff to add:

* Log more values from the Sense HAT
* Also log the time
* Report on the website when the measurement was taken
