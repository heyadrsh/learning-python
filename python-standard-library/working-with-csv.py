import csv

# Writing to CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product", "price"])
    writer.writerow([1000, "Python Course", 29.99])
    writer.writerow([1001, "Java Course", 39.99])
    writer.writerow([1002, "SQL Course", 19.99])

# Reading from CSV
with open('data.csv') as file:
    reader = csv.reader(file)
    print("\nAll rows:")
    for row in reader:
        print(row)

# Using DictReader and DictWriter
with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, ["id", "name", "price"])
    writer.writeheader()
    writer.writerows([
        {"id": 100, "name": "Premium Course", "price": 49.99},
        {"id": 101, "name": "Basic Course", "price": 19.99},
    ])

with open('data.csv') as file:
    reader = csv.DictReader(file)
    print("\nDictionary rows:")
    for row in reader:
        print(row) 