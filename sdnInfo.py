# import networkx as nx
import json
import random
import sys
import re
x=' '
filename = sys.argv[1]
with open(filename, 'r') as f:
    gData = json.load(f)
    #net = gData['graph']['sdnInfo']
    net = gData['graph']
    net2 = gData['graph']
    adminIP = sys.argv[2]
    adminBridge = sys.argv[3]
    aip = re.match('\d{1,3}.\d{1,3}.\d{1,3}.', adminIP )
    #print(aip.group(0))
    
    # bridge info
    print("---")
    print("vars_bridge:")
    print(3*x + f"- {{bridge: \'{adminBridge}\', ip: \'{adminIP}\', skip: \'yes\'}}")
    for b in net['bridges'].values():
        print(3*x + f"- {{bridge: \'{b['id']}\', ip: \'{b['ip']}\'}}")
    print("vars_switch:")
    for s in net['routers'].values():
        for c in net['controllers'].values():
            for i in range(len(s['bridges'])):
                if (s['bridges'][i]) == (c['bridges'][0]):
                    bridge = s['bridges'][i]
                    n = i 
            controllerIP = c['ip'][0]
        number = len(s['ip'])
        print(3*x + f"- {{hostname: \'{s['id']}\', vmip: \'{s['ip'][n]}\', vmBridge: \'{bridge}\', controllerIP: \'{controllerIP}\', eth: \'{number}\', ip3: \'192.168.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}\'  }}") 
    # host info
    print("vars_host:")
    for h in net['hosts'].values():
        for s in net['routers'].values():
            for i in range(len(s['bridges'])):
                if (s['bridges'][i]) == (h['bridges'][0]):
                    switch = s['id']
        print(3*x + f"- {{hostname: \'{h['id']}\', vmip: \'{h['ip'][0]}\', vmBridge: \'{h['bridges'][0]}\', ip3: \'192.168.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}\', switch: \'{switch}\'  }}") 
    for c in net['controllers'].values():
        print("vars_controller:")
        print(3*x + f"- {{hostname: \'{c['id']}\', vmip: \'{aip.group(0)}2\', vmBridge: \'{adminBridge}\', ip3: \'192.168.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}\', eth: '2'  }}")
        print(f"{c['id']}_vars:")
        print(3*x + f"- {{hostname: \'{c['id']}\', ip2: \'{c['ip'][0]}\', bridge2: \'{c['bridges'][0]}\', number: \'1\' }}")
    for s in net['routers'].values():
        print(f"{s['id']}_vars:")
        j = 1
        while j < len(s['ip']):
            print(3*x + f"- {{hostname: \'{s['id']}\', ip2: \'{s['ip'][j]}\', bridge2: \'{s['bridges'][j]}\', number: \'{j}\'}}")
            j = j + 1
    for s in net['routers'].values():
        print(f"{s['id']}_flows:" + "\n" + 3*x + "- {}")
        for r in net2['SDN Rulesets'][s['id']]:
            if(r['action'] == "FORWARD"):
                print(3*x + f"- {{destination: \'{r['header']['dest'][0]}\', source: \'{r['header']['src'][0]}\', gateway: \'{r['outIP']}\', action: \'FORWARD\'  }}")
     #   for r in net2['SDN Rulesets'][s['id']]:
     #       for h in net['hosts'].values():
     #           for i in range(len(s['bridges'])):
     #               if (s['bridges'][i]) == (h['bridges'][0]):
     #                   if(r['header']['src'][0] == h['ip'][0]):
     #                       if(r['action'] == "FORWARD"):
     #                           print(3*x + f"- {{destination: \'{r['header']['dest'][0]}\', gateway: \'{r['outIP']}\', action: \'FORWARD\'  }}")


                            