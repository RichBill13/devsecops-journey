def main():
    dollars = dollars_to_float(input("how much was the meal? "))
    percent = percent_to_float(input("how many percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.replace("$",""))
    return d

def percent_to_float(p):
    p = float(p.replace("%",""))
    return p / 100

main()
