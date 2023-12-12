def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        if len(args) < 2:
            return "Contact is in the wrong format. Provide <name> and <phone number>"
        try:
            return func(*args, **kwargs)
        except ValueError:
           return "Contact was not added. Type in a name and a phone number."
        except (KeyError, IndexError):
            return "There is no such contact! To add contact use command 'Add'." 
    return inner

@input_error
def add_contact(contacts, args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def verify_contact(contacts, args):  # an inside func
    if len(args) < 2:
        return False
    name, phone = args
    if name in contacts:
        return True
    return False

@input_error
def change_contact(contacts, args):
    if not verify_contact(contacts, args):
        return f"There is no such contact! To add contact use command 'Add'."
    name, phone = args
    contacts[name] = phone 
    return f"The contact {args[0]} has been changed successfully"
      
def show_phone(contacts, name):
    if name not in contacts:
        return "There is no such contact"
    return f"{name}: {contacts[name]}"
  
def show_all(contacts):     
    if not contacts:
        print("No contacts saved.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def print_supported_commands():
    print(f"To add a contact, use command 'Add name phone'.\n"
      f"To end assistant, use command 'Close'.\n"
      f"To change contact, use command 'Change name new_phone. '.\n"
      f"To see a phone and a name, use command 'phone name'.\n"
      f"To see all saved names and phones, use command 'All'.")
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("No command entered. Please provide a command.")
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "stop"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi", "wazzup", "morning", "greetings" ]:
            print("How can I help you?")
        elif command in ["add", "new contact", "new name"]:
            if verify_contact(contacts, args):
                print(f"The contact is already exists")
            else:
                print(add_contact(contacts, args))    
        elif command in ["change", "change contact"]:
            print(change_contact(contacts, args))
        elif command == "phone" and args[0]:
            print(show_phone(contacts, args[0]))
        elif command in ["all", "everybody"]:
            show_all(contacts)   
        elif command in ['?', 'help', 'how']:
            print_supported_commands()
        else:
            print("Invalid command.")
            print_supported_commands()


if __name__ == "__main__":
    main()