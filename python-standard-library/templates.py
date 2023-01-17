from string import Template
import datetime

# Basic string template
template = Template('Hello, $name! Welcome to $platform.')
result = template.substitute(name='John', platform='Python')
print("Basic template:", result)

# Template with dictionary
data = {
    'name': 'Alice',
    'platform': 'Python 3'
}
result = template.substitute(data)
print("Template with dictionary:", result)

# Safe substitution (doesn't raise KeyError)
template = Template('Hello, $name! Your balance is $$balance.')
result = template.safe_substitute(name='Bob')  # balance is missing
print("Safe substitution:", result)

# Custom template delimiter
class CustomTemplate(Template):
    delimiter = '%'

custom_template = CustomTemplate('Hello, %name! Welcome to %platform.')
result = custom_template.substitute(name='Charlie', platform='Custom Python')
print("\nCustom delimiter:", result)

# HTML template
html_template = Template('''
<html>
<head>
    <title>$title</title>
</head>
<body>
    <h1>Welcome $name</h1>
    <p>Your account details:</p>
    <ul>
        <li>Username: $username</li>
        <li>Email: $email</li>
        <li>Date: $date</li>
    </ul>
</body>
</html>
''')

user_data = {
    'title': 'User Profile',
    'name': 'David Smith',
    'username': 'dsmith',
    'email': 'david@example.com',
    'date': datetime.datetime.now().strftime('%Y-%m-%d')
}

html_result = html_template.substitute(user_data)
print("\nHTML template result:", html_result)

# Email template
email_template = Template('''
Subject: $subject

Dear $name,

Thank you for your recent purchase of $product.
Your order number is: $order_id

Order Details:
- Product: $product
- Price: $$price
- Shipping Address: $address

Expected delivery date: $delivery_date

Best regards,
$company_name
''')

order_data = {
    'subject': 'Order Confirmation',
    'name': 'Emily',
    'product': 'Python Course',
    'order_id': '12345',
    'price': '49.99',
    'address': '123 Python St, Codeview, PY 12345',
    'delivery_date': (datetime.datetime.now() + datetime.timedelta(days=3)).strftime('%Y-%m-%d'),
    'company_name': 'Python Learning Center'
}

email_result = email_template.substitute(order_data)
print("\nEmail template result:", email_result)

# Template with conditional text (using string formatting)
def get_greeting_template(is_premium):
    base_template = Template('Hello $name! ' + 
                           ('Welcome back to your premium account!' if is_premium 
                            else 'Welcome to your account!'))
    return base_template

premium_template = get_greeting_template(True)
regular_template = get_greeting_template(False)

print("\nConditional templates:")
print(premium_template.substitute(name='Premium User'))
print(regular_template.substitute(name='Regular User')) 