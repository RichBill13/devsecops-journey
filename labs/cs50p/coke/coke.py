def main():
    montant_du = 50
    while (montant_du > 0):
        print(f"Amount Due: {montant_du}")
        piece = int(input("Insert Coin: "))
        if(piece == 25 or piece == 10 or piece == 5):
            montant_du -= piece

    print(f"Change Owed: {abs(montant_du)}")

main()