import re


def send_broadcast_request(port):
    return "I will listen on {port}".format(port=port).encode("UTF-8")


def receive_broadcast_request(message):
    message = message.decode("UTF-8")

    if re.match(r"I will listen on \d+", message):
        port = re.findall(r"\d+", message)[0]
        return port
    else:
        print("UDP_L: Wrong request received: ", message)
        pass


def send_broadcast_response(port):
    return "‫‪I‬‬ ‫‪am‬‬ ‫‪ready‬‬ ‫‪on‬‬ ‫‪Port‬‬ {port}".format(port=port).encode("UTF_8")


def receive_broadcast_response(message):
    message = message.decode("UTF-8")

    if re.match(r"‫‪I‬‬ ‫‪am‬‬ ‫‪ready‬‬ ‫‪on‬‬ ‫‪Port‬‬ \d+", message):
        port = re.findall(r"\d+", message)[0]
        return port
    else:
        raise


def send_listening_message(port):
    return "I am listening at {port}".format(port=port).encode("UTF-8")


def receive_listening_message(message):
    message = message.decode("UTF-8")

    if re.match(r"I am listening at \d+", message):
        port = re.findall(r"\d+", message)[0]
        return port
    else:
        print("UDP_L: Wrong request received: ", message)
        pass
