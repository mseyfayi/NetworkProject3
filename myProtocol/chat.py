def receive(message):
    message = message.decode('UTF-8')
    return message.split(":", 1)


def send(name, message):
    message = "{}:{}".format(name, message)
    message = message.encode("UTF-8")
    return message
