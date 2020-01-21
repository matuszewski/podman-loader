# #!/usr/bin/env python2.7
#       python2.7 -m compileall .    # compilation to .pyc extension
#       https://stackoverflow.com/questions/21189346/shebang-line-for-python-2-7/21189383


import subprocess
from os import listdir
from os.path import isfile, join
import os

directory = "Desktop"       # .         working directory
extension = ".txt"          # .tar

def main():
    #command = "podman load --input "   # default command to run
    command = "echo "                   # only for testing
    

    # creates a list of all files ( also hidden ) in specified directory # () tuple     [] list    {} dictionary
    allfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    
    # creates an empty list to which all found *.tar archives will append
    archives = []

    
    # Display all files ( also hidden files )
    #for filename in onlyfiles:
    #    print(filename)

    print("--------------------------------------------------------------------------------------------")
    print("PODMAN LOADER:")
    print("all files: " + str(len(allfiles)))
    
    # display files with *.tar extension
    for filename in allfiles:
        if(filename.find(extension, -4) != -1): # checks if the last 4 characters are the extension ( .XXX )
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
