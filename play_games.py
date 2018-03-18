import os
import platform
platformOS = platform.system()
options = ["Play Games", "Write Code", "Browse the Internet"]
if (platformOS == "Windows"):
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
        file_to_open = "E:\\Riot Games\\League of Legends\\LeagueClient.exe"
        import subprocess
        subprocess.call([file_to_open])
    
    elif (choice == 2):
        file_to_open = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"
        import subprocess
        subprocess.call([file_to_open]) 
        print "Happy Coding!" 
    
    elif (choice == 3):
        file_to_open = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        import subprocess
        subprocess.call([file_to_open]) 
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
    
    elif (choice == 2):
        file_to_open = "/Applications/Atom.app"
        import subprocess
        subprocess.call(["open", "-a", file_to_open]) 
        print "Happy Coding!" 
    
    elif (choice == 3):
        file_to_open = "/Applications/Google Chrome.app"
        import subprocess
        subprocess.call(["open", "-a", file_to_open]) 
        print "Happy Webbing!"       
    
    else:
        print "Not ready yet."        
    
    
else:
    print "Only Windows and MacOS are Supported."

  
