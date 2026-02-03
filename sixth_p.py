import os

def count_file_type(path):
    dictioanry = {}
    inside_dir = os.listdir(path)
    for file_name in inside_dir:
        if "." in file_name:
            file_type = os.path.splitext(file_name)
            if file_type in dictioanry:
                dictioanry[file_type] += 1
            else:
                dictioanry.update({file_type: 1})
    return dictioanry

