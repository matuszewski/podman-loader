###!/usr/bin/env python2.7

#       python2.7 -m compileall .    # kompilacja do .pyc
#       https://stackoverflow.com/questions/21189346/shebang-line-for-python-2-7/21189383


import subprocess
from os import listdir
from os.path import isfile, join
import os

directory = "Desktop"       # .         working directory
extension = ".txt"          # .tar

def main():
    #command = "podman load --input "
    command = "echo "
    

    # tworzy liste wszystkich plikow w katalogu         # () tuple     [] listy     {} slowniki
    allfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    
    archives = []

    
    # WSZYSTKIE PLIKI, TEŻ UKRYTE
    #for filename in onlyfiles:
    #    print(filename)

    print("--------------------------------------------------------------------------------------------")
    print("PODMAN LOADER:")
    print("all files: " + str(len(allfiles)))
    # PLIKI Z ROZSZERZENIEM .tar
    for filename in allfiles:
        if(filename.find(extension, -4) != -1): # czy ostatnie 4 litery to dane rozszerzenie (tutaj .tar )
            print(filename)
            archives.append(filename)

            #subprocess.run(["echo", filename])
            
            #process = subprocess.Popen(command + "ea", stdout=subprocess.PIPE)
            #output, error = process.communicate()

    print("running -------------")
    for archive in archives:
        os.system("docker " + archive)
    
    pass

if __name__ == "__main__":
    main()
    pass