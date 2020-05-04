import requests


class EmuInterface:
    def __init__(self, url):
        self.url = url

    def send_data(self, key, value):
        return requests.post(self.url, data={"key": key, "value": value})

    def get_data(self, key):
        return requests.get(self.url, data={"key": key})


emu_url = "http://127.0.0.1:5000/"
obj = {"key": "fruit",
       "value": "bat"}

emuInterface = EmuInterface(url=emu_url)

x = emuInterface.send_data("fruit", "mango")
print(x.text)
y = emuInterface.send_data("animal", "cat")
print(y.text)

z = emuInterface.get_data("fruit")
print(z.text)
w = emuInterface.get_data("animal")
print(w.text)
