import json
file = open('lab4/sample-data.json', 'r')
json_data = json.loads(file.read())
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print('-------------------------------------------------- --------------------  ------  ------')


print(json_data['imdata'][0]['l1PhysIf']['attributes']['dn'],'                             ',json_data['imdata'][0]['l1PhysIf']['attributes']['fecMode'],json_data['imdata'][0]['l1PhysIf']['attributes']['mtu'])
print(json_data['imdata'][1]['l1PhysIf']['attributes']['dn'],'                             ',json_data['imdata'][0]['l1PhysIf']['attributes']['fecMode'],json_data['imdata'][0]['l1PhysIf']['attributes']['mtu'])
print(json_data['imdata'][2]['l1PhysIf']['attributes']['dn'],'                             ',json_data['imdata'][0]['l1PhysIf']['attributes']['fecMode'],json_data['imdata'][0]['l1PhysIf']['attributes']['mtu'])