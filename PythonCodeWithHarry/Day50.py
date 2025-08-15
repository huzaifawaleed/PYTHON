# File Methods Read, Readline and other Methods.

with open('info.txt', 'r') as f:
    l = 0
    while True:
        l = l + 1
        line = f.readline()
        if not line:
            break
        n1 = line.split(",")[0]
        n2 = line.split(",")[1]
        n3 = line.split(",")[2]
        print(f"Marks of Student {l} in Maths is {n1}")
        print(f"Marks of Student {l} in English is {n2}")
        print(f"Marks of Student {l} in Computer is {n3}")
#         print(line)


