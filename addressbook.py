from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.name_value = self.value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.phone_number = self.validate_phone()

    def validate_phone(self):
        if self.value.isdigit() and len(self.value) == 10:  
            return self.value
        else:
            raise Exception("The phone format is not correct.")  
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        number = Phone(phone)
        self.phones.append(number)

    def remove_phone(self, phone):
        for idx, phone_num in enumerate(self.phones):
            if phone_num.value == phone:
                del self.phones[idx]
                return f"The phone {phone} has been removed."
        return f"The phone has not been found."
        

    def edit_phone(self, old_phone, new_phone):
        for phone_num in self.phones:
            if phone_num.value == old_phone:
                phone_num.value = new_phone
                return f"Phone number {old_phone} updated to {new_phone} for contact {self.name.value}"
        return f"Phone number {old_phone} has not been found."

    def find_phone(self, phone):
        for phone_num in self.phones:
            if phone_num.value == phone:
                return f"Phone number {phone} found for the contact {self.name.value}"
        return f"Phone number {phone} hasn't been found for the contact {self.name.value}"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, name):
        if name not in self.data:
            self.data[name] = Record(name)
            return f"Contact {name} added to the address book"
        else:
            return f"Contact {name} already exists in the address book"
        
    def delete(self, name):
        if name in self:
            del self[name]
            return f"Contact {name} was successfuly deleted."
        else:
            return f"Contact {name} wasn't found"

    def find(self, name):
        if name in self:
            return f"Contact {name} found in the address book." # print all the info
        else:
            return f"Contact {name} wasn't found in the address book."
        

# Creating a new address book        
book = AddressBook() 

# Creating John record
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding John record to the Address book
book.add_record(john_record)

# Creating and adding a new Jane record 
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Printing out all the data in the Address book 
for name, record in book.data.items():
    print(record)

# Printing out Contact name: John, phones: 1112223333; 5555555555
print(john_record)  

john_record.edit_phone("1234567890", "1112223333")
print(john_record)



 

