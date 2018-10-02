# Author:Colin
import getpass

_username = "Colin"
_password = "123456"
username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("Welcome user {name} login ...".format(name=username))
else:
    print("invalid value")
print(username, password)

