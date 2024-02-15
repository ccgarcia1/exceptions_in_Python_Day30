# dealing with error and exception in Python
# FileNotFound error

# First Block the algoritm try to execute
try:
    with open("a_file.txt", "w") as file:
        # file.read()
        file.write("Written inside the try block")
        file.write("Written inside the try block")
        file.write("Written inside the try block")
    print("inside the try block")

# if there a specific exception the code goes to the exception block
except FileNotFoundError as error_message:
    file = open("a_file.txt", "w")
    file.write("Written inside the FileNotFoundError")
    print(f"There was an error{error_message} reading the file")

# This part of the code ONLY executes if the try condition didn't raise any exception
else:
    with open("a_file.txt", "r") as file:
        content = file.read()
    print(content)
    print("else")

# This part of the code ALWAYS executes independent of if we got any exception or not
finally:
    file.close()
    print("Finally")

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# try:
#     text = "abc"
#     print(text)
#
# except:
#     print("Except")
#
# else:
#     print("else")
#
# finally:
#     print("Finally")
