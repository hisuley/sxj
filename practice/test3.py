__author__ = 'pc'

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar avenue 90'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

labels = dict(phone='phone nmuber', addr='address')

name = raw_input('Name: ')

request = raw_input('Phone number (p) or address(a)? ')

key = request
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("%s's %s is " % (name, label, result))