# Sorter

##Sorter.py

###Description
sorter.py uses arguments, run it without any to see the manual

###How to Run
*You need Python
```
python sorter.py [args]
```

###Examples
sorts every file
```
python sorter.py -a
```
on linux you can do:
```
./sorter.py -a
```
to reset:(you can add -i -s etc to only reset those)
```
python sorter.py -r
```

##Exe Dir
###Description
* config.yml - essential args such as reset, exit
* filters.yml - sorter.exe uses this to make folders and to filter the files. Priority:order
* sorter.exe - This does the magic
###How to Run
Run the .exe, type -h(default) for help

##py with config files
###Same as the exe you but you can run it as:
```
python sorter.py
```
```
./sorter.py
```