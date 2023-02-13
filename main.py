import os
from subprocess import Popen

rootdir = 'G:\Github'
githubid = "ruodeee"
i = 0
for root, dirs, files in os.walk(rootdir):
    for dir in dirs:
        print(dir)
        for subroot, subdirs, subfiles in os.walk(fr"{rootdir}\{dir}"):
            for subdir in subdirs:
                with open(fr"{rootdir}\{dir}\{subdir}\setup.bat", "w") as f:
                    subdir2 = subdir.replace(" ","-")
                    l1 = f"gh repo create {subdir2} --private\n"
                    l2 = "git init\n"
                    l3 = "git add --all :/\n"
                    l4 = 'git commit -m "first commit"\n'
                    l5 = "git branch -M main\n"
                    l6 = "git remote remove origin\n"
                    l7 = f"git remote add origin https://github.com/{githubid}/{subdir2}.git\n"
                    l8 = "git push -u origin main"
                    f.writelines([l1, l2, l3, l4, l5, l6, l7, l8])
                f.close()
                if (os.path.exists(fr"{rootdir}\{dir}\{subdir}\README.md")) == False:
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