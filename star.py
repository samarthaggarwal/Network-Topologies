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
from mininet.node import RemoteController, OVSSwitch, CPULimitedHost
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def emptyNet():

    #######################################
    # Constants
    #######################################

    #######################################
    # Run mininet
    #######################################
    net = Mininet( topo=None, build=False, link=TCLink, host=CPULimitedHost )

    info( '*** Adding controller\n' )
    net.addController('c0', ip="127.0.0.1",port=6633)
    h0 = net.addHost('h0', ip='127.0.0.1')
    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.2.1' )
    h2 = net.addHost( 'h2', ip='10.0.2.2' )
    h3 = net.addHost( 'h3', ip='10.0.2.3' )
    h4 = net.addHost( 'h4', ip='10.0.2.4' )
    h5 = net.addHost( 'h5', ip='10.0.2.5' )
    h6 = net.addHost( 'h6', ip='10.0.2.6' )
    h7 = net.addHost( 'h7', ip='10.0.2.7' )
    h8 = net.addHost( 'h8', ip='10.0.2.8' )
    h9 = net.addHost( 'h9', ip='10.0.2.9' )
    h10= net.addHost( 'h10', ip='10.0.2.10')
#	host=[]
#	for i in range(n):
#		host.append(net.addHost('h'+str(i+1),ip='10.0.2.' + str(i+1)))

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', cls=OVSSwitch )    

#	switch=[]
#	for i in range(n+1):
#		switch.append(net.addSwitch('s'+str(i+1),cls=OVSSwitch))


    info( '*** Creating links\n' )
    ## controller - switch (s4)
#    net.addLink( h0, s4 )
    net.addLink(h0,s1)

    ## host - switch
    net.addLink(h1,s1)
    net.addLink(h2,s1)
    net.addLink(h3,s1)
    net.addLink(h4,s1)
    net.addLink(h5,s1)
    net.addLink(h6,s1)
    net.addLink(h7,s1)
    net.addLink(h8,s1)
    net.addLink(h9,s1)
    net.addLink(h10,s1)

    ## switches
    # switchList = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11)
    # for index in range (0, len(switchList)):
    #   for index2 in range (index+1, len(switchList)):
    #     net.addLink(switchList[index], switchList[index2])

    info( '*** Starting network\n')
    net.start()

    #info('*** Set ip address to switch\n')
    s1.cmd('ifconfig switch1 10.0.2.1')
    # s2.cmd('ifconfig switch2 10.0.2.2')
    # s3.cmd('ifconfig switch3 10.0.2.3')
    # s4.cmd('ifconfig switch4 10.0.2.4')
    # s5.cmd('ifconfig switch5 10.0.2.5')
    # s6.cmd('ifconfig switch6 10.0.2.6')
    # s7.cmd('ifconfig switch7 10.0.2.7')
    # s8.cmd('ifconfig switch8 10.0.2.8')
    # s9.cmd('ifconfig switch9 10.0.2.9')
    # s10.cmd('ifconfig switch10 10.0.2.10')
    # s11.cmd('ifconfig switch11 10.0.2.11')
    

    info('*** Enable spanning tree\n')
    # s1.cmd('ovs-vsctl set bridge switch1 stp-enable=true')
    # s2.cmd('ovs-vsctl set bridge switch2 stp-enable=true')
    # s3.cmd('ovs-vsctl set bridge switch3 stp-enable=true')
    # s4.cmd('ovs-vsctl set bridge switch4 stp-enable=true')
    # s5.cmd('ovs-vsctl set bridge switch5 stp-enable=true')
    # s6.cmd('ovs-vsctl set bridge switch6 stp-enable=true')
    # s7.cmd('ovs-vsctl set bridge switch7 stp-enable=true')
    # s8.cmd('ovs-vsctl set bridge switch8 stp-enable=true')
    # s9.cmd('ovs-vsctl set bridge switch9 stp-enable=true')
    # s10.cmd('ovs-vsctl set bridge switch10 stp-enable=true')
    # s11.cmd('ovs-vsctl set bridge switch11 stp-enable=true')

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
