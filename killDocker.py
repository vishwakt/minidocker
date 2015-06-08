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
import shlex, subprocess

#test2 = subprocess.Popen(["docker kill abc"] , stdout=subprocess.PIPE)
##call(["docker stop abc"], shell=True)
##call(["docker rm abc"], shell=True)



class killDocker( Host ):

	containerIDfile = open('cidf','r')

	for line in containerIDfile:
		call(["docker stop "+line], shell=True)
		call(["docker rm "+line], shell=True)
		print line

	containerIDfile.close()

