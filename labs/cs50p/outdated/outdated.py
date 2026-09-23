MOIS  = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


def main():
    while True:
        date = input("Date: ").strip()
        if "/" in date:
            try:
                x,y,z = date.split("/")
                jour = int(x)
                mois = int (y)
                annee = int(z)
                if 1 <= mois <= 12 and 1 <= jour <= 31:
                    print(f"{annee:04d}-{mois:02d}-{jour:02d}")
                    break
            except ValueError:
                pass
        elif "," in date:
            try:
                x,y,z = date.split(" ")
                if x in MOIS:
                    mois = MOIS.index(x) + 1
                    jour = int(y.replace(",",""))
                    annee = int(z)
                    if 1 <= jour <= 31:
                        print(f"{annee:4d}-{mois:2d}-{jour:2d}")
                        break

            except ValueError:
                pass

main()
