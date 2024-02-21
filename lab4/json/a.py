import json 

file = open ("sample-data.json")
sample_json = file.read()
sample = json.loads(sample_json)

print ("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

main_info = sample["imdata"]

for i in main_info:
    sm = i["l1PhysIf"]["attributes"]

    if len(str(sm["dn"])) == 42 :
        print ( sm["dn"] + " "*4 + " "* 20 +sm["descr"] + " "*6  + sm["speed"]+ " "*3 +sm["mtu"])

    else:
        print ( sm["dn"] + " "*5 + " "* 20 +sm["descr"] + " "*6  + sm["speed"]+ " "*3 +sm["mtu"])