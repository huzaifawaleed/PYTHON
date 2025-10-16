# | Function / Variable    | Description                                               |
# | ---------------------- | --------------------------------------------------------- |
# | `os.getcwd()`          | Get current working directory 📍                          |
# | `os.chdir(path)`       | Change the current directory 🔄                           |
# | `os.listdir(path)`     | List files and folders in a directory 📃                  |
# | `os.mkdir(path)`       | Make a new directory 📂                                   |
# | `os.makedirs(path)`    | Make nested directories (like `mkdir -p`) 🪜              |
# | `os.remove(file)`      | Delete a file ❌                                           |
# | `os.rmdir(dir)`        | Remove an empty directory 🚮                              |
# | `os.rename(src, dst)`  | Rename/move a file or directory 🔁                        |
# | `os.path.exists(path)` | Check if path exists ✅                                    |
# | `os.path.isfile(path)` | Check if it's a file 🗃️                                  |
# | `os.path.isdir(path)`  | Check if it's a directory 🗂️                             |
# | `os.path.join()`       | Join paths (cross-platform safe) 🪢                       |
# | `os.environ`           | Access environment variables 🌍                           |
# | `os.system(cmd)`       | Run system commands (like in terminal) ⚙️                 |
# | `os.name`              | Get OS type: `'posix'` (Linux/mac) or `'nt'` (Windows) 🧠 |
# | `os.stat(file)`        | Get metadata (size, modified date, etc.) 📊               |

import os 

directory = 'PythonCodeWithHarry/Day46'
# for i in range(1,50):
#     os.rmdir(f"{directory} {i + 1}")
# os.mkdir(directory)
# filePath = 'My Directory/first.py'
# with open(filePath,'w') as file:
#     file.write("")
# os.remove(filePath)    
# os.rmdir(directory)
print(os.getcwd())

