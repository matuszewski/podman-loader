import sys
import os
import subprocess
from datetime import date
from os import path
def main():
        command = "docker images | grep '/' | awk '{print($1)}'"
        images = []

        #dateTime = date.today()
        #dateTime = dateTime.strftime("%d_%m_%Y")
        #j=1
        #
        #os.system("mkdir "+ dateTime)
        #if(path.isdir(dateTime)):
        #       print("EXISTS")
        #       while (1==1):
        #               try:
        #                       if(path.isdir(dateTime)
        #                       os.system("mkdir "+ dateTime + "_" + j)
        #
        #                       break
        #               except:
        #                       j=j+1
        #print("dir done")

        p = subprocess.Popen(command, shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        #response = p.stdout.readlines(-1)[0]
        #print response

        for line in iter(p.stdout.readline, ''):
                images.append(line.rstrip())
        i = 1
        for line in images:

                # find in line the last occurance of specified character        '/'
                # and create substring from line that starts at one character after that ^ and ends in the end of that line
                archive_name = line[line.rfind('/')+1:]

                print("[" + str(i) + "] FOUND: " + line)

                export_command = "docker save -o " + archive_name + ".tar " + line
                os.system(export_command)
                print("[>] EXPORTED AS: " + archive_name + ".tar")

                i=i+1
        print('-'*80)

        # exportowanie



        print("[>] Done")
        pass

main()
