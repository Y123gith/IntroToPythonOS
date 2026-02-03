import os

def print_given_dir(path):
    original_pos = os.getcwd()
    os.chdir(path)
    print(os.listdir)
    os.chdir(original_pos)
