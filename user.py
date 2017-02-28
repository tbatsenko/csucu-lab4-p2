# File: user.py
from agent import Agent


class User(Agent):
    def __init__(self, username, password, email):
        """
        This method inits an instance of User class, which represents a user
        in Real Estate system.
        """
        super().__init__()
        self.username = username
        self.password = password
        self.email = email
        self.is_logged = False
        self.can_add_property = False

    def forgot_password(self):
        """
        This method allows user to reset the password if he knows the email.
        """
        print("Enter your email to reset the password")
        user_input = input()
        if user_input == self.email:
            print("Type the new password below:")
            new_password = input()
            self.password = new_password
        else:
            print("Email doesn't match, try again or forget about it.")

    def add_property(self):
        """
        This allows user to add properties to general Real Estate system.
        Requiers admin's permission.
        """
        if self.can_add_property:
            super().add_property()
