def main():
    salution = str(input("Greeting: "))
    montant = verification(salution)
    print(f"${montant}")

def verification(n):
    n = n.lower().strip()
    if n.startswith("hello"):
        return 0
    elif n.startswith("h"):
        return 20
    else:
        return 100

main ()
        
