from string import Template

template = Template('Hi $name, you have $balance due')
message = template.substitute(name="John", balance=100)
print(message)

template = Template('Hi ${name}, you have ${balance} due')
message = template.substitute(name="John", balance=100)
print(message)

template = Template('Hi $name, you have ${balance} due')
message = template.substitute(dict(name="John", balance=100))
print(message)

template = Template('Hi $name, you have ${balance} due')
message = template.safe_substitute(name="John")
print(message) 