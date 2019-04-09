import json

with open('json.json','r') as f:
    data=json.load(f)
    # print(json.dumps(data,indent=2))
    for item in data:
        for initem in data[item]:
            if type(initem)==dict:
                # print(json.dumps(initem,indent=2))
                # print(initem['type'])
                # for ininitem in initem:
                #     count+=1
                #     print(ininitem,end=',',)
                print(f'{item} has : ')
                for ininitem in initem:
                    print(ininitem,' value ',initem[ininitem])
                # print(f'{initem[ininitem]}')
            else:
                print(data[item][initem])