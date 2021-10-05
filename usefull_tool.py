import random

def roll_dice():
    return random.randint(1, 6)

def get_file_ext(filename):
    return filename[filename.index(".")+1:]