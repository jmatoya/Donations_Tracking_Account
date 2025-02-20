from donations_pkg.homepage import show_homepage

def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f"Welcome back {username}!")
            return username
        else:
            print("Incorrect password!")
            return ""
    else:
        print("Username not found. Please register.")   
        return ""
    
def register(database, username):
    if username in database:
        print("Username already registered! ")
        return ""
    else:
        print(f"{username} has been registered.")
        show_homepage()
        return username


    
        
    


