import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=3))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

print(''.join(random.choices(string.ascii_letters + string.digits, k=8)))

print(random.randrange(1, 100, 2))

random.seed(1)
print(random.random())
print(random.random())

random.seed(1)
print(random.random())
print(random.random()) 