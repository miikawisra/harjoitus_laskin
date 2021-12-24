jatkuu = True
while jatkuu:

    eka = int(input("Anna ensimmäinen luku:"))
    toka = int(input("Anna toinen luku:"))
    jatkuu = True
    while jatkuu:

        print("""(1) +
(2) -
(3) *
(4) /
(5)Vaihda luvut
(6)Lopeta
Valitut luvut:""", eka, toka)
        kolmas = int(input("Tee valinta (1-6):"))
        if kolmas == 1:
            print("Tulos on:", eka + toka)
        elif kolmas == 2:
            print("Tulos on:", eka - toka)
        elif kolmas == 3:
            print("Tulos on:", eka * toka)
        elif kolmas == 4:
            print("Tulos on:", eka / toka)
        elif kolmas == 5:
            neljäs = int(input("Anna uusi ensimmäinen luku:"))
            viides = int(input("Anna uusi toinen luku:"))
            print(
"""(1) +
(2) -
(3) *
(4) /
(5)Vaihda luvut
(6)Lopeta
Valitut luvut:""", neljäs, viides)
            kolmas = int(input("Tee valinta (1-6):"))
            if kolmas == 1:
                print("Tulos on:", neljäs + viides)
            elif kolmas == 2:
                print("Tulos on:", neljäs - viides)
            elif kolmas == 3:
                print("Tulos on:", neljäs * viides)
            elif kolmas == 4:
                print("Tulos on:", neljäs / viides)
            elif kolmas == 5:
                neljäs = int(input("Anna uusi ensimmäinen luku:"))
                viides = int(input("Anna uusi toinen luku:"))
            elif kolmas == 6:
                jatkuu=False
        elif kolmas == 6:
            jatkuu=False
        else:
            print("Valintaa ei tunnistettu.")
