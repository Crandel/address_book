# Simple Address Book

To use this library you need to import it

```python
from address_book import AddressBook, Person, Group
```

To create *Person* and *Group* you need to give a first and last name

```python
person = Person(first_name='first name', last_name='last name', emails=['some@com', 'some@com'])
group = Group(name='Group', persons=[person1, person2])
```

After this you can fill your Address book with persons or groups. Each person in group will be available in AddressBook.

```python
address = AddressBook(persons=[person1, person2], groups=[group1, group2])
```

Or

```python
address = AddressBook()
address.add_person(person)
address.add_group(group)
```

You can get all members, belongs to group

```python
persons = address.get_persons_from_group(group)
```

`get_persons_from_group` return generator of persons

Also you can get groups the person belongs to

```python
groups = address.get_belongs_groups(person)
```

It return generator too.

At last, you can find person in address book by name or email

```python
users = address.find_person_by_name(name='some name')
users = address.find_person_by_email(name='some email')
```

This functions return user generator even if name or email have partly coincidence


For finding person by email, if we have only common substring, we could use regex instead of str.startswith()
