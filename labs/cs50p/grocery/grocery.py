def main():
    article = {}
    while True:
        try:
            item = input("").upper()
            if item in article:
                article[item] += 1
            else:
                article[item] = 1
        except EOFError:
            print()
            break

    for item in sorted(article.keys()):
        print(f"{article[item]} {item}")

main()