#This is a test script to keep the computer from loggin me out.
#LUC computers log off after 10 min of inactivity.
#I need to render something that could potentially take over night.
#This script, succesful so far, is to make sure the computer continues rendering without me having to stay up all night just to make sure the computer doesn't log me out or delete all my work.

import time, os

while True:
        file = open("i.txt", "w")

        file.write("foo")
        file.close()

        time.sleep(5)

        os.system("del i.txt")

        time.sleep(595)


