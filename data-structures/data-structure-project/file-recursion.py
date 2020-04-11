import os

def find_files(suffix, path):
    if suffix == '':
        return []

    if len(os.listdir(path)) == 0:
        return []

    path_elements = os.listdir(path)
    path_files = [file for file in path_elements if '.' + suffix in file]
    path_folders = [file for file in path_elements if '.' not in file]

    for folder in path_folders:
        path_files.extend(find_files(suffix=suffix, path=path + '/' + folder))

    return path_files

# Gets the current folder we are in plus the folder we intend to work with
path_base = os.getcwd() + '/testdir'
print(find_files(suffix='c', path=path_base))

# print(find_files(suffix='h', path=path_base))
#
# print(find_files(suffix='z', path=path_base))
#
# print(find_files(suffix='', path=path_base))
