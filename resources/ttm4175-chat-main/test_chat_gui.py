from chat_gui import ChatGui

# TODO change to fit your team
my_id = "team1a"


def on_send(sender, receiver, message, uuid):
    print("Sending {} --> {} {}".format(sender, receiver, message[:5] + "..."))


def on_type(sender, receiver):
    print("Typing: {} --> {}".format(sender, receiver))


def on_read(sender, receiver, uuid):
    print("Read: {} --> {} {}".format(sender, receiver, uuid[:5] + "..."))


gui = ChatGui(my_id, on_send=on_send, on_type=on_type, on_read=on_read)

# We send in a fake message:
# gui.receive("x6", "Dette er en fake medling!", "absgdeff")

# We fake that chat partner x5 starts typing:
# gui.typing("x5")

gui.show()
