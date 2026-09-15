def main():
    phrase = input("texte: ")
    print(convert(phrase))

def convert(n):
    n = n.replace(":)", "🙂")
    n = n.replace(":(", "☹️")
    return n

main()            
              