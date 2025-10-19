# Seek() tell() truncate() in files.


# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(8)

# with open('sample.txt', 'r') as f:
#   print(f.read())

with open('myfile.txt', 'r') as f:
    f.seek(5)
    data = f.read(7)
    print(data)
    print(f.tell())
