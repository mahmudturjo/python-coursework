class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def describe(self):
        return f"User: {self.username}, Role: {self.role}"


class Admin(User):
    def __init__(self, username):
        super().__init__(username, "Admin")

    def has_privileges(self):
        return True


if __name__ == "__main__":
    user1 = User("alice", "Student")
    admin1 = Admin("bob")

    print(user1.describe())
    print(admin1.describe())
    print("Admin privileges:", admin1.has_privileges())
