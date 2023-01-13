try:
    age=int(input("Age: "))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("for this age can not be zero!")
except ValueError:
    print("only enter whole numbers!")