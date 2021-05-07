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

# Return statistics about system memory usage        
print("Scanning RAM: \n")
with Bar('Progress:', fill='▋', suffix='%(percent).1f%% complete') as bar:
    for i in range(100):
        sleep(0.02)
        svmem = psutil.virtual_memory()
        bar.next()
    
    # to calculate percentage of available memory
    avmem = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    prcntg = '{:.1f} %'.format(avmem)
bar.finish()

# put the object in a dictionary
mem = {'Total': get_size(svmem.total), 'Percentage-available': prcntg, 'Available': get_size(svmem.available), 'Percentage-used': f'{svmem.percent} %', 'Used': get_size(svmem.used), 'Free': get_size(svmem.free)}
print(mem)

print("\n")

# Return system swap memory statistics as a named tuple including the following fields
with Bar('Progress:', fill='▋', suffix='%(percent).1f%% complete') as bar:
    for i in range(100):
        sleep(0.02)
        swap = psutil.swap_memory() # the percentage usage calculated as (total - available) / total * 100
        bar.next()
bar.finish()
mem2 = {'Total': get_size(swap.total), 'Used': get_size(swap.used), 'Free': get_size(swap.free), 'Percentage': f'{swap.percent} %'}
print(mem2)
