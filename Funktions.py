import getpass
import hashlib


def login() -> str:
    """
    Doesn't take any arguments, returns username
    as String. This funktion asks user for two inputs
    1. Username and 2. password.
    It then hashes the password and checks if username is found
    in Users.txt and the hashed password matches the one in the file.

    If user login credentials are correct, the funktion returns
    username, if not then credentials are asked again
    """
    while True:
        usrname = input("Enter your username: ")
        pswrd = getpass.getpass(prompt="Enter your password: ")
        hashed = hashlib.sha256(pswrd.encode("utf-8")).hexdigest() #Hashing the password with SHA-256 and turning it into "readable" format

        #Changed from md5 to sha-256 after teachers advice, and finding out that people have actually been able to decypher md5 hashes
        #I did however think that salting the passwords would be a little overkill for such a small project, if i ever do something using this as a template
        #- and put it online, then i'll definetly look into salting more.

        with open("Users.txt") as t:    #Opening the file with user credentials
            for i in t:     #For loop for reading every line seperatly
                i = i.strip()
                twoparts = i.split()    #Splitting line in to a list with username and password seperatly
                if twoparts[1] == hashed and twoparts[0] == usrname: #Checking to see if username and password match in that line
                    t.close()
                    return usrname
        print("Username or parssword incorrect, please try again") #This code runs only if username or password is incorrect
        input("Press enter to continue...")

def register():
    """
    Doesn't take any arguments or return anything.
    This Funktion takes 3 inputs, first username
    and then password twice. Then it checks the file
    "Users.txt" if someone with that username exists.
    If username isn't in use, it checks if the password
    is in correct format, if it is, Users.txt file is opened
    with append mode and new users credentials are written and saved.
    """
    while True:
        print("\nRegister new account!\n")
        usrname = input("Username (Leave empty to exit): ")
        if usrname == "":
            print("")
            return
        elif len(usrname) <= 30:
            if not any(char.isspace() for char in usrname):     #Check to see if username contains spaces
                sameuser = False
                print("\nThe password requirements:\n*The password needs to be atleas 8 characters long.\n*Password needs to contain atleast 1 uppercase charachter\n*The password has to contain atleast 1 lowercase charachter\n*The password has to contain atleast one number\n*The password cant contain any spaces\n")
                pswrd = getpass.getpass(prompt="Password: ")
                password = getpass.getpass(prompt="Re-Enter your password: ")
                if pswrd == password:
                    with open("Users.txt") as t:    #Opening user credential file
                        for i in t:         #Loop to go trough every line
                            i = i.strip()
                            twoparts = i.split()        #Cleaning the line up and splittin to list with two parts
                            if twoparts[0] == usrname:  #Checking if username already exists
                                sameuser = True
                                print("Account with that username allready exists, try again.")
                        t.close()
                    if sameuser == False:
                        if len(pswrd) >= 8:     #Is length 8 charachters or over
                            if any(char.islower() for char in pswrd):   #Does password contain any uppercase charachters
                                if any(char.isupper() for char in pswrd):   #Does it contain uppercase charachters
                                    if any(char.isdigit() for char in pswrd):   #Does password contain digits
                                        if not any(char.isspace() for char in pswrd):      #Checks for spaces in passwords
                                            with open("Users.txt", "a") as file:
                                                hashed = hashlib.sha256(pswrd.encode("utf-8")).hexdigest()     #Hashing password for safer storing
                                                file.write(f"{usrname} {hashed}\n")
                                                print("Account created succesfully!")
                                                input("Press enter to continue...")
                                                return

                                        else:                                                       #if password contains spaces
                                            print("Password cant contain any spaces, try again")
                                            input("Press enter to continue...")
                                    else:                                                          #If password doesn't contain any digits
                                        print("Password requires atleast 1 digit, try again")
                                        input("Press enter to continue...")
                                else:                                                          #If password doesn't contain any uppercase charachters
                                    print("Password requires atleast 1 uppercase charachter, try again")
                                    input("Press enter to continue...")
                            else:                                                   #If password doesn't contain any lowercase charachters
                                print("Password requires atleast 1 lowercase charachter, try again")
                                input("Press enter to continue...")
                        else:
                            print("Password needs to contain atleast 8 charachters, try again")
                            input("Press enter to continue...")
                else:                                                       #If passwords dont match
                    print("Passwords didn't match, try again")
                    input("Press enter to continue...")
        else:                                                           #If username contains spaces
            print("Username cant contain any spaces, try again")
            input("Press enter to continue...")
    else:                                                           #If username is too long
        print("Username cant contain more than 30 charachters, try again")
        input("Press enter to continue...")

