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

	n=10;
    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.2.1' )
    h2 = net.addHost( 'h2', ip='10.0.2.2' )
	h3 = net.addHost('h3', ip='10.0.2.3')
	h4 = net.addHost
#	host=[]
#	for i in range(n):
#		host.append(net.addHost('h'+str(i+1),ip='10.0.2.' + str(i+1)))

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', cls=OVSSwitch )
    s2 = net.addSwitch( 's2', cls=OVSSwitch )
    s3 = net.addSwitch( 's3', cls=OVSSwitch )
    s4 = net.addSwitch( 's4', cls=OVSSwitch )
#	switch=[]
#	for i in range(n+1):
#		switch.append(net.addSwitch('s'+str(i+1),cls=OVSSwitch))


    info( '*** Creating links\n' )
    ## controller - switch (s4)
#    net.addLink( h0, s4 )
	net.addLink(h0,s11)

    ## host - switch
#    net.addLink( h1, s1 )
#    net.addLink( h2, s3 )
	net.addLink(h1,s1)
	net.addLink(h2,s2)
	net.addLink(h3,s3)
	net.addLink(h4,s4)
	net.addLink(h5,s5)
	net.addLink(h6,s6)
	net.addLink(h7,s7)
	net.addLink(h8,s8)
	net.addLink(h9,s9)
	net.addLink(h10,s10)

    ## switches
    switchList = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11)
    for index in range (0, len(switchList)):
      for index2 in range (index+1, len(switchList)):
        net.addLink(switchList[index], switchList[index2])

    info( '*** Starting network\n')
    net.start()

    #info('*** Set ip address to switch\n')
    s1.cmd('ifconfig s1 10.0.2.1')
    s2.cmd('ifconfig s2 10.0.2.2')
    s3.cmd('ifconfig s3 10.0.2.3')
    s4.cmd('ifconfig s4 10.0.2.4')

    info('*** Enable spanning tree\n')
    s1.cmd('ovs-vsctl set bridge s1 stp-enable=true')
    s2.cmd('ovs-vsctl set bridge s2 stp-enable=true')
    s3.cmd('ovs-vsctl set bridge s3 stp-enable=true')
    s4.cmd('ovs-vsctl set bridge s4 stp-enable=true')

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
