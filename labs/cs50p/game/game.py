import random

def main():
    while True:
        try:
            level = int(input("Level: "))
        
            if (level < 1):
                raise ValueError()
            break
    
        except ValueError:
            continue

    number = random.randint(1,level)
    while True:
        try:
            gues = int(input("Guess: "))
            if (gues < 0):
                raise ValueError()
            if (gues < number):
                print("Too small! ")
            elif (gues > number):
                print("Too large! ")
            else:
                print("Just right!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()


