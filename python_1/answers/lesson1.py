# Read file
reader = open('../lesson1_plain.txt')
try:
    # print out the content of the file.
    print(reader.read())
finally:
    # closer the connection to the file
    reader.close()

print("\n")

# Read file line by line 
with open('../lesson1_plain.txt', 'r') as reader:
    try:
        # Use FOR loop to interate over each line
        for line in reader:
            # print out the contents of the line.
            print(line)
    finally:
        # Close the connection to the file
        reader.close()