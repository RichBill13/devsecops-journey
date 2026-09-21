def main():
    text = input("Input: ")
    text_sans_voyelle = reduction(text)
    print(text_sans_voyelle)

def reduction(text2):
    text_filtre = ""
    for char in text2:
        if(char not in "aeiouAEIOU"):
            text_filtre += char

    return text_filtre

main()

