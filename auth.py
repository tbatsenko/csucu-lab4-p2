# File: auth.py
from user import User
import exceptions


class Authenticator(object):
    def __init__(self, admin):
        """
        Constructs an Authenticator to manage users of the program:
        add new ones, log one in, log one out, delete users.
        """
        self.admin = admin
        self.users = {}

    def add_user(self, username, password, email):
        """
        This method allows to add a new user to the system.
        """
        if username in self.users:
            raise UsernameExistsError
        if len(password) > 16:
            raise LongPasswordError
        if '@' not in email:
            raise InvalidEmailError
        self.users[username] = User(username, password, email)

    def login(self, username, password):
        """
        This method logges the user in.
        """
        try:
            user = self.users[username]
        except KeyError:
            raise UsernameNotFoundError
        if user.password != password:
            raise InvalidPasswordError
        user.is_logged = True
        return True

    def is_logged_in(self, username):
        """
        This method checks if the user with the given username is logged in.
        """
        if username in self.users:
            return self.users[username].is_logged
        return False

authenticator = Authenticator()
admin = User("admin", "superpassword")


class Admin(User):
    def __init__(self, authenticator, admin):
        """

        """
    def add_property():
