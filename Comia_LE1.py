import sys
game_library = {'Donkey kong': {'Cost': 2, 'Quantity': 5},
                'Tetris': {'Cost': 2, 'Quantity': 3},
                'Super Mario': {'Cost': 3, 'Quantity': 3}}
user_databse =  {'Name': {'Balance': 0,'Password':{}, 'Inventory': {} }
                }
admin_username = "admin"
admin_password = "adminpass"      

RedeemCodes = ['12345FREE', 'IAMHWUAPPY', 'PAZERKAMPFWAGEN', 'IAMSUAD', 'PANZERVOLKSWAGEN', 'T90MBREAKTHROUGH', 'M1A2ABRAHAMS']
def main():
    while True:
        try:
            print("********** Welcome to the Game rental stysrem **********")
            print("1.Display Available Games")
            print("2.Register User")
            print("3.Log in")
            print("4.Admin Login")
            print("5.Exit")
            print("********************")

            user_input = input("Choose an acton (1-5): ")
            if user_input == '1':
                display_available_games()
                break
            if user_input == '2':
                register()
                break
            if user_input == '3':
                login()
                break
            if user_input == '4':
                admin_credentias_check()
                break
            if user_input == '5':
                sys.exit("Terminating program...")
        
        except ValueError:
            print("Invalid input. Please try again.")

def display_available_games():
    for key, value in game_library.items():
        print(f" Game name: {key} Details: {value}")
    while True:
        try:
            choice = input("Return to main menu? (Yes or No): ").upper().strip()
            if choice == 'YES':
                main()
                break
            elif choice == 'NO':
                continue
            else:
                print("Invalid Input. Please try again")
        except ValueError:
            print("Invalid input. Please try again!")

    
def register():
    while True:
        try:
            username = input("Enter your username: ")
            if username in user_databse:
                print("User already exist! Please enter another name.")
                continue
            else:
                print("User name is valid.")
            if not username:
                main()
            
            password = input("Enter a password no less than 8 chatacters: ")
            if password in user_databse:
                print("Passowrd already exist. Please select enter a new one.")
                continue
            if len(password) < 8:
                print("Pasword length must be eqaul to or greater than 8. ")
                continue
            verify_password = input("Verify your password: ")
            if verify_password != password:
                print("Passwords do not match. Please try again.")
                continue
            else:
                print("Password verified.")
            
            user_info = { 'Balance' : 0, 
                        'Password' : password,
                        'Inventory': {}
            }
            user_databse[username] = user_info
            print("Account successfully registered")
            logged_in_main_menu(username)
            break
        except ValueError:
            print("Invalid input. Please try again.")

def login():
    while True:
        try:
            username = input("Enter your user name: ").strip()
            if not username:
                main()
                break
            if username not in user_databse:
                print("User does not exist. Please note that usernames are case sensitive.")
                continue
            else:
                print("User found.")
            
            password = input("Please enter you password: ")
            if password != user_databse[username]['Password']:
                print("Invalid credentials. Please try again.")
                continue
            else:
                print("User successfully logged in.")
                logged_in_main_menu(username)
                break
        except ValueError:
            print("Invalid Input. Plase try again.")

def admin_credentias_check():
    while True:
        try:
            admin_name = input("Enter your your admin username: ")
            if admin_name != admin_username:
                print("Invalid credentials")
                admin_credentias_check()
            elif not admin_name:
                main()
                break
            else:
                print(f"Username {admin_name} found.")

            password = input("Enter you password: ")
            if  password != admin_password:
                print("Invalid Credentilas")
                continue
            else:
                print("Succesfully logged in")
                print(f" Welcome {admin_name}")
                admin_menu()
                break
        except ValueError:
            print("Invalid Input")

def admin_menu():
    while True:
        try:
            print("What would you like to do?: ")
            print("1. Change Quantity")
            print("2. Change Price")
            print("3. Add a new game")
            print('4. Log out')

            admin_choice = (input("Enter course of action (1-5): "))
            if admin_choice == '1':
                admin_change_quantity()
                break
            if admin_choice == '2':
                admin_change_price()
                break
            if admin_choice == '3':
                admin_add_new_game()
                break
            if admin_choice == '4':
                main()
                break
        except ValueError:
            print('Invalid Input')

