import random
import string

# Generate random integers
print("Random integers:")
print(f"Between 1 and 10: {random.randint(1, 10)}")
print(f"Between 0 and 100: {random.randrange(0, 101, 2)}")  # Even numbers only

# Generate random floating-point numbers
print("\nRandom floating-point numbers:")
print(f"Between 0 and 1: {random.random()}")
print(f"Between 2 and 4: {random.uniform(2, 4)}")

# Making choices
print("\nRandom choices:")
colors = ['red', 'green', 'blue', 'yellow']
print(f"Random color: {random.choice(colors)}")
print(f"Three random colors: {random.choices(colors, k=3)}")
print(f"Sample without replacement: {random.sample(colors, k=2)}")

# Shuffling sequences
numbers = list(range(1, 11))
random.shuffle(numbers)
print(f"\nShuffled numbers: {numbers}")

# Generate random strings
print("\nRandom strings:")
# Random letter
print(f"Random letter: {random.choice(string.ascii_letters)}")
# Random lowercase letter
print(f"Random lowercase: {random.choice(string.ascii_lowercase)}")
# Random uppercase letter
print(f"Random uppercase: {random.choice(string.ascii_uppercase)}")
# Random digit
print(f"Random digit: {random.choice(string.digits)}")

# Generate random password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print(f"\nRandom password: {generate_password()}")
print(f"Longer password: {generate_password(12)}")

# Seeding the random number generator
random.seed(42)  # Set seed for reproducibility
print("\nWith seed 42:")
print(f"First random number: {random.random()}")
print(f"Second random number: {random.random()}")

# Using random for weighted choices
fruits = ['apple', 'banana', 'orange']
weights = [0.5, 0.3, 0.2]  # Probabilities must sum to 1
print(f"\nWeighted choice: {random.choices(fruits, weights=weights, k=1)[0]}")

# Generate random boolean
print(f"\nRandom boolean: {random.choice([True, False])}")
print(f"Random boolean with probability: {random.random() < 0.7}")  # 70% True 