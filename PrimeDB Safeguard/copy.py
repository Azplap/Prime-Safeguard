import threading, os, shutil

myfile="Prime_BE.accdb"
delay = 3
run = 0

def copy():

    threading.Timer(delay, copy).start()
    run += 1
    if os.path.isfile(myfile):
        shutil.copy(myfile, "testfolder")
        print "copied for: " + str(run)
    else:
        print "prime is down" + str(run)
        
copy();


