from os import stat

# reimplementation of some os.paths utils not available in micropython

S_IFDIR = 1 << 14
S_IFREG = 1 << 15

def isfile(path):
    try:
        return stat(path)[0] & S_IFREG == S_IFREG
    except (OSError, FileNotFoundError):
        return False

def isdir(path):
    try:
        return stat(path)[0] & S_IFDIR == S_IFDIR
    except (OSError, FileNotFoundError):
        return False



