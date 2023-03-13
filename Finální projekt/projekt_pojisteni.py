import sqlite3                      #import sqlite3

conn = sqlite3.connect('pojisteni.db')#propojení databáze

#vytvoření kurzoru
c = conn.cursor()


def uvod():
    print("------------------------------------------")
    print("Evidence pojištěných")
    print("------------------------------------------")
    

#----------------------------------------------------------------------------------------------------------------------------------------
def vypis_vse():
    print("JMENO" + "\t\t" + "PRIJMENI" + "\t\t" + "EMAIL" + "\t\t\t" + "VEK" + "\t\t" + "TELEFON")
    print("----" + "\t\t" + "--------" + "\t\t" + "------" + "\t\t\t" + "---" + "\t\t" + "-------")
    c.execute("SELECT * FROM pojisteni_lidi") #vzít všechny data z tabulky
    items = (c.fetchall())
    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + item[2] + "\t\t" + str(item[3]) + "\t\t" + str(item[4]))
#----------------------------------------------------------------------------------------------------------------------------------------
#hledaní s where
def email_lookup(email):
    c.execute("SELECT * from pojisteni_lidi WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
         print("JMENO" + "\t\t" + "PRIJMENI" + "\t\t" + "EMAIL" + "\t\t\t" + "VEK" + "\t\t" + "TELEFON")
         print("----" + "\t\t" + "--------" + "\t\t" + "------" + "\t\t\t" + "---" + "\t\t" + "-------")


    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + item[2] + "\t\t" + str(item[3]) + "\t\t" + str(item[4]))
#----------------------------------------------------------------------------------------------------------------------------------------
#hledaní s where
def name_lookup(name):
    c.execute("SELECT * from pojisteni_lidi WHERE jmeno = (?)", (name,))
    items = c.fetchall()

    for item in items:
         print("JMENO" + "\t\t" + "PRIJMENI" + "\t\t" + "EMAIL" + "\t\t\t" + "VEK" + "\t\t" + "TELEFON")
         print("----" + "\t\t" + "--------" + "\t\t" + "------" + "\t\t\t" + "---" + "\t\t" + "-------")


    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + item[2] + "\t\t" + str(item[3]) + "\t\t" + str(item[4]))
#----------------------------------------------------------------------------------------------------------------------------------------
#hledaní s where
def fullname_lookup(name, prijmeni):
    c.execute("SELECT * from pojisteni_lidi WHERE jmeno = (?) AND prijmeni = (?)", (name, prijmeni))
    items = c.fetchall()

    for item in items:
         print("JMENO" + "\t\t" + "PRIJMENI" + "\t\t" + "EMAIL" + "\t\t\t" + "VEK" + "\t\t" + "TELEFON")
         print("----" + "\t\t" + "--------" + "\t\t" + "------" + "\t\t\t" + "---" + "\t\t" + "-------")


    for item in items:
        print(item[0] + "\t\t" + item[1] + "\t\t" + item[2] + "\t\t" + str(item[3]) + "\t\t" + str(item[4]))
#----------------------------------------------------------------------------------------------------------------------------------------
# přidání 1 klienta
def add_client():
    jmeno = input("Zadej jméno: ")
    prijmeni = input("Zadej příjmení: ")
    email = input("Zadej email: ")
    vek = input("Zadej věk: ")
    telefon = input("Zadej telefon: ")
        
    c.execute("""
    INSERT INTO pojisteni_lidi (jmeno, prijmeni, email, vek, telefon)
    VALUES (?,?,?,?, ?)
    """, (jmeno, prijmeni, email, vek, telefon))

    conn.commit ()

    print(f"Přidán nový klient: {jmeno}\t{prijmeni}\t{email}\t{vek}\t{telefon}")


# MAZÁNÍ KONZOLE()

def vymaz():
    import os
    import time
    time.sleep(4)
    os.system("cls")

