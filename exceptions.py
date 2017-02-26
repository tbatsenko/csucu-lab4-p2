class AuthError(object):
    def __init__(self, username, user=None):
        """
        This is general class for authentication errors.
        """
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameExistsError(AuthError):
    print("This username is already taken")


class LongPasswordError(AuthError):
    print("This password is too long - it must be under 16 symbols")


class InvalidEmailError(AuthError):
    print("This email is invalid, try one that has '@' symbol")


class UsernameNotFoundError(AuthError):
    print("There is no user with such username - check spelling or register")


class InvalidPasswordError(AuthError):
    print("Password and username don't match - please try again or use" +
          "the 'forgot_password' option")
