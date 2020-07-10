import re


def send_broadcast_request(port):
    return "I will listen on {port}".format(port=port).encode("UTF-8")


def receive(message):
    message = message.decode("UTF-8")

    if re.match(r"‫‪I‬‬ ‫‪am‬‬ ‫‪ready‬‬ ‫‪on‬‬ ‫‪Port‬‬ \d+", message):
        port = re.findall(r"\d+", message)[0]
        return port
    else:
        raise


def send_listening_message(port):
    return "I am listening at {port}".format(port=port).encode("UTF-8")
