try:
    age=int(input("Age: "))
    print(age)
except ValueError:
    print("only enter whole numbers!")