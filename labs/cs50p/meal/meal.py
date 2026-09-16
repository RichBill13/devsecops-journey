def main():
    heure = input("What time is it? ")
    temps = convert(heure)
    if temps >= 7.0 and temps <= 8.0:
        print("breakfast time")
    elif temps >= 12.0 and temps <= 13.0:
        print("lunch time")
    elif temps >= 18.0 and temps <= 19.0:
        print("dinner time")

def convert(heur):
    heur = heur.strip()
    heur = heur.split(":")
    return float(heur[0]) + float(heur[1]) / 60.0

main()