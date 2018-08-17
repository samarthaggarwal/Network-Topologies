"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        n=10;
	host=[]
	for i in range(n):
		host.append(self.addHost('h'+str(i)))
	switch=self.addSwitch('s1')

#	leftHost = self.addHost( 'h1' )
#        rightHost = self.addHost( 'h2' )
#        leftSwitch = self.addSwitch( 's3' )
#        rightSwitch = self.addSwitch( 's4' )

        # Add links
	for i in range(n):
		self.addLink( host[i], switch )
#	for i in range(n-1):
#		self.addLink(switch[i],switch[i+1])
#        self.addLink( leftHost, leftSwitch )
#        self.addLink( leftSwitch, rightSwitch )
#        self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }
