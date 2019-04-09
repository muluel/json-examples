import json

with open('states.json') as f:
    data = json.load(f)

    print(data)

    for states in data['states']:
        print(states['name'],states['abbraviation'])

with open('new_states.json','w') as f:
    json.dump(data,f)