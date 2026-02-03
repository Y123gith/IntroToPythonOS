import os

def return_py_files(path):
    dir_files = os.listdir(path)
    for file in dir_files:
        n_path = os.path.join(path,file) 
        if os.path.isdir(n_path):
            return_py_files(n_path)
        if file.endswith(".py"):
            print(file)
    return
