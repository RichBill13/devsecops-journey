def main():
    mot = input("camelCase: ")
    snake = transformation(mot)
    print("snake_case: " + snake)

def transformation(mt):
    result = ""
    for i in mt:
        if i.isupper():
            result += "_" + i.lower()
        else:
            result += i

    return result

main()