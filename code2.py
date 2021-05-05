import psutil

def get_size(bytes, suffix="8"):
    factor = 1028
    for unit in["","K","H","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
