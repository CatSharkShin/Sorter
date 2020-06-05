#!/usr/bin/env python3

import yaml,os,shutil,sys,subprocess
with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
with open("filters.yml", "r") as ymlfile:
    dirs = yaml.safe_load(ymlfile)


#exit = cfg['exit']
all = cfg['all']
other = cfg['other']
#help = cfg['help']
#reset = cfg['reset']

current = os.getcwd()


def help():
    print("\nDescription: This script sorts files in the directory it is in by file extension. It also creates directories needed for the sort"
          "\n\nSynopsis: sorter.py [OPTION]...")
    options()
def options():
    print("\n\nOptions:")
    print("-"+all + ": " + "Sorts every file")
    print("-"+cfg['reset']+ ": " +"Resets given filters")
    print("-"+cfg['exit']+ ": Exits")
    print("-"+other['arg'] + ": " + " Puts files with unknown file extensions in another dictionary\n")
    for dir in dirs:
        print("-"+dir + ": " + dirs[dir]['desc'])

def reset():
    print("Resetting files...")
    doall = all in args
    if other['arg'] in args or doall:
        tomove = os.listdir(os.path.join(current,other['name']))
        for f in tomove:
            try:
                shutil.move(os.path.join(current,other['name'],f),current)
            except OSError as e:
                print("Error: %s : %s" % (other['name'], e.strerror))
        try:
            os.rmdir(other['name'])
        except OSError as e:
            print("Error: %s : %s" % (dirs[dir]['name'], e.strerror))
    for dir in dirs:
        if os.path.isdir(dirs[dir]['name']) and (dir in args or doall):
            tomove = os.listdir(os.path.join(current,dirs[dir]['name']))
            for f in tomove:
                try:
                    shutil.move(os.path.join(current,dirs[dir]['name'],f),current)
                except OSError as e:
                    print("Error: %s : %s" % (dirs[dir]['name'], e.strerror))
            try:
                os.rmdir(dirs[dir]['name'])
            except OSError as e:
                print("Error: %s : %s" % (dirs[dir]['name'], e.strerror))
    print("Reset done")

def check():
    print("Checking if the directories exist")
    dest = ""
    if not os.path.isdir(other['name']) and (other['arg'] in args or all in args):
        os.mkdir(dest+other['name'])
    for dir in dirs:
        if not os.path.isdir(dirs[dir]['name']) and (dir in args or all in args):
            os.mkdir(dest+dirs[dir]['name'])
            print(dirs[dir]['name']+" created")
    print("Checking completed")

def sort():
    #print("Sorting the files...")
    for file in [file for file in files if not os.path.isdir(file) and not file == os.path.basename(sys.argv[0]) and not file == "config.yml" and not file =="filters.yml"]:
        dest = ""
        for dir in dirs:
            if dir in args or all in args:
                for ex in dirs[dir]['ex']:
                    if file.endswith(ex):
                        dest = './' + str(dirs[dir]['name'])
                        try:
                            shutil.move(file, dest)
                        except OSError as e:
                            print("Error: %s : %s" % (dirs[dir]['name'], e.strerror))
                        break

        if dest == "" and (other['arg'] in args or all in args):
            try:
                shutil.move(file,'./'+other['name'])
            except OSError as e:
                print("Error: %s : %s" % (dirs[dir]['name'], e.strerror))
    #print("Sorting Completed...")

def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls",shell=True)
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear",shell=True)
    else:
        print("\n") * 120
#Main loop
h = False
args = []
while True:
    clear()
    print("What do you want to do?")
    print("-"+cfg['help']+" for help")
    if h:
        help()
        h = False
    args = input().replace(' ','').split('-')[1:]
    if cfg['reset'] in args:
        reset()
    else:
        files=os.listdir(current)
        check()
        sort()
    if cfg['help'] in args:
        h = True
    if cfg['exit'] in args:
        break
