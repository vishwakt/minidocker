#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.topo import Topo
from subprocess import call, check_output
from subprocess import Popen, PIPE, STDOUT
import select
import re
from mininet.util import isShellBuiltin
import commands
import subprocess
import time
from mininet.topo import Topo
from time import sleep
import sys

containerIDfile = open('cidf','w')
# dockerIDlist = list()
class Docker( Host ):

	def __init__( self, name, image = None, startString = '/bin/sh', dargs = '-c'):

		self.name = name
		self.image = image
		self.startString = startString
		self.dargs = dargs
		call(["docker stop "+self.name], shell=True)
		call(["docker rm "+self.name], shell=True)

		dockerRun = subprocess.Popen(['docker', 'run', '-d', '--name', self.name, self.image, self.startString, self.dargs, 'while true; do echo hello world; sleep 1; done'])

		#Container ID returned in JSON format
		did_cmd = ["docker","inspect","--format='{{ .Id }}'",self.name]
		pidp = Popen( did_cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False )
		ps_out = pidp.stdout.readlines()
		containerID = str(ps_out[0])
		# dockerIDlist.append(containerID)
		containerIDfile.write(containerID)

	def delete(self):
		self.line = None
		f=open("cidf","r")
		nu = sum(1 for line in f)
		f.seek(0)
		for i in range(0,nu):
			self.line=f.next().strip()
			call(["docker stop "+self.line], shell=True)
			call(["docker rm "+self.line], shell=True)
		f.close()
		call(["docker stop "+self.name], shell=True)

		# for i in range(0, len(dockerIDlist)):
		# 	call(["docker stop "+dockerIDlist[i]], shell=True)
		# 	call(["docker rm "+dockerIDlist[i]], shell=True)
		


def dockNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1')
    h2 = net.addHost( 'h2', ip='10.0.0.2')
    # h3 = net.addHost( 'h3', ip='10.0.0.3')

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )

    info( '*** Creating links\n' )
    net.addLink( h2, s1 )
    net.addLink( h1, s1 )
    # net.addLink( h3, s1 )

    info( '*** Starting network\n')
    net.start()

    f=open("cidf","r")
    nu = sum(1 for line in f)
    f.seek(0)
    for i in range(0,nu):
    	line=f.next().strip()
    	# print line+' ID'
    	ipadd = '10.0.0.'+str(i+24)+'/8'
    	# print ipadd
    	subprocess.Popen(['ovs-docker', 'add-port', 's1', 'eth1', line, ipadd])
    f.close()

    # for i in range(0, len(dockerIDlist)):
    # 	print dockerIDlist[i]
    #    	ipadd = '10.0.0.'+str(i+24)+'/8'
    # 	# print ipadd
    # 	subprocess.Popen(['ovs-docker', 'add-port', 's1', 'eth1', dockerIDlist[i], ipadd])
    time.sleep(5)

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()
    d.delete()

if __name__ == '__main__':

	setLogLevel( 'info' )
	global a
	a = len(sys.argv) 
	for i in range (1,a,2):
		x = sys.argv[int(i)]
		y = sys.argv[int(i+1)]
		d = Docker(x,y)

	containerIDfile.close()
	time.sleep(5)
	dockNet()