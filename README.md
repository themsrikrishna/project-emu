# Project Emu

A project that emulates a distributed system in a local environment. Each node is run within its own docker container, and the nodes talk to each other using REST API.

I have implemented a basic key-value store, with a simple python driver. The plan is to prototype a more complex distributed key-value, with simulations of common failures.

## Setup

Run ```./initialize <N>``` to setup N number of nodes in the distributed system.

Note: You need docker and docker-compose as pre requisites.

The nodes created are docker containers, with each node called project-emu_node-1, project-emu_node-2, project-emu_node-3 etc...

## Using the Key-Value Store

A simple snippet of a python driver for the key-value store is in the following code snippet:
```python
import requests


class EmuInterface:
    def __init__(self, r_url, w_url):
        self.read_url = r_url
        self.write_url = w_url

    def send_data(self, key, value):
        return requests.post(self.write_url, data={"key": key, "value": value})

    def get_data(self, key):
        return requests.get(self.read_url, data={"key": key})


    # Port 5000 to read/write from node 1, 5001 to read/write from node 2, etc.
    write_url = "http://127.0.0.1:5000/"
    read_url = "http://127.0.0.1:5002/"

    emuInterface = EmuInterface(r_url=read_url, w_url=write_url)

    emuInterface.send_data("holiday", "xmas")
    emuInterface.send_data("song", "dreams")

    emuInterface.get_data("holiday")
    emuInterface.get_data("song")
```