def logged_in(usrname: str):
    """
    Has one String argument "usrname", Funktion is called after
    login has been succesfull and displays the menu for logged in users.
    """
    while True:
        try:
            print(f"\nWelcome back {usrname}\n\nWould you like to:\n1.Print a cool pyramid\n2.Print a square\n3.Calculator\n4.Sign out\n5....")
            kysely = int(input("Choose(1/2/3/4): "))
        except ValueError:
            input("Please enter option 1, 2, 3, 4 or 5 (Press enter to continue)")
        else:
            if kysely in range(1, 6):
                if kysely == 1:
                    print_pyramid()

                if kysely == 2:
                    print_square()

                if kysely == 3:
                    calculator()

                if kysely == 4:
                    print("Signed out\n")
                    return

                if kysely == 5:
                    trollface()
            else:
                input("Please enter option 1, 2, 3 or 4 (Press enter to continue)")

def print_pyramid():
    """
    Doesn't take arguments or return, prints a pyramid.
    """
    print("      #\n     ###\n    #####\n   #######\n  #########\n ###########\n#############")
    print("")

def print_square():
    """
    Doesn't take arguments or return anything, just prints a square
    """
    for i in range(0,6):
        print("############")

def calculator():
    """
    Doesn't take any arguments or return anything,
    just a simple calculator that asks for counting mode,
    and two variables and prints the result of the calculation.
    """
    while True:
        exception = True        #Exception set to true so while loop starts on the first time
        mode = input("\nPlease enter counting mode(+ / * -), leave empty to exit: ")
        if mode == "":
            return
        elif mode == "+" or mode == "/" or mode == "*" or mode == "-":
            while exception == True:
                try:
                    exception = False       #Setting exception to false so while loop doesnt go again without errors
                    Firstnumber = int(input("Please enter the first number: "))
                    Secondnumber = int(input("Please enter the second number: "))
                except ValueError:
                    exception = True        #Exception back to True so inputs are asked again
                    input("Please enter only numbers(Press enter to continue)")
            if mode == "+":
                print(f"\n{Firstnumber} + {Secondnumber} = {Firstnumber + Secondnumber}")
            elif mode == "/":
                print(f"\n{Firstnumber} / {Secondnumber} = {Firstnumber / Secondnumber}")
            elif mode == "*":
                print(f"\n{Firstnumber} * {Secondnumber} = {Firstnumber * Secondnumber}")
            elif mode == "-":
                print(f"\n{Firstnumber} - {Secondnumber} = {Firstnumber - Secondnumber}")
        else:
            input("\nPlease enter '+' '/' '-' or '*' (Press enter to continue)")






