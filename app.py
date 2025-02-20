from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "password123"}
donations = []
authorized_user = ""

show_homepage()

if authorized_user == "":
    print("\nYou must be logged in to donate.\n")
else:
    print(f"\nLogged in as: {authorized_user}\n")
while True: 
    user_input = int(input("Choose an option: "))
    
    if user_input == 1:
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
        show_homepage()

        if authorized_user:
            print(f"Logged in as: {username}")
        else:
            print("Login failed. Please try again.")
            
    elif user_input == 2:
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    elif user_input == 3:
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif user_input == 4:
        show_donations(donations)
    elif user_input == 5:
        print("GoodBye!")
        exit()





 










