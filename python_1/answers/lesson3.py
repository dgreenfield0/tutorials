import json

# define the User class
class User:
    # user variables
    first = ""
    last = ""
    email = ""

    # User initialize method
    def __init__(self, first, last, email):
        self.first = first
        self.last  = last
        self.email = email

    def printme(self) :
        print("First Name " + self.first)
        print("Last Name "  + self.last)
        print("Email "      + self.email)
        print("\n")

# Read file
with open('../lesson3_json_single.txt', 'r') as reader:
    try:
        # Create an array to hold all users
        userList = []

        # Load the JSON data into a dictionary
        data = json.load(reader)
        #print(data)

        # Create a new User from the data dictionary
        user = User(**data)
        #print(user.first)

        # Add new user to User List
        userList.append(user)

        # Iterate over the user list and print the user data (using the printme method)
        for user in userList:
            user.printme()
    finally:
        # Close the connection to the file
        reader.close()

