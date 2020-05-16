from classes import User, Privileges, Admin

user1 = User('Lam', 'Pham', 18)
user1.describe_user()
user2 = User('Yang', 'Gao', 28)
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)
admin = Admin('Louis', 'Nguyen', 18)
admin.privileges.show_privileges()