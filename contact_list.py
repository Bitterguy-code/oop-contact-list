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
