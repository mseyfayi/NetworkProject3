import re


def send(port):
    return "‫‪I‬‬ ‫‪am‬‬ ‫‪ready‬‬ ‫‪on‬‬ ‫‪Port‬‬ {port}".format(port=port).encode("UTF_8")


def receive_broadcast_request(message):
    message = message.decode("UTF-8")

    if re.match(r"I will listen on \d+", message):
        port = re.findall(r"\d+", message)[0]
        return port
    else:
        print("UDP_L: Wrong request received: ", message)
        pass


def receive_listening_message(message):
    message = message.decode("UTF-8")

    if re.match(r"I am listening at \d+", message):
        port = re.findall(r"\d+", message)[0]
        return port
    else:
        print("UDP_L: Wrong request received: ", message)
        pass