def admin_change_quantity():
    while True:
        try:
            game_name = input("Enter the name of the game you wish to update: ")
            if not game_name:
                admin_menu()
            if game_name not in game_library:
                print("Game does not exist. Please try again")
                admin_change_quantity()
            else:
                print("Game successfully selected.")

            new_quantity = int(input(f"Enter the new quantitiy of copies to add to {game_name}: "))
            game_library[game_name]['Quantity'] += new_quantity
            print(f"The game {game_name} has been successfully updated.")

            admin_menu()
            break
        except ValueError:
            print("Invalid Input. Please try again")
            admin_change_quantity()

def admin_change_price():
    while True:
        try:
            game_name = input("Enter the name of the game you wish to update: ")
            print("Leave blank and press enter to retun to the main menu.")
            if not game_name:
                admin_menu()
                print("Returning to main menu...")
                break
            if game_name not in game_library:
                print("The game does not exist. Please try again")
                continue
            else:
                print("Game successfully selected")
            
            new_price = int(input(f"Etner the new price for {game_name}: "))
            game_library[game_name]['Cost'] += new_price
            print(f"The game {game_name} has been successfully updated.")

            admin_menu()
            break
        except ValueError:
            print("Invalid input. Please try again")
            admin_change_price()

def admin_add_new_game():
    while True:
        try:
            game_name = input("Enter tha name of the game you wish to add")
            if game_name in game_library:
                print("The game is already listed on the game library.")
                admin_menu()
            else:
                print(f"The game {game_name} has been successfully adeed into the game library.")
                quantity = int(input("Enter the amount of available copies: "))
                cost = int(input(f"Enter the cost for {game_name}: "))
            
                admin_newgame = {game_name : {'Cost': cost, 'Quantity': quantity}}
                game_library.update(admin_newgame)
                print(f"The game {game_name} with a quantity of {quantity} and a cost of {cost} has benn successfully added!")
                print("Returning to main menu...")

                admin_menu()
                break
        except ValueError:
            print("Invalid input. Please try again.")

def logged_in_main_menu(username):
    while True:
        try:
            print(f"Welcome {username}!")
            print("*"*18)
            print("1.Rent a Game")
            print("2.Return a Game")
            print("3.Top Up Account")
            print("4.Display Inventory")
            print("5.Redeem Free Game")
            print("6.Check Points")
            print("7. Log Out")
            print("*"*18)

            user_action = input("What would you lke to do?:")
            if user_action == '1':
                rent_a_game(username)
                break
            if user_action == '2':
                return_a_game(username)
                break
            if user_action == '3':
                top_up(username)
                break
            if user_action == '4':
                display_inventory(username)
                break
            if user_action == '5':
                redeem_game(username)
                break
            if user_action == '6':
                check_points(username)
                break
            if user_action == '7':
                main()
                break
        except ValueError:
            print("Invalid Input. Please try again.")

def rent_a_game(username):
    while True:
        try:
            game_to_rent = input("Enter the name of the game you wish to input (Leave blank and press enter to return to menu): ")
           
            if not game_to_rent:
                logged_in_main_menu(username)
                break
            if game_to_rent not in game_library:
                print("Game does not exsit! Please try again")
                continue
          
            print(f"The game {game_to_rent} has been selected!")

            if game_library[game_to_rent]['Quantity'] <= 0:
                print("Insufficient stocks!")
                continue
          
            quantity_to_rent = int(input("Enter the amount you wish to rent: ")) 
            total_cost = quantity_to_rent * game_library[game_to_rent]['Cost']

            if user_databse[username]['Balance'] < total_cost:
                print(f"The user {username} has insufficient balance! Consider topping up!")
                logged_in_main_menu(username)
                break


            if game_to_rent in user_databse[username]['Inventory']:
                user_databse[username]['Inventory'][game_to_rent] += quantity_to_rent
            else:
                user_databse[username]['Inventory'][game_to_rent] = quantity_to_rent

            game_library[game_to_rent]['Quantity'] -= quantity_to_rent
            user_databse[username]['Balance'] -= total_cost

            print(f"The game {game_to_rent} has been successfully rented with the total cost of {total_cost}  and quantity of {quantity_to_rent}. ")
            logged_in_main_menu(username)
            break
        except ValueError:
            print("Invalid input. Please try again.")

