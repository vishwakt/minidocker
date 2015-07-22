# minidocker
NFV testbed based on Mininet and Docker

The purpose of this project is to develop an API that provides the user, the ability to define new network topologies according to his need and run dedicated Docker containers running different network functions. The resulting API will be an extension to the existing Mininet API that gives user the flexibility to start up Docker containers as Mininet hosts.

Mininet hosts can be configured to work as network functions whereas Docker provides more flexibility, as predefined images for running network functions can be downloaded from DockerHub, thus saving precious time for the developer. Instead of configuring each Mininet host separately a user can use the same Docker image for emulating network functions.

Simulating a network function would require hosting a separate Virtual Machine for each new network function, which would drastically increase the overhead. Docker also solves this issue, as it is a lightweight virtualization tool capable of emulating a Virtual Machine.
