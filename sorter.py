#!/usr/bin/env python3
import os,shutil,sys,textwrap

args = str(sys.argv[1:])
#Arg debug line:
#print ("Arg count: "+str(len(sys.argv))+"Args list: %s " % args)

#These are the 'all' and 'rest' arguments, change them as you like
all = '-a'
other = {
    "arg": '-o',
    "name": "Other",
    "desc": "Description of the filter"
}
# Add new filters as you please! It is dynamic
dirs = {
    "-i": {
        "name": "Images",
        "ex": [".jpeg", ".png", ".jpg", ".gif"],
        "desc": "Sorts images"
    },
    "-t": {
        "name": "Text",
        "ex": [".doc", ".txt", ".pdf", ".xlsx", ".docx", ".xls", ".rtf"],
        "desc": "Sorts text files"
    },
    "-v": {
        "name": "Videos",
        "ex": [".mp4", ".mkv", ".mov"],
        "desc": "Sorts videos"
    },
    "-s": {
        "name": "Sounds",
        "ex": [".mp3", ".wav", ".m4a"],
        "desc": "Sorts sounds"
    },
    "-p": {
        "name": "Applications",
        "ex": [".exe", ".lnk"],
        "desc": "Sorts applications"
    },
    "-c": {
        "name": "Codes",
        "ex": [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php"],
        "desc": "Sorts code files"
    }
}
#Prints out a man if you dont give it any arguments
if len(sys.argv) == 1:
    print("\nDescription: This script sorts files in the directory it is in by file extension. It also creates directories needed for the sort"
          "\n\nSynopsis: sorter.py [OPTION]..."
          "\n\nOptions:"
          )
    print(all+": "+"Sorts every file")
    print(other['arg']+": "+" puts files with unknown file extensions in another dictionary")
    for dir in dirs:
        print(dir+": "+dirs[dir]['desc']+" "+str(dirs[dir]['ex']))
else:
    #
    current = os.getcwd()
    files=os.listdir(current)

    if '-r' in args:
        print("Resetting files...")
        doall = len(sys.argv) == 2
        for dir in dirs:
            if os.path.isdir(dirs[dir]['name']) and (dir in args or doall):
                tomove = os.listdir(os.path.join(current,dirs[dir]['name']))
                for f in tomove:
                    shutil.move(os.path.join(current,dirs[dir]['name'],f),current)
                try:
                    os.rmdir(dirs[dir]['name'])
                except OSError as e:
                    print("Error: %s : %s" % (dirs[dir]['name'], e.strerror))
        print("Reset done")
    else:
        print("Checking if the directories exist")
        dest = ""
        for dir in dirs:
            if not os.path.isdir(dirs[dir]['name']) and (dir in args or '-a' in args):
                os.mkdir(dest+dirs[dir]['name'])
                print(dirs[dir]['name']+" created")
        print("Checking completed")

        print("Sorting the files...")
        for file in [file for file in files if not os.path.isdir(file) and not file == os.path.basename(__file__)]:
            dest = ""
            for dir in dirs:
                if dir in args or all in args:
                    for ex in dirs[dir]['ex']:
                        if file.endswith(ex):
                            dest = './' + str(dirs[dir]['name'])
                            shutil.move(file, dest)
                            break

            if dest == "" and (other['arg'] in args or all in args):
                shutil.move(file,'./'+other['name'])

        print("Sorting Completed...")
