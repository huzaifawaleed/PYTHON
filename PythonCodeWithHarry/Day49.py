# File IO.

# 'r'	Read	Opens file for reading (default). File must exist.
# 'w'	Write	Creates/overwrites file.
# 'a'	Append	Adds content to the end of the file.
# 'x'	Create	Creates file, gives error if it already exists.
# 'b'	Binary	Read/write binary data (images, videos, etc.).
# 't'	Text	Text mode (default).


# f = open('myfile.txt', 'w')
# f.write("Huzaifa waleed")
# f.close()


# Asks the user to enter their name and age.
# Saves this information into a file called info.txt.
# Then reopens the file and prints the saved content.


# name = input("Enter Your Name: ")
# age = int(input("Enter Your Age: "))
# f = open('info.txt', 'a')
# f.write(f"{name}, {age}\n")
# print(name,age)
# f.close()

# with open('myfile.txt', 'r') as f:
#     content = f.read()
#     count = len(content)
#     print("Total words:", count)


# with open('myfile.txt', 'r') as f:
#     content = f.read()   
#     word = content.split()
#     print("Total words",len(word))



# import datetime as dt

# with open('myfile.txt', 'a') as f:
#     today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     f.write(f"{today} - Program Executed successfully")


#     with open('myfile.txt', 'r') as f:
#         print(f.read())