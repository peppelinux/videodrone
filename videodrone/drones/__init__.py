import glob
import random

def get_random_y4m(path='./y4ms'):
    return random.choices([i for i in glob.iglob(f'{path}/*y4m')])[0]
