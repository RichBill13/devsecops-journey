while True:
    try:
        x = int(input("What's is x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
