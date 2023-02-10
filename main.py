import os
from subprocess import Popen

rootdir = 'G:\Github'
i = 0
for root, dirs, files in os.walk(rootdir):
    for dir in dirs:
        print(dir)
        for subroot, subdirs, subfiles in os.walk(fr"{rootdir}\{dir}"):
            for subdir in subdirs:
                with open(fr"{rootdir}\{dir}\{subdir}\setup.bat", "w") as f:
                    subdir = subdir.replace(" ","-")
                    l1 = f"gh repo create {subdir} --private\n"
                    l2 = f'echo "# {subdir}" >> README.md \n'
                    l3 = "git init\n"
                    l4 = "git add --all :/\n"
                    l5 = 'git commit -m "first commit"\n'
                    l6 = "git branch -M main\n"
                    l7 = f"git remote add origin https://github.com/ruodeee/{subdir}.git\n"
                    l8 = "git push -u origin main"
                    f.writelines([l1, l2, l3, l4, l5, l6, l7, l8])          
                print(f"{rootdir}\\{dir}\\{subdir}\\")
                os.system(f"{rootdir}\{dir}\{subdir}\setup.bat")     
            subdirs[:] = [] 
    dirs[:] = [] 