import funcs
import datetime
import bcrypt

user = "0"
server_token = None
user_token = None

while user != "q":
    funcs.menu()
    user = input("Choose: ")

    if user == "1": # Create user
        user_name = input("Name: ")
        users = funcs.read_json("users.json") #Here is the list of users logged in the Json file
        users_names = [user["name"] for user in users["data"]] #Usernames of each usernames in the list
        try:
            users_names.index(user_name) #- Searches if the name chosen by user is in the list, if it is, print line 19
            print("El user existe")
        except ValueError: #If not in the list, system allows to create new account
            user_pwd = input("Password: ")
            new_user = {"name": user_name, "pwd": bcrypt.hashpw(user_pwd.encode(), bcrypt.gensalt()).decode(), "user_since": datetime.date.today().isoformat()} #Here creates new account with encripted pw
            users["data"].append(new_user) #Append to users list
            funcs.create_user(users, "users.json") #It saves in JSON file
            
    elif user == "2": # Log in
        user_name = input("Name: ")
        user_pwd = input("Password: ")
        users = funcs.read_json("users.json")
        
        for user in users["data"]:
            if user["name"] == user_name: #If username in the json list is the same as user_name:
                if bcrypt.checkpw(user_pwd.encode(), user["pwd"].encode()): # and if the password is the same, prints next line
                    print("Log in!")
                    user_token = {"expired_date": datetime.datetime.today(), "token": bcrypt.hashpw((user_pwd + user_name).encode(), bcrypt.gensalt())} 
                    server_token = user_token["token"]
                else:
                    print("User or password incorrect!")

    elif user == "3":
        if user_token:
            if (user_token["expired_date"] + datetime.timedelta(seconds=10)) > datetime.datetime.today():
                if user_token["token"] == server_token:
                    user_new_pwd_1 = input("New password: ")
                    user_new_pwd_2 = input("Repeat password: ")
                    if user_new_pwd_1 == user_new_pwd_2:
                        for user in users["data"]:
                            if user["name"] == user_name:
                                user["pwd"] = bcrypt.hashpw(user_new_pwd_1.encode(), bcrypt.gensalt()).decode()
                                funcs.create_user(users, "users.json")
                    else:
                        print("passwords don't match")