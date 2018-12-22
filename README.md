# Network Topologies

This repo contains the code for the following network topologies:
1. Linear
2. Ring
3. Star
4. Mesh

They are adapted for mininet. 

This directory should hold configuration files for custom mininets.

See custom_example.py, which loads the default minimal topology.  The advantage of defining a mininet in a separate file is that you then use the --custom option in mn to run the CLI or specific tests with it.

To start up a mininet with the provided custom topology, do:

    sudo mn --custom custom_example.py --topo mytopo
    
