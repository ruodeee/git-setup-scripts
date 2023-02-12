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
                    subdir2 = subdir.replace(" ","-")
                    l1 = f"gh repo create {subdir2} --private\n"
                    l2 = f'echo "# {subdir2}" >> README.md \n'
                    l3 = "git init\n"
                    l4 = "git add --all :/\n"
                    l5 = 'git commit -m "first commit"\n'
                    l6 = "git branch -M main\n"
                    l7 = "git remote remove origin\n"
                    l8 = f"git remote add origin https://github.com/ruodeee/{subdir2}.git\n"
                    l9 = "git push -u origin main"
                    f.writelines([l1, l2, l3, l4, l5, l6, l7, l8, l9])
                f.close()
                with open(fr"{rootdir}\{dir}\{subdir}\README.md", "w") as f:
                    l1 = f"# {subdir}\n"
                    l2 = f"## Setup\n"
                    l3 = f"## Commands"
                    f.writelines([l1, l2, l3])
                f.close()
                print(f"{rootdir}\\{dir}\\{subdir}\\")
                os.system(f"{rootdir}\{dir}\{subdir}\setup.bat")     
            subdirs[:] = [] 
    dirs[:] = [] 