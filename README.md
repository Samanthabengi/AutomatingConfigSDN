# AutomatingConfigSDN
Contains playbooks, python script, and inventory file template

The Ansible playbooks are located in the Ansible_Master directory. Each of the four master playbooks has a folder with all the child playbooks.

sdnInfo.py is the python script used to create the variable file.

ovs_inventory_tmp contains a template for an inventory file

Steps to replicate:
1. Given a script run the python script using this command: python sdnInfo.py './sdntoy.json' adminBr adminIP (need to set file name/location, admin bridge and admin IP) --> might need to be edited depending on setup of json file given
3. Once you have variables file save it as a .yml file
4. Create an inventory file using the template given
5. Make sure the /etc/hosts file doesn't already have a vm with the same name and a config file/logical volume (lvdisplay) does not already exist
6. Create VMs using this command: ansible-playbook -i inventory createMaster.yml --extra-vars "vars=vars inventory=inventory" (need to set inventory file name and vars file name)
7. Install Python using this command: ansible-playbook -i inventory pythonMaster.yml --extra-vars "vars=vars inventory=inventory" (need to set inventory file name and vars file name)
8. Install other software and set up controller on switch using this command: ansible-playbook -i inventory installMaster.yml --extra-vars "vars=tmp inventory=inventory" (need to set inventory file name and vars file name)
9. Start rest_router on the controller
10. Run HTTP POST commands using this command: ansible-playbook -i inventory curlMaster.yml --extra-vars "vars=vars inventory=inventory" (need to set inventory file name and vars file name)
