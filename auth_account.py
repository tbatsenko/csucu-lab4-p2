# File: auth_account.py
# This module shows how admin can manage user's permissions and how the user
# can register to the system
import auth
import user


def collect_user_data():
    print("Welcome to the Real Estate program!")
    print("To register fill the following info:")
    username = input("Enter your username: ")
    password = input("Enter the password (less then 16 chars): ")
    email = input("Enter your email in case you forget the password: ")
    print("Success! Your username is {}, password: {}, email: {}".format(
        username, password, email))
    return username, password, email
# initialize Authenticator
authenticator = auth.Authenticator()

# initialize Admin
admin = auth.Admin("admin", "superpassword", "admin@gmail.com", authenticator)

# add a new permission to the system
admin.add_permisstion("add_property")

# print out all permissions
print(admin.permissions)

# add admin as user
authenticator.add_user("admin", "superpassword", "admin@gmail.com")

# login admin
authenticator.login("admin", "superpassword")

# print out registered users
print(authenticator.users)

# ask user for data
user_info = collect_user_data()
new_user = user.User(user_info[0], user_info[1], user_info[2])

# add a new user to the system
authenticator.add_user(user_info[0], user_info[1], user_info[2])

# login a new user to the system
admin.authenticator.login(user_info[0], user_info[1])
print("You are logged in as {}".format(user_info[0]))

# Permit user to add properties
admin.permit_user("add_property", new_user)
print("Now you can add new properties to the database - try it now:")

# call action 'add_property' via new user
new_user.add_property()
print("--------------------------------------------------------------------")
print("Thanks for adding a new property! You can check out the updated db:")
print("")

# new user calls action 'display_properties'
new_user.display_properties()
