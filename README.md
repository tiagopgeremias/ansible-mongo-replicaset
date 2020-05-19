# ansible-mongo-replicaset

A playbook for configure cluster mongo with replicaset mode.

  

## Setup Develop Environments on Vagrant

    cd inventory/vagrant
    vagrant up

Wait to complete the provisioning of virtual machines in Virtualbox

---

## Run ansible-playbook
After completing the provisioning of the virtual machines, run the playbook for cluster configuration.

    ansible-playbook -i inventory/vagrant/hosts playcluster.yml
---
## Test Cluster connection
At the root of the repository directory, execute the commands below to check the connection to the cluster.

    pipenv install
    python test_conn.py
    
    MongoDB Cluster Info:::
	SLAVE NODE: 192.168.41.20:27017
	PRIMARY NODE: 192.168.41.21:27017
	SLAVE NODE: 192.168.41.22:27017


