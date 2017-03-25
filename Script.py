import time, os

while True:
        file = open("i.txt", "w")

        file.write("foo")
        file.close()

        time.sleep(5)

        os.system("del i.txt")

        time.sleep(595)


