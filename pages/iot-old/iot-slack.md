# The Slack API

The goal of this task is to send a message to Slack.


## Step: Create a Slack Workspace

* Create a new Slack Workspace, via [this link](https://slack.com/create#email).
* Add the other team members, and check that you can send messages.


## Step: Register a Slack App

Before you can interact with Slack from another program, you have to tell the Slack API about that.
This enables the access to the API and you will receive tokens you can use for authentication.


:steps:
1. Visit [https://api.slack.com/apps](https://api.slack.com/apps).
2. Click on **Create New App**.
3. Select a name for your app (like _TTM4175 Alarm_).
4. Select the workspace you want to use (the one created above).

## Step: Create a Bot User

Now we need to configure our Slack App. For the alarm app, we want a Bot user to send a message on behalf of the application. 

:steps:
1. Under _Add features and functionality_, select **Bots**.
2. Add a Bot User, and select proper names for it.


## Step: Install the App

:steps:
1. Go back  to the app overview page [https://api.slack.com/apps](https://api.slack.com/apps).
2. Click on your app and go to its _Basic Information_ page.
3. Select **Install your app to your workspace**, and click on **Install App to Workspace**
4. Grant the suggested permissions, and click **Allow**


## Step: Get the Access Tokens


:steps:
1. Go back  to the app overview page [https://api.slack.com/apps](https://api.slack.com/apps).
2. Click on your app and go to its _OAuth & Permissions_ page.
3. Copy the **Bot User OAuth Access Token**, startting with `xoxb-`


# Python

To access the Slack API, we use the [Python library](https://slack.dev/python-slackclient/) that wraps the API call into Python.


```bash
pip3 install slackclient
```

## Sending a Message

The code below sends a message. Make sure to adjust the token and the channel.

```python
import slack, certifi, ssl

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token='xoxb-14603XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', ssl=ssl_context)

response = client.chat_postMessage(channel='#apitest', text="Hello world!")
print(response)
```


## Sending an Image

You can also send an image (or any other file), if you use the line below instead of the `chat_postMessage` call from above. 
The file argument just has to point to a file on your computer.

```python
response = client.files_upload(channels='#apitest', file='~/image.jpg')
```