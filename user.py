# File: user.py


class User(object):
    properties = {}

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.is_logged = False

    def forgot_password(self):
        print("Enter your email to reset the password")
        user_input = input()
        if user_input == self.email:
            print("Type the new password below:")
            new_password = input()
            self.password = new_password
        else:
            print("Email doesn't match, try again or forget about it.")


# me = User('tb', '123', 'tb@gmail.com')
# me.forgot_password()
# print(me.password)
