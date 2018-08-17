#!/usr/bin/python

"""
   reference: https://www.youtube.com/watch?v=yHUNeyaQKWY

   mesh topology

       s2------s3 ----h2
       | *   * |
       |   *   |
       | *   * |
 h1----s1-----s4------h0(c0) 

 **** To prevent broadcast storm(by arp messages), 
      enable spanning tree in each switch !!!!!

      : in each switch, 
         type "ovs-vsctl set bridge <bridge_name> stp-enable=true"
   
"""

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    #######################################
    # Constants
    #######################################

    #######################################
    # Run mininet
    #######################################
    net = Mininet( topo=None, build=False )

    info( '*** Adding controller\n' )
    net.addController('c0', controller=RemoteController,ip="127.0.0.1",port=6633)
    h0 = net.addHost('h0', ip='127.0.0.1')

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.2.1' )
    h2 = net.addHost( 'h2', ip='10.0.2.2' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', cls=OVSSwitch )
    s2 = net.addSwitch( 's2', cls=OVSSwitch )
    s3 = net.addSwitch( 's3', cls=OVSSwitch )
    # s4 = net.addSwitch( 's4', cls=OVSSwitch )

    info( '*** Creating links\n' )
    ## controller - switch (s3)
    net.addLink( h0, s3 )

    ## host - switch
    net.addLink( h1, s1 )
    net.addLink( h2, s2 )

    ## switches
    switchList = (s1, s2, s3)
    for index in range (0, len(switchList)-1):
      # for index2 in range (index+1, len(switchList)):
        net.addLink(switchList[index], switchList[index+1])

    info( '*** Starting network\n')
    net.start()

    #info('*** Set ip address to switch\n')
    s1.cmd('ifconfig switch1 10.0.2.1')
    s2.cmd('ifconfig switch2 10.0.2.2')
    s3.cmd('ifconfig switch3 10.0.2.3')

    info('*** Enable spanning tree\n')
    s1.cmd('ovs-vsctl set bridge switch1 stp-enable=true')
    s2.cmd('ovs-vsctl set bridge switch2 stp-enable=true')
    s3.cmd('ovs-vsctl set bridge switch3 stp-enable=true')

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
