import os
import platform
platformOS = platform.system()
options = ["Play Games", "Write Code", "Browse the Internet"]
if (platformOS == "Windows"):
    # for retry in range(5):
    #     activity = raw_input("Do you want to play a game? ")
    #     if (activity == "yes" ):
    #         pathToGames = raw_input("What's the path to your games? ")
    #         import subprocess
    #         subprocess.Popen('explorer %s' % pathToGames, shell=True)
    #         break
    #     if (activity == "no"):
    #         print "Ok, bye."
    #         break
    #     print "Must answer 'yes' or 'no'."
    # else:
    #     print "5 invalid entries.  Exiting"
    def let_user_pick(options):
        print "What would you like to do today?"
        for idx, element in enumerate(options):
            print"{}) {}".format(idx+1,element)
        i = input("Enter number: ")
        try:
            if (0 < int(i) <= len(options)):
                return int(i)
        except:
            pass
        return None

    choice = let_user_pick( options)
    
    if (choice == 1):
        file_to_open = ""
        import subprocess
        subprocess.call(["open", "-a", file_to_open])
    
    if (choice == 2):
        file_to_open = ""
        import subprocess
        subprocess.call(["open", "-a", file_to_open]) 
        print "Happy Coding!" 
    
    if (choice == 3):
        file_to_open = ""
        import subprocess
        subprocess.call(["open", "-a", file_to_open]) 
        print "Happy Webbing!"       
    
    else:
        print "Not ready yet."       

elif (platformOS == "Darwin"):
    
    def let_user_pick(options):
        print "What would you like to do today?"
        for idx, element in enumerate(options):
            print"{}) {}".format(idx+1,element)
        i = input("Enter number: ")
        try:
            if (0 < int(i) <= len(options)):
                return int(i)
        except:
            pass
        return None

    choice = let_user_pick( options)
    
    if (choice == 1):
        file_to_open = "/Applications/Spotify.app"
        import subprocess
        subprocess.call(["open", "-a", file_to_open])
    
    if (choice == 2):
        file_to_open = "/Applications/Atom.app"
        import subprocess
        subprocess.call(["open", "-a", file_to_open]) 
        print "Happy Coding!" 
    
    if (choice == 3):
        file_to_open = "/Applications/Google Chrome.app"
        import subprocess
        subprocess.call(["open", "-a", file_to_open]) 
        print "Happy Webbing!"       
    
    else:
        print "Not ready yet."        
    
    
else:
    print "Only Windows and MacOS are Supported."

# def let_user_pick(options):
#     print("Please choose:")
#     for idx, element in enumerate(options):
#         print("{}) {}".format(idx+1,element))
#     i = input("Enter number: ")
#     try:
#         if 0 < int(i) <= len(options):
#             return int(i)
#     except:
#         pass
#     return None
  
