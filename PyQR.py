import os
import time
import sys

arg1 = input("\nInsert the linkt or short text you want to make into a QR code\n")

arg2 = input("\nPress ""s"" if you want to save the file [Default = delete]\n")

arg3 = input("\nType the name of the png file, this is optional [standard is qr.png]\n")



if arg2 == "s":
    if arg3 == "":
        arg3 = "qr.png"
        os.system("qr " + arg1 + " > " + arg3)
    
    elif ".png" not in arg3:
        os.system("qr " + arg1 + " > " + arg3 + ".png")
    
    if ".png" not in arg3:
        if arg3 == "":
            arg3 = "qr.png"
            os.system(arg3)
        else:
            os.system(arg3 + ".png")

    else:
        os.system(arg3)

else:
    if arg3 == "":
        arg3 = "qr.png"
        os.system("qr " + arg1 + " > " + arg3)
    
    elif ".png" not in arg3:
        os.system("qr " + arg1 + " > " + arg3 + ".png")
    
    if ".png" not in arg3:
        if arg3 == "":
            arg3 = "qr.png"
            os.system(arg3)
        else:
            os.system(arg3 + ".png")
    else:
        os.system(arg3)


    time.sleep(0.25)


    if ".png" not in arg3:
        if arg3 == "":
            arg3 = "qr.png"
            os.system(arg3)
        else:    
            os.system("del " + arg3 + ".png")
    
    else:
        os.system("del " + arg3)

