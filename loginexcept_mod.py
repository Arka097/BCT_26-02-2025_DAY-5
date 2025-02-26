from prettytable import PrettyTable

users = []  # List to store user data

def sign_up():
    try:
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        password = input("Enter Password: ").strip()

        if name and email and password:  # Ensure no empty input
            users.append({"name": name, "email": email, "password": password})
            print("Sign-up successful!\n")
        else:
            print("All fields are required!\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

def login():
    try:
        email = input("Enter Email: ").strip()
        password = input("Enter Password: ").strip()

        # **Forcing an error for testing purposes**
        if email == "error":
            print(1 / 0)  # This will cause ZeroDivisionError

        for user in users:
            if user["email"] == email and user["password"] == password:
                print("Login successful!\n")
                return

        print("Login failed! Incorrect email or password.\n")
    except ZeroDivisionError:
        print("An intentional error occurred: Division by zero!\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

def show_users():
    try:
        if not users:
            print("No users available.\n")
            return

        table = PrettyTable(["Name", "Email"])
        for user in users:
            table.add_row([user["name"], user["email"]])

        print("\nRegistered Users:")
        print(table)
    except Exception as e:
        print(f"An error occurred: {e}\n")

def delete_user():
    try:
        email = input("Enter Email to delete: ").strip()

        for user in users:
            if user["email"] == email:
                users.remove(user)
                print("User deleted.\n")
                return

        print("User not found.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

while True:
    try:
        print("\n1. Sign Up\n2. Login\n3. Show Users\n4. Delete User\n5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            show_users()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")
    except Exception as e:
        print(f"An unexpected error occurred in the menu: {e}\n")
