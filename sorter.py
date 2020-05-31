#!/usr/bin/env python3
import os,shutil,sys,textwrap

args = str(sys.argv[1:])
#Arg debug line:
#print ("Arg count: "+str(len(sys.argv))+"Args list: %s " % args)
if len(sys.argv) == 1:
    print("\nDescription: This script sorts files in the directory it is in by file extension. It also creates directories needed for the sort"
          "\n\nSynopsis: sorter.py [OPTION]..."
          "\n\nOptions:"
          "\n-a : Sorts every file"
          "\n-i : Sorts images"
          "\n-t : Sorts text files"
          "\n-v : Sorts videos"
          "\n-s : Sorts sound files"
          "\n-app : Sorts applications"
          "\n-c : Sorts code files"
          "\n-r : Resets everything"
          )
else:
    current = os.getcwd()

    files=os.listdir(current)

    images=[".jpeg",".png",".jpg",".gif"]
    text=[".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"]
    videos=[".mp4",".mkv"]
    sounds=[".mp3",".wav",".m4a"]
    applications=[".exe",".lnk"]
    codes = [".c",".py",".java",".cpp",".js",".html",".css",".php"]

    dirs = {"-i" : "Images","-t" : "Text","-v" : "Videos","-s" : "Sounds","-a" : "Applications","-c" : "Codes","-o":"Others"}
    #To change directory names, change the text after the ':'s
    if len(sys.argv) == 2 and '-r' in args:
        print("Resetting files...")
        for dir in dirs.values():
            tomove = os.listdir(os.path.join(current,dir))
            for f in tomove:
                shutil.move(os.path.join(current,dir,f),current)
        print("Reset done")
    else:
        print("Checking if the directories exist")
        dest = ""
        for dir in dirs:
            if not os.path.isdir(dirs[dir]) and (dir in args or '-a' in args):
                os.mkdir(dest+dirs[dir])
                print(dirs[dir]+" created")

        print("Checking completed")

        print("Sorting the files...")
        for file in [file for file in files if not os.path.isdir(file) and not file == os.path.basename(__file__)]:
            dest = ""
            if '-i' in args or '-a' in args:
                for ex in images:
                    if file.endswith(ex):
                        dest='./'+dirs['-i']
                        shutil.move(file,dest)
                        break

            if '-t' in args or '-a' in args:
                for ex in text:
                    if file.endswith(ex):
                        dest='./'+dirs['-t']
                        shutil.move(file,dest)
                        break

            if '-s' in args or '-a' in args:
                for ex in sounds:
                    if file.endswith(ex):
                        dest='./'+dirs['-s']
                        shutil.move(file,dest)
                        break

            if '-v' in args or '-a' in args:
                for ex in videos:
                    if file.endswith(ex):
                        dest='./'+dirs['-v']
                        shutil.move(file,dest)
                        break

            if '-app' in args or '-a' in args:
                for ex in applications:
                    if file.endswith(ex):
                        dest= './'+dirs['-a']
                        shutil.move(file,dest)
                        break

            if '-c' in args or '-a' in args:
                for ex in codes:
                    if file.endswith(ex):
                        dest= './'+dirs['-c']
                        shutil.move(file,dest)
                        break

            if dest == "" and ('-o' in args or '-a' in args):
                shutil.move(file,'./'+dirs['-o'])

        print("Sorting Completed...")
