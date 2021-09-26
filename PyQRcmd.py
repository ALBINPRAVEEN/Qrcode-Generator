import os
import time
import sys

arg2 = str(sys.argv[2])

try:
    os.system("qr " + str(sys.argv[1]) + " > " + arg2)
    
    if ".png" not in arg2:
        os.system(arg2 + ".png")
    elif ".png" in arg2:
        os.system(arg2)

    time.sleep(0.25)
     
    if ".png" not in arg2:
        os.system("del " + arg2 + ".png")
    elif ".png" in arg2:
        os.system("del " + arg2)

except:
    print("You need to specify the string you want as a QR-code and the name of the png\nFor example\nPython PyQRcmd.py link.com qr.png")