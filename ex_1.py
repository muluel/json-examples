import json

people_string = '''
{
    "people": [
        {
            "name" : "Muhammed Uluel",
            "phone" : "654-555-4715",
            "emails" :  ["mu@gmail.com","um@outlook.com"],
            "has_licience" : true,
            "price" : 25
        },
        {
            "name" : "Sarp Anderson",
            "phone" : "654-555-4581",
            "emails" :  null,
            "has_licience" : true,
            "price" : 62
        }
    ]
}
'''
data = json.loads(people_string)
print('Type of people_string : ',type(people_string))
print('Type of data variable : ',type(data))
print("Type of data['pople'] : ",type(data['people']))
total=0
for person in data['people']:
    print('Type of person : ', type(person))
    print('Type of person : ', type(person['name']))
    total+=person['price']
print(total/2)