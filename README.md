# project-emu

A project that emulated a distributed system in a local environment. Each node is run within its own docker container, and the nodes talk to each other using REST API.

## Setup

Run ```./initialize <N>``` to setup N number of nodes in the distributed system.

Note: You need docker and docker-compose as pre requisites.

The nodes created are docker containers, with each node called project-emu_node-1, project-emu_node-2, project-emu_node-3 etc...