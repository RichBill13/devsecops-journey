def main():
    x = str(input("What's the Answer to the Great Question of life, the Universe, and Everything?"))
    print(verification(x))

def verification(n):
    # nettoyer la reponse convertir en minuscule et retirer les espaces
    n = n.lower().strip()
    if n == "42" or n == "forty-two"  or n == "forty two":
        return "Yes"
    else:
        return "No"

main()