import random

def main():
    niveau = get_level()
    score = 0
    for _ in range(10):
        nbr1 = generate_integer(niveau)
        nbr2 = generate_integer(niveau)
        result = nbr1 + nbr2
        Try = 1
        while True:
            try:
                user_answer = int(input(f"{nbr1} + {nbr2} = "))

                if result == user_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    Try += 1
            except ValueError:
                print("EEE")
                Try += 1
            if Try > 3:
                print(f"{nbr1} + {nbr2} = {result}")
                break

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            x = int(input("Level: "))

            if (x != 1 and x != 2 and x != 3):
                raise ValueError()
            return x

        except ValueError:
            continue

def generate_integer(level):
    if(level == 1):
        r1 = random.randint(0,9)
        return r1
    elif(level == 2):
        r2 = random.randint(10,99)
        return r2
    elif(level == 3):
        r3 = random.randint(100,999)
        return r3
    else:
        raise ValueError()

if __name__ == "__main__":
    main()








