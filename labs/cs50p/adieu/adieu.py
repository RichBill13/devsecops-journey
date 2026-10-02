import inflect

p = inflect.engine()
noms = []
while True:
    try:
        # ask for the name and remove space around
        nom = input("Name: ").strip()

        #checking the name
        if nom != "":
            noms.append(nom)
    except EOFError:
        

        ## security: check if there's at least one name
        if len(noms) < 1:
            print("error: enter at least one name !")
            continue
        break
liste = p.join(noms)
print(f"Adieu, adieu, to {liste}")