def trollface():
    """
    Dont mind this funktion, its secret.
    (Also doesn't take variables or return anything)
    Used to print something.
    """
    NotTrollface = """
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣛⣋⣉⣉⣉⣉⣉⣉⣉⣉⣉⢀⣀⡠⠤⠤⠤⠤⠤⣀⣉⣑⠲⢦⣄⡀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡿⠟⠉⠀⠈⠁⢀⡤⠤⠭⣉⣉⡉⠉⠉⠉⠀⠀⠀⢠⡤⠀⠀⠠⠤⠬⠭⣙⠢⢬⡙⠢⢄⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠠⡌⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣍⢳⡌⠙⠂⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡟⠀⠀⠀⠀⠁⢀⣀⣀⣀⣀⡀⠀⡇⠀⠀⠀⠀⠀⠀⢁⣠⣶⣶⢶⣶⣶⣶⣶⣦⣄⠈⠃⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿
    ⣿⣿⡿⢋⡠⠤⠤⠤⠤⢰⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⠀⠀⠀⣴⣿⠟⣉⣤⣾⣿⣿⣿⣿⣿⣽⣷⠄⠰⠶⠀⠀⠠⠤⠤⠾⣿⣿⣿⣿⣿
    ⣿⣏⡴⣫⠴⢂⣀⣀⡀⠀⠀⠈⠉⠉⠉⠉⠛⣿⡟⠉⠀⠀⠀⠉⠻⡿⠟⠉⠉⠀⢺⣦⣄⠈⠉⠁⢈⣡⣴⣶⠿⠿⣿⣶⣄⠀⠻⡿⣿⣿
    ⣿⣾⠀⡏⠺⠟⠛⠛⢻⣷⣤⣶⡆⠀⠀⠀⣠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠻⠿⠟⠛⠛⠋⣀⣼⡆⠀⠈⢻⣧⠀⣿⠙⣿
    ⣿⣿⡀⣧⡀⠀⣰⣿⠀⠉⠉⠀⠀⣀⣴⣾⠟⠃⠀⠀⠀⠀⠀⠀⠶⢶⣶⡲⢤⣀⣀⣀⠀⠀⠀⣀⣠⣶⡾⠿⢻⣿⣶⣤⡀⣿⠀⣿⠀⣿
    ⣿⣿⡳⠤⣅⢠⣿⣿⣦⠀⢠⠤⠜⠻⠿⢿⣦⡀⠀⠀⠀⠶⠿⠿⡷⣠⣿⠇⠀⢀⣀⣤⣤⣶⢿⣿⠏⠉⠀⣀⣾⡏⠉⠉⣼⡏⢀⠏⣴⣿
    ⣿⣿⣿⠀⠀⢸⣿⣿⢻⣿⣦⣤⣀⡀⠀⠀⠛⠿⠿⠇⠀⢀⣀⣠⣤⣬⣷⣾⣿⠟⠛⠛⠉⢀⣼⣿⣤⣴⣿⣿⡟⠁⠀⠀⠠⠖⣫⣾⣿⣿
    ⣿⣿⣿⡆⠀⢸⣿⣏⣸⡇⠈⣻⡿⠛⠻⠿⣿⡿⠿⠟⠻⣿⠟⠛⠋⠉⠀⢿⣷⣀⣠⣴⣶⣾⣿⣿⠛⣡⣾⠏⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿
    ⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣶⣿⣷⣤⣤⣤⣿⣧⣤⣤⣤⣿⣤⣤⣤⣶⣶⣿⣿⣿⠿⠿⠋⠉⢸⣿⣴⡿⠋⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿
    ⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⣿⣧⠀⠀⠀⣠⣴⡿⠋⠁⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡇⠀⠀⢻⣿⣿⡟⣿⣟⢻⣿⡟⠛⠻⣿⠋⠉⠉⠁⣿⠀⠀⠀⠀⠀⠘⣿⣄⣴⣿⠟⠉⠀⡀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠃⠀⠀⠀⠹⢿⣶⣾⣿⣄⣻⣷⣄⣀⣿⣇⣀⣀⣀⣿⣆⣠⣤⣴⣶⠾⠿⠛⢉⣀⡴⠶⣊⡠⠶⣫⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠀⠀⠀⠀⠠⣄⠀⠉⠉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠉⠉⢀⣠⠤⠖⢉⡥⠴⢊⣩⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠀⠀⢰⣄⠀⠈⠛⠦⢤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠠⠤⠤⣔⣺⣯⠭⠔⠚⢋⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣄⠀⠀⠈⠑⠲⠤⠤⠤⠤⠤⠤⠤⠀⠒⠒⠒⠒⠒⠋⠉⠀⠀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""
    print(NotTrollface)
#login()
#register()
