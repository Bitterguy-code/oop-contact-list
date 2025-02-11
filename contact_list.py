class ContactList:
    def __init__(self, name, contact_list):
        self.name = name
        self.contact_list = contact_list

    @property
    def get_contacts(self):
        return self.contact_list
    
    @get_contacts.setter
    def set_contacts(self, new_contact):
        self.contact_list = new_contact

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def set_name(self, new_name):
        self.name = new_name

    def add_contact(self,contact):
        self.contact_list.append(contact)
        print(contact)

    def remove_contact(self,name):
        x = 0
        for lizt in self.contact_list:
            if lizt['name'] == name:
                self.contact_list.pop(x)
                break
            elif len(self.contact_list.keys()) - 1 == x:
                f"There is no contact by {name}."
            else:
                x += 1

    def find_shared_contacts(self, targettlist):

        result = []
        for lizt in self.contact_list:
            for person in targettlist.contact_list:
                if lizt['name'] == person['name']:
                    result.append(person)
        return result

# friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
# work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

# my_friends_list = ContactList('My Friends', friends)
# my_work_buddies = ContactList('Work Buddies', work_buddies)

# # my_friends_list.remove_contact('Alice')
# # print(my_friends_list.contact_list)

# test_contact = [{'name':'Jeff', 'number':'555-5555'}]
# my_friends_list.add_contact(test_contact)
# print(len(my_friends_list.contact_list))

# # print(my_friends_list.find_shared_contact(work_buddies))
# # 

# # my_friends_list.set_contacts = test_contact
# # print(my_friends_list.get_contacts)

# contacts = [{'name': 'Alice', 'number': '123-4567'}]
# my_list = ContactList('My List', contacts)
# my_list.add_contact({'name': 'Bob', 'number': '987-6543'})
# print(len(my_list.get_contacts) == 2)
# print(my_list.get_contacts[0]['name'] == 'Alice')
# print(my_list.get_contacts)

friends = [{'name': 'Alice', 'number': '867-5309'}, {'name': 'Bob', 'number': '555-5555'}]
work_buddies = [{'name': 'Alice', 'number': '867-5309'}, {'name': 'Carlos', 'number': '555-5555'}]
my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)
shared_contacts = my_friends_list.find_shared_contacts(my_work_buddies)
len(shared_contacts) == 1
shared_contacts[0]['name'] == 'Alice'