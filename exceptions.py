class AuthError(object):
    def __init__(self, username, user=None):
        """
        This is general class for authentication errors.
        """
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameExistsError(AuthError):
    # in case ("This username is already taken")
    pass


class LongPasswordError(AuthError):
    # in case ("This password is too long - it must be under 16 symbols")
    pass


class InvalidEmailError(AuthError):
    # in case ("This email is invalid, try one that has '@' symbol")
    pass


class UsernameNotFoundError(AuthError):
    # in case("There is no user with such username-check spelling or register")
    pass


class InvalidPasswordError(AuthError):
    # in case ("Password and username don't match - please try again or use" +
    # "the 'forgot_password' option")
    pass


class PermissionError(Exception):
    pass