def return_a_game(username):
    while True:
        try:
            game_name = input('Input the name of the game you wish to return: ')
            if not game_name:
                logged_in_main_menu(username)
            if game_name not in user_databse[username]['Inventory']:
                print("The game does not exist. Please check if you are renting any games.")
                print("********* Inventory *********")
                display_inventory(username)
                logged_in_main_menu(username)
                break

            copies_to_return = int(input("How many copies would you like to return?"))
            if copies_to_return < user_databse[username]['Inventory'][game_name]:
                print("Quanity entered was more than what was rented. Please try again! ")
                continue
            if copies_to_return <= 0:
                print("No copies returned. Please enter a non-zero or negative integer!")
                continue

            user_databse[username]['Inventory'][game_name] -= copies_to_return
            game_library[game_name]['Quantity'] += copies_to_return

            print(f"The game {game_name} has been successfully returned")
            print("Returning you now to the main menu")
            logged_in_main_menu(username)
            break
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")

def display_inventory(username):
    if not user_databse.get(username, {}).get('Inventory'):
        print("Your inventory is empty")
        logged_in_main_menu(username)
    else:

        print(f"Hello {username}, your inventory is as follows:")
        if username in user_databse:
            for key, value in user_databse[username]['Inventory'].items():
                print(f"Game: {key}, Quantity: {value}")
        else:
            print(f"{username} does not exist")
            main()
        while True:
            try:
                print("Return to user main menu?")
                user_choice = input("Yes or No?: ").strip().upper()
                if user_choice == 'YES':
                    logged_in_main_menu(username)
                    break
                elif user_choice == 'NO':
                    display_inventory(username)
                    break
                else:
                    print("Invalid Input> Please try again!")
                    continue
            except ValueError:
                print("Invalid Input. Please try again!")
            
def top_up(username):
    while True:
        try:
            print("Welcome to the top up menu!")
            print("Exchange rate: \n 1$ = 3 points")

            top_up_amount = int(input("Enter the amount to top up (Non-zero Integers only): "))
            if top_up_amount <= 0:
                print("Please do not enter zero or negative integers !!!")
                continue

            points_balance = top_up_amount * 3

            print(f"Confirm amout to top up. {top_up_amount}$ for {points_balance} points")
            print("Proceed with top-up? Note: NON-REFUNDABLE")

            user_choice = input("Yes or No?: ").strip().upper()
            if user_choice =='YES':
                user_databse[username]['Balance'] += points_balance
                print(f"{points_balance} points has been added to the user {username}")
                
                action = input("Show Balance? (Yes or No): ").strip().upper()
                if action == 'YES':
                    check_points(username)
                    break
                elif action =='NO':
                    print("Returning to main...")
                    logged_in_main_menu(username)
                    break
                else:
                    print("Invali input. Please try again!")

            elif user_choice =='NO':
                top_up(username)
            else:
                print("Invalid Input. Please try again!")
                continue
        except ValueError:
            print("Invalid Input")


def redeem_game(username):
    print(f"Welcome to the redeem shop {username}")
    while True:
        try:
            redeem_code = input("Enter the redeem code: ").strip().upper()
            print("Leave blank and press enter to return to the main menu !!!")
            if redeem_code not in RedeemCodes:
                print("Invalid redeem code!")
                continue
            elif not redeem_code:
                logged_in_main_menu(username)
                break
            elif redeem_code in RedeemCodes:
                print("Redeem code successfully verified.")
                redeem_game_with_code(username)
                break
            else:
                print("Invlaid input. Please try again. ")
        except ValueError:
            print("Invalid input. Please try again")

def redeem_game_with_code(username):
    while True:
        try:
            print("NOTE: Using redeem codes to rent games entitles you to be able to rent one game with exactly one copy")
            game_name = input("Enter the game you wish to redeem: ")
            if game_name in game_library:

                quantity_to_rent = 1

                if game_name in user_databse[username]['Inventory']:
                    user_databse[username]['Inventory'][game_name] += quantity_to_rent
                else:
                    user_databse[username]['Inventory'][game_name] = quantity_to_rent
                
                game_library[game_name]['Quantity'] -= quantity_to_rent

                print(f"The gamne {game_name} has been added to your inventory.")
                print("Returning yo main menu...")
                logged_in_main_menu(username)
                break
            elif game_name not in game_library:
                print("Game does not exsit. Please try again")
                continue
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def check_points(username):
    
    points = user_databse[username]['Balance']

    print(f"{username}, you have {points} points available in your account")

    while True:
        try:
            user_actions = input("Return to main menu (Yes or No): ").strip().upper()
            if user_actions == 'YES':
                print("Returing to the main menu...")
                logged_in_main_menu(username)
                break
            elif user_actions =='NO':
                continue
            elif not user_actions:
                logged_in_main_menu(username)
                break
            else:
                print("Invalid Input. Please try again")
        except ValueError:
            print("Invalid input. Please try again!")
         
main()