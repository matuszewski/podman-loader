#!/usr/bin/env python
# >>> python2.7 -m compileall .    # compilation to .pyc extension

import subprocess
from os import listdir
from os.path import isfile, join
import os

directory = "."             # .     working directory
extension = ".tar"          # .tar

def main():
    # command = "podman load --input "   # default command to run
    command = "echo "


    # creates a list of all files (also hidden) in specified directory
    allfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

    # creates an empty list to which all found *.tar archives will append
    archives = []


    # Display all files (also hidden)
#   for filename in onlyfiles:
#       print(filename)

    print('-'*30)
    print("PODMAN LOADER:")
    print("[>] workdir:\t" + directory)
    print("[>] extension:\t" + extension)
    print('-'*30)


    print("[>] all files: " + str(len(allfiles)))

    # display files with *.tar extension
    for filename in allfiles:
        if(filename.find(extension, -4) != -1): # checks if the last 4 characters are the extension ( .XXX )
            print(filename)
            archives.append(filename)

            #subprocess.run(["echo", filename])

            #process = subprocess.Popen(command + "ea", stdout=subprocess.PIPE)
            #output, error = process.communicate()

    print("[>] " + extension + " files: " + str(len(archives)))

    print("[>] running")

    for archive in archives:
        os.system("podman load --input " + archive)
        print("\t loaded " + archive)

    print("[>] done")

    pass

if __name__ == "__main__":
    main()
    pass
