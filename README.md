# minidocker
NFV testbed based on Mininet and Docker

Save "docker.py" in mininet folder

Run as superuser

	sudo python docker.py #name1 #docker-image1 #name2 #docker-image2 ...

	ex. sudo python docker.py dock1 ubuntu dock2 centos
	This will start up 2 docker containers ubuntu and centos, which would be connected to Mininet with an Open vSwitch
