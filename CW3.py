import os
def read_log(func):
    def wrapper(*args):
        a = os.listdir(args)
        for i in a:
            if i.endswith('.log'):
                return i.read

    return wrapper


def file_list(directory):
    return os.listdir(directory)
