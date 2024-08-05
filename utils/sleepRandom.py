import random
from time import sleep

def send_keys_random_time(element, keys):
    for key in keys:
        element.send_keys(key)
        sleep(random.randrange(0,1))