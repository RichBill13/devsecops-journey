def main():
    pourcentage = get_fraction()
    if (pourcentage <= 1):
        print("E")
    elif (pourcentage >= 99):
        print("F")
    else:
        print(f"{pourcentage}%")

def get_fraction():
    while True:
        try:
            fract = input("Fraction: ")
            x,y = fract.split("/")
            numerateur = int(x)
            denominateur = int(y)
            if (numerateur <= denominateur and denominateur > 0):
                pourcent = round ((numerateur / denominateur) * 100)
                return pourcent

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()



