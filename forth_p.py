import os

def recursive_printing(path):
    name_list = os.listdir(path)
    print(name_list)
    for name in name_list:
        n_path = os.path.join(path,name) 
        if os.path.isdir(n_path):
            recursive_printing(n_path)
    return
