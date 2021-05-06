import psutil
from time import sleep
from progress.bar import Bar

# function to get the Size
def get_size(bytes, suffix="B"):
    factor = 1028
    for unit in["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor
