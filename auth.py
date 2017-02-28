# File: auth.py
from user import User
from exceptions import *


class Authenticator(object):
    def __init__(self):
        """
        Constructs an Authenticator to manage users of the program:
        add new ones, log one in, log one out, delete users.
        """
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


class Admin(User):
    def __init__(self, username, password, email, authenticator):
        """
        This method inits an Admin to manage user's permissions.
        """
        super().__init__(username, password, email)
        if password != "superpassword":
            raise NotAdminError
        self.authenticator = authenticator
        self.permissions = {}

    def add_permisstion(self, perm_name):
        """
        This method allows to add permissions.
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, user):
        """
        This method alllows to permit user to make an action.
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not Exists")
        else:
            if user.username not in self.authenticator.users:
                raise UsernameNotFoundError
            perm_set.add(user.username)
            if 'add' and 'property' in perm_name:
                user.can_add_property = True
