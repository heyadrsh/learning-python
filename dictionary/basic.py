# Basic dictionary operations in Python
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])  # Accessing dictionary values
print(customer.get("birthdate", "Not available"))  # Using get() with default value 