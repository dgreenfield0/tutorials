# Read file
reader = open('../lesson1_plain.txt')
try:
    # print out the content of the file.
    print(reader.read())
finally:
    # closer the connection to the file
    reader.close()
