__author__ = 'pc'
#a simple database usage

import shelve


def store_person(db):
    """
    Query user for data and store it in the shelf object
    """
    pid = raw_input('Enter unique ID number: ')
    person = {}
    person['name'] = raw_input('Enter name: ')
    person['age'] = raw_input('Enter age: ')
    person['phone'] = raw_input('Enter phone nmuber: ')

    db[pid] = person


def lookup_person(db):
    """
    Query user for ID and desired field, and fetch the corresponding data from
    the shelf object
    """
    pid = raw_input('Enter aID nubber')
    field = raw_input('What would you like to know ?(name, age, phone)')
    field = field.strip().lower()
    print field.capitalize() + ':', db[pid][field]


def print_help():
    print 'The available commands are:  '
    print 'store: Store information about a person'
    print 'lookup: Look up a person from ID number'
    print 'quit: Save changes and exit'
    print '?: Prints this message'


def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
     #This filename can be changed
    database = shelve.open('C:\\database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'Store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return

    finally:
        database.close()


if __name__ == '__main__':
    main()
