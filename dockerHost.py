#!/usr/bin/python

"""
An API for running Docker containers as Mininet Hosts
"""
"""Example topology


 host1 ---switch1        switch2--- host2
                |        |
                |        |
                -switch3--
                    |
                    |
                 Docker1
                    |
                    |
                 switch4
                    |
                    |
                  host3

"""

from mininet.net import Mininet
from mininet.node import Controller, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from subprocess import call, check_output
from subprocess import Popen, PIPE, STDOUT
import select
import re
from mininet.util import isShellBuiltin
import docker
import select
import re
from mininet.util import isShellBuiltin
import commands
import subprocess
import time
from mininet.topo import Topo
from time import sleep
import sys

def dockerNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip = '10.0.0.1')
    h2 = net.addHost( 'h2', ip = '10.0.0.2')
    h3 = net.addHost( 'h3', ip = '11.0.0.3')
    h5 = net.addDocker( 'd1', 'pkt/ins', 'p')

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )

    info( '*** Creating links\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s2 )
    net.addLink( s1, s3 )
    net.addLink( s2, s3 )
    net.addLink( s4, h3 )

    info( '*** Starting network\n')
    net.start()
    net.addDockerLink( 's3', 'd1', '10.0.0.25' )
    net.addDockerLink( 's4', 'd1', '11.0.0.25' )

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    dockerNet()
