class AddressBook():
    '''
    Address book with persons and groups
    '''
    def __init__(self, *args, **kwargs):
        '''
        Args:
            persons (`list` of obj:`Person` or obj:`Person` , optional): Single person
                                                                         or list of persons
            groups (`list` of obj:`Group` or obj:`Group` , optional): Single group or list of groups
        '''
        self.persons = {id(p): p for p in list(kwargs.get('persons', []))}
        self.groups = {g.name: g for g in list(kwargs.get('groups', []))}

    def add_person(self, person):
        '''
        Args:
            person (obj:`Person`): Person object.
        '''
        self.persons[id(person)] = person

    def add_group(self, group):
        '''
        Args:
            group (obj:`Group`): Group object.
        '''
        self.groups[group.name] = group
        for id, p in group.persons.items():
            self.persons[id] = p

    def get_persons_from_group(self, group):
        '''
        Args:
            group (obj:`Group`): Group object.
        Returns:
            gen of obj:`Person`: Generator of `Person` for success, None otherwise.
        '''
        group = self.groups.get(group.name)
        if group:
            return (p for p in group.persons.values())

    def get_belongs_groups(self, person):
        '''
        Args:
            person (obj:`Person`): Person object.
        Returns:
            gen of obj:`Group`: Generator of `Group` for success, None otherwise.
        '''
        return (g for g in self.groups.values() if g.persons(id(person)))

    def find_person_by_name(self, name):
        '''
        Args:
            name (str): Person first name, last name or both.
        Returns:
            gen of obj:`Person`: Generator of `Person` for success, Empty generator otherwise.
        '''
        return (p for p in self.persons.values() if p.check_name(name))

    def __str__(self):
        return 'Number of persons: %(p)d; Number of groups: %(g)d' % {'p': len(self.persons), 'g': len(self.groups)}


class Person():
    '''
    Implement Person contact info for Address Book
    '''
    def __init__(self, first_name, last_name, *args, **kwargs):
        '''
        Args:
            first_name (str): First name.
            last_name (str): Last name.
            streets (`list` of `str` or `str` , optional): Single street address or list of addresses
            emails (`list` of `str` or `str` , optional): Single email or list of emails
            phones (`list` of `str` or `str` , optional): Single phone or list of phones
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.streets = list(kwargs.get('streets', []))
        self.emails = list(kwargs.get('emails', []))
        self.phone = list(kwargs.get('phones', []))

    def check_name(self, name):
        '''
        Args:
            name (str): Person name.
        Returns:
            bool: True for success, False otherwise.
        '''
        name_tuple = (self.first_name, self.last_name, ' '.join(self.first_name, self.last_name))
        for n in name_tuple:
            if n.startswith(name):
                return True
        return False

    def __str__(self):
        return 'Person %s %s' % (self.first_name, self.last_name)


class Group():
    '''
    Implement group of persons
    '''
    def __init__(self, name, **kwargs):
        '''
        Args:
            name (str): Group name.
            persons (`list` of obj:`Person` or obj:`Person`, optional): Single person or list of persons
        '''
        self.name = name
        self.persons = {id(p): p for p in list(kwargs.get('persons', []))}

    def __str__(self):
        return 'Group %s with %d persons' % (self.name, len(self.persons))
