import os
import platform
platformOS = platform.system()

if (platformOS == "Windows"):
    for retry in range(5):
        activity = raw_input("Do you want to play a game? ")
        if (activity == "yes" ):
            pathToGames = raw_input("What's the path to your games? ")
            import subprocess
            subprocess.Popen('explorer %s' % pathToGames, shell=True)
            break
        if (activity == "no"):
            print "Ok, bye."
            break
        print "Must answer 'yes' or 'no'."
    else:
        print "5 invalid entries.  Exiting"
else:
    print "Only Windows is Supported."


  
