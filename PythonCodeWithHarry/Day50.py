# File Methods Read, Readline and other Methods.

import os

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

# with open('new.txt', 'w') as f:
#     day = ['1\n', '2\n', '3']
#     f.writelines(day)


# os.remove('new.txt')

with open('new.txt', 'a') as f:
    f.write("\n 4")
    