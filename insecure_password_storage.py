import hashlib

# Sample user database as a dictionary
users_db = {}

def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # UNSAFE: Storing the password in plaintext
    users_db[username] = password
    print(f"User {username} registered successfully!")

def login_user():
    username = input("Enter username to login: ")
    password = input("Enter password: ")

    # UNSAFE: Comparing password in plaintext
    if username in users_db and users_db[username] == password:
        print(f"Welcome back, {username}!")
    else:
        print("Invalid username or password.")

def change_password():
    username = input("Enter your username: ")
    old_password = input("Enter your current password: ")

    if username in users_db and users_db[username] == old_password:
        new_password = input("Enter your new password: ")
        # UNSAFE: Storing the new password in plaintext
        users_db[username] = new_password
        print("Password changed successfully!")
    else:
        print("Invalid username or password.")

def display_users():
    print("Registered Users:")
    for username, password in users_db.items():
        print(f"Username: {username}, Password: {password}")

# Main function for user interaction
def main():
    while True:
        print("\n1. Register User")
        print("2. Login")
        print("3. Change Password")
        print("4. Display Users (For testing only)")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            change_password()
        elif choice == '4':
            display_users()
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
