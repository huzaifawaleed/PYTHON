# File Methods Read, Readline and other Methods.

with open('info.txt', 'r') as f:
    l = 0
    while True:
        l = l + 1
        line = f.readline()
        if not line:
            break
        n1 = int(line.split(",")[0])
        n2 = int(line.split(",")[1])
        n3 = int(line.split(",")[2])
        print(f"Marks of Student {l} in Maths is {n1+5}")
        print(f"Marks of Student {l} in English is {n2+8}")
        print(f"Marks of Student {l} in Computer is {n3+7}")
#         print(line)

with open('Day51.py', 'w') as f:
    day = ["Seek(), Tell() and other functions in Files."]
    f.writelines(day)
