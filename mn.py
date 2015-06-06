from mininet.net import Mininet
from mininet.node import Controller, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from subprocess import call, check_output
from subprocess import Popen, PIPE, STDOUT
import select
import re
from mininet.util import isShellBuiltin
import commands
import subprocess
import time

class DockerHost( Host ):
	#User enters number of docker containers to run
	numberOfContainers = int(raw_input("Enter number of containers to run: "))
	#File to store Container IDs
	containerIDFfile = open('cidf','w')
	
	for i in range(0,numberOfContainers):
		#User enters name of docker container
		dname = raw_input("Enter name of container to run: ")

		#Running infinite loop on Ubuntu container
		dockerRun = 'docker run -d --name '+ dname +' ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"'
		call(dockerRun, shell=True)

		#call("sleep 1", shell=True)
		#Container ID returned in JSON format
		did_cmd = ["docker","inspect","--format='{{ .Id }}'",dname]
		pidp = Popen( did_cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False )
		ps_out = pidp.stdout.readlines()
		containerID = str(ps_out[0])
		#containerIDFfile = open('cidf','w')
		containerIDFfile.write(containerID)
		#containerIDFfile.close()
		#print containerID
	containerIDFfile.close()

def emptyNet():

	"Create an empty network and add nodes to it."

	net = Mininet( controller=Controller )

	info( '*** Adding controller\n' )
	net.addController( 'c0' )

	info( '*** Adding hosts\n' )
	h1 = net.addHost( 'h1', ip='10.0.0.1')
	h2 = net.addHost( 'h2', ip='10.0.0.2')

	info( '*** Adding switch\n' )
	s1 = net.addSwitch( 's1' )
	s2 = net.addSwitch( 's2' )	

	info( '*** Creating links\n' )
	net.addLink( h2, s1 )
	net.addLink( s1, h2 )

	info( '*** Starting network\n')
	net.start()

	info( '*** Running CLI\n' )
	CLI( net )

	info( '*** Stopping network' )
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	emptyNet()
