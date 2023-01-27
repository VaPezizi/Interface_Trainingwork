import Funktions

while True:
    try:
        print("_________________________\nWelcome to The Interface\n\nWould you like to:\n1.Sign in\n2.Register\n3.Exit")
        kysely = int(input("Choose(1/2/3): "))
    except ValueError:
        input("Please enter option 1, 2 or 3 (Press enter to continue)")
    else:
        if kysely in range(1, 4):
            if kysely == 1:
                print("")
                Username = Funktions.login()
                if Username != "":
                    Funktions.logged_in(Username)
                

            if kysely == 2:
                Funktions.register()

            if kysely == 3:
                exit()
        else:
            input("Please enter option 1, 2 or 3 (Press enter to continue)")
