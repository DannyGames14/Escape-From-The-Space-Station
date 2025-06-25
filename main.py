import time
import random
inventory=[]
health = 100

def print_slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print()

def random_event():
    global health
    event = random.choice(["nic", "zranění", "baterie"])

    if event == "nic":
        print("Nic zvláštního se nestalo...")
    elif event == "zranění":
        damage = random.randint(10, 60)
        health -= damage
        print(f"Upadl jsi přes potrhaný drát. Ztratil jsi {damage} HP. Zbývá ti {health} HP")
    elif event == "baterie":
        print("Na zemi jsi našel náhradní baterky")
        inventory.append("baterie")

def show_inventory():
    print("\n---INVENTÁŘ---")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Inventář je prázdný")
    print("---------------------\n")

def start_game():
    print_slow("Probudil ses v potemnělé místnosti vesmírné stanice...")
    print_slow("Nemáš ponětí co se stalo")
    print_slow("Na zemi leží svítilna.")
    first_room()

def first_room():
    print("\nCo chceš udělat?")
    print("1. Zvednout svítilnu")
    print("2. Odejít z místnosti")
    choise = input("> ")

    if choise.lower() == "inv":
        show_inventory()
        return first_room()

    if choise == "1":
        if "svítilna" not in inventory:
            inventory.append("svítilna")
            print("Svítilna je nyní ve tvém inventáři")
            hallway()
        else:
            print("Svítilnu již máš. Nevejde se ti do inventáře")
            first_room()
    elif choise == "2":
        print("Svítilnu jsi nezvedl.")
        hallway()
    else:
        print("Neplatná volba")
        first_room()

def hallway():
    print_slow("\nVyšel jsi na temnou chodbu.")
    if "svítilna" in inventory:
        print_slow("Svítilna osvětluje cestu")
    else:
        print_slow("Ve tmě skoro nic nevidíš")

    random_event()
    if health <= 0:
        print("Umřel jsi")
        exit()

    print("Na konci chodby jsou dvoje dveře.")
    print("1. Vlevo - dveře s panelem")
    print("2. Vpravo - těžké kovové dveře")
    print("3. Dveře s červeným varováním")
    print("4. dveře se žlutým pruhem")
    choise2 = input("> ")

    if choise2.lower() == "inv":
        show_inventory()
        return hallway()

    if choise2 == "1":
        control_room()
    elif choise2 == "2":
        storage_room()
    elif choise2 == "3":
        alien_room()
    elif choise2 == "4":
        maintenance_room()
    else:
        print("Neplatná volba")
        hallway()

def control_room():
    print_slow("\nVstoupil jsi do ovládací místnosti.")

    random_event()
    if health <= 0:
        print("Umřel jsi")
        exit()

    print_slow("Vidíš blikající terminál s nápisem: Zadej kód pro odemčení únikového modulu.")

    code = input("Zadej kód: ")
    if code == "042":
        print_slow("Kód přijat! Start modulu selhal.")
        if "laser_gun" in inventory:
            print("Použít laserovou pistoli?")
            choice = input("> ")
            if choice == "ano":
                print_slow("Terminál jsi rozstřelil. Zdá se, že modul je připraven letět")
                escape()
        hallway()
    else:
        print_slow("Kód odmítnut. Zkus se porozhlédnout jinde.")
        hallway()
def storage_room():
    print_slow("\nVstoupil jsi do skladu.")
    if "kód" not in inventory:
        print_slow("Na zemi leží lístek s psaním")
        print("1. Sebrat lístek")
        print("2. Vrátit se do chodby")
        choice = input("> ")

        if choice.lower() == "inv":
            show_inventory()
            return storage_room()

        if choice == "1":
            inventory.append("kód")
            print("Sebral jsi lístek.")
            if "svítilna" in inventory:
                print("Posvítil sis na lístek.")
                print("Stojí na něm kód 042")
            hallway()
        elif choice == "2":
            hallway()
        else:
            print("Neplatná volba.")
            storage_room()
    else:
        print("Už tu nic není")
        hallway()

def maintenance_room():
    print_slow("\nVstoupil jsi do údržbářské místnosti")
    if "klíč" not in inventory:
        print_slow("Na stole leží klíč")
        print("1. Sebrat klíč")
        print("2. Vrátit se na chodbu")
        choise = input("< ")

        if choise.lower() == "inv":
            show_inventory()
            return maintenance_room()

        if choise == "1":
            inventory.append("klíč")
            print("Sebral jsi klíč. Nyní je ve tvém inventáři")
            hallway()
        elif choise == "2":
            hallway()
        else:
            print("Neplatná volba")
            maintenance_room()
    elif "svítilna" in inventory:
        print_slow("Svítilna osvětluje dveře na konci místnosti.")
        print("Chceš do dveří vstoupit?")
        choice = input("> ")

        if choice == "ano":
            infantry()
        hallway()
    else:
        print("Už tu nic není")
        hallway()

def infantry():
    print_slow("Vstoupil jsi do márnice!")
    print_slow("aaah...")
    print_slow("Na zemi leží zraněný člen posádky!")
    print("Chceš s ním mluvit?")
    choice = input("> ")

    if choice == "ano":
        print("Znemožnil nám únik, nic s tím neuděláme. Mužeme to akorát celé odpálit!")
    maintenance_room()
def alien_room():
    if "klíč" not in inventory:
        print("Nemáš klíč k těmto dveřím")
        hallway()
        return

    print_slow("Dveře jsou zadrhlé a otvíraly se pomalu.")
    print("V místnosti je MIMOZEMŠŤAN!")
    print("1. Pokusit se bojovat")
    print("2. Pokusit se utéct")
    choise = input("> ")

    if choise == "2":
        print("Utíkáš do chodby a zaboucháváš dveře.")
        hallway()
    elif choise == "1":
        result = random.choice(["výhra", "prohra"])
        if result == "výhra":
            print("Porazil jsi mimozemšťana! V jeho hnízdě je laserová pistole!")
            if "laser_gun" not in inventory:
                inventory.append("laser_gun")
                hallway()
        else:
            print_slow("Myslím...")
            time.sleep(2)
            print_slow("...že si není dobré zacházet si s mimozemšťany.")
            print("Mimozemšťan tě porazil... Umřel jsi!")
            start_game()
    else:
        print("Neplatná volba. Mimozemšťan tě porazil... Umřel jsi!")
        exit()

def escape():
    print_slow("Nasedl jsi do únikového modulu a odlétáš k Zemi! VYHRÁL JSI!")
    exit()

start_game()