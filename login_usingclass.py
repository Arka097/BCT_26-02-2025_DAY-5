from prettytable import PrettyTable

class UserManager:
    def __init__(self):
        self.users = []

    def sign_up(self):
        try:
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            password = input("Enter Password: ").strip()

            if name and email and password:
                self.users.append({"name": name, "email": email, "password": password})
                print("Sign-up successful!\n")
            else:
                print("All fields are required!\n")
        except Exception:
            print("An error occurred. Please try again.\n")

    def login(self):
        try:
            email = input("Enter Email: ").strip()
            password = input("Enter Password: ").strip()

            for user in self.users:
                if user["email"] == email and user["password"] == password:
                    print("Login successful!\n")
                    return
            print("Login failed! Incorrect email or password.\n")
        except Exception:
            print("An error occurred. Please try again.\n")

    def show_users(self):
        try:
            if not self.users:
                print("No users available.\n")
                return

            table = PrettyTable(["Name", "Email"])
            for user in self.users:
                table.add_row([user["name"], user["email"]])

            print("\nRegistered Users:")
            print(table)
        except Exception:
            print("An error occurred. Please try again.\n")

    def delete_user(self):
        try:
            email = input("Enter Email to delete: ").strip()

            for user in self.users:
                if user["email"] == email:
                    self.users.remove(user)
                    print("User deleted.\n")
                    return

            print("User not found.\n")
        except Exception:
            print("An error occurred. Please try again.\n")


if __name__ == "__main__":
    manager = UserManager()

    while True:
        try:
            print("\n1. Sign Up\n2. Login\n3. Show Users\n4. Delete User\n5. Exit")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                manager.sign_up()
            elif choice == "2":
                manager.login()
            elif choice == "3":
                manager.show_users()
            elif choice == "4":
                manager.delete_user()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Try again.\n")
        except Exception:
            print("An unexpected error occurred. Please try again.\n")
