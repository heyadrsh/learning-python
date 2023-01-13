def greetings(first_name,last_name):
    print(f'Hey {first_name} {last_name} !')

print(greetings("John","Smith")) #positional arguments

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")

print(greetings(first_name, last_name)) #positional arguments

print(greetings(last_name="Smith", first_name="John")) #keywords arguments
