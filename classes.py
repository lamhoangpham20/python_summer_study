class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} restaurant has {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self):
        self.number_served += 1



class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """something"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanila', 'banana', 'coconut']

    def get_flavors(self):
        for flavor in self.flavors:
            print(flavor)


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post",
                           "can ban user", "can invite user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()
