import psutil
import wmi
from time import sleep
from progress.bar import Bar

# Connecting
c = wmi.WMI()
# stock here Process Id
proc = []

# function to get the Size
def get_size(bytes, suffix="B"):
    factor = 1028
    for unit in["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor
# End
      
print("Scanning RAM: \n")
print("system virtual memory: \n")
# Return statistics about system memory usage
with Bar('Progress:', fill='▋', suffix='%(percent).1f%% complete') as bar:
    for i in range(100):
        sleep(0.02)
        svmem = psutil.virtual_memory() # physical memory usage
        bar.next()

    # to calculate percentage of available memory
    avmem = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    prcntg = '{:.1f} %'.format(avmem)
bar.finish() 
# put the object in a dictionary
mem = {'Total': get_size(svmem.total), 'Percentage-available': prcntg, 'Available': get_size(svmem.available), 'Percentage-used': f'{svmem.percent} %', 'Used': get_size(svmem.used), 'Free': get_size(svmem.free)}
print(mem)
# End

print("\n")

print("system swap memory: \n")
# Return system swap memory statistics as a named tuple including the following fields
with Bar('Progress:', fill='▋', suffix='%(percent).1f%% complete') as bar:
    for i in range(100):
        sleep(0.02)
        swap = psutil.swap_memory() # the percentage usage calculated as (total - available) / total * 100
        bar.next()
bar.finish()
mem2 = {'Total': get_size(swap.total), 'Used': get_size(swap.used), 'Free': get_size(swap.free), 'Percentage': f'{swap.percent} %'}
print(mem2)
# End

'''
# Return an iterator yielding a WindowsService class instance for all Windows services installed.
# Get a Windows service by name, returning a WindowsService instance.
with Bar('Progress:', fill='▋', suffix='%(percent).1f%% complete') as bar:
    for i in range(100):
        sleep(0.02)
        winserv = list(psutil.win_service_iter())
        s = psutil.win_service_get('alg') # windows service by name
        bar.next()
bar.finish()

print(winserv)

print("\n")

print(s.as_dict())
# End
'''

print("\n")

print("Services: \n")
# Get all Windows services using the WMI module
with Bar('Progress:', fill='▋', suffix='%(percent).1f%% complete') as bar:
    for i in range(100):
        sleep(0.02)
        
        bar.next()
print("ID:     Name:\n")
for process in c.Win32_Process ():
    print (f"{process.ProcessId}       {process.Name}")
bar.finish()

# Get get a specific Windows service
for process in c.Win32_Process (name="notepad.exe"):
    print (f"{process.ProcessId}       {process.Name}")
# End

# calculate how much Processes are runnig
for process in c.Win32_Process():
    proc.append(process.ProcessId)
print(f"{len(proc)} Processes are running in your Device.")
# End

# ex:7 étudiant : Alaa Mostafa/Hamed Şahîn/Elanigri Zakaria/Anas Elbair. 
    
