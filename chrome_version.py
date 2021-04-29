import subprocess


output = subprocess.check_output(
    r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
    shell=True
)



print(output.decode('utf-8').strip())