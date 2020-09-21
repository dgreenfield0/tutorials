import array

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
with open('../lesson2_delimited.txt', 'r') as reader:
    try:
        # Create an array to hold all users
        userList = []

        # Read file line by line
        for line in reader:
            # print(line)

            # remove new line character 
            line = line.rstrip('\n')

            # print(line)

            # split the line by the comma delimeter
            userData = line.split(",")

            # print(userData[0])
            # print(userData[1])
            # print(userData[2])

            # Create a new User object from the split user data
            user = User(userData[0], userData[1], userData[2])

            #print(user.first +" "+ user.last)

            # Add new user to User List
            userList.append(user)

        # Iterate over the user list and print the user data (using the printme method)
        for user in userList:
            user.printme()
    finally:
        # Close the connection to the file
        reader.close()

