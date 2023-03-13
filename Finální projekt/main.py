"""
████████╗░█████╗░███╗░░░███╗░█████╗░██╗░░██╗██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
╚══██╔══╝██╔══██╗████╗░████║██╔══██╗╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
░░░██║░░░██║░░██║██╔████╔██║██║░░██║░╚███╔╝░██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
░░░██║░░░██║░░██║██║╚██╔╝██║██║░░██║░██╔██╗░██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
░░░██║░░░╚█████╔╝██║░╚═╝░██║╚█████╔╝██╔╝╚██╗██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
"""

import projekt_pojisteni

lets_continue = "ano" #---------------------------


while lets_continue != "ne":#----------------------
    projekt_pojisteni.uvod()
    volba = int(input("Vyberte si akci: \n1 - Pridat noveho pojisteneho\n2 - Vypsat vsechny pojistene \n3 - Vyhledat pojisteneho \n4 - Konec \n"))
    print("")
    if volba == 4:#vymaze obrazovku
        lets_continue = "ne"
        projekt_pojisteni.vymaz()
    elif volba == 3:#hleda pomoci jmena a prijmeni
        first_name = input("zadej jmeno: ")
        last_name = input("zadej prijmeni: ")

        #první velká
        capitalized_first_name = first_name.capitalize()
        capitalized_last_name = last_name.capitalize()

        projekt_pojisteni.fullname_lookup(capitalized_first_name, capitalized_last_name)
    elif volba == 2:#vypise vsechny
        projekt_pojisteni.vypis_vse()
    elif volba == 1:#prida klienta
        projekt_pojisteni.add_client()
    else:
        print("Zadej prosím číslo od 1 - 4 pro volbu akce")
        projekt_pojisteni.vymaz()
        lets_continue = input("Chcete pokračovat? (ano/ne)")

#-----------------  TOHOTO SI NEVŠÍMAT, JEN JSEM ZKOUŠEL ------------------------

#------------------------VÝPIS VŠECH-----------------------------------
# projekt_pojisteni.vypis_vse()

#---------------------VYHLEDÁVÁNÍ POMOCÍ MAILU--------------------------

# email = input("Zadejte prosím email...")
# # projekt_pojisteni.email_lookup(email)


#--------------------VYHLEDÁVÁNÍ POMOCÍ JMÉNA----------------

# name = input("Zadejte prosím jméno: ")
# projekt_pojisteni.name_lookup(name)

#-------------------VYHLEDÁVÁNÍ POMOCÍ JMÉNA A PŘÍJMENÍ-----------------

# first_name = input("Zadejte prosím jméno: ")
# last_name = input("Zadejte prosím příjmení: ") 
# projekt_pojisteni.fullname_lookup(first_name, last_name)


#------------------------PŘIDÁNÍ DALŠÍHO KLIENTA----------------------

# projekt_pojisteni.add_client()

#-------------------------VYMAZÁNÍ KONZOLE-------------------------------
#                 takové to...chcete pokracovat ? + cls

