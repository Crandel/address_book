from copy import copy
import unittest
from address_book import AddressBook, Person, Group


class AddressBookTestCase(unittest.TestCase):

    def setUp(self):
        self.address_book = AddressBook()
        self.person1 = Person(first_name='p1fn', last_name='p1ln', emails=['p1em1@com', 'p1em2@com'])
        self.person2 = Person(first_name='p2fn', last_name='p2ln', emails=['p2em1@com', 'p2em2@com'])
        self.person3 = Person(first_name='p3fn', last_name='p3ln', emails=['p3em1@com', 'p3em2@com'])
        self.group1 = Group(name='Group1', persons=self.person1)
        self.group2 = Group(name='Group2', persons=[self.person3, self.person1])

    def test_wrong_creation(self):
        with self.assertRaises(TypeError):
            test_group = Group()
        with self.assertRaises(TypeError):
            test_person = Person()

    def test_add_person(self):
        self.address_book.add_person(self.person1)
        self.assertTrue(id(self.person1) in self.address_book.persons)
        self.address_book.add_person(self.person2)
        self.assertTrue(id(self.person2) in self.address_book.persons)

    def test_add_group(self):
        self.address_book.add_group(self.group2)
        self.assertTrue(self.group2.name in self.address_book.groups)
        group_persons = copy(self.group2.persons)
        address_persons = copy(self.address_book.persons)
        self.assertTrue(set(group_persons).intersection(address_persons))

    def test_get_belongs_groups(self):
        groups_from_address = self.address_book.get_belongs_groups(self.person1)
        for group in groups_from_address:
            self.assertTrue(id(self.person1) in group.persons)

    def test_get_persons_from_group(self):
        person_from_group = self.address_book.get_persons_from_group(self.group2)
        for person in person_from_group:
            self.assertTrue(person.first_name in ['p3fn', 'p1fn'])

    def test_find_person_by_name(self):
        persons = self.address_book.find_person_by_name('p1fn')
        for p in persons:
            self.assertEqual('p1fn', p.first_name)

    def test_find_person_by_email(self):
        persons1 = self.address_book.find_person_by_email('p1em1@com')
        for p1 in persons1:
            self.assertTrue(p1.check_email('p1em1@com'))
        persons2 = self.address_book.find_person_by_email('p1em1')
        for p2 in persons2:
            self.assertTrue(p2.check_email('p1em1@com'))
