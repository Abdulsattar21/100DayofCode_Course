try:
    age = int(input("Age: "))
    income = 2000
    print(income / age)
except ValueError: # there is a lot of error massages like (ZeroDividerError)
    print("invalid Value")
except ZeroDivisionError:
    print("age can't be zero")
